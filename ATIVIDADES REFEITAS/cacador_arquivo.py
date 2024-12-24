import os

os.system('cls')

def lista_arquivos(pasta=None):
    while True:
        if pasta is None:
            pasta = input(r'Digite o endereço completo da pasta, sem aspas "": ').strip()

        try:
            arquivos = os.listdir(pasta)  # Lista os arquivos na pasta
            print('\nArquivos encontrados na pasta:')
            print(*arquivos, sep='\n')  # Exibe os arquivos
        except FileNotFoundError:
            print('Erro: Pasta não encontrada.')
            pasta = None  # Permite que o usuário insira novamente
            continue
        except PermissionError:
            print('Erro: Permissão negada ao acessar a pasta.')
            pasta = None  # Permite que o usuário insira novamente
            continue
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return

        # Pergunta ao usuário o que deseja fazer
        print("\nOpções:")
        print("1 - Abrir um arquivo")
        print("2 - Abrir uma subpasta")
        print("3 - Encerrar o programa")
        escolha = input("Digite o número da sua escolha: ").strip()

        if escolha == '1':  # Abrir arquivo
            nome_arquivo = input('Digite o nome do arquivo (com extensão): ').strip()
            caminho_completo = os.path.join(pasta, nome_arquivo)

            try:
                os.startfile(caminho_completo)  # Abre o arquivo
                print(f'Arquivo "{nome_arquivo}" foi aberto com sucesso!')
            except FileNotFoundError:
                print(f'Erro: Arquivo "{nome_arquivo}" não encontrado.')
            except Exception as e:
                print(f'Erro ao abrir o arquivo: {e}')

        elif escolha == '2':  # Abrir subpasta
            subpasta = input('Digite o nome da subpasta que deseja abrir: ').strip()
            nova_pasta = os.path.join(pasta, subpasta)

            if os.path.isdir(nova_pasta):
                pasta = nova_pasta  # Atualiza a pasta atual
                print(f'Abrindo subpasta: {nova_pasta}')
            else:
                print(f'Erro: "{subpasta}" não é uma pasta válida.')

        elif escolha == '3':  # Encerrar
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Chama a função
lista_arquivos()
