import os
import json
import hashlib

def init():
    json_file=open(os.path.join(__file__.replace("main.py",""),"..","data","dict.json"),"w",encoding="utf-8")
    json_content=json.loads(json_file.read())
    json_file.close()
    return json_content

def build_pdf():
    pass

def manage_word():
    pass

def build_id():
    def gen_id(string:Dict[str,str])->str:
        hasher=hashlib.sha1()
        hasher.update(string)
        return hasher.hexdigest()
    gen_id({
        "en":"test",
        "ja":"テスト",
        "zh":"测试"
    })
    pass

def main():
    pass

if __name__ == "__main__":
    main()