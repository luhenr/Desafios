"""
Como eles estão viajando em direções opostas, a distância entre eles está diminuindo a uma taxa de 110 km/h + 80 km/h = 190 km/h.

Usando a fórmula da velocidade média, podemos calcular o tempo que leva para eles se encontrarem:

tempo = distância / velocidade média

Como a distância entre as duas cidades é de 100 km, a distância que eles cobrem antes de se encontrarem é de 50 km para cada um. Então, o tempo que leva para eles se encontrarem é:

tempo = 50 km / 190 km/h = 0,263 horas = 15,78 minutos

Agora que sabemos em quanto tempo eles se encontrarão, podemos calcular a distância que cada um percorre antes disso.

O carro viaja a uma velocidade constante de 110 km/h, então em 15,78 minutos ele percorre:

distância percorrida pelo carro = velocidade × tempo = 110 km/h × (15,78 minutos / 60) = 28,67 km

O caminhão viaja a uma velocidade de 80 km/h, mas leva 5 minutos a mais em cada pedágio, então sua velocidade efetiva é de:

velocidade efetiva do caminhão = distância / tempo = 80 km/h × (1 hora / 1,083 horas) = 73,8 km/h

O tempo que o caminhão leva para percorrer os 50 km até encontrar o carro é:

tempo = distância / velocidade = 50 km / 73,8 km/h = 0,678 horas = 40,68 minutos

Durante esse tempo, o caminhão também passa por dois pedágios, o que adiciona 10 minutos ao seu tempo total. Portanto, a distância que ele percorre antes de se encontrar com o carro é:

distância percorrida pelo caminhão = velocidade × tempo = 73,8 km/h × (50,68 minutos / 60) = 62,01 km

Agora podemos calcular a distância de cada veículo até Ribeirão Preto no momento em que eles se encontram. O carro já percorreu 28,67 km nessa direção, então está a uma distância de:

distância do carro a Ribeirão Preto = 100 km - 28,67 km = 71,33 km

O caminhão, por outro lado, já percorreu 62,01 km na direção oposta, então está a uma distância de:

distância do caminhão a Ribeirão Preto = 100 km + 62,01 km = 162,01 km
"""
distancia_total = 100
velocidade_carro = 110
velocidade_caminhao = 80
tempo_pedagio = 5

# Converter o tempo do pedágio de minutos para horas
tempo_pedagio = tempo_pedagio / 60

# Calcular o tempo que leva para os veículos se encontrarem
velocidade_media = velocidade_carro + velocidade_caminhao
tempo_encontro = distancia_total / velocidade_media

# Calcular a distância percorrida por cada veículo até o encontro
distancia_carro = velocidade_carro * (tempo_encontro - (tempo_pedagio / 60))
distancia_caminhao = velocidade_caminhao * tempo_encontro + \
    (2 * tempo_pedagio * velocidade_caminhao / 60)

# Calcular a distância de cada veículo até Ribeirão Preto no momento do encontro
distancia_carro_rp = distancia_total - distancia_carro
distancia_caminhao_rp = distancia_total + distancia_caminhao

# Verificar qual veículo está mais próximo de Ribeirão Preto
if distancia_carro_rp < distancia_caminhao_rp:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
