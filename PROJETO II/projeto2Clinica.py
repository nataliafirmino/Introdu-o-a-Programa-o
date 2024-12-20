from prettytable import PrettyTable

'''pacientes = []
medicos = []
consultas = []'''

def cadastrarPacientes(nomePaciente, cpfPaciente):
    dados = f'NOME: {nomePaciente} || CPF: {cpfPaciente}'
    pacientes.append(dados)
    return pacientes

def cadastrarMedico(nome, crm, especialidade):
    dados = f'NOME: {nome} || CRM: {crm} || ESPECIALIDADE: {especialidade}'
    medicos.append(dados)
    return medicos

def agendarConsulta(cpfPaciente, crmMedico, dataConsulta):
    consulta = f' CPF: {cpfPaciente} || CRM: {crmMedico} || DATA DA CONSULTA: {dataConsulta}'
    consultas.append(consulta)
    return consultas

#nas funçoes de cadastramento/agendamento foi utilizado f-string para identificar as variaveis/parametro, ficando melhor a visualização e entendimento.

def atualizarEspecialidade(crm, espescialidade):
    f'CRM: {crm} || NOVA ESPECIALIDADE {especialidade}'
    for medico in range(len(medicos)): #for para percorrer o vetor de medicos.
        if crm in medicos[medico]: #condição para verificar se o crm pertence ao vetor de medicos.
            dado = medicos[medico].split('||') #separando as informações no vetor.
            dado[2] = especialidade #o indice 2 da variavel dado é igual a especialidade.
            dadoEspecialidade = f'{dado[0]} || {dado[1]} || ESPECIALIDADE: {dado[2]}' #a variavel contem dados como o nome, crm e especialidade.
            medicos.pop(medico) #excluindo as informaçoes anteriores do vetor de medicos para poder atualizar a especialidade.
            medicos.append(dadoEspecialidade) #adicionando ao vetor de medicos.
            return medicos
        
def cancelarConsulta(cpfPaciente, crmMedico, dataConsulta):
    for consulta in range(len(consultas)): #repetição para percorrer o vetor de consultas e excluir conforme dados informados no parametro.
        if cpfPaciente in consultas[consulta] and crmMedico in consultas[consulta] and dataConsulta in consultas[consulta]: #se na condiçao encontrar esses dados, excluir consulta.
            consultas.pop(consulta) #função pop para cancelar a consultas, com base nos dados informados acima.
            return consultas
        
def relatorioConsultas(cpfPaciente):
    consultasPaciente = [] #vetor individual para as consultas do paciente (por CPF).
    for consulta in range(len(consultas)): #repetição para percorrer o vetor de consultas.
        dados = consultas[consulta]
        dados = dados.split('||') #após encontrar esses dados, separar com duas barrinhas.

        dataConsulta = dados[2] #Para facilitar o trabalho na hora de imprimir o relatorio de consultas, a data está no indice 2, na variavel dados.

        if cpfPaciente in dados[0]: #condiçao para verificar se o cpf está no indice zero, a primeira posição do vetor.
            for medico in range(len(medicos)):
                if dados[1] in medicos[medico]: #condiçao para verificar se o CRM está no indice um, a segunda posição do vetor.
                    medicoDados = medicos[medico] #variavel para armazenar as informaçoes com o indice medico do vetor de medicos.
                    medicoDados = medicoDados.split('||') #separando as informaçoes com duas barrinhas
                    dadosConsulta = f'{medicoDados[0]} || {medicoDados[2]} || {dataConsulta}' #variavel para armazenar nome, especialidade e data, para exibir no relatorio.
                    dadosConsulta = dadosConsulta.split('||') #separando as informaçoes com duas barrinhas
                    consultasPaciente.append(dadosConsulta)    #adicionando ao vetor.
                     
    for paciente in range(len(pacientes)): #Pegando os dados do paciente buscado no vetor.
        if cpfPaciente in pacientes[paciente]: #condição para verificar se o cpf esta no vetor.
            dadosPaciente = pacientes[paciente] #se estiver, a variavel armazena os dados do paciente
            break #quando encontrar as informaçoes, a repetiçao para
    
    if len(consultasPaciente) == 0: #Se o vetor de consultas do paciente estiver vazio, significa que nao tem consultas para aquele paciente.
        print('NÃO HÁ REGISTROS DESSES DADOS NO SISTEMA')

    else:
        print(f'{"-"*18} INFORMAÇÕES DO PACIENTE {"-"*18}\n{dadosPaciente}\n{"-"*61}') #exibindo as informaçoes do paciente.       
        
        tabela = PrettyTable()
        tabela.field_names = ['NOME DO MÉDICO', 'ESPECIALIDADE', 'DATA DA CONSULTA']
        for i in range(len(consultasPaciente)):
            coluna = consultasPaciente[i]
            tabela.add_row(coluna)
        print(tabela) #a tabela exibe todas as informaçoes buscadas acima, e exibe as informaçoes do relatorio

arquivo = open('pacientes.txt', 'a')#abrindo a arquivo em modo a(append), para criar o arquivo.
arquivo.close()
arquivo = open('pacientes.txt')
pacientes = arquivo.read()
pacientes = pacientes.split(',')
arquivo.close()

arquivo = open('medicos.txt', 'a') #abrindo a arquivo em modo a(append), para criar o arquivo.
arquivo.close()
arquivo = open('medicos.txt')
medicos = arquivo.read()
medicos = medicos.split(',')
arquivo.close()

arquivo = open('consultas.txt', 'a') #abrindo a arquivo em modo a(append), para criar o arquivo.
arquivo.close()
arquivo = open('consultas.txt')
consultas = arquivo.read()
consultas = consultas.split(',')
arquivo.close()


#estrategia utilizada para excluir as virgulas no final das informações no arquivo.
pacientes.pop(len(pacientes)-1)
medicos.pop(len(medicos)-1)
consultas.pop(len(consultas)-1)

while True:
    print(f'''
    {'='*20} MENU {'='*20}
    || 1 - Cadastro de paciente;                ||
    || 2 - Cadastro de médico;                  ||
    || 3 - Agendar consulta;                    ||
    || 4 - Atualizar especialidade do médico;   ||
    || 5 - Cancelar consulta;                   ||
    || 6 - Relatório de consultas por paciente; ||
    || 0- Sair.                                 ||
    {'='*46}''')

    opcao = int(input('Informe um número para a opção desejada:'))

    if opcao == 0: 
        arquivo = open('pacientes.txt', 'w')
        for paciente in pacientes: #repetição para verificar no vetor o indice paciente.
            arquivo.write(paciente + ',') #escreve no arquivo, adicionando a virgula para separar as informações.
        arquivo.close()

        arquivo = open('medicos.txt', 'w')
        for medico in medicos:
            arquivo.write(medico + ',')
        arquivo.close()

        arquivo = open('consultas.txt', 'w')
        for consulta in consultas:
            arquivo.write(consulta + ',')
        arquivo.close()
        break
    


    elif opcao == 1:
        nomePaciente = input('Informe o nome do paciente:')
        cpfPaciente = input('Informe o CPF do paciente:')
        cadastrarPacientes(nomePaciente, cpfPaciente)

        input('Tecle enter para continuar...')

    elif opcao ==2:
        nomeMedico = input('Informe o nome do médico:')
        crmMedico = input('Informe o CRM do médico:')
        especialidade = input('Informe a especialidade do médico:')
        cadastrarMedico(nomeMedico, crmMedico, especialidade)

        input('Tecle enter para continuar...')

    elif opcao == 3:
        cpfPaciente = input('Informe o CPF do paciente:')
        crmMedico = input('Informe o CRM do médico:')
        dataConsulta = input('Informe a data da consulta:')
        agendarConsulta(cpfPaciente, crmMedico, dataConsulta)

        input('Tecle enter para continuar...')

    elif opcao == 4:
        crmMedico = input('Informe o CRM do médico:')
        especialidade = input('Informe a nova especialidade do médico:')
        atualizarEspecialidade(crmMedico, especialidade)

        input('Tecle enter para continuar...')
    
    elif opcao == 5:
        cpfPaciente = input('Informe o CPF do paciente:')
        crmMedico = input('Informe o CRM do médico:')
        dataConsulta = input('Informe a data da consulta que deseja cancelar:')
        cancelarConsulta(cpfPaciente, crmMedico, dataConsulta)

        input('Tecle enter para continuar...')

    elif opcao == 6:
        cpfPaciente = input('Informe o CPF do paciente:')
        for paciente in range(len(pacientes)):
            if cpfPaciente in pacientes[paciente]:
                nomePaciente = pacientes[paciente]
        relatorioConsultas(cpfPaciente)
        
        input('Tecle enter para continuar...')
