ProdutoUm = input()
ProdutoDois = input()

ListaUm = ProdutoUm.split()
ListaDois = ProdutoDois.split()

ListaFUm = [float(val) for val in ListaUm]
ListaFDois = [float(val) for val in ListaDois]

if ListaFUm[1] or ListaFDois[1] > 0:
    MultiLUm = ListaFUm[1] * ListaFUm[2]
    MultiLDois = ListaFDois[1] * ListaFDois[2]
    TotalSomaListas: float = MultiLUm + MultiLDois
print("VALOR A PAGAR: R$ {:.2F}".format(TotalSomaListas))