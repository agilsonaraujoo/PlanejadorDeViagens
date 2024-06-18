import os
import time
from datetime import datetime

'''AQUI DEFINIREMOS O NOME DO ARQUIVO'''
armazena_usuarios = 'usuarios.txt'
armazena_viagens = 'viagens.txt'

'''CADASTRO DO USUÁRIO ATRAVÉS DA FUNÇÃO CADASTRAR USUÁRIO'''
def cadastrar_usuario(usuarios):
    usuario = input("Digite o nome de usuário: ")
    if usuario in usuarios:
        print("O usuário que você acabou de colocar já existe!")
    else:
        senha = input("Digite a senha: ")
        usuarios[usuario] = senha
        salvar_usuarios(usuarios)
        print("Seu usuário acaba de ser registrado com sucesso!")

'''AUTENTICAÇÃO DE USUÁRIO'''
def autenticar_usuario(usuarios):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido!")
        return usuario
    else:
        print("Usuário ou senha incorretos!")
        return None

'''CARREGAMENTO DOS USUARIOS QUE ESTÃO NO ARQUIVO TXT'''
def carregar_usuarios():
    usuarios = {}
    if os.path.exists(armazena_usuarios):
        with open(armazena_usuarios, 'r', encoding='utf-8') as arquivo_usua:
            for linha in arquivo_usua:
                usuario, senha = linha.strip().split(':')
                usuarios[usuario] = senha
    return usuarios

'''ESSA FUNÇÃO TEM COMO INTUITO SALVAR OS USUARIOS NO ARQUIVO TXT '''
def salvar_usuarios(usuarios):
    with open(armazena_usuarios, 'w', encoding='utf-8') as arquivo_usua:
        for usuario, senha in usuarios.items():
            arquivo_usua.write(f"{usuario}:{senha}\n")

'''NESSA FUNÇÃO O OBJETIVO É ADICIONAR UMA VIAGEM NOVA'''
def adicionar_viagem(viagens, usuario):
    destino = input("Digite o destino: ")
    
    while True:
        try:
            data_inicio_str = input("Digite a data de início (DATA/MÊS/ANO): ")
            data_inicio = validar_data(data_inicio_str)
            
            data_termino_str = input("Digite a data de término (DATA/MÊS/ANO): ")
            data_termino = validar_data(data_termino_str)
            
            if data_termino < data_inicio:
                raise ValueError("A data de término não pode ser anterior à data de início.")
            
            if data_inicio < datetime.now().date():
                raise ValueError("A data de início não pode ser anterior à data atual.")
            
            break
        
        except ValueError:
            print(f"Data inválida. Use o formato DATA/MÊS/ANO.")
    
    atividades = input("Adicione atividades para essa viagem separado por vírgula: ").split(',')
    
    if usuario not in viagens:
        viagens[usuario] = []
    
    viagens[usuario].append({
        "destino": destino,
        "data_inicio": data_inicio_str,
        "data_termino": data_termino_str,
        "atividades": atividades
    })
    
    salvar_viagens(viagens)
    print('Carregando informações...')
    time.sleep(3)
    print("Viagem adicionada com sucesso!")

'''AQUI SERÁ CONVERTIDO UMA STRING EM DATA'''
def validar_data(data_str):
    return datetime.strptime(data_str, '%d/%m/%Y').date()

'''LISTAMENTO DAS VIAGENS DO USUÁRIO'''
def listar_viagens(viagens, usuario):
    if usuario in viagens:
        for idx, viagem in enumerate(viagens[usuario], 1):
            print(f"Viagem {idx}: {viagem}")
    else:
        print("Nenhuma viagem encontrada para este usuário.")

'''AQUI SERÁ A FUNÇÃO QUE DARÁ A POSSIBILIDADE DO USUÁRIO EXCLUIR UMA VIAGEM!'''
def excluir_viagem(viagens, usuario):
    if usuario in viagens and viagens[usuario]:
        listar_viagens(viagens, usuario)
        viagem_idx = int(input("Digite o número da viagem que deseja excluir: ")) - 1
        if 0 <= viagem_idx < len(viagens[usuario]):
            viagens[usuario].pop(viagem_idx)
            salvar_viagens(viagens)
            print("A viagem acabou de ser excluida")
        else:
            print("O índice da viagem que você quer cancelar é inválido!")
    else:
        print("Não encontramos nenhuma viagem para esse usuário.")

'''Aqui é onde as viagens do arquivo txt serão carregadas!'''
def carregar_viagens():
    viagens = {}
    if os.path.exists(armazena_viagens):
        with open(armazena_viagens, 'r', encoding='utf-8') as file:
            usuario_atual = None
            for linha in file:
                linha = linha.strip()
                if linha.startswith('Usuário:'):
                    usuario_atual = linha.split(':')[1]
                    viagens[usuario_atual] = []
                elif usuario_atual:
                    partes = linha.split('|')
                    viagem = {
                        "destino": partes[0],
                        "data_inicio": partes[1],
                        "data_termino": partes[2],
                        "atividades": partes[3].split(',')
                    }
                    viagens[usuario_atual].append(viagem)
    return viagens

'''AQUI SERÁ ONDE SALVARESMOS A VIAGEM NO ARQUIVO TXT.'''
def salvar_viagens(viagens):
    with open(armazena_viagens, 'w', encoding='utf-8') as file:
        for usuario, lista_viagens in viagens.items():
            file.write(f"Usuário:{usuario}\n")
            for viagem in lista_viagens:
                atividades = ','.join(viagem['atividades'])
                file.write(f"{viagem['destino']}|{viagem['data_inicio']}|{viagem['data_termino']}|{atividades}\n")

'''ESSA É A FUNÇÃO MAIN OU FUNÇÃO PRINCIPAL, TODAS AS OUTRAS FUNÇÕES FICAM DENTRO DELA.'''

def main():
    usuarios = carregar_usuarios()
    viagens = carregar_viagens()
    
    while True:
        print("\n1. Fazer Login\n2. Cadastrar\n3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            usuario = autenticar_usuario(usuarios)
            if not usuario:
                print("Usuário ainda não possui conta. Por favor, cadastre-se.")
                continue
            
            while True:
                print("\n1. Adicionar Viagem\n2. Listar Viagens\n3. Deletar Viagem\n4. Sair")
                opcao = input("Escolha uma opção: ")
                
                if opcao == '1':
                    adicionar_viagem(viagens, usuario)
                elif opcao == '2':
                    listar_viagens(viagens, usuario)
                elif opcao == '3':
                    excluir_viagem(viagens, usuario)
                elif opcao == '4':
                    break
                else:
                    print("A opção que você inseriu é inválida!")
        
        elif escolha == '2':
            cadastrar_usuario(usuarios)
        
        elif escolha == '3':
            print("Saindo...")
            time.sleep(3)
            print('Sistema finalizado com sucesso')
            break
        
        else:
            print("A opção que você inseriu é inválida!")

main()
