#================================================================================================================================== +
  #By Samuel Pierre/Clayton Sobral 																									+
  #Version: 0.1																														+
  #Beta Test																														+
  #08-06-2022 15:05																													+	
  #README - Este aplicativo foi desenvolvido com o intuito de melhorar a coleta dos processamentos diarios do sistema (dategen)#    +
#==================================================================================================================================	+

import time
import os
import datetime
import tkinter
import random
import pyautogui as pag 
from datetime import date
from tkinter import *
from tkinter import messagebox	
from ast import With
#=================================================================================#
#                                       FIDIS									  #
#=================================================================================#

date = datetime.datetime.now()
date_s = str(date)[:-10]
date_b = str(date)[:-16]
actual_date = date.today()
date_in_text = actual_date.strftime('%d-%m-%Y')

way = f"//10.91.134.114/Clientes/FIDIS/Entrada/{date_in_text}"
way_logs = "C://Users/samuel.pierre/Desktop/notepad++/Projeto_GD_brd/Projeto_GD"

archive_list = os.listdir(way)

quantity = len(archive_list)

file_logs = os.listdir(way_logs)
mkdir = False	
	
for print_list in range(quantity):
	print(archive_list[print_list])


for n2 in file_logs:
	if ("Logs" in file_logs):
		print('este diretorio Ja existe')
	else:
		mkdir = True
			
def received_files():
	print("Arquivos FIDIS recebidos com sucesso")
	n = 0
	while(n < quantity):
		# print(archive_list[n])
		# print(f"{archive_list[n]} foi recebido em {date_s}")
		with open(f"Log-recebido-em-{date_b}.txt", 'a') as arquivo_acrescentar:
			arquivo_acrescentar.write(f"{archive_list[n]} Foi recebido em {date_s} \n")
		n = n + 1
		
def no_received_files():
	print(f"Atenção são as {date.hour} e ainda não recebemos nenhum arquivo do cliente")

if(quantity == 0):
	no_received_files()
else:
	received_files()

#=================================================================================#
#                                       SOFISA									  #
#=================================================================================#

date = datetime.datetime.now()
date_s = str(date)[:-10]
date_b = str(date)[:-16]
actual_date = date.today()
date_in_text = actual_date.strftime('%d-%m-%Y')

way = f"//10.91.134.114/Clientes/Sofisa/Entrada/{date_in_text}"
way_logs = "C://Users/samuel.pierre/Desktop/notepad++/Projeto_GD_brd/Projeto_GD"

archive_list = os.listdir(way)

quantity = len(archive_list)

file_logs = os.listdir(way_logs)
mkdir = False
for print_list in range(quantity):
	print(archive_list[print_list])
for n2 in file_logs:
    if ("Logs" in file_logs):
        print('este diretorio Ja existe')
    else:
        mkdir = True
		
def received_files():
    print("Arquivos SOFISA recebidos com sucesso")
    n = 0
    while(n < quantity):
        # print(archive_list[n])
        # print(f"{archive_list[n]} foi recebido em {date_s}")
        with open(f"Log-recebido-em-{date_b}.txt", 'a') as arquivo_acrescentar:
            arquivo_acrescentar.write(f"{archive_list[n]} Foi recebido em {date_s} \n")
        n = n + 1
		
def no_received_files():
    print(f"Atenção são as {date.hour} e ainda não recebemos nenhum arquivo do cliente")
	
if(quantity == 0):
    no_received_files()
else:
    received_files()
	
time.sleep(1)
pag.alert(text=f'Verificação efetuada com sucesso!',title='ATENÇÃO',button='ok')
