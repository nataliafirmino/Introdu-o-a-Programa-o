#Crie uma função que recebe como parâmetros o login e a senha do usuário.
#Caso seja “fernanda” e 12345, retorne verdadeiro, caso contrário retorne falso.

def logar(login,senha):
    if  login=='fernanda' and senha==12345:
        return True
    else:
        return False
    
login=input('Informe o login:')
senha=int(input('Informe a senha:'))
resultado=logar(login,senha)
if  resultado==True:
    print('LOGIN EFETUADO')
else:
    print('LOGIN NEGADO')