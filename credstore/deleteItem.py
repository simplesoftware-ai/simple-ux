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

from graphcode.logging import logCritical, logError, logWarn, logInfo, logDebug, logException, logExceptionWithValueError, raiseValueError

from graphcode.itemDB import GcItemDB
from graphcode.itemDB.getItem import getData, decryptThenDecompressData

def deleteItemRequest(request_dict):
  
  if "t" not in request_dict['attributes'].keys():
    request_dict['attributes']['t'] = request_dict['apiName'].split(".")[0]
  
  if "p" not in request_dict['attributes'].keys():
    request_dict['attributes']['p'] = {request_dict['metadata']['orgName']}
  else:
    if request_dict['attributes']['p'] in ['global']:
      #request_dict['attributes']['p'] = f"{request_dict['attributes']['p']}"
      pass
    elif request_dict['attributes']['p'] in ['user']:
      request_dict['attributes']['p'] = f"{request_dict['metadata']['userName']}/{request_dict['attributes']['p']}"
    else:
      request_dict['attributes']['p'] = f"{request_dict['metadata']['orgName']}/{request_dict['attributes']['p']}"

  thisData = f"{request_dict['attributes']['t']}/{request_dict['attributes']['p']}.{request_dict['attributes']['k']}"
  logDebug("thisData:{}".format(thisData))

  return deleteItem(
    table=request_dict['attributes']['t'], 
    key=f"{request_dict['attributes']['p']}.{request_dict['attributes']['k']}", 
    cipherKey='DEFAULT-CIPHER-KEY'
    )

def deleteItem(table, key, cipherKey='DEFAULT-CIPHER-KEY'):
  getDataResponse_dict = getData(
    table=table, 
    key=key
    )
  
  #for thisKey in getDataResponse_dict.keys():
  #  logDebug("getDataResponse_dict[{}]:[{}]".format(thisKey, getDataResponse_dict[thisKey]))
  
  manifest_dict_data = decryptThenDecompressData(data=getDataResponse_dict["data"], cipherKey=cipherKey)
  #for thisKey in manifest_dict_data.keys():
  #  logDebug("manifest_dict_data[{}]:[{}]".format(thisKey, manifest_dict_data[thisKey]))
  
  manifest_dict = manifest_dict_data["data"]
  #for thisKey in manifest_dict.keys():
  #  logDebug("manifest_dict_data[{}]:[{}]".format(thisKey, manifest_dict[thisKey]))
  
  deletedItem_list = []
  if manifest_dict["isPaginatedData"]:
    for cipherKey in manifest_dict["cipherKeys"]:
      
      try:
        deletedItem_list.append(
          deleteData(
            table=table, 
            key="__{}_paginatingId_{}__".format(key, len(deletedItem_list)),
            )
          )
      except:
        deletedItem_list.append(
          logException("failed to delete key:[{}]".format("__{}_paginatingId_{}__".format(key, len(deletedItem_list))))
          )

  deletedItem_list.append(
    deleteData(
      table=table, 
      key=key
      )
    )
  
  return {
      "status_code": 200,
      "deletedItems": deletedItem_list
    }

def deleteData(table, key):
  gcItemDB = GcItemDB()

  try:
    return {
      "status_code": 200,
      "key": gcItemDB.delete(
        table = table, 
        key=key
        ),
      "status":"deleted"
      }
  except:
    logExceptionWithValueError("failed to delete {}/{}".format(table, key))

  