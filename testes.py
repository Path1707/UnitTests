import pytest
import csv
import main

# ------------------- Passo 2 -------------------------
def teste_positivo_calcular_area_de_um_cubo():
    altura = 5
    largura = 5

    resultado_obtido = main.area_de_um_cubo(altura, largura)
    resultado_esperado = 150

    assert resultado_obtido == resultado_esperado


def teste_negativo_calcular_area_de_um_cubo():
    altura = 5
    largura = 0

    resultado_obtido = main.area_de_um_cubo(altura, largura)
    resultado_esperado = 'Altura ou largura inválidos'

    assert resultado_obtido == resultado_esperado
# ----------------------------------------------------

# ------------------- Passo 3 -------------------------
lista_para_testes = [
    (3, 6, 18),
    (3, 0, 'Base ou altura invalidos'),
    (-3, 6, 'Base ou altura invalidos'),
    (0, -6, 'Base ou altura invalidos')
]


@pytest.mark.parametrize('base, altura, resultado_esperado', lista_para_testes)
def teste_area_de_um_paralelegrama(base, altura, resultado_esperado):
    resultado_obtido = main.area_de_um_paralelograma(base, altura)
    assert resultado_obtido == resultado_esperado


# ----------------------------------------------------

# ------------------- Passo 4 -------------------------
def ler_dados_csv():
    dados_csv = []
    caminho_do_arquivo = 'C:\\Users\\pathm\\PycharmProjects\\UnitTests\\vendors\\massa_area_piramide.csv'
    try:
        with open(caminho_do_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'arquivo não encontrado: {caminho_do_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


@pytest.mark.parametrize('id, base, altura, resultado_esperado, tipo_teste', ler_dados_csv())
def teste_area_de_uma_piramide_regular(id, base, altura, resultado_esperado, tipo_teste):
    resultado_obtido = main.area_de_uma_piramide_regular(int(base), int(altura))

    if tipo_teste == 'positivo':
        assert float(resultado_esperado) == resultado_obtido
    else:
        assert resultado_esperado == resultado_obtido

# --------------------------------------------------------
