'''
Copyright (c) 2020-2025 ESCROVA LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

THIS SOFTWARE IS NOT PROVIDED TO ANY ENTITY OR ANY GROUP OR ANY PERSON
TO THREATEN, INCITE, PROMOTE, OR ACTIVELY ENCOURAGE VIOLENCE, TERRORISM,
OR OTHER SERIOUS HARM. IF NOT, THIS SOFTWARE WILL NOT BE PERMITTED TO USE.
IF NOT, THE BENEFITS OF ALL USES AND ALL CHANGES OF THIS SOFTWARE ARE GIVEN
TO THE ORIGINAL AUTHORS WHO OWNED THE COPYRIGHT OF THIS SOFTWARE  ORIGINALLY.
THE CONDITIONS CAN ONLY BE CHANGED BY THE ORIGINAL AUTHORS' AGREEMENT
IN AN ADDENDUM, THAT MUST BE DOCUMENTED AND CERTIFIED IN FAIRNESS MANNER.
'''

from graphcode.logging import printLog
from graphcode.inspect import isDict, isDictProxy

from graphcode.path import getAppName, findFilePath

from multiprocessing.managers import DictProxy
from multiprocessing import Manager

from typing import Dict, Any, Optional
from functools import reduce
from operator import getitem
from contextlib import contextmanager

import os
from os.path import expanduser, join, abspath, basename, exists, isfile, isdir

import time

import json

class ConfManager:
  def __init__(self, conf_dict: Optional[Dict[str, Any]] = None, debug: bool = False):
    """
    Initialize the configuration manager.
    
    Args:
      conf_dict: Initial configuration dictionary or DictProxy
      debug: Whether to enable debug logging
    """
    self.manager = Manager()
    self.conf_proxy = None
    self.lock = self.manager.Lock()
    self.debug = debug
    
    try:
      self._initializeConfig(conf_dict)
    except Exception as e:
      if self.debug:
        raise ValueError(printLog(f"Error initializing config: {e}"))
      else:
        raise ValueError(f"Error initializing config: {e}")

  def _initializeConfig(self, conf_dict: Optional[Dict[str, Any]]) -> None:
    """
    Initialize the configuration store with the provided dictionary.
    
    Args:
      conf_dict: Configuration dictionary or DictProxy
    """
    if conf_dict is None:
      with self.lock:
        self.conf_proxy =  self.manager.dict()
      if self.debug:
        printLog(f"{type(self.conf_proxy).__name__}:self.conf_proxy:[{self.conf_proxy}]")
      
      try:
        self.loadJson(findFilePath(filename=f"{getAppName()}.json"))
      except:
        try:
          self.loadJson(findFilePath(filename=f"{getAppName().lower()}.json"))
        except:
          self.loadJson(findFilePath(filename="conf.json"))

    elif isinstance(conf_dict, dict):
      self._convertToProxy(conf_dict)
      if "conf" not in conf_dict.keys():
        try:
          self.loadJson(findFilePath(filename=f"{getAppName()}.json"))
        except:
          try:
            self.loadJson(findFilePath(filename=f"{getAppName().lower()}.json"))
          except:
            self.loadJson(findFilePath(filename="conf.json"))
    
    elif isinstance(conf_dict, DictProxy):
      self.conf_proxy = conf_dict
    
    else:
      raise TypeError(f"Expected dict or DictProxy, got {type(conf_dict).__name__}")

  def _convertToProxy(self, conf_dict: Dict[str, Any]) -> None:
    """
    Convert a regular dictionary to DictProxy.
    
    Args:
      conf_dict: Dictionary to convert
    """
    if not isinstance(conf_dict, dict):
      raise TypeError(f"Expected dict, got {type(conf_dict).__name__}")

    with self.lock:
      self.conf_proxy = self.manager.dict()
      for key, value in conf_dict.items():
        self.putItem(key, value)
    if self.debug:
      printLog(f"{type(self.conf_proxy).__name__}:self.conf_proxy:[{self.conf_proxy}]")
        
  def putItem(self, key: str, value: Any) -> None:
    """
    Add or update an item in the configuration.
    
    Args:
      key: Configuration key
      value: Configuration value
    """

    if isinstance(value, dict):
      value_dict = self.manager.dict()
      for k, v in value.items():
        with self.lock:
          value_dict[k] = v
      with self.lock:
        self.conf_proxy[key] = value_dict
    elif isinstance(value, list):
      value_list = self.manager.list()
      for item in value:
        with self.lock:
          value_list.append(item)
      with self.lock:
        self.conf_proxy[key] = value_list
    else:
      with self.lock:
        self.conf_proxy[key] = value

  def getItem(self, key: str, default: Any = None) -> Any:
    """
    Get an item from the configuration.
    
    Args:
        key: Configuration key
        default: Default value if key not found
        
    Returns:
        Configuration value or default
    """
    with self.lock:
      return self.conf_proxy.get(key, default)

  def getProxy(self):
    """
    Context manager for accessing the configuration proxy.
    
    Yields:
      DictProxy: The configuration proxy
    """
    try:
      return self.conf_proxy
    except Exception as e:
      if self.debug:
        printLog(f"Error accessing config proxy: {e}")
      raise

  def __enter__(self):
    """Support for with statement."""
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    """Cleanup when exiting with statement."""
    if self.conf_proxy is not None:
      self.conf_proxy.clear()
      self.conf_proxy = None
    
  def get(self, *keys: str, default: Any = None) -> Any:
    """
    Get a value from nested dictionary using variable number of keys.
    
    Args:
      *keys: Variable number of keys to access nested values
      default: Default value to return if path not found
        
    Returns:
      The value at the specified path or default if not found
        
    Example:
      get('key1')               -> conf['key1']
      get('key1', 'key2')       -> conf['key1']['key2']
      get('key1', 'key2', 'key3') -> conf['key1']['key2']['key3']
    """
    try:
      # Get the base configuration dictionary
      conf_dict = self.getDictionary()
      
      # If no keys provided, return entire config
      if not keys:
        return conf_dict
      
      # Use reduce to traverse the nested dictionary
      return reduce(getitem, keys, conf_dict)
        
    except (KeyError, TypeError, AttributeError) as e:
      return default

  def get_safe(self, *keys: str, default: Any = None) -> Optional[Any]:
    """
    Safely get a value from nested dictionary with explicit error handling.
    
    Args:
      *keys: Variable number of keys to access nested values
      default: Default value to return if path not found
        
    Returns:
      The value at the specified path or default if not found
    """
    try:
      return self.get(*keys)
    except Exception as e:
      print(f"Error accessing config path {'.'.join(keys)}: {str(e)}")
      return default
  
  def getDictionary(self) -> Dict:
    return dict(self.conf_proxy) if self.conf_proxy is not None else dict(self.initConfStore())
  
  def loadJson(self, path) -> DictProxy:
    conf_dict = json.load(open(path, 'r'))
    if self.debug:
      printLog(f"loaded json:[{path}]")

    json_proxy = self.manager.dict()
    for key in conf_dict:
      self.putItem(key, conf_dict[key])
      if self.debug:
        printLog(f"added: {type(conf_dict[key]).__name__}:{key}:[{conf_dict[key]}]")
    
    return json_proxy

  def saveJson(self, path, conf_proxy):
    json.dump(dict(conf_proxy), open(path, 'w'), indent=2)

  def saveConf(self):
    """
    Save the configuration to the configuration file.
    """
    conf_dict = self.getItem('conf')
    if conf_dict is not None:
      if "_conf_" in conf_dict.keys():
        conf_dict["_conf_"]["revision"] += 1
        conf_dict["_conf_"]["lastupdate"] = time.time()
      else:
        conf_dict["_conf_"] = {
          "revision": 1,
          "lastupdate": time.time() 
        }
        conf_dict["_conf_"]
      self.saveJson(self.credStore.getItem('confDir'), self.credStore.getItem('conf'))
    else:
      if self.debug:
        printLog("No configuration to save")


