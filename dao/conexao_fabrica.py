from mysql.connector import connect
import mysql.connector.errors as error


class ConexaoFabrica:

    def conection_factory(self):
        try:
            conexao = connect(
                host='localhost',
                user='root',
                password='123456',
                database='vendedor',
                auth_plugin='mysql_native_password'
            )
            cursor = conexao.cursor()

            return conexao, cursor
        except error as err:
            print(err.msg, '-', err.sqlstate, '-', err.errno, '-', err.args)
            conexao.close()
