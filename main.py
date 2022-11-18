from entidades.vendedor_ouro import VendedorOuro
from dao.vendedordao import VendedorOuroDAO
from dao.msql_dao import MysqlDAO

while True:

    op = int(input('1 - Inserir \n'
                   ''))
    if op == 1:
        # inp_id = int(input('Digite o código do vendedor: '))
        # inp_nm = (input('Digite o nome do vendedor: '))
        # inp_seg = (input('Digite o segmento do vendedor: '))
        inp_id = 3
        inp_nm = 'vend3'
        inp_seg = 'ouro'
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vo = VendedorOuro(inp_id, inp_nm, inp_seg)
        vendedordao.inserir(vo)
    else:
        break
