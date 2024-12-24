import limpador
import impressao_legal

from itertools import groupby


alunos = [
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Antonio', 'nota': 'C'},
    {'nome': 'Carlika', 'nota': 'A'},
    {'nome': 'Preta', 'nota': 'C'},
    {'nome': 'Karol', 'nota': 'A'},
    {'nome': 'Karoline', 'nota': 'B'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Pedro', 'nota': 'B'}
]

alunos_organizados = sorted(alunos, key=lambda aluno: aluno['nota'])
grupos = groupby(alunos_organizados, key=lambda aluno: aluno['nota'])

for chave, grupo in grupos:
    print(chave)
    impressao_legal.impressao(list(grupo))