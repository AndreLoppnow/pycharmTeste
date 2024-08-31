IdTrabalhador = input()
HorasTrabalhadas = input()
ValorHoraTrabalhada = input()
Salario = int(HorasTrabalhadas) * float(ValorHoraTrabalhada)

print("NUMBER = " + str(IdTrabalhador))
print("SALARY = U$ {:.2f}".format(Salario))