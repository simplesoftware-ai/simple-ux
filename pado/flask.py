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
from graphcode.logging import getConfProxy, setConfProxy
from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug
from graphcode.logging import logException, logExceptionWithValueError, raiseValueError

from pado.render import renderTemplates
from pado.filters.iterate import iterate

from multiprocessing import Manager
from flask import Flask

import os
from os.path import join

def startApp(
    appName=__name__, 
    ruleHome='codex',
    staticDir='static', 
    templateDir='templates',
    port='5025'):

  app = Flask(
    appName, 
    static_folder=staticDir, 
    template_folder=templateDir
    )
  logDebug(f"app.name:[{app.name}]")
  logDebug(f"app.static_folder:[{app.static_folder}]")
  logDebug(f"app.template_folder:[{app.template_folder}]")
  
  app.add_template_filter(iterate)

  rule_dict = renderTemplates(
    ruleHome = ruleHome,
    templateDir = templateDir
  )
  
  for rulePath, ruleItem_dict in rule_dict.items():
    logDebug(f"[{rulePath}]:[{ruleItem_dict}]")

    app.add_url_rule(
      rule = ruleItem_dict['rule'],
      endpoint = ruleItem_dict['endpoint'],
      view_func = ruleItem_dict['view_func'],
      methods = ruleItem_dict['methods']
      )

  return app
