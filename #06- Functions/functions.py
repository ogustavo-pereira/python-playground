

def userLogin(userName, password):
    if(userName == 'demo' and password == 'demo'):
        print('Você esta logado!')
    else:
        print('Acesso negado')



def main():
    userName=input("Insira nome do usuário: ")
    password=input("Insira a senha: ")
    userLogin(userName, password)


main()