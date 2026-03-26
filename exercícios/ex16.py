dias = int (input('quantos dias alugados ?'))
Km = float (input('quantos km rodados?'))
diaria = dias*60
percurso = Km * 0.15
Custo = diaria + percurso 

print('o total a pagar é de R${:.2f}'.format(custo))
