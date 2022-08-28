
import json


d = {'project_path': 'path', 'tests_path': 'path', 'vagrant_path': 'path'}


with open("paths.json", "w") as fp:
    json.dump(d , fp) 


with open("paths.json", "r") as fp:
    test = json.load(fp)

    print(test)
