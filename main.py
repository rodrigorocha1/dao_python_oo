from entidades.vendedor_ouro import VendedorOuro
from dao.vendedordao import VendedorOuroDAO
from dao.msql_dao import MysqlDAO
from dao.banco import BANCO

while True:

    op = int(input('1 - Inserir \n'
                   '2 - Listar por Id'))
    if op == 1:
        # inp_id = int(input('Digite o código do vendedor: '))
        # inp_nm = (input('Digite o nome do vendedor: '))
        # inp_seg = (input('Digite o segmento do vendedor: '))
        inp_id = 4
        inp_nm = 'vend4'
        inp_seg = 'ouro'
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vo = VendedorOuro(inp_id, inp_nm, inp_seg)
        vendedordao.inserir(vo)
    elif op == 2:
        id_vendedor = 2
        b = VendedorOuroDAO(MysqlDAO())
        vendedor = b.listar_id(id_vendedor)
        print(vendedor)

    elif op == 3:
        vendedordao = VendedorOuroDAO(MysqlDAO())
        print(vendedordao.listar_todos())



    else:
        break
