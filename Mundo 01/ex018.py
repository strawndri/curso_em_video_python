# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dele.

import math

angulo = int(input('Digite o ângulo: '))

rad = math.radians(angulo) #convertendo o ânuglo para radianos
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'''Um ângulo de {angulo} graus contém: 
\n sen {angulo}° = {seno} 
\n cos {angulo}° = {cosseno} 
\n tg {angulo}° = {tangente}''')

