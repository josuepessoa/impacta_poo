def eh_primo(n):
	"""Função que verifica se um número é primo

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é um número primo e falso caso contrário.

	Exemplos
	--------
	Um número é dito primo se possuir apenas 2 divisores, isto é,
	não possuir nenhum divisor além do 1 e do próprio n.
	29 é primo:
		divisores de 29: 1, 29
	30 NÃO é primo:
		divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número primo e False caso contrário.
	"""
	if n < 2:
		return False  # o return sempre encerra a função!
	qtd_divisores = 0
	i = 1  # variável contadora
	while i <= n:
		if n % i == 0:  # testa se n é divisível por i
			qtd_divisores += 1
		i += 1  # incrementa o valor de i
	if qtd_divisores == 2:
		return True
	else:
		return False


def lista_primos(n):
	"""Função que retorna uma lista de primos até n

	Recebe um número natural n, com n >= 2, e retorna uma
	lista com todos o números primos estritamente menores
	que n, em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Lista com todos os números primos menores
			que n, em ordem crescente.
	"""
	lista = []
	for i in range(2, n):   # lembre-se: i varia de 2 até n-1
		if eh_primo(i):   # podemos chamar a função aqui mesmo, pois ela sempre retorna um valor booleano
			lista.append(i)
	return lista