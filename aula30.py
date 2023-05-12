velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100 # LOCAL ONDE O RADAR 1 ESTÁ
RADAR_RANGE = 1

carro_passou_no_radar = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_passou_no_radar:
    print('Velocidade carro passou do radar 1')

if carro_passou_no_radar and carro_multado:
    print('Carro multado em radar 1')