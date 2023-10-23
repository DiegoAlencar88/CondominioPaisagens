#VARIAVEIS 

import pyautogui
import time
##BIBLIOTECA INFO

linha_atual = 0


for _ in range(15):

    time.sleep(3)
    pyautogui.PAUSE = 2
    #ABRIR ABA
    pyautogui.click(x=234, y=488)
    #CLICAR ABA
    pyautogui.click(x=213, y=603)

    #SELEÇÂO QNTS X

    pyautogui.click(x=458, y=300)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    #QUANTAS UNIDADES

    pyautogui.click(x=454, y=359)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    #CONTA CONTABIL


    pyautogui.click(x=467, y=344)
    pyautogui.write("1.9 ")
    pyautogui.press("tab")
    pyautogui.click(x=484, y=412)

    #CRIAR O VINCULO COM A PLANILHA
    import pandas as pd

    tabela = pd.read_csv("paisagensok.csv", sep=";")


    for linha in tabela.index:

        Consumo = tabela.loc[linha_atual, "Consumo"]

    pyautogui.write(str(Consumo))

    ####AQUI CODIGO PARA PUCHAR
    pyautogui.write(" m³ (agosto a setembro)")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")



    #PAGINA VALOR E UNIDADE


    ####CRIAR LINHA VALOR PLANILHA

    tabela = pd.read_csv("paisagensok.csv", sep=";")

    for linha in tabela.index:

        Pagar = tabela.loc[linha_atual, "Pagar"]
    pyautogui.write(str(Pagar))

    pyautogui.press("tab")

    ##CRIAR LINHA PARA UNIDADE E BLOCO (COLOCAR COMANDO PARA ESPAÇO)

    tabela = pd.read_csv("paisagensok.csv", sep=";")

    for linha in tabela.index:

        Unidade = tabela.loc[linha_atual, "Unidade"]
    pyautogui.write(str(Unidade))

    pyautogui.press("space")

    tabela = pd.read_csv("paisagensok.csv", sep=";")

    for linha in tabela.index:

        Bloco = tabela.loc[linha_atual, "Bloco"]
    pyautogui.write(str(Bloco))
    #comando para clicar na unidade



    pyautogui.click(x=487, y=427)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    linha_atual += 1

