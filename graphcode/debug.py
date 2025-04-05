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

from multiprocessing.managers import DictProxy

import logging

import json

def iterateValue(value, depth=0, maxDepth=3):
  from graphcode.logging import logMsg

  """Iterate through the values recursively and format them as plain text."""
  if depth >= maxDepth:
     logging.critical(logMsg(value))
     return value
      
  if isinstance(value, list):
    for item in value:
      if not isinstance(item, str): 
        iterateValue(value, depth+1, maxDepth)
      else:
        logging.critical(logMsg(item))

  elif isinstance(value, dict):
    for key in value.keys():
      if not isinstance(value[key], str): 
        iterateValue(value[key], depth+1, maxDepth)
      else:
        logging.critical(logMsg(f"depth{depth}:{key}:[{value[key]}]"))
  else:
    logging.critical(logMsg(value))

def printeValue(value, maxDepth=3):
  """Iterate through the values recursively and format them as plain text."""
  plainText = recuseValue(value, maxDepth=maxDepth).strip()
  return plainText

def recuseValue(value, depth=0, maxDepth=3):
  """Recursively process the value based on its type."""
  if depth > maxDepth:
    return json.dumps(value)
  
  plainText = ''
  indent = "\t" * depth
  
  if isinstance(value, dict):
    for key, val in value.items():
      valueType = type(val).__name__
      if isinstance(val, (dict, list)):
        plainText += f'\n{indent}({valueType})\t{key}:{recuseValue(val, depth+1, maxDepth)}'
      else:
        plainText += f"\n{indent}({valueType})\t{key}:[{val}]"
              
  elif isinstance(value, list):
    for i, item in enumerate(value):
      valueType = type(item).__name__
      plainText += f'\n{indent}({valueType})\t[{i}]:{recuseValue(item, depth+1, maxDepth)}'
          
  else:
    valueType = type(value).__name__
    plainText += f"\n{indent}({valueType})\t{value}"
      
  return plainText

def printProxy(conf_proxy):
  for key, value in conf_proxy.items():
    if isinstance(value, DictProxy):
      printLog(f"{key}:{value.keys()}")
    else:
      printLog(f"{key}:[{value}]")