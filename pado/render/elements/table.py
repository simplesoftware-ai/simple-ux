
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

from pado.render.elements import getType, getIcon, getWidth, getTitle, getSubTitle, getLabel, getContent, getId, getLabels, getRows, getImage, getTarget
from pado.render.elements.dropdown import renderDropdownElements

def renderTableElement(id, labels, rows):
  
  return f"""<table id="{id}">
                <thead>
                    <tr>""" + """
                        {% for label in """+ labels +""" %}
                        <th>{{ label }}</th>{% endfor %}""" + """
                    </tr>
                </thead>
                <tfoot>
                    <tr>""" + """
                        {% for label in """+ labels +""" %}
                        <th>{{ label }}</th>{% endfor %}""" + """
                    </tr>
                </tfoot>
                <tbody>
                    {% for row in """+ rows +""" %}
                        <tr>
                        {% for cell in row %}
                            {% if 'Status' in """+ labels +""" %}
                                {% if cell == "Full-time" %}<td><div class="badge bg-primary text-white rounded-pill">{{ cell }}</div></td>
                                {% elif cell == "Pending" %}<td><div class="badge bg-warning rounded-pill">{{ cell }}</div></td>
                                {% elif cell == "Part-time" %}<td><div class="badge bg-secondary text-white rounded-pill">{{ cell }}</div></td>
                                {% elif cell == "Contract" %}<td><div class="badge bg-info rounded-pill">{{ cell }}</div></td>
                                {% else %}<td>{{ cell }}</td>{% endif %}
                            {% else %}<td>{{ cell }}</td>{% endif %}{% endfor %}

                            {% if 'Actions' in """+ labels +""" %}
                            <td>
                                <button class="btn btn-datatable btn-icon btn-transparent-dark me-2"><i class="fa-solid fa-ellipsis-vertical"></i></button>
                                <button class="btn btn-datatable btn-icon btn-transparent-dark" data-bs-toggle="modal" data-bs-target="#deleteRowModal" data-id="{{ row[0] }}"><i class="fa-regular fa-trash-can"></i></button>
                            </td>
                            {% endif %}
                        </tr>
                    {% endfor %}
                </tbody>
            </table>"""

def renderTable(element_dict, fullDirPath):
  width = getWidth(element_dict)
  title = getTitle(element_dict)
  id = getId(element_dict)
  labels = getLabels(element_dict)
  rows = getRows(element_dict)
  image = getImage(element_dict)
  
  try:
    dropdownElementHtml = renderDropdownElements(dropdownElement_list=element_dict['actions'])
  except Exception as e:
    logError("failed to render dropdown menu -> Error:[{e}]")
    dropdownElementHtml = ""
  
  return f"""
    <div class="card mb-4">
        <div class="card-header">{title}</div>
        <div class="card-body">
            {renderTableElement(id, labels, rows)}
        </div>
    </div>
  """