import json

with open('array.json') as f:
    d = json.load(f) # d - это список python
    print(d)