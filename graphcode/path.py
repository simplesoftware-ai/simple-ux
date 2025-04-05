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

from os import getcwd, path
from pathlib import Path


def getAppName():
  """
  Get the name of the configuration manager.

  Returns:
    str: The name of the configuration manager
  """
  return path.basename(getcwd())

def getBasenames(filename: str) -> list[str]:
  """
  Parse a filename and return possible base names.
  
  Args:
      filename (str): The filename to parse
      
  Returns:
      list[str]: List of possible base names for the file
  """
  
  
  # Strip whitespace from beginning and end of filename
  filename = filename.strip()

  # Get base names once
  if len(filename.split(".")) > 1:
    fileType = filename.split(".")[-1]

    if len(filename.split(" ")) > 1 and " " not in fileType:
      fileName = filename.split(" ")[0]

      return [f"{fileName}.{fileType}", filename]
    
    else:
      return [filename]
    



def findFilePath(filename):
  """
  Find the path to the configuration file.

  Args:
    filename (str): The filename to search for

  Returns:
    str: The path to the configuration file

  Raises:
    FileNotFoundError: If no configuration file is found
  """

  # Get base names once
  baseNames = getBasenames(filename)
  print(f"baseNames:[{baseNames}]")

  # Create search paths using list comprehension
  searchPaths = []
  for name in baseNames:
    for case in [name, name.lower()]:
      searchPaths.extend([
        Path("/etc") / f"{case}",
        Path.home() / f"{case}",
        Path.home() / f".{case}",
        Path.home() / f"{case}",
        Path(getcwd()) / "conf" / f"{case}",
        Path(getcwd()) / f"{case}"
      ])
  
  # Search for existing configuration file
  for confPath in searchPaths:
    if confPath.is_file():
      print(f"confPath:[{confPath}] found")
      return str(confPath)

    print(f"confDir:[{confPath}] not found")

  raise FileNotFoundError(f"Configuration file not found in any of these locations: {searchPaths}")