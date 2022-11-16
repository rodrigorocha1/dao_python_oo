from abc import ABC, abstractmethod


class IDao(ABC):
    @abstractmethod
    def inserir(self, id: int, nome: str, segmento: str):
        pass

    @abstractmethod
    def listar_id(self):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def delete_id(self):
        pass

    @abstractmethod
    def delete_todos(self):
        pass