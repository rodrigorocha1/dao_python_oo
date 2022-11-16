from idao import IDao


class MysqlDAO(IDao):
    def inserir(self, id: int, nome: str, segmento: str):
        print(id, nome, segmento)

    def listar_id(self):
        pass

    def listar_todos(self):
        pass

    def delete_id(self):
        pass

    def delete_todos(self):
        pass
