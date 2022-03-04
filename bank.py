from time import sleep

print('-' * 50)
print(f'{"JF Bank":^50}')
print('-' * 50)
print(' BEM VINDO AO NOSSO BANCO! OQUE DESEJAS FAZER?')
print('-' * 50)
# ---------- Variavéis ----------
contas = ['Nome Completo: ',
          'Data de Nascimento: ',
          # 'Graduação: ',
          # 'Experiência Profissional: ',
          'Valor Inicial: ']
usuarios = list()
senhas = []
# ------------ Corpo -------------
while True:
    print('''[1] Criar Conta
[2] Levantamento
[3] Consulta
[4] Informações dos Usuários
[5] Sair''')
    print('-' * 50)
    escolha = int(input('\033[1;34mPrima a Tecla Desejada: \033[m'))
    if escolha == 1:
        print('-' * 50)
        print(f'{"FICHA DE INSCRIÇÂO":^50}')
        print('-' * 50)
        contas[0] = str(input('Nome Completo: ')).split()
        contas[1] = int(input('Ano de Nascimento: '))
        # contas[2] = str(input('Graduação: '))
        # contas[3] = int(input('Experiência Profissional: '))
        contas[2] = int(input('Depósito Inicial: '))
        sleep(.5)
        print('-' * 50)
        print(f'\033[1;32mCADASTRAMENTO CONCLUÍDO, SEJÁ BEM-VINDO Sr. {contas[0][0]}!\033[m')
        print('-' * 50)
        sleep(.7)
        usuarios.append(contas[:])
        # print(usuarios)
    elif escolha == 2:
        user = input('Nome do Usuário: ')
        if user not in contas:
            print('Usuário Inválido!, Deseja Abrir uma Conta?')
        else:
            sake = int(input('Quanto deseja Levantar: '))
            if sake > contas[4]:
                dep = str(input('Deseja fazer outro Depósito[y/n]? '))
                if dep in 'Yy':
                    contas[4] = int(input('Novo Depósito: '))
                else:
                    print('Quantia Insuficiente')
            else:
                tr = contas[4] - sake
                print(f'Montante Restante é de: {tr}')
    elif escolha == 3:
        print('Consulta de Conta')
        print(f'Nome Completo: {contas[0]}')
        print(f'Data de Nascimento: {contas[1]}')
        # print(f'Graduação: {contas[2]}ª Classe [Médio Concluido]')
        # print(f'Experiência Profissional: {contas[3]} Anos')
        print(f'Saldo na Conta: {contas[4]}AOA')
        # print(f'BI Nº: {contas[5]}')
        # print(f'Nº Conta: {contas[6]}')
        # print(f'IBAN: {contas[7]}')
        print('-' * 50)
    elif escolha == 4:
        print('-'*50)
        print(f'Usuários: {usuarios[:]}')
        print('-'*50)
    elif escolha == 5:
        print('-'*50)
        break
