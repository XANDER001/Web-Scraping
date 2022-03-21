import requests
import urllib3
import pandas as pd
import time
import os
import csv
import pathlib
from tqdm import tqdm
from fake_useragent import UserAgent
# program version 2
os.system('cls')
#Storage CSV after Scraping
filecsv = pathlib.Path(__file__).parent.joinpath('url.csv')
# read how many row in csv file and also to count how much images will be downloaded
def csv_store():
    with open(filecsv,'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for row in csvreader:
            row.append(row)
            result = csvreader.line_num
            csv_store.final_result = result - 1
# Directory
all_in_one = pathlib.Path(__file__).parent.joinpath('Manga')
# to know how many folder inside Manga
check_data = os.listdir(all_in_one)

# test folder to check if code properly work
if len(check_data) == 0:
    a = os.path.join(all_in_one,"Test Folder")
    os.mkdir(a)
    print("Folder Has been Create")
    exit()
else:
    pass

#Read url in CSV
urls = pd.read_csv(filecsv)

# listing folder
count = 0
for data in check_data:
    count += 1
    print(f"{count}.{data}")

while True:
    try:
        name_folder = int(input("Enter Number : "))
        if name_folder <= count:
            name_folder -= 1
            Access_list = check_data[name_folder]
            break
        else:
            print("\n == Folder Not Found == \n")
    except ValueError as vr:
        print("Only numeric")

# for checking if check True or False
dir_location = f"{all_in_one}/{Access_list}"
check = os.path.isdir(dir_location)

while True:
    if check == True:
        dir_option = os.listdir(dir_location)
        count = 0
        for data in dir_option:
            count += 1
            print(f"{count}.{data}")
        try:
            # join and make folder
            print("\nNote: if you input numberic more then menu list can make new folder")
            folder = int(input("Enter Option : "))
            folder -= 1
            # for exception indexerror
            h = dir_option[folder]
            # for exception fileexistserror
            full_path = os.path.join(all_in_one,Access_list,h)
            os.mkdir(full_path)
            break
        
        except IndexError as idx:
            # making the new folder
            new_folder = str(input("New Folder Name : "))
            full_path = os.path.join(all_in_one,Access_list,new_folder)
            os.mkdir(full_path)
            c = 1
            break

        except FileExistsError as fe:
            # This code to contine downloader
            print("Would You like to Continue Downloader Y/N")
            op_continue = str(input("Enter Your Option : "))
            if op_continue == 'Y'  or op_continue == 'y':
                c = len([name for name in os.listdir(f"{dir_location}/{h}") if os.path.isfile(os.path.join(f"{dir_location}/{h}", name))])+1
                break
            elif op_continue == 'N' or op_continue == 'n':
                pass
            else:
                print("\nOut of Option\n")
    else:
        print("That's not folder")
        exit()
        break

print("""1.jpg\n2.png""")
while True:
    try:
        format_img = int(input("What you prefer format image : "))
        if format_img == 1:
            fmg = 'jpg'
            break
        elif format_img == 2:
            fmg = 'png'     
            break
        else:
            print("only receive number 1 and 2")
    except ValueError as ve:
        print("Only numeric")

x = UserAgent()
csv_store()
# Start Timing
start_time = time.time()

try:
    # This Code Using SSL
    with tqdm(total=csv_store.final_result) as pbar:
        for i,url in enumerate(urls.values,c):
            head = {"User-Agent":x.random}
            response = requests.get(url[0], headers=head,stream = True,verify=True)
            with open(f"{full_path}\\{i}.{fmg}",'wb') as f:
                if response.status_code == 200:
                    f.write(response.content)
                elif response.status_code == 403:
                    print("\nClose Connection")
                elif response.status_code == 404:
                    print("\nNot Found URL")
                else :
                    print("Theres something wrong with the connection",response.status_code)
            pbar.update(1)
    
except requests.exceptions.SSLError as sle:
    # This Code Not Using SSL
    print("\nWarning this downloader Not Using SSL ")
    # SSL Warning option
    print("Are You Sure want to download : (y/n)")
    warSSL = str(input("Enter Your Option : "))
    if warSSL == 'y' or warSSL == 'Y':
        urllib3.disable_warnings()
        with tqdm(total=csv_store.final_result) as pbar:
            for i,url in enumerate(urls.values,c):
                head = {'User-Agent':x.random}
                response = requests.get(url[0], headers=head,stream = True,verify=False)
                with open(f"{full_path}\\{i}.{fmg}",'wb') as f:
                    if response.status_code == 200:
                        f.write(response.content)
                    elif response.status_code == 403:
                        print("\nClose Connection")
                    elif response.status_code == 404:
                        print("\nNot Found URL")
                    else :
                        print("\nThere's something wrong with the connection",response.status_code)
                pbar.update(1)
    else:
        exit()

result_time = int(time.time()-start_time)
print(f"Time : {result_time/60:.2f} Minute")
print("\n")
print("+++++++++++++++++++++++++++++++++++++++")
print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
print("+++++++++++++++++++++++++++++++++++++++")
