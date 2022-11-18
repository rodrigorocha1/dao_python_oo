from typing import Type
from dao.idao import IDao
from entidades.vendedor_ouro import VendedorOuro


class VendedorOuroDAO:
    def __init__(self, repositorio: Type[IDao]):
        self.__repositorio = repositorio

    def inserir(self, vendedor_ouro: VendedorOuro):
        self.__repositorio.inserir(vendedor_ouro)

    def listar_id(self, id_vendedor: int):
        return self.__repositorio.listar_id(id_vendedor)

    def listar_todos(self) -> list:
        return self.__repositorio.listar_todos()

    def atualizar(self, id_vendedor: int, segmento: str):
        self.__repositorio.atualizar(id_vendedor, segmento)

    def delete_id(self, id_vendedor: int):
        self.__repositorio.delete_id(id_vendedor)

    def delete_todos(self):
        self.__repositorio.delete_todos()
