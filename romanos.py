#!/usr/bin/env python
# -*- coding: latin1 -*-

# script para conversão de algarismos indo-arábicos em algarismos romanos
# por Matheus Boy

# “Smart data structures and dumb code works a lot better than the other
# way around.”
# —Eric Raymond, The Cathedral and the Bazaar, chapter 5


import os

def romanos(num):
    """
    Função principal do script, tem como entrada um inteiro e como retorno
    uma string.
    
    A entrada consiste em um número inteiro e a saída em uma string com a
    representação desse número em algarismos romanos.    
    
    """

    rom = ""
    # essa lista gigante quebra um galho danado
    # <pog> dicionário é o caralho </pog>
    div = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"],
           [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"],
           [4, "IV"], [1, "I"]]
           
    # ainda estou pensando num jeito de representar os números maiores que 3999       
    if num > 3999:
        print "Número maior que 3999, representação impossível"
    elif num < 0:
        print "Número negativo"
    elif num == 0:
        print "Não há representação romana para o zero"
    else:
        # algoritmo esperto
        for d in div:
            a = num / d[0]
            i = 0
            while (i < a):
                rom += d[1]
                i += 1
            num -= a * d[0]
    return rom


def info():
    """
    
    Função básica que imprime na tela as opções do script.
    
    """
    print "Digite \"n\" para entrar com um único número"
    print "Digite \"l\" para entrar com uma lista de números"
    print "Digite \"d\" para demonstração"
    print "Digite \"i\" para exibir esta mensagem"
    print "Digite \"q\" para encerrar a execução"


def scan():
    """
    
    Função de entrada de dados e manipulação dos mesmos.
    
    """
    msg = "Comando inválido. Digite \"i\" para obter a lista de comandos..."
    comandos = ["n", "l", "d", "i", "q"]
    op = ""
    l = []
    demo = [3499, 1234, 999, 1992, 13, 528, 256, 64]
    # loop do processamento e entrada de dados
    while (op!="q"):
        try:            
            # loop de entrada dos comandos
            op = str(raw_input())
            while (op not in comandos):
                print msg
                op = str(raw_input())
            if op == "n":
                print "Entre com um número"
                n = int(raw_input())
                print romanos(n)
            elif op == "l":
                print "Entre com uma lista de números, para finalizar a entrada, digite 0 (zero):"
                n = int(raw_input())
                while (n != 0):
                    l.append(n)
                    n = int(raw_input())
                for x in l:
                    print romanos(x)
            elif op == "i":
                info()
            elif op == "d":
                for x in demo:
                    print str(x) + " -> " + romanos(x)
            elif op == "q":
                os.system("clear")
                raise SystemExit
        # SystemExit é uma forma "bonita" - a.k.a. menos feia - 
        # de se encerrar a execução do script
        except EOFError:
            os.system("clear")
            raise SystemExit
        except KeyboardInterrupt:
            os.system("clear")
            raise SystemExit
            
os.system("clear")
print "_\|/_ ===== Conversor de algarismos romanos ===== _\|/_\n"
info()
scan()
