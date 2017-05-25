#!  /usr/local/bin/python3

# mapIt.py: Mostra no Google Maps um endereço fornecido via linha de comando ou área de transferência.


import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
	# O endereço virá da linha de comando
    address = ''.join(sys.argv[1:])
else:
	# O endereço está na área de transferência
	address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
