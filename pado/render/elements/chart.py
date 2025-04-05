
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

from pado.render.elements import getType, getIcon, getWidth, getTitle, getSubTitle, getLabel, getContent, getId, getImage, getTarget
from pado.render.elements.dropdown import renderDropdownElements

def renderChart(element_dict, fullDirPath):
  width = getWidth(element_dict)
  title = getTitle(element_dict)
  id = getId(element_dict)
  image = getImage(element_dict)
  
  try:
    dropdownElementHtml = renderDropdownElements(dropdownElement_list=element_dict['actions'])
  except Exception as e:
    logError("failed to render dropdown menu -> Error:[{e}]")
    dropdownElementHtml = ""

  return f"""
      <!-- Begin: Chart -->
        <div class="col-xl-{width} mb-4">
            <div class="card card-header-actions h-100">
                <div class="card-header">
                    {title}
                    <div class="dropdown no-caret">
                        <button class="btn btn-transparent-dark btn-icon dropdown-toggle" id="areaChartDropdownExample" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="text-gray-500" data-feather="more-vertical"></i></button>
                        <div class="dropdown-menu dropdown-menu-end animated--fade-in-up" aria-labelledby="areaChartDropdownExample">
                            {dropdownElementHtml}
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="chart-area"><canvas id="{id}" width="100%" height="30"></canvas></div>
                </div>
            </div>
        </div>
      <!-- End: Chart -->
"""
