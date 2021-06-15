import os

def gravaApostadores(apostadores):
    arquivoapostadores = open("apostadores.txt",'w')
    for a in apostadores:
        arquivoapostadores.write("%s\n" %a)
    arquivoapostadores.close()




def recuperaApostadores():
    apostadores = []
    if(os.path.exists("apostadores.txt")):
        arquivoapostadores = open("apostadores.txt",'r')
        for linha in arquivoapostadores:
            apostador = linha.strip().split(";")
            apostadores.append(apostador[0])
        arquivoapostadores.close()
    return apostadores



def gravaJogos(jogos):
    arquivojogos = open("jogos.txt",'w')
    for a in jogos:
        arquivojogos.write("%s;%s;%s;%s\n" %(a[0],a[1],a[2],a[3]))
    arquivojogos.close()



def recuperaJogos():
    jogos = []
    if(os.path.exists("jogos.txt")):
        arquivojogos = open("jogos.txt",'r')
        for linha in arquivojogos:
            jogo = linha.strip().split(";")
            jogos.append(jogo)
        arquivojogos.close()
    return jogos



def gravaTimes(times):
    arquivotimes = open("times.txt",'w')
    for a in times:
        arquivotimes.write("%s\n" %a)
    arquivotimes.close()



def recuperaTimes():
    times = []
    if(os.path.exists("times.txt")):
        arquivotimes = open("times.txt",'r')
        for linha in arquivotimes:
            time = linha.strip().split(";")
            times.append(time[0])
        arquivotimes.close()
    return times



def gravaApostas(apostas):
    arquivoapostas = open("apostas.txt",'w')
    for a in apostas:
        arquivoapostas.write("%s;%s;%s;%s;%s\n" %(a[0],a[1],a[2],a[3],a[4]))
    arquivoapostas.close()



def recuperaApostas():
    apostas = []
    if(os.path.exists("apostas.txt")):
        arquivoapostas = open("apostas.txt",'r')
        for linha in arquivoapostas:
            aposta = linha.strip().split(";")
            apostas.append(aposta)
        arquivoapostas.close()
    return apostas
