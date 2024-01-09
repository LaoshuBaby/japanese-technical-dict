import os
import json

json_file=open(os.path.join(__file__.replace("csv2json.py",""),"..","data","dict.json"),"w",encoding="utf-8")
json_content=json.loads(json_file.read())
json_file.close()