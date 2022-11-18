from dao.conexao_fabrica import ConexaoFabrica
from dao.idao import IDao
from entidades.vendedor_ouro import VendedorOuro


class BANCO(IDao):

    def inserir(self, vendedor_ouro: VendedorOuro):
        pass

    def listar_id(self, id_vendedor):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()

        cursor = conexao.cursor()
        comando = f'SELECT * FROM vendedor where id_vendedor = {id_vendedor}'
        cursor.execute(comando)
        resultado = cursor.fetchone()

        return resultado

    def listar_todos(self):
        pass

    def delete_id(self):
        pass

    def delete_todos(self):
        pass
