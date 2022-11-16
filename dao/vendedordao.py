from typing import Type
from dao.idao import IDao
from dao.msql_dao import MysqlDAO


class VendedorDAO:
    def __init__(self, repositorio: Type[IDao]):
        self.__repositorio = repositorio

    def inserir(self, id: int, nome: str, segmento: str):
        self.__repositorio.inserir(id, nome, segmento)

    def listar_id(self):
        pass

    def listar_todos(self):
        pass

    def delete_id(self):
        pass

    def delete_todos(self):
        pass


