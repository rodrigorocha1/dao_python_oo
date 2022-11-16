import abc
from abc import ABC, abstractmethod


class Vendedor(ABC):
    def __init__(self, id_vendedor: int, nome: str, segmento: str):
        self._id_vendedor = id_vendedor
        self._nome = nome
        self._segmento = segmento

    @property
    def id_vendedor(self):
        return self._id_vendedor

    @id_vendedor.setter
    def id_vendedor(self, id_vendedor: int):
        self._id_vendedor = id_vendedor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_vend: str):
        self._nome = nome_vend

    @property
    def segmento(self):
        return self._segmento

    @segmento.setter
    def segmento(self, segmento: str):
        self._segmento = segmento

    @abstractmethod
    def calcula_comissao(self, valor_venda: float):
        pass
