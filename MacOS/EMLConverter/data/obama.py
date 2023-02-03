import sys
import email
import json
from email import policy
from email.parser import BytesParser

sys_path, file = __file__.rsplit("/", 1)
class Application():
    def __init__(self, master=None):
        self.path = ""
        self.htmlPath = ""
        data = {}
        with open(sys_path + '/config.json', 'r') as file:
            data = json.load(file)
        self.htmlPath = data['htmlPath']
        self.main()

    def main(self):
        try:
            data = {}
            with open(sys_path + "/config.json", "r") as file:
                data = json.load(file)
            if data["emlPath"]:

                self.path = data["emlPath"]
                print(self.path)
                email = self.convert_eml_to_html()
                self.save_file(email)
        except Exception as e:
            data = {}
            with open(sys_path + "/config.json", "r") as file:
                data = json.load(file)
            data["output"] = "0"
            with open(sys_path + "/config.json", "w") as file:
                json.dump(data, file)


    def save_file(self, html):
        with open(self.htmlPath, "w", encoding="utf-8") as file:
            file.truncate()
            file.writelines(html)
        data = {}
        with open(sys_path + "/config.json", "r") as file:
            data = json.load(file)
        data["output"] = "1"
        with open(sys_path + "/config.json", "w") as file:
            json.dump(data, file)

    # Scripts
    def convert_eml_to_html(self):
        with open(self.path, "rb") as fp:
            msg = BytesParser(policy=policy.default).parse(fp)
            html = msg.get_body(preferencelist=("html")).get_content()
        return html

Application()
