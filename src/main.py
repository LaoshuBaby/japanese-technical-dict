import os
import json

def init():
    json_file=open(os.path.join(__file__.replace("main.py",""),"..","data","dict.json"),"w",encoding="utf-8")
    json_content=json.loads(json_file.read())
    json_file.close()

def build_pdf():
    pass

def manage_word():
    pass

def build_id():
    pass

def main():
    pass

if __name__ == "__main__":
    main()