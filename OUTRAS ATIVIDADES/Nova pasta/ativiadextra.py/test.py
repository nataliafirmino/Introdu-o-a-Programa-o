# Solicitar um número inteiro de três dígitos ao usuário
numero = int(input("Digite um número inteiro de três dígitos: "))

# Separar os dígitos usando divisões e módulos
primeiro_digito = numero // 100
segundo_digito = (numero // 10) % 10
terceiro_digito = numero % 10

# Calcular a soma dos dígitos
soma_digitos = primeiro_digito + segundo_digito + terceiro_digito

# Exibir o resultado
print("A soma dos dígitos é:", soma_digitos)

