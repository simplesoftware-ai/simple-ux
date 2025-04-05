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

from pado.render.elements import getType, getIcon, getTitle, getSubTitle, getLabel, getTarget

from pado.render.elements.calendar import renderCalendar
from pado.render.elements.dropdown import renderDropdown

def renderText(bodyItemName, bodyItemValue_dict):
  return bodyItemName

def renderMainTitle(mainHeaderHtml, header_dict):
  icon = getIcon(element_dict=header_dict)
  title = getTitle(element_dict=header_dict)
  subtitle = getSubTitle(element_dict=header_dict)

  return mainHeaderHtml.replace("${__main_title__}", f"""
                <div class="col-auto mt-4">
                    <h1 class="page-header-title">
                        <div class="page-header-icon"><i data-feather="{icon}"></i></div>
                        {title}
                    </h1>
                    <div class="page-header-subtitle">{subtitle}</div>
                </div>"""
  )

def renderMainHeaderElement(bodyItemName, bodyItemValue_dict):
  if getType(bodyItemValue_dict) in ['text']:
    return renderText(bodyItemName, bodyItemValue_dict)
  
  elif getType(bodyItemValue_dict) in ['calendar']:
    return renderCalendar(bodyItemName, bodyItemValue_dict)
  
  elif getType(bodyItemValue_dict) in ['dropdown']:
    return renderDropdown(bodyItemName, bodyItemValue_dict)
  
  else:
    logWarn(f"unsupported type:[{getType(bodyItemValue_dict)}]")
    return ""

def renderMainHeaderElements(header_dict):
  mainHeaderHtml = """
    <div class="container-xl px-4">
        <div class="page-header-content pt-4">
            <div class="row align-items-center justify-content-between">
                <!-- Begin: Main Header -->
                ${__main_title__}
                <!-- End: Main Header -->

                <!-- Begin: Main Header Elements -->
                ${__main_header_elements__}
                <!-- End: Main Header Elements -->
            </div>
        </div>
    </div>
"""
  mainHeaderHtml = renderMainTitle(mainHeaderHtml, header_dict)
  
  mainHeaderElementHtml = ""
  for bodyItemName, bodyItemValue_dict in header_dict['body'].items():
    try:
      mainHeaderElementHtml += renderMainHeaderElement(bodyItemName, bodyItemValue_dict)
    #   logSleeping(10, mainHeaderElementHtml)
    except:
      logSleeping(10, logException(bodyItemName))
  
  mainHeaderHtml = mainHeaderHtml.replace("${__main_header_elements__}", mainHeaderElementHtml)
  return mainHeaderHtml

def renderMainHeader(mainHtml, header_dict, fullDirPath):
  try:
    return mainHtml.replace("${__main_header__}", 
                            renderMainHeaderElements(header_dict))
  except:
    return mainHtml.replace("${__main_header__}","""
    <div class="container-xl px-4">
        <div class="page-header-content pt-4">
            <div class="row align-items-center justify-content-between">
                <!-- Begin: Main Header -->
                <div class="col-auto mt-4">
                    <h1 class="page-header-title">
                        <div class="page-header-icon"><i data-feather="activity"></i></div>
                        Landing Page
                    </h1>
                    <div class="page-header-subtitle">Example landing page and components examples</div>
                </div>
                <!-- End: Main Header -->
                <!-- Begin: Search -->
                <div class="col-12 col-xl-auto mt-4">
                    <div class="input-group input-group-joined border-0" style="width: 16.5rem">
                        <span class="input-group-text"><i class="text-primary" data-feather="calendar"></i></span>
                        <input class="form-control ps-0 pointer" id="litepickerRangePlugin" placeholder="Select date range..." />
                    </div>
                </div>
                <!-- End: Search -->
                <!-- Begin: Action -->
                <div class="col-12 col-xl-auto mt-4">
                    <div class="dropdown">
                        <button class="btn btn-success dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Actions</button>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                            <a class="dropdown-item" href="#!" data-bs-toggle="modal" data-bs-target="#exampleModal1">Modal#1 (xlarge/static)</a>
                            <a class="dropdown-item" href="#!" data-bs-toggle="modal" data-bs-target="#exampleModal2">Modal#2 (large)</a>
                            <a class="dropdown-item" href="#!" data-bs-toggle="modal" data-bs-target="#exampleModal3">Modal#3 (standard)</a>
                        </div>
                        <!-- Begin: Modal: exampleModal#1 -->
                        <div class="modal modal-xl fade" id="exampleModal1" data-bs-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Default Bootstrap Modal</h5>
                                        <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <!-- Modal Body -->
                                    <div class="modal-body text-black">
                                        This modal window is included with the Bootstrap framework. The styling has been changed for the Simple UX theme.
                                    </div>
                                    <!-- Modal Footer -->
                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                                        <button class="btn btn-primary" type="button">Save changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End: Modal: exampleModal#1 -->
                        <!-- Begin: Modal: exampleModal#2 -->
                        <div class="modal modal-lg fade" id="exampleModal2" data-bs-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Default Bootstrap Modal</h5>
                                        <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <!-- Modal Body -->
                                    <div class="modal-body text-black">
                                        This modal window is included with the Bootstrap framework. The styling has been changed for the Simple UX theme.
                                    </div>
                                    <!-- Modal Footer -->
                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                                        <button class="btn btn-primary" type="button">Save changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End: Modal: exampleModal#2 -->
                        <!-- Begin: Modal: exampleModal#3 -->
                        <div class="modal fade" id="exampleModal3" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Default Bootstrap Modal</h5>
                                        <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <!-- Modal Body -->
                                    <div class="modal-body text-black">
                                        This modal window is included with the Bootstrap framework. The styling has been changed for the Simple UX theme.
                                    </div>
                                    <!-- Modal Footer -->
                                    <div class="modal-footer">
                                        <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                                        <button class="btn btn-primary" type="button">Save changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End: Modal: exampleModal#3 -->
                    </div>
                </div>
                <!-- End: Action -->
            </div>
        </div>
    </div>
""")