from bs4 import BeautifulSoup
import ssl
import urllib3
import os


ssl._create_default_https_context = ssl._create_unverified_context
os.system('cls')
link = input("Enter Url : ")

http = urllib3.PoolManager()
response = http.request('GET',link)
soup = BeautifulSoup(response.data,"html.parser")
#You can change the code with another code to download from different website
with open("url.csv","w") as f:
	f.write("pass\n")
	for i in soup.findAll():
		#you should get data from that website where is url you want to Scraping
f.closed
print("\n")
print("+++++++++++++++++++++++++++++++++++++++")
print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
print("+++++++++++++++++++++++++++++++++++++++")
