from entidades.vendedor_ouro import VendedorOuro
from dao.vendedorourodao import VendedorOuroDAO
from dao.msql_dao import MysqlDAO

while True:

    op = int(input('1 - Inserir \n'
                   '2 - Listar por Id\n'
                   '3 - Listar todos\n'
                   '4 - Atualizar segmento do vendedor\n'
                   '5- Apagar um registro\n'
                   '6 - Apagar todos'))
    if op == 1:
        # inp_id = int(input('Digite o código do vendedor: '))
        # inp_nm = (input('Digite o nome do vendedor: '))
        # inp_seg = (input('Digite o segmento do vendedor: '))
        inp_id = 5
        inp_nm = 'vend5'
        inp_seg = 'ouro'
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vo = VendedorOuro(inp_id, inp_nm, inp_seg)
        vendedordao.inserir(vo)
    elif op == 2:
        id_vendedor = 4
        b = VendedorOuroDAO(MysqlDAO())
        vendedor = b.listar_id(id_vendedor)
        print(vendedor)

    elif op == 3:
        vendedordao = VendedorOuroDAO(MysqlDAO())
        lista_todos = vendedordao.listar_todos()
        for vendedor in lista_todos:
            print(vendedor)

    elif op == 4:
        segmento = 'prata'
        id_vendedor = 1
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vendedordao.atualizar(id_vendedor, segmento)

    elif op == 5:
        id_vendedor = 1
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vendedordao.delete_id(id_vendedor)

    elif op == 6:
        vendedordao = VendedorOuroDAO(MysqlDAO())
        vendedordao.delete_todos()

    else:
        break
