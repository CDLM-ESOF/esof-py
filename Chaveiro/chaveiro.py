#! python3 (Windows)


import os, csv, pyperclip, random


def carregarCredenciais():
	credenciais = {} #Dicionário
	with open("credenciais.csv") as arq_csv:
                leitor_csv = csv.reader(arq_csv)
                for linha in leitor_csv:
                        if len(linha) == 2:
                                credenciais[linha[0]] = linha[1]
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


def removerCredencial():
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
        op = int(input("Digite o número associado à credencial a ser removida: "))
        if op <= 0 or op > len(listaCredenciais):
                print("Opção inválida!")
                return
        del credenciais[listaCredenciais[op-1]] #Remover a chave do dicionário

        # Rearmazenar arquivo csv
        f = csv.writer(open("credenciais.csv", "w+"))
        for login, senha in credenciais.items():
                f.writerow([login, senha])
        print("A credencial \"" + listaCredenciais[op-1] + "\" foi apagada")


# Menu de opções iniciais
while True:
        os.system('cls')
        op = int(input("""Digite o número associado à sua opção:
1) Consultar senha
2) Armazenar nova credencial
3) Remover credencial
0) Sair
"""))
        if op == 0:
                os.system('cls')
                exit()
        elif op == 1:
                os.system('cls')
                consultarSenha()
                os.system('pause')
                os.system('cls')
        elif op == 2:
                os.system('cls')
                criarCredencial()
                os.system('pause')
                os.system('cls')
        elif op == 3:
                os.system('cls')
                removerCredencial()
                os.system('pause')
                os.system('cls')
        else:
                print("Opção inválida!")
                os.system('pause')
                os.system('cls')
