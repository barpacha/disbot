import os
import requests
import json

def delete_file(file:str):
    os.remove(file)

def download(url:str, name:str):
    for file in all_files():
        if file == name:
            return False
    f=open(r'saved\\' + name,"wb")
    ufr = requests.get(url)
    f.write(ufr.content)
    f.close()
    return True

def all_files():
    return os.listdir('saved')

def load_binding():
    try:
        with open('binding.json', 'r') as j:
            json_data = json.load(j)
        return json_data
    except:
        return None

def find_binding(text:str):
    json_file = load_binding()
    if json_file is None:
        return None
    for i in json_file:
        if i['text'] == text:
            return i['name']
    return None

def upload_binding(text:str, name_file:str):
    json_file = load_binding()
    if json_file is None:
        json_file = [{
            'text': text,
            'name':name_file
        }]
    else:
        if not find_binding(text) is None:
            return
        json_file.append({
            'text': text,
            'name': name_file
        })
    with open('binding.json', 'w') as file:
        json.dump(json_file, file)

def del_binding(text:str):
    json_file = load_binding()
    if json_file is None:
        return False
    for i in json_file:
        if i['text'] == text:
            json_file.remove(i)
            with open('binding.json', 'w') as file:
                json.dump(json_file, file)
            return True
    return False