import GravadorDeAposta


def opcoescadastro():
    print("MENU \n")
    print("Escolha uma Opção: \n")
    print("1. Cadastrar time")
    print("2. Cadastrar Jogo")
    print("3. Cadastrar apostador")
    print("4. Cadastrar aposta de apostador")
    print("5. Obter valor de uma aposta")
    print("6. Obter o valor a ser pago por um certo apostador")
    print("7. Obter o valor que um certo apostador irá ganhar")
    print("8. Obter o placar de um jogo")
    print("9. Listar times cadastrados")
    print("10. Listar todos os jogos cadastrados")
    print("11. Listar todos os apostadores")
    print("12. Listar todas as apostas de um apostador")
    print("13. Sair \n")


def cadastrartime(times):
    print("CADASTRO NOVO TIME")
    timeNovo = str.upper(input("Digite um time: \n"))
    times.append(timeNovo)
    print(times)


def cadastrarjogo(jogos):
    print("CADASTRO JOGO")
    time1 = str.upper(input("Digite nome do primeiro time: \n"))
    gols1 = int(input("Digite a quantidade de gols do primeiro time: \n"))
    time2 = str.upper(input("Digite nome do segundo time: \n"))
    gols2 = int(input("Digite a quantidade de gols do segundo time: \n"))
    jogos.append([time1, gols1, time2, gols2])


def cadastroapostador(apostadores):
    print("CADASTRO APOSTADOR")
    nome = str.upper(input("Digite o nome do apostador: \n"))
    apostadores.append(nome)


def cadrastaraposta(apostas):
    print("CADASTRAR APOSTA")
    nome = str.upper(input("Digite o seu nome: \n"))
    time1 = str.upper(input("Digite nome do primeiro time: \n"))
    gols1 = int(input("Digite a quantidade de gols do primeiro time: \n"))
    time2 = str.upper(input("Digite nome do segundo time: \n"))
    gols2 = int(input("Digite a quantidade de gols do segundo time: \n"))
    apostas.append([nome, time1, gols1, time2, gols2])


def valordaaposta(valoraposta):
    print("OBTER VALOR DA APOSTA")
    print("O valor da aposta é R$ %.2f" %valoraposta)
    

def valoraserpago(apostas):
    print("OBTER VALOR A SER PAGO")
    nome = str.upper(input("Digite o nome de uma apostador: \n"))
    cont = 0
    for s in apostas:
        if(s[0] == nome):
            cont+=1
    v = (cont * valoraposta)
    print("O Valor a ser pago é: R$ %.2f" %v)




def calculaValorAGanhar(apostadores, apostas, valoraposta, jogos):
    pontos = []
    nome = str.upper(input("Digite o nome do apostador: \n"))
    for k in range(len(apostadores)):
        pontos.append(0)
        for s in apostas:
            if(s[0] == nome):
                for n in jogos:
                    if(n[0] == s[1] and n[2] == s[3]):
                        if(n[1] == s[2] and n[3] == s[4]):
                            pontos[k]+=5
                            print(pontos)


def placarjogos(jogos):
    print("OBTER O PLACAR DE UM JOGO")
    time1 = str.upper(input("Digite o nome do time 1: \n"))
    time2 = str.upper(input("Digite o nome do time 2: \n"))
    for s in jogos:
        if(time1 == s[0] and time2 == s[2]):
            print("O placar do jogo foi: \n",s[0] ,s[1], "x" ,s[2] ,s[3])


def timescadrastados(times):
    print("TIMES CADASTRADOS")
    print(times)


def jogoscadrastados(jogos):
    print("TODOS OS JOGOS CADASTRADOS")
    for s in jogos:
        print(s[0], "x" ,s[2])


def todosapostadores(apostadores):
    print("TODOS OS APOSTADORES")
    print(apostadores)


def listarapostas(apostas):
    print("LISTAR TODAS AS APOSTAS DE UM APOSTADOR")
    nomeDoApostador = str.upper(input("Digite o nome de um apostador: \n"))
    for s in apostas:
        if(s[0] == nomeDoApostador):
            print(s[1] ,s[2], "x" ,s[3] ,s[4])

valoraposta = 2.00
times = GravadorDeAposta.recuperaTimes()
jogos = GravadorDeAposta.recuperaJogos()
apostadores = GravadorDeAposta.recuperaApostadores()
apostas = GravadorDeAposta.recuperaApostas()
sair = False
while(sair == False):
         opcoescadastro() 
         opcao = int(input())
         if(opcao == 1):
             cadastrartime(times)
         elif(opcao == 2):
             cadastrarjogo(jogos)
         elif(opcao == 3):
             cadastroapostador(apostadores)
         elif(opcao == 4):
             cadastraraposta(apostas)
         elif(opcao == 5):
             valordaaposta(valoraposta)
         elif(opcao == 6):
             valoraserpago(apostas)
         elif(opcao == 7):
             calculaValorAGanhar(apostadores, apostas, jogos, valoraposta)
         elif(opcao == 8):
             placarjogos(jogos)
         elif(opcao == 9):
             timescadrastados(times)
         elif(opcao == 10):
             jogoscadrastados(jogos)
         elif(opcao == 11):
             todosapostadores(apostadores)
         elif(opcao == 12):
             listarapostas(apostas)
         elif(opcao == 13):
             sair = True
             GravadorDeAposta.gravaTimes(times)
             GravadorDeAposta.gravaJogos(jogos)
             GravadorDeAposta.gravaApostadores(apostadores)
             GravadorDeAposta.gravaApostas(apostas)
             print("ADEUS")
        
             
