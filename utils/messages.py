import os
import json

_msgs = {}
msgdir = os.path.normpath(f'{os.path.dirname(__file__)}/../type16')
with open(f'{msgdir}/messages.json', 'r') as f:
    msgs = json.load(f)

def get_msg(key):
    return msgs.get(key)