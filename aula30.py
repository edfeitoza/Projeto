'''
CONSTANTE => "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
#Variaveis em minusculo acomodam valores variaveis
velocidade = 65     #velocidade atual do carro
local_carro = 102    #local em que o carro esta na estrada

#VARIAVEIS EM MAIUSCULO ACOMODAM VALORES CONSTANTES
RADAR_1 = 60        #velocidade maxima do radar 1
LOCAL_1 = 100       #local onde o radar 1 esta
RADAR_RANGE = 1     #A distancia onde o radar pega

#Diminuindo complexidade do código
velocidade_radar = velocidade > RADAR_1
Local_Radar_Range1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
Local_Radar_Range2 = local_carro >= (LOCAL_1 + RADAR_RANGE)


if velocidade_radar:
    print('Velocidade acima do permitido no radar1')

if Local_Radar_Range1 and Local_Radar_Range2 and velocidade_radar:
    print('Carro multado no Radar1')
    
else:
    print('Carro não foi multado!')