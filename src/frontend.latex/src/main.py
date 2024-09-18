import os
import json
import hashlib
from typing import Dict, List

MANUAL_COMPLIE = False


def init():
    json_file = open(
        os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "data", "dict.json"
        ),
        "r",
        encoding="utf-8",
    )
    json_content = json.loads(json_file.read())
    json_file.close()
    return json_content


def gen_id():
    def gen_id_hasher(string: Dict[str, str]) -> str:
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

    this_id = gen_id_hasher({"en": "test", "ja": "テスト", "zh": "测试"})
    print(this_id)
    pass


def gen_latex(json_content: dict) -> None:
    latex_file_path = os.path.join(
        os.path.dirname(__file__), "..","template", "main.tex"
    )
    latex_file = open(latex_file_path, "r", encoding="utf-8")
    latex_file_content = latex_file.read()
    latex_file.close()
    symbol = "Word & 单词 & タンゴ \\\\ \midrule\n"

    def gen_insert_list(json_content: dict) -> List[str]:
        dict_entries = json_content["dict"]
        insert_list = []
        template = "{en} & {zh} & {ja} \\\\ \midrule"
        for entry in dict_entries:
            insert_list.append(template.format(**entry["string"]))
        return insert_list

    latex_file = open(latex_file_path, "w", encoding="utf-8")
    latex_file_content = latex_file.write(
        latex_file_content.replace(
            symbol,
            symbol
            + "".join([i + " \n" for i in gen_insert_list(json_content)]),
        )
    )
    latex_file.close()
    return None


def manage_word():
    pass


def build_pdf() -> None:
    os.chdir("..")
    os.chdir("template")
    os.system("xelatex main")
    return None


def main() -> None:
    return None


if __name__ == "__main__":
    json_content = init()
    # # gen_id then overwrite disk file
    # gen_id()
    gen_latex(json_content)
    if MANUAL_COMPLIE == False:
        build_pdf()
    else:
        pass
