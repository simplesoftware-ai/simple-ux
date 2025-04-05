
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

def renderBox(element_dict, fullDirPath):
  width = getWidth(element_dict)
  title = getTitle(element_dict)
  content = getContent(element_dict)
  image = getImage(element_dict)
  
  return f"""
      <!-- Begin: Card -->
        <div class="col-lg-6 col-xl-{width} mb-4">
            <div class="card h-100">
                <div class="card-body h-100 p-5">
                    <div class="row align-items-center">
                        <div class="col-xl-8 col-xxl-12">
                            <div class="text-center text-xl-start text-xxl-center mb-4 mb-xl-0 mb-xxl-4">
                                <h1 class="text-primary">{title}</h1>
                                <p class="text-gray-700 mb-0">{content}</p>
                            </div>
                        </div>
                        <div class="col-xl-4 col-xxl-12 text-center"><img class="img-fluid" """ +""" src="{{ url_for('static', filename='""" + image +"""') }}" style="max-width: 26rem" /></div>
                    </div>
                </div>
            </div>
        </div>
      <!-- End: Card -->
"""