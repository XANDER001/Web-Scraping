from bs4 import BeautifulSoup
import ssl
import urllib3
import os


ssl._create_default_https_context = ssl._create_unverified_context
os.system('cls')
link = input("Masukan Url : ")

http = urllib3.PoolManager()
response = http.request('GET',link)
soup = BeautifulSoup(response.data,"html.parser")
#You can change the code with another code to download from different website
with open("url.csv","w") as f:
	f.write("pass\n")
	for i in soup.findAll('div',class_='col-xs-12 col-sm-6 col-md-4 col-lg-2'):
		for j in i.find_all('div',class_='thumbnail'):
			for k in j.find_all('img'):
				link = k.get('src')
				link_delete = link.replace("/thumb/","")
				full_url = 'https://www.erofus.com/medium/'+link_delete
				f.write(full_url)
				f.write("\n")
f.closed
print("\n")
print("+++++++++++++++++++++++++++++++++++++++")
print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
print("+++++++++++++++++++++++++++++++++++++++")
