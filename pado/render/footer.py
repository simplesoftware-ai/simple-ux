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

from pado.render.elements import getType, getWidth, getPosition, getIcon, getTitle, getSubTitle, getLabel, getTarget

from os.path import join

import json

def loadFooterJson(fullDirPath):
  footerJsonPath = join(fullDirPath, "footer.json")
  try:
    return json.load(open(footerJsonPath, "r"))
  except IOError as e:
    logDebug(f"Footer configuration not found at {footerJsonPath}, using default")
    # Return default footer configuration
    return {
      "Copyright": {
        "icon": " <i data-feather=\"copyright\"></i>",
        "width": "12",
        "position": "",
        "title": " © 2025 ESCROVA LLC",
        "target": None
      },
      "Privacy": {
        "icon": " <i data-feather=\"shield\"></i>",
        "width": "12",
        "position": "",
        "title": " Privacy Policy",
        "target": "#!"
      },
      "Terms": {
        "icon": " <i data-feather=\"file-text\"></i>",
        "width": "12",
        "position": "",
        "title": " Terms of Service",
        "target": "#!"
      }
    }

def loaFooterTemplate(fullDirPath):
  footerTemplatePath =join(fullDirPath, "footer.html")
  try:
    with open(footerTemplatePath, 'r') as f:
      footerHtml = f.read()
  except IOError as e:
    logException(f"Error reading file {footerTemplatePath}: {str(e)}")
    footerHtml = None
  
  return footerHtml

def renderFooterItem(itemName, itemValue_dict):
  icon = getIcon(itemValue_dict)
  width = getWidth(itemValue_dict)
  position = getPosition(itemValue_dict)
  title = getTitle(itemValue_dict)
  target = getTarget(itemValue_dict)

  if target is not None:
    return f"\n{" "*6}<div class=\"col-md-{width}{position} small\"><a href=\"{target}\">{itemName}{icon}{title}</a></div>"
    
  else:
    return f"\n{" "*6}<div class=\"col-md-{width}{position} small\">{itemName}{icon}{title}</div>"

def renderFooterElements(fullDirPath):
  footer_dict = loadFooterJson(fullDirPath)
  
  if footer_dict is None:
    logDebug("No footer configuration available")
    return ""

  renderedHtml = ""
  for itemName, itemValue_dict in footer_dict.items():
    try:
      renderedHtml += renderFooterItem(itemName, itemValue_dict)
    except Exception as e:
      logError(f"Error rendering footer item {itemName}: {str(e)}")
   
  return renderedHtml
    
def renderFooter(html, fullDirPath):
  try:
    footerElementHtml = renderFooterElements(fullDirPath)

    footerHtml = loaFooterTemplate(fullDirPath)
    return html.replace(
            '${__footer__}',
            footerHtml.replace("${__main_footer__}", footerElementHtml)
    )
  
  except:
    return html.replace(
        '${__footer__}', """
                        <div class="container-xl px-4">
                            <!-- Begin: Footer Row -->
                            <div class="row">
                                <div class="col-md-6 small">Copyright &copy; ESCROVA LLC 2024</div>
                                <div class="col-md-6 text-md-end small">
                                    <a href="#!">Privacy Policy</a>
                                    &middot;
                                    <a href="#!">Terms &amp; Conditions</a>
                                </div>
                            </div>
                            <!-- End: Footer Row -->
                        </div>
        """)