import os
import requests

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
