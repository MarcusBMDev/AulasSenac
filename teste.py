import math

# Função para calcular a quantidade de latas necessárias
def calcular_latas(area):
    cobertura_por_lata = 18 * 6  # 1 lata de 18 litros cobre 18 * 6 metros quadrados
    quantidade_latas = math.ceil(area / cobertura_por_lata)  # Arredonda para cima
    return quantidade_latas

# Função para calcular a quantidade de galões necessários
def calcular_galoes(area):
    cobertura_por_galao = 3.6 * 6  # 1 galão de 3,6 litros cobre 3,6 * 6 metros quadrados
    quantidade_galoes = math.ceil(area / cobertura_por_galao)  # Arredonda para cima
    return quantidade_galoes

# Função para calcular a quantidade de latas e galões misturados
def calcular_mistura(area):
    cobertura_por_lata = 18 * 6
    cobertura_por_galao = 3.6 * 6
    quantidade_latas_cheias = math.ceil(area / cobertura_por_lata)  # Arredonda para baixo
    area_restante = area - quantidade_latas_cheias * cobertura_por_lata
    quantidade_galoes = math.ceil(area_restante / cobertura_por_galao)  # Arredonda para cima
    return quantidade_latas_cheias, quantidade_galoes

# Função para calcular o preço em cada situação
def calcular_preco(area):
    quantidade_latas = calcular_latas(area)
    quantidade_galoes = calcular_galoes(area)
    quantidade_latas_cheias, quantidade_galoes_mistura = calcular_mistura(area)

    preco_latas = quantidade_latas * 80
    preco_galoes = quantidade_galoes * 25
    preco_mistura = (quantidade_latas_cheias * 80) + (quantidade_galoes_mistura * 25)

    return preco_latas, preco_galoes, preco_mistura

# Solicitar a entrada do usuário
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcular e exibir os resultados
preco_latas, preco_galoes, preco_mistura = calcular_preco(area_a_ser_pintada)

print(f"Quantidade de latas a serem compradas: {calcular_latas(area_a_ser_pintada)}")
print(f"Preço total comprando apenas latas: R$ {preco_latas:.2f}")

print(f"Quantidade de galões a serem comprados: {calcular_galoes(area_a_ser_pintada)}")
print(f"Preço total comprando apenas galões: R$ {preco_galoes:.2f}")

quantidade_latas_cheias, quantidade_galoes_mistura = calcular_mistura(area_a_ser_pintada)
print(f"Quantidade de latas a serem compradas na mistura: {quantidade_latas_cheias}")
print(f"Quantidade de galões a serem comprados na mistura: {quantidade_galoes_mistura}")
print(f"Preço total na mistura: R$ {preco_mistura:.2f}")