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
            print(f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(database_erro)
        except error.DataError as desc_erro:
            print(f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(desc_erro)
        finally:
            cursor.close()

    def listar_id(self):
        pass

    def listar_todos(self):
        pass

    def delete_id(self):
        pass

    def delete_todos(self):
        pass
