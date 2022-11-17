import mysql.connector


class ConexaoFabrica:
    def conection_factory(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456',
                database='vendedor'
            )
            return conexao.cursor()
        except mysql.connector.Error as err:
            print(err.msg, '-', err.sqlstate, '-', err.errno, '-', err.args)
        finally:
            conexao.close()
