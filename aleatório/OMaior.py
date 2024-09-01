Entrada = input()
ConverterEntrada = Entrada.split()
EntradaEmLista = [int(val) for val in ConverterEntrada]

maior = EntradaEmLista[0]
if (EntradaEmLista[1]>maior):
    maior = EntradaEmLista[1]
if(EntradaEmLista[2]>maior):
    maior = EntradaEmLista[2]

print(str(maior) + " eh o maior")
    