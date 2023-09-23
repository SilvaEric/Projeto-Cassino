from time import sleep
from random import randint
import os
saldo=0
def menu ():
    print('___[    MENU CASSINO    ___')
    print('___[ 1 ] Jogo Par X Impar _')
    print('___[ 2 ] Jogo do Bicho ____')
    print('___[ 3 ] Jogo Pedra, Papel, Tesoura_')
    print('___[ 4 ] Jogo do Dado _____')
    print('___[ 5 ] Inserir Fichas ___')
    print('___[ 6 ] Consultar Saldo___')
    acao=int(input(' O que deseja fazer : '))
    if acao == 1:
        os.system('cls')
        Jogo_Impar_x_Par()
        
    elif acao== 2 :
        os.system('cls')
        Jogo_Bicho()
    elif acao== 3:
        os.system('cls')
        Jogo_P_P_T()
       
    elif acao == 4:
        os.system('cls')
        Jogo_Dado()
        
    elif acao==5 :
        os.system('cls')
        inserir_fichas()
       
    elif acao==6 :
        os.system('cls')
        Consultar_Saldo()

def Consultar_Saldo ():
    global saldo
    print(f'Saldo Atual : {saldo} ')
    quest=int(input(' Deseja retornar ao Menu ? Digite [1] \n Deseja Inserir Credito ? Digite [2]\n Insira sua ação :'))
    if quest == 1:
        menu()
    if quest == 2:
        inserir_fichas()

def inserir_fichas ():
    global saldo
    fichas=int(input('Insira o valor de fichas que você deseja depositar :'))
    saldo += fichas
    menu()
    return saldo

def inserir_fichas_Durante_Jogo ():
    global saldo
    fichas=int(input('Insira o valor de fichas que você deseja depositar :'))
    saldo += fichas
    print('    [1] Continuar Jogo')
    print('    [2] Menu')
    quest=int(input(':'))
    if quest == 1:
        return saldo
    if quest ==2:
        menu()
        return saldo

def debitar_fichas (Valor_apostado):
    global saldo
    saldo-= Valor_apostado
    return saldo

def creditar_fichas(Valor_apostado, Multiplicador):
    global saldo
    saldo+= Valor_apostado + (Valor_apostado*Multiplicador)
    return saldo

def Checar_valor(valor_apostado, saldo):
    if valor_apostado <= saldo :
        return True
    else :
        return False

def Jogo_Bicho ():
        #boas vindas ao jogo do bicho
    print('[        BEM VINDO AO JOGO DO BICHO      ]')

    #Resumo
    print('O jogo do bicho consiste na seguinte maneira, cada animal possui seu número próprio, totalizando 25 animais e logicamente 25 numeros (1 à 25). \n\nVocê poderá consultar a lista de cada animal com seu respectivo número, ANTES DE selecionar o número em que deseja APOSTAR \n\nApós consultar a lista voce deverá escolher um numero \ncaso o numero do animal que voce escolheu, for igual ao do animal sorteado, voce tera como premiação 25x o valor de sua aposta, se não, voce perderá TODO o valor apostado\n ')

    #Regras
    print('[REGRAS]\n1.Voce nao pode apostar um valor maior do que aquele que possui\n2.voce so deve escolher um numero entre 1 e 25 \n\n')

    #opçao continuar ou voltar
    check=str(input('Se deseja CONTINUAR tecle: [C]\n\n   Se deseja VOLTAR AO MENU tecle: [V] \n:')).upper()
    while check == 'C':

        #lista jogo do bicho
        lista=['1 - Avestruz','2 - Águia','3 - Burro','4 - Borboleta','5 - Cachorro','6 - Cabra','7 - Carneiro','8 - Camelo','9 - Cobra','10 - Coelho','11 - Cavalo','12 - Elefante','13 - Galo','14 - Gato','15 - Jacaré','16 - Leão','17 - Macaco','18 - Porco','19 - Pavão','20 - Peru','21 - Touro','22 - Tigre','23 - Urso','24 - Veado','25 - Vaca\n\n']

        #Pedir ao usuario que escolha um numero correspondente a um animal e mostrar opçoes
        escolha_n_animal_usr=int(input('Escolha O NUMERO corresponde ao animal que você deseja ( se nao souber qual o numero para o seu animal você podera teclar [0] para consultar a lista de numeração dos animais ):'))
        while escolha_n_animal_usr == 0:
            for x in lista:
                print(x)
            escolha_n_animal_usr=int(input('\n\nEscolha O NUMERO corresponde ao animal que você deseja : '))
            
        while escolha_n_animal_usr <1 or escolha_n_animal_usr>25 :
                escolha_n_animal_usr=int(input('\n\nNumero inválido insira um numero existente na lista : '))
        #perguntar ao usuario o valor da aposta
        valor_aposta=int(input('\n\nInsira o valor da sua aposta :'))

        #checagem do saldo do usuario limite = saldo do usuario
        global saldo

        while not Checar_valor(valor_aposta, saldo) :
            valor_aposta=int(input('\n\nO valor Inserido Não pode ser maior que o Saldo que você Possui (se deseja inserir mais fichas para apostar basta digitar [0])\n Insira o valor de sua aposta :'))
            if valor_aposta == 0:
                inserir_fichas_Durante_Jogo()
                valor_aposta=int(input('\n\nInsira o valor da sua aposta :'))
            Checar_valor(valor_aposta, saldo)

        debitar_fichas(valor_aposta)

        #inicio do jogo
        sorteio_n_animal=randint(1,25)
        print('...')
        sleep(2)
        print('Por favor Aguarde enquanto calculamos o resultado do jogo ')
        sleep(3)
        print('...')
        sleep(2)
        print(f'\n\n    RESULTADO ------>    {sorteio_n_animal}    <----------')

        #calcular e mostrar resultado
        if sorteio_n_animal==escolha_n_animal_usr:
            print(f'PARABÉNS VOCÊ VENCEU !! O animal da vez foi {lista[sorteio_n_animal-1]}')
            venceu=True
        else :
            print(f'IIIH deu ZEBRA!! O animal da vez foi {lista[sorteio_n_animal-1]}')
            venceu=False

        #mostrar o valor ganho ou perdido na aposta
        if venceu is True:
            creditar_fichas(valor_aposta, 25)
            print(f'seu saldo foi atualizado!! Saldo : {saldo} Você ganhou com essa aposta {valor_aposta*25} Fichas .')
        if venceu is False:
            print(f'seu saldo foi atualizado!! Saldo : {saldo} Você perdeu com essa aposta {valor_aposta} Fichas.')

        #opção sair ou permanecer jogando
        check=input(' Se deseja CONTINUAR JOGANDO tecle: [C]\n Se deseja VOLTAR AO MENU tecle: [V] : ').upper()
    if check == 'V':
        print('\n\nObrigado por visitar o Jogo do Bicho, sinta-se a vontade para retornar uma outra hora =)\n\n')
        sleep(3)
        print('Vamos te redirecionar para o Menu ...\n\n')
        sleep(3)
        print('...\n\n')
        sleep(2)
        menu()

def Jogo_P_P_T ():
    #print('1 - Pedra. 2 - Papel 3 - Tesoura'

    print('------Pedra, Papel e Tesoura--------')
    print(' ') #a única finção desses espaços aleatórios é estetica
    print('---Regra do Jogo---\nNesse jogo você deve escolher entre:\nPedra, Papel e Tesoura e seu adversário (o computador) também escolherá.\nPedra perde para papel (o papel embrulha a pedra); papel perde para tesoura (esta corta o papel);\ne, finalmente, a tesoura perde para a pedra, que quebra a tesoura. ')
    print(' ')
    print('---Regra da Aposta---\nSe ganhar, você receberá o triplo do que foi apostado.\nSe der empate, seus créditos serão devolvidos.\nSe você perder, o valor apostado será perdido.')
    print(' ')
    aposta = int(input('Deposite sua aposta: '))
    while not Checar_valor(aposta, saldo) :
            aposta=int(input('\O valor Inserido Não pode ser maior que o Saldo que você Possui (se deseja inserir mais fichas para apostar basta digitar [0])\nInsira o valor de sua aposta :'))
            if aposta == 0:
                inserir_fichas_Durante_Jogo()
                aposta=int(input('Insira o valor da sua aposta : '))
            Checar_valor(aposta, saldo)

    debitar_fichas(aposta)
    print(' ')
    print('1 - Pedra.\n2 - Papel\n3 - Tesoura')


    jogador = int(input('Escolha um número: 1 para Pedra, 2 para Papel ou 3 para Tesoura : '))
    while jogador > 3 or jogador < 1:
        jogador = int(input('Número inválido. Digite novamente : '))
    print(' ')
    if jogador == 1:
        print('Você escolheu Pedra.')
    elif jogador == 2:
        print('Você escolheu Papel.')
    elif jogador == 3:
        print('Você escolheu Tesoura.')
    

    print(' ')

    computador = randint(1,3)
    if computador == 1:
        print('O computador escolheu Pedra.')
    elif computador == 2:
        print('O computador escolheu Papel.')
    elif computador == 3:
        print('O computador escolheu Tesoura.')

    print(' ')

    if (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print('Parabéns!!! Você ganhou!')
        creditar_fichas(aposta, 3)
        aposta = aposta * 3
        print(f'Sua aposta triplicou! Lucro da aposta : {aposta}. Saldo atual : {saldo}')

    elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 3) or (jogador == 3 and computador == 1):
        print('Que Pena. Você perdeu!')
        print(f'Você perdeu sua aposta : {aposta}. Saldo Atual : {saldo}')
        #os creditos apostados foram perdidos. não sei como fazer isso

    elif jogador == computador:
        creditar_fichas(aposta, 0)
        print('Deu empate.')
        print(f'Sua aposta {aposta} foi devolvida. Saldo Atual : {saldo} ')
        #os creditos apostados voltam. nem me pergunte como fazer isso
        

    resposta = str(input('Deseja jogar novamente? Digite [S]im ou [N]ão : ')).upper()
    if resposta == 'S':
        Jogo_P_P_T()
    elif resposta == 'N':
        print('\nObrigado por visitar o Jogo Pedra, Papel, Tesoura> Sinta-se a vontade para retornar uma outra hora =)\n\n')
        sleep(3)
        print('\nVamos te redirecionar para o Menu ...')
        sleep(3)
        print('\n...')
        sleep(2)
        menu()
    #isso é pra ver se o jogador quer jogar novamente ou voltar para o menu.

def Jogo_Impar_x_Par ():

    print('Par ou Ímpar')
    print(' ')
    print('Regras do Jogo')
    print(' ')
    print('O jogador diz "par" ou "impar", e o computador também.\nDepois cada um dos jogadores dizem 1 ou 2.\nSomam-se o número colocados pelos dois jogadores.\nSe a soma é um número par, ganha quem disse "par".\nSe a soma é um número impar, ganha quem disse "impar".')
    print(' ')
    print('Regras da Aposta')
    print(' ')
    print('Se ganhar, você receberá o dobro do que foi apostado.\nSe você perder, o valor apostado será perdido.')
    print(' ')
    aposta=int(input('Qual valor da sua aposta : '))
    while not Checar_valor(aposta, saldo) :
            aposta=int(input('O valor Inserido Não pode ser maior que o Saldo que você Possui (se deseja inserir mais fichas para apostar basta digitar [0])\nInsira o valor de sua aposta :'))
            if aposta == 0:
                inserir_fichas_Durante_Jogo()
                aposta=int(input('Insira o valor da sua aposta : '))
            Checar_valor(aposta, saldo)

    debitar_fichas(aposta)

    print(' ')
    escolha=str(input('Faça a sua escolha [P]ar  ou [I]mpar : ')).upper()
    print(' ')
    numero=int(input('Digite um número : '))
    print(' ')
    comp=randint (1,2)
    soma = comp + numero

    print(f'Você escolheu o número {numero}.')
    print(f'O computador escolheu o número {comp}.')
    print(' ')
    if (escolha == 'P' and soma % 2 == 0) or (escolha == 'I' and soma % 2 == 1):
        creditar_fichas(aposta, 2)
        print('Você ganhou!')
        aposta = aposta*2
        print(f'Sua aposta dobrou! Lucro da aposta : {aposta}. Saldo atual : {saldo}')
    else:
        print('Você perdeu!')
        print(f'Você perdeu sua aposta. Saldo atual : {saldo}')

    resposta = str(input('Deseja jogar novamente? Digite [S]im ou [N]ão : ')).upper()
    if resposta == 'S':
        Jogo_Impar_x_Par()
            #joga novamente
    elif resposta == 'N':
        print('\nObrigado por visitar o Jogo Impar_x_Par, sinta-se a vontade para retornar uma outra hora =)\n\n')
        sleep(3)
        print('\nVamos te redirecionar para o Menu ...')
        sleep(3)
        print('\n...')
        sleep(2)
        menu()
            #volta pro menu

def Jogo_Dado ():
    print('---Jogo do Dado---')
    print(' ')
    print('Regra do Jogo')
    print(' ')
    print('Você escolherá um número de 1 a 6. O computador irá jogar os dados.\nSe a face do dado que saiu for o mesmo número que você escolheu, você ganhará.')
    print(' ')
    print('Regra da Aposta')
    print(' ')
    print('Se você ganhar o jogo, sua aposta irá elencar 6 vezes.\nSe você perder o jogo, você perderá sua aposta.')
    print(' ')

    aposta = int(input('Deposite sua aposta: '))
    while not Checar_valor(aposta, saldo) :
            aposta=int(input('O valor Inserido Não pode ser maior que o Saldo que você Possui (se deseja inserir mais fichas para apostar basta digitar [0])\nInsira o valor de sua aposta :'))
            if aposta == 0:
                inserir_fichas_Durante_Jogo()
                aposta=int(input('Insira o valor da sua aposta : '))
            Checar_valor(aposta, saldo)
    debitar_fichas(aposta)
    print(' ')
    escolha = int(input('Escolha um número de 1 a 6: '))
    while escolha > 6 or escolha < 1:
        escolha = int(input('Número inválido. Digite novamente: '))
    computador = randint(1,6)
    print(' ')
    print(f'Você escolheu o número {escolha}')
    print(' ')
    print(f'O dado foi lançado...\n A face que apareceu foi {computador}')
    print(' ')
    if escolha == computador:
        creditar_fichas(aposta, 6)
        aposta = aposta * 6
        print('Parabéns!!! Você ganhou!')
        print(f'lucro da aposta : {aposta}. Saldo Atual : {saldo}')
    else:
        print('Que pena, você perdeu! Mais sorte na próxima.')
        print('Você perdeu o valor da sua aposta.')

    resposta = str(input('Deseja jogar novamente? Digite [S]im ou [N]ão: ')).upper()
    if resposta == 'S':
        Jogo_Dado()
        #joga novamente
    elif resposta == 'N':
        print('\nObrigado por visitar o Jogo do DADO, sinta-se a vontade para retornar uma outra hora =)\n\n')
        sleep(3)
        print('\nVamos te redirecionar para o Menu ...')
        sleep(3)
        print('\n...')
        sleep(2)
        menu()
        #volta pro menu

menu()

    
    


   