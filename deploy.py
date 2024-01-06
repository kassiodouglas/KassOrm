import re

nova_versao = input("Digite a nova versão (por exemplo, 0.1.1): ")

with open('setup.py', 'r') as f:
    conteudo = f.read()

conteudo_atualizado = re.sub(r'version=\'[0-9.]*\'', f'version=\'{nova_versao}\'', conteudo)

with open('setup.py', 'w') as f:
    f.write(conteudo_atualizado)
