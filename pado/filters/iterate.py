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
def iterate(value):
  resultTag = ""
  try:
    if isinstance(value, dict):
      for key in value.keys():
        if key in ["outputs", "charts"]:
          resultTag += "<b>{}</b>:<br>".format(key)
          for key2 in value[key].keys():
            if key2 in ["wbResults", "charts"]:
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2)
            
            elif isinstance(value[key][key2], dict):
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2)
              for key3 in value[key][key2].keys():
                resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:{}<br>".format(key3, value[key][key2][key3])
            else:
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:{}<br>".format(key2, value[key][key2])
        elif key in ["profileSelect"]:
          resultTag += "<b>{}</b>:<br>".format(key)
          for key2 in value[key].keys():
            resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2, len(value[key][key2]))
            
        elif key in ["jsCharts"]:
          resultTag += "<b>{}</b>:len:{:,}<br>".format(key, len(value[key]))
        else:
          resultTag += "<b>{}</b>:{}<br>".format(key, value[key])
    else:
      resultTag = json.dump(value)
  except Exception as e:
    resultTag =  logException("Error:[{}]->unable to unpack value:[{}]".format(e, value))
  
  if len(resultTag) > 25000:
    resultTag = "size:{:,}Bytes<br>displaying the first 25K in the value:<br>{}..........{}".format(len(resultTag),resultTag[:25000],resultTag[-1000:])
    
  return resultTag