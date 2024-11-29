import os

def listar_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            print(f"Diretório: {caminho}")
            listar_arquivos(caminho)
        else:
            print(f"Arquivo: {caminho}")