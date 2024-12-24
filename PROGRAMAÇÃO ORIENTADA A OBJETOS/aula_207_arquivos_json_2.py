import limpar
import json

from aula_207_arquivos_json_1 import FILE_PATH, Person

with open(FILE_PATH, 'r') as files:
    data = json.load(files)
    print(*data, sep='\n')
