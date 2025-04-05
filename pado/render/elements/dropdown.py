
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

from pado.render.elements import getType, getIcon, getDelimiter, getTitle, getSubTitle, getLabel, getTarget, getEffect

def renderDropdownLink(dropdownElementItem_dict): 
  icon = getIcon(element_dict=dropdownElementItem_dict)
  if icon != "":
    icon = f"<i data-feather=\"{icon}\"></i>"

  effect = getEffect(element_dict=dropdownElementItem_dict)

  divider = getDelimiter(element_dict=dropdownElementItem_dict)

  target = getTarget(element_dict=dropdownElementItem_dict)
  if target is None:
    target = "#!"

  label = getLabel(element_dict=dropdownElementItem_dict)
  if effect is None:
    return f"{'\t'*7}<a class=\"dropdown-item\" href=\"{target}\">{icon}{divider}{label}</a>\n"
  else:
    return f"{'\t'*7}<a class=\"dropdown-item\" href=\"{target}\"><span class=\"{effect}\">{icon}{divider}{label}</span></a>\n"

def renderDropdownModal(dropdownElementItem_dict): 
  icon = getIcon(element_dict=dropdownElementItem_dict)
  if icon != "":
    icon = f"<i data-feather=\"{icon}\"></i>"

  divider = getDelimiter(element_dict=dropdownElementItem_dict)

  target = getTarget(element_dict=dropdownElementItem_dict)

  label = getLabel(element_dict=dropdownElementItem_dict)
  return f"{'\t'*7}<a class=\"dropdown-item\" href=\"#!\" data-bs-toggle=\"modal\" data-bs-target=\"#{target}\">{icon}{divider}{label}</a>\n"
  
def renderDropdownElements(dropdownElement_list):
  if isinstance(dropdownElement_list, list):
    dropdownElementHtml = ""
    for dropdownElementItem_dict in dropdownElement_list:
      if getType(dropdownElementItem_dict) in ['modal']:
        dropdownElementHtml += renderDropdownModal(dropdownElementItem_dict)
        # logSleeping(10, dropdownElementHtml)
      elif getType(dropdownElementItem_dict) in ['divider']:
        dropdownElementHtml += f"{'\t'*7}<div class=\"dropdown-divider\"></div>\n"
      else:
        dropdownElementHtml += renderDropdownLink(dropdownElementItem_dict)
        # logSleeping(10, dropdownElementHtml)
    
    return dropdownElementHtml
  else:
    logWarn(f"dropdownElement_list is not a list: {type(dropdownElement_list).__name__}:dropdownElement_list:{dropdownElement_list}")
    return ""

def renderDropdown(elementName, elementValue_dict):
  dropdownElementHtml = renderDropdownElements(elementValue_dict['elements'])
  return f"""
                <!-- Begin: {elementName} -->
                <div class="col-12 col-xl-auto mt-4">
                    <div class="dropdown">
                        <button class="btn btn-success dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{elementName}</button>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <!-- Begin: dropdown menu links -->
                            {dropdownElementHtml}
                            <!-- End: dropdown menu links -->
                        </div>
                    </div>
                </div>
                <!-- End: {elementName} -->"""