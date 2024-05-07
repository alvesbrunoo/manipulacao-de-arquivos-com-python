name = input('Digite seu nome:\n')

"""
- Arquivos:
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""
#Alternativa 1
# file = open('names.txt', 'a')
# file.write(f'{name}\n')
# file.close()

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')