import copy, sys

VARIAVEIS_DECISAO = list(map(lambda x: float(x),raw_input().split(" ")))

RESTRICOES_MATRIZ = []

valor = raw_input()
while valor != "-":
	RESTRICOES_MATRIZ.append(list(map(lambda x: float(x),valor.split(" "))))
	valor = raw_input()

def definir_coluna_pivo(linha):
	menor_indice = 0
	menor_valor = linha[0]
	for i in range(1, len(linha)):
		if linha[i] < menor_valor:
			menor_valor = linha[i]
			menor_indice = i
	return menor_indice

def definir_linha_pivo(matriz, indice_coluna_pivo):
	menor_restricao_indice = 1
	menor_restricao_valor = sys.maxint
	for i in range(1, len(matriz)):
		if matriz[i][indice_coluna_pivo] == 0:
			continue
		valor_atual = matriz[i][posicao_coluna_valor] / (matriz[i][indice_coluna_pivo] * 1.0)
		#print(valor_atual)
		if valor_atual < 0:
			continue
		if valor_atual < menor_restricao_valor:
			menor_restricao_valor = valor_atual
			menor_restricao_indice = i
	return menor_restricao_indice 

def calcular_nova_linha_pivo(linha, elemento_pivo):
	for i in range(0, len(linha)):
		linha[i] = linha[i] / (elemento_pivo*1.0)
	return linha

def calcular_novo_tableau(matriz, indice_linha_pivo, indice_coluna_pivo):
	matriz_copia = copy.deepcopy(matriz)
	for i in range(0, len(matriz)):
		if i == indice_linha_pivo:
			continue
		for j in range(0, len(matriz[i])):
			valor_pivo_linha_atual = copy.copy(matriz[i][indice_coluna_pivo])
			novo_valor = matriz[i][j] - (valor_pivo_linha_atual * matriz[indice_linha_pivo][j])
			matriz_copia[i][j] = novo_valor
	return matriz_copia


def monta_tableau_inicial():
	matriz = []

	z = (list(map(lambda x: x * -1, VARIAVEIS_DECISAO))) + ((restricoes + 1) *[0])

	matriz.append(z)

	for i in range(len(RESTRICOES_MATRIZ)):
		item = RESTRICOES_MATRIZ[i][:variaveis_decisao] + ((restricoes + 1) *[0])
		item[posicao_coluna_valor] = RESTRICOES_MATRIZ[i][variaveis_decisao]
		item[variaveis_decisao + i] = 1
		matriz.append(item)
	return matriz

def resolve_simplex(matriz):
	i = 0
	while True:

		i += 1
		
		indice_coluna_pivo = definir_coluna_pivo(matriz[0])

#		print("Coluna pivo: %s" % indice_coluna_pivo)

		if matriz[0][indice_coluna_pivo] >= 0:
			break

		indice_linha_pivo = definir_linha_pivo(matriz, indice_coluna_pivo)
		elemento_pivo = matriz[indice_linha_pivo][indice_coluna_pivo]

#		print("Elemento pivo: %s" % elemento_pivo)

		variaveis_decisao_entrada[indice_coluna_pivo] = indice_linha_pivo

		nova_linha_pivo = calcular_nova_linha_pivo(matriz[indice_linha_pivo], elemento_pivo)
		matriz = calcular_novo_tableau(matriz, indice_linha_pivo, indice_coluna_pivo)

#		print("---------------------------------------------------")

#		print(matriz[0])
#		print(matriz[1])
#		print(matriz[2])
		#print(matriz[3])

		#if i == 2:
		#	exit()


	resultado = matriz[0][posicao_coluna_valor]

	#print(variaveis_decisao_entrada)

	resultado_print = []

	for i in variaveis_decisao_entrada:
		if i == -1:
			resultado_print.append(0)
		else:
			resultado_print.append(matriz[i][posicao_coluna_valor])

	resultado_print.append(resultado)

	#resultado_print = list(map(lambda x: matriz[x][posicao_coluna_valor], variaveis_decisao_entrada)) + [resultado]

	print(" ".join(format(x, "0.2f").rstrip("0").rstrip(".") for x in resultado_print))


restricoes = len(RESTRICOES_MATRIZ)
variaveis_decisao = len(VARIAVEIS_DECISAO)
variaveis_decisao_entrada = [-1] * (variaveis_decisao)
posicao_coluna_valor = restricoes + variaveis_decisao

matriz = monta_tableau_inicial()

#print("---------------------------------------------------")

#print(matriz[0])
#print(matriz[1])
#print(matriz[2])


resolve_simplex(matriz)