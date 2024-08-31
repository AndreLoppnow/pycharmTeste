Entrada = input()
Conversao = Entrada.split()
Pi = 3.14159
Lista = [float(val) for val in Conversao]

AreaTriangulo = (Lista[0]*Lista[2])/2

AreaCirculo = Pi*(Lista[2]**2)
if Lista[0] > Lista[1]:
     AreaTrapezio = (Lista[1]+Lista[0])*Lista[2]/2
else:
    AreaTrapezio = ((Lista[0]+Lista[1])*Lista[2])/2
    
AreaQuadrado = Lista[1]*Lista[1]
AreaRetangulo = Lista[0]*Lista[1]

print("TRIANGULO: {:.3f}".format(AreaTriangulo))
print("CIRCULO: {:.3f}".format(AreaCirculo))
print("TRAPEZIO: {:.3f}".format(AreaTrapezio))
print("QUADRADO: {:.3f}".format(AreaQuadrado))
print("RETANGULO: {:.3f}".format(AreaRetangulo))