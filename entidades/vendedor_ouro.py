from entidades.vendedor import Vendedor


class VendedorOuro(Vendedor):

    def __init__(self, id_vendedor: int, nome: str, segmento: str):
        super().__init__(id_vendedor, nome, segmento)

    def calcula_comissao(self, valor_venda: float):
        return valor_venda * 0.45
