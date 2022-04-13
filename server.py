#/usr/bin/python3

import socket # yang terutama sekali
import threading # biar makin dinasmis
import time # hehe:D

soket=socket.socket()
host="192.168.100.167" # bisa dialokasikan
port=9901                              # bisa dialokasikan
soket.bind((host,port))
perintah ="1" # aku masih mencari tahu cara agar perintah ini dapat diubah ubah saat menjalankan program point 1

soket.listen(50) # makin banyak makinbagus kan? hahaha :D

def perulangan(): # terus terus mengulang sampai baterai latop habis :D
	while True:
		koneksi,alamat=soket.accept() # karena data yang dikembalikan berupa tuple.			print("Mematikan : ",alamat) # biar keren :D
		print("Mematikan perangkat : ",alamat) # biar keren :D
		koneksi.send(perintah.encode()) # melaju....

proses_perulangan =threading.Thread(target=perulangan).start()
