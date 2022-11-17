from entidades.vendedor_ouro import VendedorOuro

while True:
    op = int(input('1 - Inserir \n'
                   ''))
    if op == 1:
        inp_id = int(input('Digite o código do vendedor'))
        inp_nm = int(input('Digite o nome do vendedor'))
        inp_seg = int(input('Digite o segmento do vendedor'))

        vo = VendedorOuro(inp_id, inp_nm, inp_seg)



    else:
        break
