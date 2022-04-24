
def area_de_um_cubo(altura, largura):
    if altura > 0 and largura > 0:
        return 6 * altura * largura
    else:
        return 'Altura ou largura inválidos'


def area_de_um_paralelograma(base, altura):
    if base > 0 and altura > 0:
        return base * altura
    else:
        return 'Base ou altura invalidos'

def area_de_uma_piramide_regular(base, altura):
    if base > 0 and altura > 0:
        area_face = (base * altura) / 2
        area_base = base**2
        return (4 * area_face) + area_base
    else:
        return 'Base ou altura invalidos'

def verificar_se_e_numero(candidato):
    try:
        float(candidato)
    except:
        return False
    return True




if __name__ == '__main__':

    resultado = area_de_um_cubo(5, 5)
    if verificar_se_e_numero(resultado):
        print(f'Area total (cubo) = {resultado}m²')
    else:
        print(f'Mensagem: {resultado}')


    resultado = area_de_um_paralelograma(8, 5)
    if verificar_se_e_numero(resultado):
        print(f'Area total (paralelograma) = {resultado}m²')
    else:
        print(f'Mensagem: {resultado}')

    resultado = area_de_uma_piramide_regular(18, 15)
    if verificar_se_e_numero(resultado):
        print(f'Area total (pirâmide regular) = {resultado}m²')
    else:
        print(f'Mensagem: {resultado}')









