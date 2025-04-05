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
from graphcode.logging import getConfProxy
from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug, logSleeping
from graphcode.logging import logException, logExceptionWithValueError, raiseValueError

from pado.render.elements import getType
from pado.render.elements import getValue, getId
from pado.render.elements import getOptions

from pado.lib import getEndpoint

from flask import make_response, render_template

from os import getcwd
from os.path import dirname, basename, join

import json
from uuid import uuid4

class Response:
  def __init__(self, request, rulePath):
    self.request = request
    logDebug(f"self.request:[{self.request}]")

    endpoint = getEndpoint(rulePath)
    logDebug(f"endpoint:[{endpoint}]")
    
    form_dict = self.loadInuptForm(rulePath)
    self.codex_dict = {
      "atk": uuid4(),
      "debug": True,
      "endpoint": endpoint,
      "form": form_dict,
      "inputs": self.getInputValues(form_dict),
      "options": self.getOptionValues(form_dict),
      "conf": dict(getConfProxy()),
      **self.loadMetaData(rulePath)
      }
    
    if "title" not in self.codex_dict.keys():
      self.codex_dict["title"] = self.codex_dict["name"]

  def loadInuptForm(self, rulePath):
    logDebug(f"loaded: [{join(dirname(rulePath), 'form.json')}]")
    try:
      return json.load(open(join(dirname(rulePath), 'form.json'), 'r'))
    except:
      logException(f"failed to load: [{join(dirname(rulePath), 'form.json')}]")
      return {}

  def loadMetaData(self, rulePath):
    logDebug(f"loaded: [{join(dirname(rulePath), 'metadata.json')}]")
    try:
      return json.load(open(join(dirname(rulePath), 'metadata.json'), 'r'))
    except:
      logException(f"failed to load: [{join(dirname(rulePath), 'metadata.json')}]")
      return {}
      
  def getInputValues(self, form_dict):
    if self.request.method == 'GET':
      input_dict = self.request.args.to_dict()
    elif self.request.method == 'POST':
      input_dict = self.request.form.to_dict()
    
    value_dict = {}
    for formName in form_dict.keys():
      try:
        for formItem_dict in form_dict[formName]['elements']:
          try:
            _type = getType(formItem_dict)
            id = getId(formItem_dict)
            
            if 'atk' in input_dict.keys():
              value_dict['atk'] = input_dict['atk']
              if _type in ['multiselect','checkbox'] and id not in value_dict.keys():
                value_dict[id] = self.request.args.getlist(id)
              
              elif _type in ['switch']:
                if id in input_dict.keys() and input_dict[id] == "on":
                  value_dict[id] = True
                else:
                  value_dict[id] = False

              else:
                value_dict[id] = input_dict[id]

            else:
              if _type in ['switch']:
                if getValue(formItem_dict) == True:
                  value_dict[id] = True
                else:
                  value_dict[id] = False
              else:
                value_dict[id] = getValue(formItem_dict)
            
          except:
            logException(f"failed to get value for: [{getId(formItem_dict)}]")
            continue
      except:
        logException(f"failed to iterate form elements for: [{formName}]")
        continue
    
    return value_dict
    
  def getOptionValues(self, form_dict):
    option_dict = {}
    for formName in form_dict.keys():
      try:
        for formItem_dict in form_dict[formName]['elements']:
          try:
            option_list = getOptions(formItem_dict)
            if len(option_list) > 0:
              option_dict[getId(formItem_dict)] = getOptions(formItem_dict)
          except:
            logException(f"failed to get value for: [{getId(formItem_dict)}]")
            continue
      except:
        logException(f"failed to iterate form elements for: [{formName}]")
        continue

    return option_dict
    
def getCodex(request, rulePath):
  return Response(request, rulePath).codex_dict
  
def render(codex_dict):
  return make_response(
    render_template(
      f"{codex_dict['endpoint']}.html", 
      codex = codex_dict
    )
  )

def render_500(msg, codex_dict={}):
  return make_response(
    render_template(
      "e500.html",
      codex = {
        "error": msg,
        **codex_dict
      }
    )
  )

def responseHandler(request, action, rulePath):
  try:
    codex_dict = getCodex(request = request, rulePath = rulePath)
    logDebug(f"codex_dict:[{codex_dict}]")
    try:
      return render(action(codex_dict))
    except Exception as e:
      # Get line number where error occurred
      return render_500(logException(), codex_dict) # 500 Internal Server Error (default)
  except Exception as e:
    # Get line number where error occurred
    from graphcode.logging import getConfProxy
    return render_500(logException(), {"title":"index", "description":f"{e}", "conf":dict(getConfProxy())}) # 500 Internal Server Error (default)
  

