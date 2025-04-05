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

from graphcode.path import findFilePath

from pado.lib import getRuleNameScheme

import json

def renderSideMenu():
  conf_proxy = getConfProxy()
  #logDebug(f"conf_proxy:[{conf_proxy}]")
  
  # Load the leftnav.json file
  leftnav_dict = json.load(open(findFilePath('sidenav.json'), 'r'))
  #logDebug(f"leftnav_dict.keys():[{leftnav_dict.keys()}]")

  indent = 8
  html = ""
  for headName in leftnav_dict.keys():
    if headName.startswith("__"):
      logWarn(f"skipping: [{headName}]")
      continue
    else:
      html += addHeadHtml(indent, headName)
    
    #logDebug(f"{headName}:[{leftnav_dict[headName]}]")
    if isAccordionItem(accordion_dict=leftnav_dict[headName]):
      #logDebug(f"headName:[{headName}]:\tProcessing accordion")
      html += getAccordionHtml(indent, accordion_dict=leftnav_dict[headName])
    # else:
    #   logDebug(f"headName: [{headName}]:\t is not an accordion")

  #logDebug(f"thisHtml:[\n{html}]")

  return html
  
def getIcon(accordionItem_dict):
  # This block attempts to get the icon value from the nested dictionary structure
  # If the '__badge__' key doesn't exist, it catches the exception and sets icon to None
  try:
    # - Attempts to extract the '__icon__' value from the accordion dictionary for the current accordion name
    # - Removes the '__icon__' key after extracting its value
    # - If removing '__icon__' leaves an empty dictionary, sets that accordion entry to None
    # - If '__icon__' key doesn't exist, catches exception and sets icon to None
    icon = accordionItem_dict['__icon__']
    del accordionItem_dict['__icon__']
  except:
    icon = None
  
  return icon

def getBadge(accordionItem_dict):
  # This block attempts to get the icon value from the nested dictionary structure
  # If the '__badge__' key doesn't exist, it catches the exception and sets icon to None
  try:
    # - Attempts to extract the '__badge__' value from the accordion dictionary for the current accordion name
    # - Removes the '__badge__' key after extracting its value
    # - If removing '__badge__' leaves an empty dictionary, sets that accordion entry to None
    # - If '__badge__' key doesn't exist, catches exception and sets badge to None
    badge = accordionItem_dict['__badge__']
    del accordionItem_dict['__badge__']
  except:
    badge = None
  
  return badge

def getParentPath(accordionPath):
  return accordionPath[1:-len(accordionPath.split("/")[-1])-1].replace("/","").replace(" ", "")

def getNavName(navName):
  return navName.replace(" ", "")

def addIndent(indent, html):
  html = f"{'\t'*indent}{html}\n"
  #logDebug(html)
  return html

def addHeadHtml(indent, headName):
  html  = addIndent(indent, f"<!-- Sidenav Menu Heading ({headName})-->")
  html += addIndent(indent, f"<div class=\"sidenav-menu-heading\">{headName}</div>")

  #logDebug(f"{headName}:[\n{html}]")
  return html

def addAccordionHtml(indent, accordionName, accordionPath, icon, badge):
  parentPath = getParentPath(accordionPath)
  if len(parentPath) > 0:
    html  = addIndent(indent, f"<!-- Nested Sidenav Accordion Menu ({parentPath}:{accordionName})-->")
  else:
    html  = addIndent(indent, f"<!-- Sidenav Accordion Menu ({accordionName})-->")

  html += addIndent(indent, f"<a class=\"nav-link collapsed\" href=\"javascript:void(0);\" data-bs-toggle=\"collapse\" data-bs-target=\"#collapse{getNavName(accordionName)}\" aria-expanded=\"false\" aria-controls=\"collapse{getNavName(accordionName)}\">")
  if icon is not None:
    html += addIndent(indent +1, f"<div class=\"nav-link-icon\"><i data-feather=\"{icon}\"></i></div>")
  html += addIndent(indent +1, f"{accordionName}")
  html += addIndent(indent +1, f"<div class=\"sidenav-collapse-arrow\"><i class=\"fas fa-angle-down\"></i></div>")
  html += addIndent(indent, f"</a>")

  #logDebug(f"{accordionName}:[\n{html}]")
  return html

def addNestedAccordionItemsHtml(indent, accordionName, accordionPath, accordionItem_dict):
  #logDebug(f"accordionItem_dict:[{accordionItem_dict}]")
  
  parentPath = getParentPath(accordionPath)
  if len(parentPath) > 0:
    html = addIndent(indent, f"<nav class=\"sidenav-menu-nested nav accordion\" id=\"accordionSidenav{getNavName(parentPath)}{getNavName(accordionName)}\">")
  else:
    html = addIndent(indent, f"<nav class=\"sidenav-menu-nested nav accordion\" id=\"accordionSidenav{getNavName(accordionName)}\">")
  
  for itemName in accordionItem_dict.keys():
    if not itemName.startswith("__"):
      if isNestedAccordionItem(accordionItem_dict[itemName]):  
        #logDebug(f"parentPath:[{parentPath}]")
        if len(parentPath) > 0:
          html += addIndent(indent +1, f"<!-- Nested Sidenav Accordion ({parentPath} -> {accordionName} -> {itemName}) -->")
          html += addIndent(indent /1, f"<a class=\"nav-link collapsed\" href=\"javascript:void(0);\" data-bs-toggle=\"collapse\" data-bs-target=\"#pagesCollapse{getNavName(itemName)}\" aria-expanded=\"false\" aria-controls=\"pagesCollapse{getNavName(itemName)}\">")
          
        else:
          html += addIndent(indent +1, f"<!-- Nested Sidenav Accordion ({accordionName} -> {itemName}) -->")
          html += addIndent(indent +1, f"<a class=\"nav-link collapsed\" href=\"javascript:void(0);\" data-bs-toggle=\"collapse\" data-bs-target=\"#pagesCollapse{getNavName(itemName)}\" aria-expanded=\"false\" aria-controls=\"pagesCollapse{getNavName(itemName)}\">")

        html += addIndent(indent +2, f"{itemName}")
        html += addIndent(indent +2, f"<div class=\"sidenav-collapse-arrow\"><i class=\"fas fa-angle-down\"></i></div>")
        html += addIndent(indent +1, f"</a>")

        #logDebug(f"rulePath:[{accordionName}/{itemName}]")
        icon = getIcon(accordionItem_dict[itemName])
        badge = getBadge(accordionItem_dict[itemName])

        html += addIndent(indent +1, f"<div class=\"collapse\" id=\"pagesCollapse{getNavName(itemName)}\" data-bs-parent=\"#accordionSidenav{getNavName(accordionName)}Menu\">")
        html += addNestedAccordionItemsHtml(indent +2, itemName, f"{accordionPath}/{itemName}", accordionItem_dict[itemName])
        html += addIndent(indent +1, f"</div>")

      elif isAccordionItem(accordionItem_dict[itemName]):  
        if len(parentPath) > 0:
          html += addIndent(indent +1, f"<!-- Nested Sidenav Accordion ({parentPath} -> {accordionName} -> {itemName}) -->")
          html += addIndent(indent +1, f"<a class=\"nav-link collapsed\" href=\"javascript:void(0);\" data-bs-toggle=\"collapse\" data-bs-target=\"#pagesCollapse{getNavName(accordionName)}{getNavName(itemName)}\" aria-expanded=\"false\" aria-controls=\"pagesCollapse{getNavName(accordionName)}{getNavName(itemName)}\">")
          
        else:
          html += addIndent(indent +1, f"<!-- Nested Sidenav Accordion ({accordionName} -> {itemName}) -->")
          html += addIndent(indent +1, f"<a class=\"nav-link collapsed\" href=\"javascript:void(0);\" data-bs-toggle=\"collapse\" data-bs-target=\"#pagesCollapse{getNavName(itemName)}\" aria-expanded=\"false\" aria-controls=\"pagesCollapse{getNavName(itemName)}\">")

        html += addIndent(indent +2, f"{itemName}")
        html += addIndent(indent +2, f"<div class=\"sidenav-collapse-arrow\"><i class=\"fas fa-angle-down\"></i></div>")
        html += addIndent(indent +1, f"</a>")

        if len(parentPath) > 0:
          html += addIndent(indent +1, f"<div class=\"collapse\" id=\"pagesCollapse{getNavName(accordionName)}{getNavName(itemName)}\" data-bs-parent=\"#accordionSidenav{parentPath}{getNavName(accordionName)}\">")
          html += addAccordionNavHtml(indent +2, itemName, accordionItem_dict[itemName], f"{parentPath}/{accordionName.lower().replace(' ', '-')}")
        else:
          html += addIndent(indent +1, f"<div class=\"collapse\" id=\"pagesCollapse{getNavName(itemName)}\" data-bs-parent=\"#accordionSidenav{getNavName(accordionName)}Menu\">")
          html += addAccordionNavHtml(indent +2, itemName, accordionItem_dict[itemName], accordionName.lower().replace(" ","-"))

        html += addIndent(indent +2, f"</div>")
      
      else:
        html += addAccordionNavItemHtml(indent +1, itemName, f"{accordionPath}/{itemName}", icon, badge)

  html += addIndent(indent, f"</nav>")

  #logDebug(f"{accordionName}:[\n{html}]")
  return html

def addAccordionNavHtml(indent, accordionName, accordionItem_dict, parentPath):
  html = addIndent(indent +1, f"<nav class=\"sidenav-menu-nested nav\"><!--addAccordionNavHtml(): {parentPath} -->")
  for navName in accordionItem_dict.keys():
    if not navName.startswith("__"):
      icon = getIcon(accordionItem_dict[navName])
      badge = getBadge(accordionItem_dict[navName])
      html += addAccordionNavItemHtml(indent +2, navName, f"/{parentPath}/{accordionName}/{navName}", icon, badge)
  html += addIndent(indent+1, f"</nav>")

  #logDebug(f"{accordionName}:[\n{html}]")
  return html
  
def addAccordionNavItemHtml(indent, navName, navPath, icon, badge):
  if badge is not None:
    html  = addIndent(indent, f"<a class=\"nav-link\" href=\"{getRuleNameScheme(navPath)}\">")
    html += addIndent(indent +1, f"{navName}")
    html += addIndent(indent +1, f"<span class=\"badge bg-primary-soft text-primary ms-auto\">{badge}</span>")
    html += addIndent(indent, f"</a>")
  
  else:
    html  = addIndent(indent, f"<a class=\"nav-link\" href=\"{getRuleNameScheme(navPath)}\">{navName}</a>")

  ##logDebug(f"{navName}:[\n{html}]")
  return html

def addNavHtml(indent, navName, navPath, icon, badge):
  html  = addIndent(indent, f"<!-- Sidenav Link ({navName})-->")
  html += addIndent(indent, f"<a class=\"nav-link\" href=\"{getRuleNameScheme(navPath)}\">")
  if icon is not None:
    html += addIndent(indent +1, f"<div class=\"nav-link-icon\"><i data-feather=\"{icon}\"></i></div>")
  html += addIndent(indent +1, f"{navName}")
  html += addIndent(indent, f"</a>")

  #logDebug(f"{navName}:[\n{html}]")
  return html

def addNavItemsHtml(indent, accordionName, accordionPath, accordionItem_dict):
  parentPath = getParentPath(accordionPath)
  html = addIndent(indent +1, f"<nav class=\"sidenav-menu-nested nav\"><!--addNavItemsHtml():{parentPath}:{accordionItem_dict} -->")
  for navName in accordionItem_dict.keys():
    if not navName.startswith("__"):
      icon = getIcon(accordionItem_dict[navName])
      badge = getBadge(accordionItem_dict[navName])
      html += addAccordionNavItemHtml(indent +2, navName, f"/{accordionName}/{navName}", icon, badge)
  html += addIndent(indent+1, f"</nav>")

  #logDebug(f"{accordionName}:[\n{html}]")
  return html

def isAccordionItem(accordion_dict):  # This code checks if a dictionary represents an accordion menu structure
  # It returns True if any item in the dictionary:
  # 1. Has a non-__ prefixed key
  # 2. Contains a nested dictionary
  # 3. Has either:
  #    - Both __icon__ and __badge__ keys with additional keys
  #    - Just __icon__ with additional keys  
  #    - Just __badge__ with additional keys
  #    - Just additional keys
  # Returns False otherwise
  if not isinstance(accordion_dict, dict):
    #logDebug(f"unexpected {type(accordion_dict).__name__}:accordion_dict:[{accordion_dict}]")
    return False
  
  if "__icon__" in accordion_dict.keys():
    #logDebug(f"'icon' found")
    if "__badge__" in accordion_dict.keys():
      #logDebug(f"'badge' found")
      if len(accordion_dict.keys()) > 2:
        #logDebug(f"accordion_dict.keys():[{accordion_dict.keys()}]")
        return True
      # else:
      #   isAccordionFound = False
    elif len(accordion_dict.keys()) > 1:
      #logDebug(f"accordion_dict.keys():[{accordion_dict.keys()}]")
      return True
      
    # else:
    #   isAccordionFound = False
  
  elif "__badge__" in accordion_dict.keys():
    if len(accordion_dict.keys()) > 1:

      #logDebug(f"accordion_dict.keys():[{accordion_dict.keys()}]")
      return True
    
    # else:
    #   isAccordionFound = False

  elif len(accordion_dict.keys()) > 0:
    #logDebug(f"accordion_dict.keys():[{accordion_dict.keys()}]")
    return True
  
  else:
    #logDebug(f"accordion_dict.keys():[{accordion_dict.keys()}]")
    return False

def isNestedAccordionItem(accordion_dict):
  #logDebug(f"accordion_dict:[{accordion_dict}]")
  
  # Check if the input accordion_dict is a dictionary type
  # Returns False if it's not a dictionary, since only dictionaries can represent accordion menus
  if not isinstance(accordion_dict, dict):
    #logDebug(f"unexpected {type(accordion_dict).__name__}:accordion_dict:[{accordion_dict}]")
    return False
  
  isAccordionFound = False
  for itemName in accordion_dict.keys():
    ##logDebug(f"itemName:[{itemName}]")
    if not itemName.startswith("__"):
      if isAccordionItem(accordion_dict[itemName]):
        #logDebug(f"{itemName} is an accordion")
        return True
        
      #<-end: if isinstance(accordion_dict[itemName], dict):
    #<-end: if not itemName.startswith("__"):
  #<-end: for itemName in accordion_dict.keys():

  return isAccordionFound
      

def getAccordionHtml(indent, accordion_dict):

  html = ""
  for accordionName in accordion_dict.keys():
    #logDebug(f"accordionName:[{accordionName}]")

    if not accordionName.startswith("__"):
      # This section extracts the dictionary for the current accordion item
      accordionItem_dict = accordion_dict[accordionName]

      # Get the icon and badge values from the accordion item dictionary
      # getIcon() and getBadge() handle extracting these special properties
      # and cleaning up the dictionary afterwards
      icon = getIcon(accordionItem_dict)
      badge = getBadge(accordionItem_dict)

      if isAccordionItem(accordionItem_dict):
        #logDebug(f"{accordionName} is an accordion")
        #logDebug(f"accordion_dict[{accordionName}]:[{accordionItem_dict}]")
        
        #logDebug(f"{accordionName}:[{accordionItem_dict.keys()}]")
        if isNestedAccordionItem(accordionItem_dict):
          #logDebug(f"{accordionName} is an accordion menu")
          html += addAccordionHtml(indent, accordionName, f"/{accordionName}", icon, badge)

          html += addIndent(indent, f"<div class=\"collapse\" id=\"collapse{getNavName(accordionName)}\" data-bs-parent=\"#accordionSidenav\">")
          html += addNestedAccordionItemsHtml(indent +1, accordionName, f"/{accordionName}", accordionItem_dict)
          html += addIndent(indent, f"</div>")
          
        else:
          html += addAccordionHtml(indent, accordionName, f"/{accordionName}", icon, badge)
          html += addIndent(indent, f"<div class=\"collapse\" id=\"collapse{getNavName(accordionName)}\" data-bs-parent=\"#accordionSidenav\">")

          #logDebug(f"{accordionName} is not an accordion menu")
          html += addNavItemsHtml(indent +1, accordionName, f"/{accordionName}", accordionItem_dict)

          html += addIndent(indent, f"</div>")
      
      
      else:
        #logDebug(f"{accordionName} is not an accordion")
        html += addNavHtml(indent, accordionName, f"/{accordionName}", icon, badge)

  return html            