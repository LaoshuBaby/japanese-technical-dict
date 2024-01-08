import os
import json

# import pandas

origin_file=open(os.path.join(__file__.replace("csv2json.py",""),"..","data","dict.csv"),"r",encoding="utf-8")
origin_file_content=origin_file.read()
origin_file.close()

origin_file_content=[i.split(",") for i in origin_file_content]

dict_array=[]
for i in origin_file_content:
    dict_array.append({
        "id":"",
        "string":{
            "en":origin_file_content[i][0],
            "ja":origin_file_content[i][1],
            "zh":origin_file_content[i][2],
        },
        "tags":[]
    })

json_file=open(os.path.join(__file__.replace("csv2json.py",""),"..","data","dict.json"),"r",encoding="utf-8")
json_content=json.dumps({"dict":dict_array},indent=2)
json_file.write(json_content)
json_file.close()