Vendedor = input()
SalarioFixo = float(input())
VendasMes =float(input())

PercentagenVendas = VendasMes * 0.15
TotalSalarioPercentagem = PercentagenVendas+SalarioFixo
print("TOTAL = R$ {:.2f}".format(TotalSalarioPercentagem))