from controller import ControllerCadastro, ControllerLogin

while True:
    print('========== [MENU] ==========')
    decidir = int(input('Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair\n'))
    if decidir == 1:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email:')
        senha = input('Digite sua senha: ')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        if resultado == 2:
            print('Tamanho do nome inválido')
        elif resultado == 3:
            print('Email maior que 200 caracteres')
        elif resultado == 4:
            print('Tamanho de senha inválido')
        elif resultado == 5:
            print('O email já está cadastrado')
        elif resultado ==6:
            print('Erro interno do sistema')
        elif resultado == 1:
            print('Cadastro realizado com sucesso')
    elif decidir == 2:
        email = input('Digite seu email')
        senha = input('Digite sua senha')
        resultado = ControllerLogin.login(email, senha)
        if not resultado:
            print('Email ou senha inválidos')
        else:
            print(resultado)
    else:
        break