import json
import re
 
with open('test.txt') as f:
    lines = f.readlines()
dict1 = {}
dict2 = {}
serial = "serial"
id = "id"
special_char = ['"',':']
ls_dict = []
for line in lines:
    z = line.strip()
    val = z[:z.index(":")]
    dict1[serial] = val
    ids = re.sub(r'^.*?id', '', z)
    ids = ids[:ids.index(",")]
    for i in special_char:
        ids = ids.replace(i,"")
    dict2[id] = ids
    dict1.update(dict2)
    ls_dict.append(dict1)
jstr = json.dumps(ls_dict)
jstr_object = json.loads(jstr)
print(json.dumps(jstr_object, indent=1))

