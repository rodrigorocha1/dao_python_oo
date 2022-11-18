from abc import ABC, abstractmethod
from entidades.vendedor_ouro import VendedorOuro


class IDao(ABC):
    @abstractmethod
    def inserir(self, vendedor_ouro: VendedorOuro):
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
