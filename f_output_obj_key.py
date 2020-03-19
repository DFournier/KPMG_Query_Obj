def print_obj_key(obj,key):
  import json
  with open(obj) as f:
    data = json.load(f)
  #print(data)
  keystr = key
  #print(keystr)
  str = "print(data"
  #print(str)
  #print(len(keystr))
  while len(keystr)>0:
    str = str + "['" + keystr[0:1] + "']"
    #print(str)
    keystr = keystr[2:]
    #print(keystr)
    #print(len(keystr))
  str = str + ')'
  #print(str)
  exec(str)
