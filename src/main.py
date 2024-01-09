import os
import json
import hashlib
from typing import Dict


def init():
    json_file = open(
        os.path.join(
            __file__.replace("main.py", ""), "..", "data", "dict.json"
        ),
        "w",
        encoding="utf-8",
    )
    json_content = json.loads(json_file.read())
    json_file.close()
    return json_content


def build_pdf():
    pass


def manage_word():
    pass


def build_id():
    def gen_id(string: Dict[str, str]) -> str:
        hasher = hashlib.sha1()
        hasher.update(
            json.dumps(
                string, skipkeys=False, ensure_ascii=False, sort_keys=True
            ).encode("utf-8")
        )
        # return hash(string) is wrong because in Python dict is unhashable
        import re

        id = "-".join(re.findall(".{8}", hasher.hexdigest())).upper()
        return id

    this_id = gen_id({"en": "test", "ja": "テスト", "zh": "测试"})
    print(this_id)
    pass


def main():
    pass


if __name__ == "__main__":
    build_id()
