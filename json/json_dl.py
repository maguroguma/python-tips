# -*- coding: utf-8 -*-

import json

json_dict = {
    'name': 'masahiro yokoyama',
    'age': 30
}

print(json.dumps(json_dict))
print(type(json.dumps(json_dict)))
print(json.dumps(json.dumps(json_dict)))
print(type(json.dumps(json.dumps(json_dict))))
print(json.dumps(json.dumps(json.dumps(json_dict))))
