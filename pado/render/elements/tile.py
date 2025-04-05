
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

from pado.render.elements import getType, getIcon, getWidth, getTitle, getSubTitle, getLabel, getContent, getImage, getTarget

def getActionHtml(element_dict):
  action_dict = element_dict.get('action', None)
  try:
    if isinstance(action_dict, dict):
      actionType = getType(action_dict)
      target = getTarget(action_dict)
      if actionType in ['modal']:
        return f"""
                        <div class="card-footer d-flex align-items-center justify-content-between small">
                            <a class="text-white stretched-link" href="#!" data-bs-toggle="modal" data-bs-target="#{target}">{action_dict['label']}</a>"
                            <div class="text-white"><i class="fas fa-angle-right"></i></div>
                        </div>\n"""
      else:
        return f"""
                        <div class="card-footer d-flex align-items-center justify-content-between small">
                            <a class="text-white stretched-link" href="{target}">{action_dict['label']}</a>
                            <div class="text-white"><i class="fas fa-angle-right"></i></div>
                        </div>\n"""

    else:
      logWarn(f"{type(action_dict).__name__}:action_dict:[{action_dict}] must be dict")
      return ""
    
  except Exception as e:
    logException(e)
    return ""

def renderTile(element_dict, fullDirPath):
  width = getWidth(element_dict)
  background = element_dict.get('background', 'primary')
  color = element_dict.get('color', 'white')
  icon = getIcon(element_dict)
  title = getTitle(element_dict)
  content = getContent(element_dict)
  image = getImage(element_dict)

  actionHtml = getActionHtml(element_dict)

  return f"""
      <!-- Begin: Card -->
        <div class="col-lg-6 col-xl-{width} mb-4">
            <div class="card bg-{background} text-{color} h-100">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="me-3">
                            <div class="text-white-75 small">{title}</div>
                            <div class="text-lg fw-bold">{content}</div>
                        </div>
                        <i class="feather-xl text-white-50" data-feather="{icon}"></i>
                    </div>
                </div>
                {actionHtml}
            </div>
        </div>
      <!-- End: Card -->
"""