import requests
import json


class ParsingError(Exception):
    def __init__(self, msg="Data Parsing Error"):
        self.msg = msg

    def __str__(self):
        return self.msg


def parser(url: str):
    """url 에서 텍스트 받아서 리턴

    Args:
        url(str): url (raw)

    Return:
        text(str): 인터넷에서 받은 텍스트
    """
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    else:
        raise ParsingError


class Info():
    def __init__(self):
        url_info = "M:\girlsfrontline-resources-extract\data\info.json"
        try:
            with open(url_info) as f:
                self.info = json.loads(f.read())
                self.status = True
        except ParsingError:
            self.status = False

    def __getitem__(self, item):
        return self.info[item]

    def dl(self, file_name):
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(parser(self.info[file_name]))


if __name__ == '__main__':
    pass
