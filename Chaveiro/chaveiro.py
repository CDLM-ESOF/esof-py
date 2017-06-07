#! /usr/local/bin/python3
#! python3 (Windows)


import os, csv, pyperclip, random


def carregarCredenciais():
	credenciais = {} #Dicionário
	for login, senha in csv.reader(open("credenciais.csv")):
		credenciais[login] = senha
	return credenciais


def consultarSenha():
	# As credenciais são armazenadas em um arquivo csv
	if not os.path.exists(os.path.join(os.getcwd(), "credenciais.csv")):
		print("Seu chaveiro está vazio!")
		return
	credenciais = carregarCredenciais() #Carregar as credenciais existentes

	print("Seu chaveiro possui %d credenciais:" % len(credenciais))
	listaCredenciais = list(credenciais.keys())
	if len(listaCredenciais) == 0:
		return
	for i, login in enumerate(listaCredenciais):
		print("%d) " % (i+1) + login)
	op = int(input("Digite o número associado à credencial desejada: "))
	if op <= 0 or op > len(listaCredenciais):
		print("Opção inválida!")
		return
	pyperclip.copy(credenciais[listaCredenciais[op-1]]) #Copiar a senha para a área de transferência
	print("A senha para \"" + listaCredenciais[op-1] + "\" foi copiada para a área de transferência")


def gerarSenha():
	num_caract = int(input("Número de caracteres: "))
	so_numero = str(input("Apenas números? (s/n): ")).lower().strip()
	if so_numero[0] == 's':
		c = "1234567890"
	elif so_numero[0] == 'n':
		c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	else:
		print("Resposta inválida!")
		return ""

	senha = ""
	while len(senha) < num_caract:
		senha = senha + random.choice(c)
	return senha


def criarCredencial():
	login = input("Digite o nome da nova credencial: ")
	print("Selecione uma opção:\n1) Digitar senha\n2) Gerar senha aleatória")
	op = int(input(": "))
	senha = ""
	if op == 1:
		senha = input("Senha: ")
	elif op == 2:
		senha = gerarSenha()
		if not senha:
			return
		print("Senha: " + senha)
	else:
		print("Opção inválida!")
		return

	credenciais = {}
	# Carregar, caso existam, as credenciais pré-existentes
	if os.path.exists(os.path.join(os.getcwd(), "credenciais.csv")):
		credenciais = carregarCredenciais()
	# Incluir nova credencial
	credenciais[login] = senha

	# Rearmazenar arquivo csv
	f = csv.writer(open("credenciais.csv", "w+"))
	for login, senha in credenciais.items():
		f.writerow([login, senha])
	print("Sua nova credencial foi adicionada ao chaveiro")


# Menu de opções iniciais
while True:
	op = int(input("""
Digite o número associado à sua opção:
1) Consultar senha
2) Armazenar nova credencial
0) Sair
"""))
	if op == 0:
		exit()
	elif op == 1:
		consultarSenha()
	elif op == 2:
		criarCredencial()
	else:
		print("Opção inválida!")
