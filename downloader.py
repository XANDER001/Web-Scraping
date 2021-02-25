import pandas as pd
import ssl
import os
import urllib.request
from os import path
from tqdm import tqdm
from numpy_test import final_result


#Fix SSL
ssl._create_default_https_context = ssl._create_unverified_context

#Headers
open=urllib.request.build_opener()
open.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(open)

os.system("cls")

#folder_name = str(input("Folder Name : "))
#name = folder_name.capitalize()

def image(i,url,file_path):

    filename = '{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path,filename)
    urllib.request.urlretrieve(url, full_path)
    #print('{} saved.'.format(filename))


FILENAME = 'url.csv'#watch out if the file not in the same folder this code cannot execute
FILE_PATH = 'Manga/'


path = os.path.join(FILE_PATH,'')
urls = pd.read_csv(FILENAME)
#os.mkdir(path)


#Progses bar
print("Download : ")
with tqdm(total=final_result) as pbar:
    for i,url in enumerate(urls.values,1):
		#receive data image
        image(i, url[0], path)
		#update progsesbar with new line url image
        pbar.update(1)


print("\n")
print("+++++++++++++++++++++++++++++++++++++++")
print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
print("+++++++++++++++++++++++++++++++++++++++")
