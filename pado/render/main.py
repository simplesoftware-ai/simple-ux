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

from pado.render.main_header import renderMainHeader
from pado.render.main_body import renderMainBody

from os.path import join

import json

def loadMainJson(fullDirPath):
  mainJsonPath =join(fullDirPath, "main.json")
  try:
    return json.load(open(mainJsonPath, "r"))
  except IOError as e:
    logException(f"Error loading {mainJsonPath}: {str(e)}")
    return None

def loadMainTemplate(fullDirPath):
  mainTemplatePath =join(fullDirPath, "main.html")
  try:
    with open(mainTemplatePath, 'r') as f:
      mainHtml = f.read()
  except IOError as e:
    logException(f"Error reading file {mainTemplatePath}: {str(e)}")
    mainHtml = None
  
  return mainHtml

def renderMain(html, fullDirPath):

  mainHtml = loadMainTemplate(fullDirPath)
  if mainHtml is not None:

    try:
      main_dict = loadMainJson(fullDirPath)
      
      mainHtml = renderMainHeader(mainHtml, header_dict=main_dict['header'], fullDirPath=fullDirPath)
      mainHtml = renderMainBody(mainHtml, bodyElement_list=main_dict['body'], fullDirPath=fullDirPath)
    
    except:
      logError("failed to reder main.html")
    
    return html.replace('${__main__}', mainHtml)
    
  else:
    logError("failed to load main.html")
    return html

  

