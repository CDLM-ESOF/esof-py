#! /usr/local/bin/python3

# fileDownloader: Baixa um arquivo da internet
# Primeiro argumento: URL do arquivo
# Segundo argumento: caminho do arquivo a ser salvo no disco


import sys, requests


if len(sys.argv) < 3:
	print("Forneça a URL e o caminho do arquivo a ser salvo no disco!")
	exit()
online_address = sys.argv[1]
local_address = sys.argv[2]

res = requests.get(online_address)
res.raise_for_status()
dl_file = open(local_address, "wb")
for chunk in res.iter_content(100000):
	dl_file.write(chunk)
dl_file.close()
