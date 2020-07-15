"""
trabalhar apenas na terca ou apenas na quarta, tv de 32 com sorvete
trabalhar os dois dias, tv de 50 com sorvete
nao trabalhar, sem tv, + saude
"""

trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_quinta or trabalho_terca
Saudavel = not sorvete

print('Tv50={} Tv32={} Sorvete={} Saudavel={} '.format(
    tv_50, tv_32, sorvete, Saudavel))
print('teste')