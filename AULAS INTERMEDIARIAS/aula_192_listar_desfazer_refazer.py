import limpador
import os
import json

# Inicializar listas
listador = []
desfeitas = []

# Verifica se o arquivo JSON existe e carrega os dados existentes
arquivo_json = 'listas.json'
if os.path.exists(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        try:
            listador = json.load(arquivo)
        except json.JSONDecodeError:
            listador = []
else:
    # Cria o arquivo vazio caso não exista
    with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump([], arquivo)

while True:
    entrada = input('\nLISTAR, DESFAZER, REFAZER\nDIGITE UMA TAREFA OU COMANDO: ').strip().lower()

    if entrada == 'listar':
        print("\nTarefas atuais:")
        print("\n".join(listador) if listador else "Nenhuma tarefa adicionada.")

    elif entrada == 'desfazer':
        if listador:
            ultima_tarefa = listador.pop()
            desfeitas.append(ultima_tarefa)
            print(f"Tarefa '{ultima_tarefa}' desfeita.")
        else:
            print("Nenhuma tarefa para desfazer.")

    elif entrada == 'refazer':
        if desfeitas:
            tarefa_refeita = desfeitas.pop()
            listador.append(tarefa_refeita)
            print(f"Tarefa '{tarefa_refeita}' refeita.")
        else:
            print("Nenhuma tarefa para refazer.")

    elif entrada == 'limpar':
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela no Windows ou Linux/Mac

    elif entrada == 's':
        print("Encerrando o programa.")
        break

    elif entrada:
        listador.append(entrada)
        desfeitas.clear()  # Limpa o histórico de desfeitas após adicionar uma nova tarefa
        print(f"Tarefa '{entrada}' adicionada.")

    else:
        print("Entrada inválida, tente novamente.")

    # Atualiza o arquivo JSON com as mudanças
    with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump(listador, arquivo, indent=4)







