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

import logging

from typing import Dict, Any, Optional

from os import getpid, getppid
from os.path import abspath, expanduser, join, exists

import sys
import inspect

import time

global_conf_proxy = None

def setConfProxy(conf_proxy):
  global global_conf_proxy
  global_conf_proxy = conf_proxy

  return global_conf_proxy

def getConfProxy():
  global global_conf_proxy
  return global_conf_proxy

def initLog():
  global global_conf_proxy

  from graphcode.conf import ConfManager
  # Initialize configuration manager with credentials dictionary
  confManager = ConfManager(global_conf_proxy)
  # Get application name from config
  name = confManager.get("name")
  # Get log directory path from config    
  logDir = expanduser(confManager.get("logs"))
  
  # Create log directory if it doesn't exist
  if not exists(logDir):
    printLog(f"ogDir:[{logDir}] is created")
    
    from os import makedirs
    makedirs(logDir, exist_ok=True)
    
  # Get log level from config
  logLevel = confManager.get("logLevel")
  # If no log level specified, set "DEBUG" as the default
  if logLevel is None:   
    logLevel =  "DEBUG"
    confManager.putItem("logLevel", logLevel)

  # Get log filename from config
  logFilename = confManager.get("logFilename")
  # If no filename specified, generate one with timestamp
  if logFilename is None:    
    # Import time module for working with timestamps
    import time
    # Import timezone from pytz for handling timezone conversions
    from pytz import timezone
    # Import datetime class for date/time operations
    from datetime import datetime 

    # Generate UTC timestamp for log filename
    logFileTimestamp = datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z')
    # Create full log filepath with name and timestamp
    logFilename = join(logDir, f"{name}-{logFileTimestamp}.log")
    # Store generated filename in config
    confManager.putItem("logFilename", logFilename)

    printLog(f"logDir:[{logDir}] is set")
    printLog(f"{name}:[{confManager.get("logFilename")}](logLevel:{logLevel}) is set")
  else:
    printLog(f"{name}:[{confManager.get("logFilename")}](logLevel:{logLevel}) is loaded")

  # Configure logging with file and console output

  logging.basicConfig(
    handlers=[
      logging.FileHandler(logFilename),
      logging.StreamHandler()
    ],
    format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', 
    datefmt='%Y/%m/%d %H:%M:%S',
    level=confManager.get("logLevel")
  )

  global_conf_proxy = confManager.getProxy()
  return global_conf_proxy


def displayLoggingConfig() -> None:
  """Display the current logging configuration"""
  
  # Get the root logger
  root = logging.getLogger()
  
  # Get current configuration details
  config = {
    'level': logging.getLevelName(root.getEffectiveLevel()),
    'handlers': [],
    'formatter': None
  }
  
  # Collect handler information
  for handler in root.handlers:
    handler_info = {
      'type': handler.__class__.__name__,
      'level': logging.getLevelName(handler.level)
    }
    
    # Get formatter details if available
    if handler.formatter:
      handler_info['formatter'] = {
        'format': handler.formatter._fmt if hasattr(handler.formatter, '_fmt') else 'Unknown',
        'datefmt': handler.formatter.datefmt if handler.formatter.datefmt else 'Unknown'
      }
        
    # Get filename for FileHandler
    if isinstance(handler, logging.FileHandler):
      handler_info['filename'] = handler.baseFilename
        
    config['handlers'].append(handler_info)
  
  # Display configuration
  printLog("=" * 50)
  printLog("Current Logging Configuration:")
  printLog("-" * 50)
  printLog(f"Root Level: {config['level']}")
  for idx, handler in enumerate(config['handlers'], 1):
    printLog(f"Handler {idx}:")
    printLog(f"  Type: {handler['type']}")
    printLog(f"  Level: {handler['level']}")
    if 'filename' in handler:
      printLog(f"  File: {handler['filename']}")
    if 'formatter' in handler:
      printLog("  Formatter:")
      printLog(f"    Format: {handler['formatter']['format']}")
      printLog(f"    DateFmt: {handler['formatter']['datefmt']}")
  printLog("=" * 50)

def getLoggingConfig() -> Dict[str, Any]:
  """
  Get the current logging configuration as a dictionary.
  
  Returns:
    Dict containing the current logging configuration
  """
  root = logging.getLogger()
  
  return {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
      'level': logging.getLevelName(root.getEffectiveLevel()),
      'handlers': [h.__class__.__name__ for h in root.handlers]
    },
    'handlers': {
      h.__class__.__name__: {
        'class': h.__class__.__name__,
        'level': logging.getLevelName(h.level),
        'formatter': 'default',
        **(({'filename': h.baseFilename} if isinstance(h, logging.FileHandler) else {}))
      } for h in root.handlers
    },
    'formatters': {
      'default': {
        'format': root.handlers[0].formatter._fmt if root.handlers else 'Unknown',
        'datefmt': root.handlers[0].formatter.datefmt if root.handlers else 'Unknown'
      }
    }
  }


def printLog(msg):

  # Import time module for working with timestamps
  import time
  # Import timezone from pytz for handling timezone conversions
  from pytz import timezone
  # Import datetime class for date/time operations
  from datetime import datetime 
  # Import psutil for process information
  import psutil

  process_metadata = psutil.Process()
  
  try:
    msg = f"{datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y/%m/%d %H:%M:%S %Z')}" \
          + f"\t{getppid()}:{getpid()}" \
          + f"\t{inspect.stack()[2][1][len(abspath('.'))+1:]}:{inspect.stack()[2][2]}\t{inspect.stack()[2][3]}" \
          + f"\t{inspect.stack()[1][1][len(abspath('.'))+1:]}:{inspect.stack()[1][2]}\t{inspect.stack()[1][3]}" \
          + f"\t{msg}"
  except:
    msg = f"{datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y/%m/%d %H:%M:%S %Z')}" \
          + f"\t{getppid()}:{getpid()}" \
          + f"\t{inspect.stack()[1][1][len(abspath('.'))+1:]}:{inspect.stack()[1][2]}\t{inspect.stack()[1][3]}" \
          + f"\t{msg}"
  
  print(msg)

  return msg

def get_local_stack_info(countI):
    try:
        return f"{inspect.stack()[countI+1][1][len(abspath('.'))+1:]}:{inspect.stack()[countI+1][2]}:{inspect.stack()[countI+1][3]}"
    except IndexError:
        return "Unknown location"
    
def get_remote_stack_info(countI):
    try:
        return f"{inspect.stack()[countI+2][1][len(abspath('.'))+1:]}:{inspect.stack()[countI+2][2]}:{inspect.stack()[countI+2][3]}"
    except IndexError:
        return "Unknown remote"

def logMsg(msg):
    skip_functions = {
        "logInfo", "logError", "logTrace", "logUnitTest", "logDebug", 
        "logWarn", "logCritical", "raiseValueError", "logSleeping",
        "logException", "logExceptionWithValueError",
        "logMsg",  "logMsgForException", 
        "loadJson",  "iterateValue", "printeValue", "recuseValue",
        "getData", "getItem", "putItemW", "deleteItem", 
        "getItemWithS3", "putItemWithS3","deleteItemWithS3", 
        "displayItemDetails", "setLogLevel",
        "getResponse", "iterateResponse",
        "printDictionary"
    }

    countI = 0
    for stackItem in inspect.stack():
        if stackItem.function not in skip_functions:
          break
        countI += 1

    local_stack_info = get_local_stack_info(countI)
    remote_stack_info = get_remote_stack_info(countI)
    
    return f"\t{getppid()}:{getpid()}\t{remote_stack_info}\t{local_stack_info}\t{msg}"

def logMsgForException(msg=None):
  # Retrieve the current exception information
  exc_type, exc_obj, exc_tb = sys.exc_info()
  f = exc_tb.tb_frame
  lineno = exc_tb.tb_lineno
  filename = f.f_code.co_filename[len(abspath("./"))+1:]

  # Initialize the stack counter
  countI = 0
  
  # Iterate through the call stack to find the caller function
  countI_list = []
  for stackItem in inspect.stack():
    if stackItem.function in ["logException", "logExceptionWithValueError", "logMsgForException"]:
      countI_list.append(countI)
    countI += 1
  
  if len(countI_list) > 0:
    countI = countI_list[-1]
  
  # Define a helper function to format the message
  def format_msg(extra_info=""):
    nonlocal msg
    
    path_len = len(abspath('.'))
    caller_info = f"{filename}:{lineno}:{f.f_code.co_name}"
    try:
      remote_info = f"{inspect.stack()[countI+3][1][path_len:]}:{inspect.stack()[countI+3][2]}:{inspect.stack()[countI+3][3]}"
      local_info = f"{inspect.stack()[countI+2][1][path_len:]}:{inspect.stack()[countI+2][2]}:{inspect.stack()[countI+2][3]}"
      exception_info = f"{remote_info}\t{local_info}\tEXCEPTION IN ({caller_info}) \"{exc_type}: {exc_obj}\""
    except:
      try:
        local_info = f"{inspect.stack()[countI+2][1][path_len:]}:{inspect.stack()[countI+2][2]}:{inspect.stack()[countI+2][3]}"
        exception_info = f"{local_info}\tEXCEPTION IN ({caller_info})() \"{exc_type}: {exc_obj}\""
      except:
        exception_info = f"EXCEPTION IN ({caller_info})({filename}:{lineno}) \"{exc_type}: {exc_obj}\""
    
    return f"\t{getppid()}:{getpid()}\t{exception_info}{extra_info}"
  
  # Format the message based on whether a custom message was provided
  if msg is None:
      msg = format_msg()
  else:
      msg = format_msg(extra_info=f" -> ERROR:[{msg}]")
  
  return msg

def getLogFilename():
    """Retrieve the filename of the first logging handler."""
    try:
        return logging.getLogger().handlers[0].baseFilename
    except (IndexError, AttributeError):
        return None

def setLogLevel(logLevel):
    """Set the logging level for the root logger."""
    logPriorityNumber = getLogPriorityNumber(logLevel)
    logging.getLogger().setLevel(logPriorityNumber)
    logDebug("logLevel:[{}]({}) is set".format(logLevel, logging.getLogger().level))

def getLogPriorityNumber(logLevel):
    """Convert a log level string to a logging level number."""
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARN": logging.WARN,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    return log_levels.get(logLevel, logging.INFO)
    
def logDebug(msg):
  if logging.getLogger().level <= logging.DEBUG:
    logging.debug(logMsg(msg))
  
  return msg
  
def logInfo(msg):
  if logging.getLogger().level <= logging.INFO:
    logging.info(logMsg(msg))
  
  return msg
  
def logWarn(msg):
  if logging.getLogger().level <= logging.WARN:
    logging.warn(logMsg(msg))
  
  return msg
  
def logError(msg):
  if logging.getLogger().level <= logging.ERROR:
    logging.error(logMsg(msg))
  
  return msg

def raiseValueError(msg, sleep=0):
  __beginTime__ = time.time()
  
  if logging.getLogger().level <= logging.ERROR:
    logging.error(logMsg(msg))

    if isinstance(sleep, int) or isinstance(sleep, float):
      if sleep > 0:
       if sleep < 1:
        time.sleep()
       else:
        count = 0
        while count < sleep:
          logging.critical(logMsg(f"===========>..... awakinging in {(sleep - count):,} seconds .....<==========="))
          count += 1
          time.sleep(count - (time.time() - __beginTime__))
        elapsedTime = time.time() - __beginTime__
        #logDebug(f"elaped time:{elapsedTime}")
    
    raise ValueError(msg)

def logException(msg = ""):
  if logging.getLogger().level <= logging.ERROR:
    errMsg = logMsgForException(msg)
    logging.exception(errMsg)
  
  return errMsg

def logExceptionWithValueError(msg = ""):
  if logging.getLogger().level <= logging.ERROR:
    errMsg = logMsgForException(msg)
    logging.exception(errMsg)
    raise ValueError(errMsg)

def logCritical(msg):
  if logging.getLogger().level <= logging.CRITICAL:
    logging.critical(logMsg(msg))
  
  return msg

def logSleeping(seconds, msg=None):
  if logging.getLogger().level <= logging.CRITICAL:
    
    if isinstance(seconds, int) or isinstance(seconds, float):

      if msg is not None:
        if isinstance(msg, dict) or isinstance(msg, list):
          from graphcode.debug import iterateValue
          iterateValue(value=msg, depth=0, maxDepth=3)
        else:
          logDebug(msg) 

      count = 0
      __beginTime__ = time.time()
      while count < seconds:
        logging.critical(logMsg(f"===========>..... awakinging in {(seconds - count):,} seconds .....<==========="))
        count += 1
        time.sleep(count - (time.time() - __beginTime__))
      elapsedTime = time.time() - __beginTime__
      logDebug(f"elaped time:{elapsedTime}")
    
    else:
      if msg is not None:
        logDebug(msg)   

  return msg
