#! /usr/local/bin/python3

# latestNews: Abre as páginas das últimas notícias do site Inovação Tecnológica


import requests, webbrowser, bs4


print("Buscando as últimas notícias de Inovação Tecnológica...")
res = requests.get("http://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=principal")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
# Listar todas as manchetes:
manchetes = soup.select("div #manchete")
# Abrir cada manchete:
for index, manchete in enumerate(manchetes):
	print(index + 1, ") ", manchete.select("a")[0].getText())
	link = manchete.select("a")[0].get("href")
	webbrowser.open("http://www.inovacaotecnologica.com.br" + link[2:])
