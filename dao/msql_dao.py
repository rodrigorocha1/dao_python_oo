from dao.idao import IDao
from entidades.vendedor_ouro import VendedorOuro
from dao.conexao_fabrica import ConexaoFabrica
import mysql.connector.errors as error
from colorama import Fore, Style


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
            print(Fore.GREEN, 'Registro Inserido')
            print(Style.RESET_ALL)
            print()

        except error.DatabaseError as database_erro:
            print(Fore.RED,
                  f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(database_erro)
            print(Style.RESET_ALL)
        except error.DataError as desc_erro:
            print(Fore.RED,
                  f'Erro ao inserir o registro {vendedor_ouro.id_vendedor}, {vendedor_ouro.nome}, {vendedor_ouro.segmento}')
            print(desc_erro)
            print(Style.RESET_ALL)
        finally:
            cursor.close()

    def listar_id(self, id_vendedor):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()

        cursor = conexao.cursor()
        comando = f'SELECT * FROM vendedor where id_vendedor = {id_vendedor}'
        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(Fore.GREEN, 'Sucesso')
        print(Style.RESET_ALL)
        return resultado

    def listar_todos(self):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()
        sql_select_all = 'SELECT * ' \
                         'FROM vendedor.vendedor '
        cursor.execute(sql_select_all)
        dados_todos = cursor.fetchall()
        cursor.close()
        print(Fore.GREEN, 'Sucesso')
        print(Style.RESET_ALL)
        return dados_todos

    def atualizar(self, id_vendedor: int, segmento: str):
        try:
            c = ConexaoFabrica()
            conexao, cursor = c.conection_factory()
            sql_update = f'UPDATE vendedor ' \
                         f'SET  segmento = "{segmento}" ' \
                         f'where id_vendedor = {id_vendedor}'
            cursor.execute(sql_update)
            conexao.commit()
            cursor.close()
            print(Fore.GREEN, 'Atualização feita')
            print(Style.RESET_ALL)

        except error.DataError as database_error:
            print(Fore.RED, f'Error no tipo de dado:  {id_vendedor} - {database_error}')
            print(Style.RESET_ALL)
            cursor.close()

    def delete_id(self, id_vendedor: int):
        try:
            c = ConexaoFabrica()
            conexao, cursor = c.conection_factory()
            sql_delete_id = f'DELETE from vendedor ' \
                            f'where id_vendedor = {id_vendedor} '
            cursor.execute(sql_delete_id)
            conexao.commit()
            cursor.close()
            print(Fore.GREEN, 'Delete Feito')
            print(Style.RESET_ALL)
        except error.DataError as database_error:
            print(Fore.RED, f'Error no tipo de dado:  {id_vendedor} - - {database_error}')
            print(Style.RESET_ALL)
            cursor.close()

    def delete_todos(self):
        c = ConexaoFabrica()
        conexao, cursor = c.conection_factory()
        sql_delete_todos = f'DELETE from vendedor '
        cursor.execute(sql_delete_todos)
        print(Fore.GREEN, 'Delete Feito')
        print(Style.RESET_ALL)
        conexao.commit()
        cursor.close()
