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
from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug
from graphcode.logging import logException, logExceptionWithValueError, raiseValueError

from os import getcwd
from os.path import join, basename, dirname

def getRuleNameScheme(ruleName):
  return ruleName.strip().replace(' ', '-').replace("\\","/").lower()

def getRuleName(dirName):
  if dirName.startswith("__"):
    if dirName in ["__root__"]:
      #logDebug(f"Processing directory: {dirName}\t->\truleName:[/]")
      return "/"
    else:
      #logDebug(f"Processing directory: {dirName}\t->\truleName:[None]")
      return None
  else:
    #logDebug(f"Processing directory: {dirName}\t->\truleName:[/{dirName}]")
    return f"{getRuleNameScheme(dirName)}"

def getRulePath(fullDirPath, ruleHomeDir):
  rulePath = fullDirPath.replace(ruleHomeDir, "")
  if rulePath in ["/__root__"]:
    return "/"
  else:
    return rulePath
  
def getTemplateName(fullDirPath, ruleHomeDir):
  if basename(fullDirPath) in ["__root__"]:
    #logDebug(f"Processing directory: {rulePath}\t->\truleName:[/]")
    return "index"
  else:
    #logDebug(f"Processing directory: {rulePath}\t->\truleName:[{rulePath}]")
    return getRuleNameScheme(fullDirPath.replace(ruleHomeDir, ""))[1:].replace("/", "-")

def getEndpoint(rulePath):
  endpoint = dirname(rulePath).replace(join(getcwd(), getConfProxy()['pado']['rule']),"")
  if endpoint in ["/__root__"]:
    return "index"
  else:
    return endpoint[1:].replace("/","-")

def loadResponsePackage(fullDirPath):
  responsePath = fullDirPath.replace(getcwd(), "")[1:].replace("/", ".")
  
  response = __import__(f"{responsePath}.response", fromlist=[''])
  
  return response