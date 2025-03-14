import time
import os  # Para verificar se o arquivo existe antes de ler

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_USUARIOS = "usuarios.txt"

# Função para carregar os usuários do arquivo
def carregar_usuarios():
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):  # Verifica se o arquivo existe
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            for linha in arquivo:
                usuario, senha = linha.strip().split(";")  # Separa usuário e senha
                usuarios[usuario] = senha
    return usuarios

# Função para salvar um novo usuário no arquivo
def salvar_usuario(usuario, senha):
    with open(ARQUIVO_USUARIOS, "a") as arquivo:
        arquivo.write(f"{usuario};{senha}\n")  # Escreve no formato "usuario;senha"

# Função principal do sistema
def sistema():
    usuarios = carregar_usuarios()

    while True:
        print("\n📌 MENU: Escolha uma opção")
        print("1 - Criar conta")
        print("2 - Entrar na conta")
        print("3 - Sair")

        opcao = input("Digite sua escolha: ")

        # ✅ Criar conta
        if opcao == "1":
            usuario = input("Escolha um nome de usuário: ")

            if usuario in usuarios:
                print("❌ Esse nome de usuário já existe! Tente outro.")
            else:
                senha = input("Crie uma senha: ")
                usuarios[usuario] = senha  # Atualiza o dicionário
                salvar_usuario(usuario, senha)  # Salva no arquivo
                print("✅ Conta criada com sucesso!")

        # ✅ Entrar na conta
        elif opcao == "2":
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")

            if usuario in usuarios and usuarios[usuario] == senha:
                print(f"✅ Bem-vindo, {usuario}!")
                break  # Sai do loop quando o login for bem-sucedido
            else:
                print("❌ Usuário ou senha incorretos! Tente novamente.")

        # 🚪 Sair do sistema
        elif opcao == "3":
            print("👋 Saindo do sistema...")
            time.sleep(1)
            break  # Encerra o loop e finaliza o programa

        else:
            print("⚠️ Opção inválida! Escolha 1, 2 ou 3.")

# 🔥 Executa o sistema
sistema()
