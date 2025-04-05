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
from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug
from graphcode.logging import logException, logExceptionWithValueError, raiseValueError

from pado.render.search_form import renderSearchForm
from pado.render.top_menu_dropdown import renderTopMenuDropdown
from pado.render.search_dropdown import renderSearchDropdown
from pado.render.alert_dropdown import renderAlertDropdown
from pado.render.message_dropdown import renderMessageDropdown
from pado.render.user_dropdown import renderUserDropdown
from pado.render.side_head import renderSideHead
from pado.render.side_body import renderSideBody
from pado.render.side_footer import renderSideFooter
from pado.render.main import renderMain
from pado.render.footer import renderFooter
from pado.render.elements.modal import renderModals

from pado.lib import getRuleName
from pado.lib import getRulePath
from pado.lib import getTemplateName
from pado.lib import loadResponsePackage

import os
from os.path import join, isdir, exists

def listDirRecursively(dirPath):
  dir_list = []
  if isdir(dirPath):
    for dirName in os.listdir(dirPath):
      fullDirPath = join(dirPath, dirName)

      # process if it's directory
      if isdir(fullDirPath) \
        and (dirName.startswith("__root__") or not dirName.startswith("__")):

          logDebug(f"adding[{fullDirPath}]")
          dir_list.append(fullDirPath)
          dir_list.extend(listDirRecursively(fullDirPath))

  return dir_list

def loadTemplate(fullDirPath):
  with open(join(fullDirPath, 'template.html'), 'r') as f:
    return f.read()

def renderHtml(fullDirPath):
  templateHtml = loadTemplate(fullDirPath)
  logDebug(f"template: loaded [{join(fullDirPath, 'template.html')}]")
  # render - top bar
  renderedHtml = renderSearchForm(templateHtml)
  renderedHtml = renderTopMenuDropdown(renderedHtml)
  renderedHtml = renderSearchDropdown(renderedHtml)
  renderedHtml = renderAlertDropdown(renderedHtml)
  renderedHtml = renderMessageDropdown(renderedHtml)
  renderedHtml = renderUserDropdown(renderedHtml)

  # render - left nav
  renderedHtml = renderSideBody(renderedHtml)

  # render - side nav
  renderedHtml = renderSideHead(renderedHtml)
  renderedHtml = renderSideBody(renderedHtml)
  renderedHtml = renderSideFooter(renderedHtml)

  # render - main
  renderedHtml = renderMain(renderedHtml, fullDirPath)

  # render - footer
  renderedHtml = renderFooter(renderedHtml, fullDirPath)
  
  # render - modals
  renderedHtml = renderModals(renderedHtml, fullDirPath)

  return renderedHtml

def loadTopDropdownTemplate(fullDirPath):
  topDropdownPath =join(fullDirPath, "topDropdown.html")
  try:
    with open(topDropdownPath, 'r') as f:
      topDropdownHtml = f.read()
  except IOError as e:
    logError(f"Error reading file {topDropdownPath}: {str(e)}")
    topDropdownHtml = None
  
  return topDropdownHtml

def renderTemplates(ruleHome, templateDir='templates'):
  ruleHomeDir = join(os.getcwd(), ruleHome)

  rule_dict = {}
  for fullDirPath in listDirRecursively(ruleHomeDir):
    logDebug(f"fullPath:[{fullDirPath}]")
    
    rulePath = getRulePath(fullDirPath, ruleHomeDir)
    logDebug(f"rulePath:[{rulePath}]")

    templateName = getTemplateName(fullDirPath, ruleHomeDir)
    logDebug(f"templateName:[{templateName}]")
    
    try:
      templateHtml = renderHtml(fullDirPath)
      try:
        with open(join(os.getcwd(), f"{templateDir}/{templateName}.html"), 'w') as f:
          f.write(templateHtml)

        view = loadResponsePackage(fullDirPath)
        logDebug(f"{rulePath} loaded [{view}]")
        rule_dict[rulePath] = {
            "rule": getRuleName(rulePath),
            "endpoint": templateName,
            "template": f"{templateName}.html",
            "view_func": view.response,
            "methods": ['GET', 'POST']
        }
      except IOError as e:
        logError(f"Error reading file {join(fullDirPath, 'template.html')}: {str(e)}")

        from codex.e500.response import response as e500Response
        rule_dict[rulePath] = {
            "rule": getRuleName(rulePath),
            "endpoint": templateName,
            "template": "e500.html",
            "view_func": e500Response,
            "methods": ['GET']
        }
        continue
    except Exception as e:
      logError(f"failed to render template: {str(e)}")
      from codex.___root__.response import response
      rule_dict[rulePath] = {
        "rule": getRuleName(rulePath),
        "endpoint": templateName,
        "template": "e404.html",
        "view_func": response,
        "methods": ['GET']
      }
      continue

  return rule_dict