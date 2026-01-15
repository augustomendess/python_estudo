notaA=float(input("digite sua nota A: "))
notaB=float(input("digite sua nota B: "))

#calcular media
mediafinal = (notaA + notaB) /2

#prova real
if mediafinal >= 7.0:
    print ("A Média: %.1f - Aprovado " % mediafinal)
else:
    print ("A Média: %.1f - reprovado" % mediafinal)