from typing import Type
from dao.idao import IDao
from entidades.vendedor_ouro import VendedorOuro


class VendedorOuroDAO:
    def __init__(self, repositorio: Type[IDao]):
        self.__repositorio = repositorio

    def inserir(self, vendedor_ouro: VendedorOuro):
        self.__repositorio.inserir(vendedor_ouro)

    def listar_id(self, id_vendedor: int):
        pass

    def listar_todos(self):
        pass

    def delete_id(self):
        pass

    def delete_todos(self):
        pass
