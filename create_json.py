import json


def create():
    str_json = {}
    str_json['Notes'] = []
    with open('Notes', 'w') as file:
        json.dump(str_json,file,indent=3)

def share_json():
    return file