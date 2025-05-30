'''
Peaceful Use License

Copyright (c) 2025 simplesoftware.ai
Copyright (c) 2020-2025 ESCROVA LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

THIS SOFTWARE IS NOT PROVIDED TO ANY ENTITY OR ANY GROUP OR ANY PERSON
TO THREATEN, INCITE, PROMOTE, OR ACTIVELY ENCOURAGE VIOLENCE, TERRORISM,
OR OTHER SERIOUS HARM. IF NOT, THIS SOFTWARE WILL NOT BE PERMITTED TO USE.
IF NOT, THE BENEFITS OF ALL USES AND ALL CHANGES OF THIS SOFTWARE ARE GIVEN
TO THE ORIGINAL AUTHORS WHO OWNED THE COPYRIGHT OF THIS SOFTWARE  ORIGINALLY.
THE CONDITIONS CAN ONLY BE CHANGED BY THE ORIGINAL AUTHORS' AGREEMENT
IN AN ADDENDUM, THAT MUST BE DOCUMENTED AND CERTIFIED IN FAIRNESS MANNER.
'''
from graphcode.logging import printLog
from graphcode.logging import logMsg, logDebug, logException
from graphcode.debug import printProxy

from graphcode.conf import ConfManager

from multiprocessing import Process
from multiprocessing.managers import DictProxy


def confSetProcess(conf_proxy: DictProxy, worker_id: int):
  from graphcode.logging import setConfProxy, initLog
  setConfProxy(conf_proxy)
  initLog()
  logDebug(f"Worker#{worker_id:,}:[{conf_proxy.keys()}]")

  """Worker process that modifies shared data"""
  conf_proxy[f"worker:{worker_id}"] = f"data from worker {worker_id}"

def confConsumerProcess(conf_proxy: DictProxy, worker_id: int):
  from graphcode.logging import setConfProxy, initLog
  setConfProxy(conf_proxy)
  logDebug(f"Worker#{worker_id:,}:[{conf_proxy.keys()}]")
  
  confManager = ConfManager(initLog())
  targetKey = f"worker:{worker_id}"
  logDebug(f"name:[{confManager.get('name')}]\t->\t[{confManager.get(targetKey)}]")
  
def main():
  from graphcode.logging import initLog
  conf_proxy = initLog()

  # Create multiple processes
  p_list = []
  for i in range(3):  # Create 3 worker processes
    p = Process(
      target=confSetProcess, 
      args=(conf_proxy, i,),
      name=f"{conf_proxy['name']}#{i}"
      )
    p.name = f"{conf_proxy['name']}#{i}"
    p_list.append(p)
    p.start()
  
  # Wait for all processes to complete
  for p in p_list:
    p.join()
  
  # Create multiple processes
  p_list = []
  for i in range(3):  # Create 3 worker processes
    p = Process(
      target=confConsumerProcess, 
      args=(conf_proxy, i,),
      name=f"{conf_proxy['name']}#{i}"
      )
    p.name = f"{conf_proxy['name']}#{i}"
    p_list.append(p)
    p.start()
  
  # Wait for all processes to complete
  for p in p_list:
    p.join()
  
  # # Print final state
  # logDebug("Final credStore:")
  # shared_dict = conf_proxy['conf']
  # logDebug(f"{type(shared_dict).__name__}:shared_dict:[{shared_dict}]")
  # # print("Shared list:", data_manager.get_list())

  return conf_proxy

if __name__ == "__main__":
  try:
    conf_proxy = main()
  except:
    logException("failed to run main()")

  


