print('Conversor Binario!!!')
print('------------- -bin:\n') #Binario
print('\ndec -bin')
print('hex -bin\n')
print('------------- -dec:\n') #Decimal
print('\nbin -dec')
print('hex -dec\n')
print('------------- -hex:\n') #Hexadecimal
print('\ndec -hex')
print('bin -hex\n')
print('-------------------\n\n')
entrada = input('Digite a entrada, e ao lado o tipo que ele é para o que quer converte-la: ')
valor = ''
validar = True
parametro = ''

for i in range(len(entrada)):
	if entrada[i] != ' ' and validar != False:
		valor += entrada[i]

	elif entrada[i] == ' ' and validar != False:
		validar = False
		continue

	else:
		parametro += entrada[i]

if parametro[0] != 'h':
	valorInt = int(valor)

def classificarBinario(numerador):
	valor = ''

	if numerador == int(numerador):
		valor = '0'

	else:
		valor = '1'

	return valor

def converterDecimalParaBinario(entrada):
	valoresNovos = []
	valoresNovos.append(entrada)
	valor = ''
	contar = 0
	valorFinal = ''

	while contar >= 0:
		if int(valoresNovos[contar] / 2) != 1:
			valoresNovos.append(int(valoresNovos[contar] / 2))
			valor += classificarBinario(valoresNovos[contar] / 2)
			contar += 1
		else:
			if valoresNovos[contar] / 2 == 1:
				valor += '0'

			valor += '1'
			break
	
	contar = 1

	for i in range(len(valor)):
		valorFinal += valor[len(valor) - contar]
		contar += 1

	return valorFinal

def classificarDecimalParaHexadeximal(elementoDaEntrada):
	matrizHexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11']
	resultado = ''

	for i in range(len(matrizHexadecimal)):
		if elementoDaEntrada == i:
			resultado = matrizHexadecimal[i]
			break

	return resultado

def converterDecimalParaHexadecimal(entrada):
	tamanhoEntrada = len(str(entrada))
	valoresNovos = []
	valoresNovos.append(entrada)
	valor = ''
	valorFinal = ''
	contar = 0

	while contar >= 0:
		if valoresNovos[contar] / 16 >= 1:
			valoresNovos.append(int(valoresNovos[contar] / 16))
			valor += classificarDecimalParaHexadeximal(valoresNovos[contar] % 16)
			contar += 1

		else: 
			valor += classificarDecimalParaHexadeximal(valoresNovos[len(valoresNovos) - 1])
			break

	contar = 1

	for i in range(len(valor)):
		valorFinal += valor[len(valor) - contar]
		contar += 1

	return valorFinal

def converterBinarioParaDecimal(entrada):
	entradaString = str(entrada)
	tamanhoEntrada = len(entradaString)
	resultadosSeparados = []
	resultadoTotal = 0
	contar = 1

	for i in range(tamanhoEntrada):
		resultadosSeparados.append(int(entradaString[tamanhoEntrada - contar]) * (2 ** i))
		contar += 1

	for j in range(len(resultadosSeparados)):
		resultadoTotal += resultadosSeparados[j]

	return resultadoTotal

def converterBinarioParaHexadecimal(entrada):
	entradaConvertidaEmDecimal = converterBinarioParaDecimal(entrada)
	entradaConvertidaEmHexadecimal = converterDecimalParaHexadecimal(entradaConvertidaEmDecimal)

	return entradaConvertidaEmHexadecimal

def converterHexadecimalParaBinario(entrada):
	entradaConvertidaEmDecimal = converterHexadecimalParaDecimal(entrada)
	entradaConvertidaEmBinario = converterDecimalParaBinario(entradaConvertidaEmDecimal)

	return entradaConvertidaEmBinario

def classificarHexadecimalParaDecimal(elementoDaEntrada):
	matrizHexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '10', '11']
	resultado = 0

	for i in range(len(matrizHexadecimal)):
		if elementoDaEntrada == matrizHexadecimal[i]:
			resultado = i

	return resultado

def converterHexadecimalParaDecimal(entrada):
	tamanhoEntrada = len(entrada)
	resultadosSeparados = []
	resultadoTotal = 0
	contar = 1

	for i in range(tamanhoEntrada):
		resultadosSeparados.append(classificarHexadecimalParaDecimal(entrada[tamanhoEntrada - contar]) * (16 ** i))
		contar += 1

	for j in range(len(resultadosSeparados)):
		resultadoTotal += resultadosSeparados[j]

	return resultadoTotal

def avaliarParametro(parametro):
	resultado = ''

	if parametro == 'dec -bin':
		resultado = converterDecimalParaBinario(valorInt)
	elif parametro == 'dec -hex':
		resultado = converterDecimalParaHexadecimal(valorInt)
	elif parametro == 'bin -dec':
		resultado = converterBinarioParaDecimal(valorInt)
	elif parametro == 'bin -hex':
		resultado = converterBinarioParaHexadecimal(valorInt)
	elif parametro == 'hex -bin':
		resultado = converterHexadecimalParaBinario(valor)
	elif parametro == 'hex -dec':
		resultado = converterHexadecimalParaDecimal(valor)
	else:
		resultado = 'Você deve ter digitado errado.'

	return resultado

print('\n{}'.format(avaliarParametro(parametro)))
		

