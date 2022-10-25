import json 
import config
with open(config.JSON_FILE_PATH,"r") as file:
    json_data = json.load(file)
print(len(json_data["Columns"]))