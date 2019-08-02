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
		if valoresNovos[contar] / 2 != 1:
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

def converterBinarioParaDecimal(entrada):
	pass

def converterBinarioParaHexadecimal(entrada):
	pass

def converterDecimalParaHexadecimal(entrada):
	pass

def converterHexadecimalParaBinario(entrada):
	pass

def converterHexadecimalParaDecimal(entrada):
	pass

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
		resultado = converterHexadecimalParaBinario(valorInt)
	elif parametro == 'hex -dec':
		resultado = converterHexadecimalParaDecimal(valorInt)
	else:
		resultado = 'Você deve ter digitado errado.'

	return resultado

print('\n{}'.format(avaliarParametro(parametro)))
		

