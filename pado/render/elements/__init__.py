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
from graphcode.logging import setConfProxy
from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug, logSleeping
from graphcode.logging import logException, logExceptionWithValueError, raiseValueError

def getType(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    return element_dict['type']
  except:
    return "text"
  
def getMethod(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    return element_dict['method']
  except:
    return "get"

def getWidth(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['width'] is None:
      width = ""
    else:
      width = f"{element_dict['width']}"
  except:
    width = ""
  
  return width

def getRows(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['rows'] is None:
      rows = ""
    else:
      rows = f"{element_dict['rows']}"
  except:
    rows = ""
  
  return rows

def getValue(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['value'] is None:
      value = ""
    else:
      value = element_dict['value']
  except:
    value = ""
  
  return value

def getOptions(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['options'] is None:
      options = []
    else:
      options = element_dict['options']
  except:
    options = []
  
  return options

def getPlaceholder(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['placeholder'] is None:
      placeholder = ""
    else:
      placeholder = element_dict['placeholder']
  except:
    placeholder = ""
  
  return placeholder

def getPosition(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['position'] in ['right']:
      position = " text-md-end"
    elif element_dict['position'] in ['center']:
      position = " text-md-center"
    else:
      position = " text-start"
  except:
    position = " text-start"
  
  return position

def getIcon(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['icon'] is None:
      icon = ""
    elif element_dict['icon'] in ['(C)']:
      icon = "&copy;"
    else:
      icon = element_dict['icon']
  except:
    icon = ""
  
  return icon

def getDelimiter(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['delimiter']:
      delimiter = "&nbsp;"
    else:
      delimiter = ""
  except:
    delimiter = ""
  
  return delimiter

def getTitle(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['title'] is None:
      title = ""
    else:
      title = element_dict['title']
  except:
    title = ""
  
  return title

def getSubTitle(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['subtitle'] is None:
      subtitle = ""
    else:
      subtitle = element_dict['subtitle']
  except:
    subtitle = ""

  return subtitle

def getLabel(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['label'] is None:
      label = ""
    else:
      label = element_dict['label']
  except:
    label = ""

  return label

def getLabels(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['labels'] is None:
      labels = ""
    else:
      labels = element_dict['labels']
  except:
    labels = ""

  return labels

def setIdNamingScheme(label):
  id = ""
  isCapital = False
  for char in label:
    if char.isalnum():
      if id == "":
        id += char.lower()
      elif isCapital:
        id += char.upper()
        isCapital = False
      else:
        id += char
    elif char == ' ':
      isCapital = True
    else:
      id += '-'
  
  return id

def getId(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['id'], str):
      id = element_dict['id']
    else:
      id = ""
  except:
    id = ""

  if id == "":
    id = setIdNamingScheme(getLabel(element_dict))
  return id

def getRows(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['rows'] is None:
      rows = ""
    else:
      rows = element_dict['rows']
  except:
    rows = ""

  return rows

def getContent(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['content'] is None:
      content = ""
    else:
      content = element_dict['content']
  except:
    content = ""

  return content

def getId(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['id'], str):
      id = element_dict['id']
    else:
      id = ""
  except:
    id = ""

  if id == "":
    id = setIdNamingScheme(getLabel(element_dict))

  return id

def getImage(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['image'] is None:
      image = ""
    else:
      image = element_dict['image']
  except:
    image = ""

  return image

def getTarget(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if element_dict['target'] is None:
      target = None
    elif len(element_dict['target'].strip()) == 0:
      target = "#!"
    else:
      target = element_dict['target']
  except:
    target = "#!"

  return target

def getActions(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['actions'], list):
      actions = element_dict['actions']
    else:
      actions = ""
  except:
    actions = ""

  return actions

def getEffect(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['effect'], str):
      effect = element_dict['effect']
    else:
      effect = ""
  except:
    effect = ""

  return effect

def getSolid(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['solid'], bool):
      if element_dict['solid']:
        solid = " solid"
      else:
        solid = ""
    else:
      solid = ""
  except:
    solid = ""

  return solid

def getRequired(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['required'], bool):
      if element_dict['required']:
        if getDisabled(element_dict) in [' disabled']:
          logWarn("'disabled' conflicts with 'required'")
          required = ""
        else:
          required = " required"
      else:
        required = ""
    else:
      required = ""
  except:
    required = ""

  return required

def getDisabled(element_dict):
  # logDebug(f"element_dict: {element_dict}")
  try:
    if isinstance(element_dict['disabled'], bool):
      if element_dict['disabled']:
        disabled = " disabled"
      else:
        disabled = ""
    else:
      disabled = ""
  except:
    disabled = ""

  return disabled