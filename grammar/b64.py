# -*- coding: utf-8 -*-

import base64
import json
import gzip

event = {
    'uuid': 'uuid1',
    'timestamp': 1234567890,
    'kanji': '諸行無常',
    'ascii': 'shogyou mujou',
}

def compress_jsonstr(json_str: str):
    return base64.b64encode(gzip.compress(json_str.encode('utf-8')))

def decompress_jsonstr(compressed):
    return gzip.decompress(base64.b64decode(compressed)).decode('utf-8')

# base64_event = base64.b64encode(gzip.compress(json.dumps(event).encode('utf-8')))
# print(base64_event)
# decoded_event = gzip.decompress(base64.b64decode(base64_event))
# print(decoded_event)

# print(event)
# print(json.dumps(event))
# print(json.dumps(event).encode('utf-8'))
# obj = compress_jsonstr(json.dumps(event))
# print(obj)
# print(decompress_jsonstr(obj))
# print(decompress_jsonstr(obj).decode('utf-8'))
# print(json.loads(decompress_jsonstr(obj).decode('utf-8')))

json_str = json.dumps(event)
print(json_str)
print(compress_jsonstr(json_str))
print(decompress_jsonstr(compress_jsonstr(json_str)))

print(json_str == decompress_jsonstr(compress_jsonstr(json_str)))

# json_str_utf8 = json.dumps(event, encodig='utf8')
# print(json_str_utf8)
