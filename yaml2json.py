import json
import os
import sys
import yaml


# check there is a file passed
# if len(sys.argv) > 1:
#     # opening the file
#     if os.path.exists(sys.argv[1]):
#         source_file = open(sys.argv[1], "r")
#         source_content = yaml.load(source_file)
#         source_file.close()
#     # if the file isn't found
#     else:
#         print("Error: File not found")
#         exit(1)
# else:
#     print("Wrong execution format")
#
# # processing the conversion
# output = json.dump(source_content)
#
# target_file = open(sys.argv[2], "w")
# target_file.write(output)
# target_file.close()

def verify_yaml_file(file_path):
    try:
        with open(file_path, 'r') as stream:
            yaml.safe_load(stream)
            print("The YAML file is valid.")
    except yaml.YAMLError as exc:
        print("Error in YAML file:", exc)

file_path = 'input.yml'
verify_yaml_file(file_path)

def yaml_to_json(yaml_path, json_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    with open(json_path, 'w') as json_file:
        json.dump(yaml_data, json_file)

yaml_path = 'input.yml'
json_path = 'output.json'
yaml_to_json(yaml_path, json_path)
print("file converted successfully")