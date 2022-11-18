from dao.idao import IDao
from entidades.vendedor_ouro import VendedorOuro
from dao.conexao_fabrica import ConexaoFabrica
import mysql.connector.errors as error


class MysqlDAO(IDao):
    def inserir(self, vendedor_ouro: VendedorOuro):

        try:
            c = ConexaoFabrica()
            conexao, cursor = c.conection_factory()

            sql_insert = f'INSERT INTO vendedor (id_vendedor, nome, segmento) ' \
                         f'VALUES ({vendedor_ouro.id_vendedor}, "{vendedor_ouro.nome}", "{vendedor_ouro.segmento}")'
            print(sql_insert)
            cursor.execute(sql_insert)
            conexao.commit()
            print('Registro Inserido')

        except error.DatabaseError as database_erro:
            print(
                f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(database_erro)
        except error.DataError as desc_erro:
            print(
                f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(desc_erro)
        finally:
            cursor.close()

    def listar_id(self, id_vendedor):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()

        cursor = conexao.cursor()
        comando = f'SELECT * FROM vendedor where id_vendedor = {id_vendedor}'
        cursor.execute(comando)
        resultado = cursor.fetchone()

        return resultado

    def listar_todos(self):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()
        sql_select_all = 'SELECT * ' \
                         'FROM vendedor.vendedor '
        cursor.execute(sql_select_all)
        dados_todos = cursor.fetchall()
        cursor.close()
        return dados_todos

    def atualizar(self, id_vendedor: int, segmento: str):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()
        sql_update = f'UPDATE vendedor ' \
                     f'SET  segmento = "{segmento}" ' \
                     f'where id_vendedor = {id_vendedor}'
        cursor.execute(sql_update)
        conexao.commit()
        cursor.close()

    def delete_id(self):
        pass

    def delete_todos(self):
        pass
