
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

from pado.render.elements import getType, getMethod
from pado.render.elements import getIcon, getWidth, getRows
from pado.render.elements import getValue, getPlaceholder
from pado.render.elements import getOptions
from pado.render.elements import getTitle, getSubTitle
from pado.render.elements import getLabel, getId
from pado.render.elements import getContent, getImage
from pado.render.elements import getTarget, getActions
from pado.render.elements import getSolid
from pado.render.elements import getRequired, getDisabled
from pado.render.elements.cardActions import renderCardActions

from os.path import join

import json

def loadFormJson(fullDirPath):
  formJsonPath =join(fullDirPath, "form.json")
  try:
    return json.load(open(formJsonPath, "r"))
  except IOError as e:
    logException(f"Error loading {formJsonPath}: {str(e)}")
    return None

def getForm(title, fullDirPath):
  form_dict = loadFormJson(fullDirPath)
  if title in form_dict.keys():
    return form_dict[title]
  elif title.lower() in form_dict.keys():
    return form_dict[title.lower()]
  else:
    return form_dict['default']

def getElementAttributes(elementItem_dict):
  width = getWidth(elementItem_dict)
  if width in [""]:
    widthTag = ""
  else:
    widthTag = f"col-lg-{width}"

  return {
    "type":getType(elementItem_dict),
    "label":getLabel(elementItem_dict),
    "id": getId(elementItem_dict),
    "type":getType(elementItem_dict),
    "icon":getIcon(elementItem_dict),
    "width": width,
    "widthTag": widthTag,
    "rows": getRows(elementItem_dict),
    "value": getValue(elementItem_dict),
    "options": getOptions(elementItem_dict),
    "placeholder": getPlaceholder(elementItem_dict),
    "solid": getSolid(elementItem_dict),
    "required":getRequired(elementItem_dict),
    "disabled":getDisabled(elementItem_dict)
  }

def renderTextElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  valueTag=f" value=\"{{{{ codex.inputs.{attr_dict['id']} }}}}\""
  textHtml = f"""
                          <div class="{attr_dict['widthTag']}">
                            <label for="{attr_dict['id']}InputForm">{attr_dict['label']}</label>
                            <input class="form-control" type="{attr_dict['type']}" id="{attr_dict['id']}InputForm" name="{attr_dict['id']}" placeholder="{attr_dict['placeholder']}" {valueTag}{attr_dict['required']}{attr_dict['disabled']}>
                          </div>"""
  return textHtml

def renderEmailElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  valueTag=f" value=\"{{{{ codex.inputs.{attr_dict['id']} }}}}\""
  textHtml = f"""
                          <div class="{attr_dict['widthTag']}">
                            <label for="{attr_dict['id']}InputForm">{attr_dict['label']}</label>
                            <input class="form-control" type="{attr_dict['type']}" id="{attr_dict['id']}InputForm" name="{attr_dict['id']}" placeholder="{attr_dict['placeholder']}" {valueTag}{attr_dict['required']}{attr_dict['disabled']}>
                          </div>""" + """
                          <script>
                            // Function to validate email address
                            function validateEmail(email) {
                              const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                              return regex.test(email);
                            }

                            // Add event listener to the form
                            document.getElementById('""" + f"{attr_dict['id']}InputForm" +"""').addEventListener('input', function(event) {
                              const emailInput = this.value;
                              const messageId = this.id + 'Message';
                              let message = document.getElementById(messageId);
                              
                              if (!message) {
                                message = document.createElement('div');
                                message.id = messageId;
                                this.parentNode.appendChild(message);
                              }

                              if (validateEmail(emailInput)) {
                                message.style.color = 'green';
                                message.textContent = 'Email is valid!';
                              } else {
                                message.style.color = 'red';
                                message.textContent = 'Please enter a valid email address.';
                              }
                            });
                          </script>
                          """
  return textHtml

def renderSearchElement(elementItem_dict):
  textAreaHtml = ""
  ""
  return textAreaHtml

def renderTextAreaElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  textAreaHtml = f"""
                          <div class="mb-0 {attr_dict['widthTag']}">
                            <label for="{attr_dict['id']}Textarea">{attr_dict['label']}</label>
                            <textarea class="form-control" id="{attr_dict['id']}Textarea" name="{attr_dict['id']}" rows="{attr_dict['rows']}">{{{{ codex.inputs.{attr_dict['id']} }}}}</textarea>
                          </div>"""
  return textAreaHtml

def renderSelectElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  
  optionsHtml = ""
  if isinstance(attr_dict['options'], list):
    optionsHtml += """
                              {% for option in """ + f"codex.options.{attr_dict['id']}" + """ %}
                                {% if option == """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                  <option selected>{{ option }}</option>
                                {% else %}
                                  <option>{{ option }}</option>
                                {% endif %}
                              {% endfor %}"""

  elif isinstance(attr_dict['options'], str):
    if len(attr_dict['options'].strip()) > 2:
      if attr_dict['options'][0] in ['{'] and attr_dict['options'][-1] in ['}']:
        optionsHtml += """
                              {% for option in """ + f"{attr_dict['options']}" + """ %}
                                {% if option == """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                  <option selected>{{ option }}</option>
                                {% else %}
                                  <option>{{ option }}</option>
                                {% endif %}
                              {% endfor %}"""
      else:
        optionsHtml += f"""
                                  <option>{attr_dict['options']}</option>"""
        
    else:
      logWarn(f"invalid options for {type(attr_dict['options']).__name__}:{attr_dict['id']}:[{attr_dict['options']}]")

  selectHtml = f"""
                          <div class="{attr_dict['widthTag']}">
                            <label for="{attr_dict['id']}FormControlSelect">{attr_dict['label']}</label>
                            <select class="form-control" id="{attr_dict['id']}FormControlSelect" name="{attr_dict['id']}">
                              {optionsHtml}
                            </select>
                          </div>
  """
  return selectHtml

def renderMultiSelectElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  
  optionsHtml = ""
  if isinstance(attr_dict['options'], list):
    optionsHtml += """
                              {% for option in """ + f"codex.options.{attr_dict['id']}" + """ %}
                                {% if option in """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                  <option selected>{{ option }}</option>
                                {% else %}
                                  <option>{{ option }}</option>
                                {% endif %}
                              {% endfor %}"""

  elif isinstance(attr_dict['options'], str):
    if len(attr_dict['options'].strip()) > 2:
      if attr_dict['options'][0] in ['{'] and attr_dict['options'][-1] in ['}']:
        optionsHtml += """
                              {% for option in """ + f"{attr_dict['options']}" + """ %}
                                {% if option in """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                  <option selected>{{ option }}</option>
                                {% else %}
                                  <option>{{ option }}</option>
                                {% endif %}
                              {% endfor %}"""
      else:
        optionsHtml += f"""
                                  <option>{attr_dict['options']}</option>"""
        
    else:
      logWarn(f"invalid options for {type(attr_dict['options']).__name__}:{attr_dict['id']}:[{attr_dict['options']}]")

  multipleSelectHtml = f"""
                          <div class="{attr_dict['widthTag']}">
                            <label for="{attr_dict['id']}FormControlSelect">{attr_dict['label']}</label>
                            <select class="form-control" id="{attr_dict['id']}FormControlSelect" name="{attr_dict['id']}" multiple="">
                              {optionsHtml}
                            </select>
                          </div>
  """
  return multipleSelectHtml

def renderCheckboxElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  
  checkBoxHtml = ""
  if isinstance(attr_dict['options'], list):
    checkBoxHtml += f"""
                          <div class="{attr_dict['widthTag']}">"""+"""
                              {% for option in """ + f"codex.options.{attr_dict['id']}" + """ %}
                                {% if option in """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                    <div class="form-check">
                                        """ + f"""<input class="form-check-input" id="{attr_dict['id']}CheckBox"  name="{attr_dict['id']}" type="checkbox" value="{{{{ option }}}}" checked>
                                        <label class="form-check-label" for="{attr_dict['id']}CheckBox">{{{{ option }}}}</label>
                                    </div>""" + """
                                {% else %}
                                  <div class="form-check">
                                      """+f"""<input class="form-check-input" id="{attr_dict['id']}CheckBox"  name="{attr_dict['id']}" type="checkbox" value="{{{{ option }}}}">
                                      <label class="form-check-label" for="{attr_dict['id']}CheckBox">{{{{ option }}}}</label>
                                  </div>""" + """
                                {% endif %}
                              {% endfor %}
                          </div>"""
    
  return checkBoxHtml

def renderRadioElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  
  radioHtml = ""
  if isinstance(attr_dict['options'], list):
    radioHtml += f"""
                          <div class="{attr_dict['widthTag']}">"""+"""
                              {% for option in """ + f"codex.options.{attr_dict['id']}" + """ %}
                                {% if option in """+ f"codex.inputs.{attr_dict['id']}" + """ %}
                                    <div class="form-check" class="col-lg-3">
                                        """ + f"""<input class="form-check-input" id="{attr_dict['id']}CheckBox"  name="{attr_dict['id']}" type="radio" value="{{{{ option }}}}" checked>
                                        <label class="form-check-label" for="{attr_dict['id']}CheckBox">{{{{ option }}}}</label>
                                    </div>""" + """
                                {% else %}
                                  <div class="form-check">
                                      """+f"""<input class="form-check-input" id="{attr_dict['id']}CheckBox"  name="{attr_dict['id']}" type="radio" value="{{{{ option }}}}">
                                      <label class="form-check-label" for="{attr_dict['id']}CheckBox">{{{{ option }}}}</label>
                                  </div>""" + """
                                {% endif %}
                              {% endfor %}
                          </div>"""
    
  return radioHtml

def renderSwitchElement(elementItem_dict):
  attr_dict = getElementAttributes(elementItem_dict)
  switchHtml = f"""
                <div class="form-check form-switch {attr_dict['widthTag']}">
                <input class="form-check-input" type="checkbox" id="{attr_dict['id']}Switch" name="{attr_dict['id']}" {{% if codex.inputs.{attr_dict['id']} %}}checked{{% endif %}} {attr_dict['required']}{attr_dict['disabled']}>
                <label class="form-check-label" for="{attr_dict['id']}Switch">{attr_dict['label']}</label>
                </div>"""
  return switchHtml

def renderRangeElement(elementItem_dict):
  rangeHtml = ""
  ""
  return rangeHtml

def renderFileElement(elementItem_dict):
  fileHtml = ""
  ""
  return fileHtml

def renderButtonElement(elementItem_dict):
  buttonHtml = ""
  ""
  return buttonHtml

def renderSubmitElement(elementItem_dict):
  submitHtml = ""
  ""
  return submitHtml

def renderFormElements(form_dict):
  formElementHtml = """
                      <div class="mb-1">
                        <div class="row"> <!-- begin: form row -->"""
  
  for elementItem_dict in form_dict['elements']:
    _type = getType(elementItem_dict)

    if _type in ['text']:
      formElementHtml += renderTextElement(elementItem_dict)
    
    if _type in ['email']:
      formElementHtml += renderEmailElement(elementItem_dict)
    
    elif _type in ['search']: # extended type
      formElementHtml += renderSearchElement(elementItem_dict)
    
    elif _type in ['textarea']:
      formElementHtml += renderTextAreaElement(elementItem_dict)
    
    elif _type in ['select']:
      formElementHtml += renderSelectElement(elementItem_dict)
    
    elif _type in ['multiselect']: # extended type
      formElementHtml += renderMultiSelectElement(elementItem_dict)
    
    elif _type in ['checkbox']:
      formElementHtml += renderCheckboxElement(elementItem_dict)
    
    elif _type in ['radio']:
      formElementHtml += renderRadioElement(elementItem_dict)
    
    elif _type in ['switch']: # extended type
      formElementHtml += renderSwitchElement(elementItem_dict)
    
    elif _type in ['range']:
      formElementHtml += renderRangeElement(elementItem_dict)
    
    elif _type in ['file']:
      formElementHtml += renderFileElement(elementItem_dict)
    
    elif _type in ['button']:
      formElementHtml += renderButtonElement(elementItem_dict)
    
    elif _type in ['submit']:
      formElementHtml += renderSubmitElement(elementItem_dict)
    
    elif _type in ['divider']:
      formElementHtml += """
                        </div> <!-- end: form row -->
                      </div>
                      <div class="mb-1">
                        <div class="row"> <!-- begin: form row -->"""
    
    else:
      logWarn(f"Unknown element type: {_type}")

  formElementHtml += """
                        </div> <!-- end: form row -->
                      </div>"""
    
  return f"""
                      {formElementHtml}
                      <div class="mt-3">
                          <button type="submit" class="btn btn-primary">Submit</button>
                      </div>
"""
  
def renderStanardForm(form_dict):
  formElementHtml = renderFormElements(form_dict)
  
  method = getMethod(form_dict)
  if method.lower() in ['get', 'post']:
    method = f" method=\"{method.lower()}\"" 
  else:
    method = ""

  action = getTarget(form_dict)
  if action == "#!":
    action = f""
  else:
    action = f" action=\"{action.strip()}\"" 

  return f"""
                  <form{method}{action}>
                    <input type='hidden' name='atk' value='"""+"{% if codex.atk %}{{ codex.atk }}{% endif %}"+f"""' />
                  {formElementHtml}
                  </form>"""

def renderAjaxForm(form_dict):
  formElementHtml = renderFormElements(form_dict)

  return f"""
                  <form id="ajaxForm" onsubmit="submitForm(event)">
                    {formElementHtml}
                  </form>"""+"""
                  <script>
                    function submitForm(e) {
                      e.preventDefault();
                      const formData = new FormData(document.getElementById('ajaxForm'));
                      fetch('/form', {
                        method: 'POST',
                        body: formData
                      })
                      .then(response => response.json())
                      .then(data => {
                        console.log('Success:', data);
                      })
                      .catch((error) => {
                        console.error('Error:', error);
                      });
                    }
                  </script>
"""
  return formHtml

def renderFormCard(title, fullDirPath):
  form_dict = getForm(title, fullDirPath)
  _type = getType(form_dict)

  if _type in ['ajax']:
    return renderAjaxForm(form_dict)
  else:
    return renderStanardForm(form_dict)
  
def renderForm(element_dict, fullDirPath):
  width = getWidth(element_dict)
  title = getTitle(element_dict)
    
  formHtml = renderFormCard(title, fullDirPath)
  actionsHtml = renderCardActions(element_dict)
  
  return f"""
      <!-- Begin: Card -->
        <div class="col-lg-6 col-xl-{width} mb-4">
            <div class="card card-header-actions h-100">
                <div class="card-header">
                    {title}
                    {actionsHtml}
                </div>
                <div class="card-body">
                    {formHtml}
                </div>
            </div>
        </div>
      <!-- End: Card -->
"""
