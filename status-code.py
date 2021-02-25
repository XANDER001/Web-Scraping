import os
os.system("cls")
print("remeber number always start from 0 or 1")
num = int(input("Masukan Banyak angka : "))
link = str(input("Masukan URL : "))
i = {}
#Pemasukan string ke url.csv
with open("url.csv","w") as f:
	f.write("pass \n")
	for i in range(1,num):
		f.write(link.format(i))
		f.write("\n")
	f.closed
print("\n")
print("+++++++++++++++++++++++++++++++++++++++")
print("+█▀▀ █▀▀█ █▀▄▀█ █▀▀█ █   █▀▀ ▀▀█▀▀ █▀▀+")
print("+█   █  █ █ ▀ █ █  █ █   █▀▀   █   █▀▀+")
print("+▀▀▀ ▀▀▀▀ ▀   ▀ █▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀+")
print("+++++++++++++++++++++++++++++++++++++++")
