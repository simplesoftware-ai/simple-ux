
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

def renderTimeline(element_dict, fullDirPath):
  width = getWidth(element_dict)
  title = getTitle(element_dict)
  content = getContent(element_dict)
  image = getImage(element_dict)
  
  return f"""
      <!-- Begin: Card -->
        <div class="col-lg-6 col-xl-{width} mb-4">
            <div class="card card-header-actions h-100">
                <div class="card-header">
                    {title}
                    <div class="dropdown no-caret">
                        <button class="btn btn-transparent-dark btn-icon dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="text-gray-500" data-feather="more-vertical"></i></button>
                        <div class="dropdown-menu dropdown-menu-end animated--fade-in-up" aria-labelledby="dropdownMenuButton">
                            <h6 class="dropdown-header">Filter Activity:</h6>
                            <a class="dropdown-item" href="#!"><span class="badge bg-green-soft text-green my-1">Commerce</span></a>
                            <a class="dropdown-item" href="#!"><span class="badge bg-blue-soft text-blue my-1">Reporting</span></a>
                            <a class="dropdown-item" href="#!"><span class="badge bg-yellow-soft text-yellow my-1">Server</span></a>
                            <a class="dropdown-item" href="#!"><span class="badge bg-purple-soft text-purple my-1">Users</span></a>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="timeline timeline-xs">
                        <!-- Timeline Item 1-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">27 min</div>
                                <div class="timeline-item-marker-indicator bg-green"></div>
                            </div>
                            <div class="timeline-item-content">
                                New order placed!
                                <a class="fw-bold text-dark" href="#!">Order #2912</a>
                                has been successfully placed.
                            </div>
                        </div>
                        <!-- Timeline Item 2-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">58 min</div>
                                <div class="timeline-item-marker-indicator bg-blue"></div>
                            </div>
                            <div class="timeline-item-content">
                                Your
                                <a class="fw-bold text-dark" href="#!">weekly report</a>
                                has been generated and is ready to view.
                            </div>
                        </div>
                        <!-- Timeline Item 3-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">2 hrs</div>
                                <div class="timeline-item-marker-indicator bg-purple"></div>
                            </div>
                            <div class="timeline-item-content">
                                New user
                                <a class="fw-bold text-dark" href="#!">Valerie Luna</a>
                                has registered
                            </div>
                        </div>
                        <!-- Timeline Item 4-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">1 day</div>
                                <div class="timeline-item-marker-indicator bg-yellow"></div>
                            </div>
                            <div class="timeline-item-content">Server activity monitor alert</div>
                        </div>
                        <!-- Timeline Item 5-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">1 day</div>
                                <div class="timeline-item-marker-indicator bg-green"></div>
                            </div>
                            <div class="timeline-item-content">
                                New order placed!
                                <a class="fw-bold text-dark" href="#!">Order #2911</a>
                                has been successfully placed.
                            </div>
                        </div>
                        <!-- Timeline Item 6-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">1 day</div>
                                <div class="timeline-item-marker-indicator bg-purple"></div>
                            </div>
                            <div class="timeline-item-content">
                                Details for
                                <a class="fw-bold text-dark" href="#!">Marketing and Planning Meeting</a>
                                have been updated.
                            </div>
                        </div>
                        <!-- Timeline Item 7-->
                        <div class="timeline-item">
                            <div class="timeline-item-marker">
                                <div class="timeline-item-marker-text">2 days</div>
                                <div class="timeline-item-marker-indicator bg-green"></div>
                            </div>
                            <div class="timeline-item-content">
                                New order placed!
                                <a class="fw-bold text-dark" href="#!">Order #2910</a>
                                has been successfully placed.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      <!-- End: Card -->
"""