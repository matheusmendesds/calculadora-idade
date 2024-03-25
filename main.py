from tkinter import *
from tkinter import ttk

#importando Tkcalendar
from tkcalendar import Calendar, DateEntry

#importando dateutil
from dateutil.relativedelta import relativedelta

#importando datetime
from datetime import date

#cores

cor1='#3b3b3b' #preto clareado
cor2='#333333' #preto mais escuro
cor3='#ffffff' #branca
cor4='#fcc058' #laranja

#criando janela do app

janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

janela.configure(bg=cor1)

#criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0,relief=FLAT, bg=cor2)
frame_cima.grid(row=0,column=0)
frame_baixo= Frame(janela, width=310,height=300, pady=0, padx=0,relief=FLAT,bg=cor1)
frame_baixo.grid(row=1,column=0)

#criando labels
label_title = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat',anchor='center', font='Ivy 15 bold', bg=cor2, fg=cor3)
label_title.place(x=0,y=30)

label_subtitle= Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0,relief='flat', anchor='center', font='Arial 35 bold',bg=cor2, fg=cor4 )
label_subtitle.place(x=0,y=60)

#Função para calcular idade

def calcular():
    inicial=cal_data_inicial.get()
    final=cal_data_nasc.get()

    

    #separando valores

    dia_atual,mes_atual,ano_atual = [ int(f) for f in inicial.split('/')]
    data_atual= date(ano_atual, mes_atual, dia_atual)

    dia_nasc,mes_nasc,ano_nasc = [ int(f) for f in final.split('/')]
    data_nasc= date(ano_nasc, mes_nasc, dia_nasc)
    
    anos = relativedelta(data_atual, data_nasc).years
    meses = relativedelta(data_atual, data_nasc).months
    dias = relativedelta(data_atual, data_nasc).days

    label_anos['text'] = anos
    label_mes['text'] = meses
    label_dia['text'] = dias

    
#Criando labels para frame

label_data_inicial = Label(frame_baixo, text="Data Atual", height=1, padx=0, pady=0,relief='flat', anchor=NW, font=('Ivy 11'), bg=cor1, fg=cor3)
label_data_inicial.place(x=50,y=30)

cal_data_inicial = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2024)
cal_data_inicial.place(x=190, y=30)

label_data_nascimento = Label(frame_baixo, text="Data de Nascimento", height=1, padx=0, pady=0,relief='flat', anchor=NW, font=('Ivi 11'), bg=cor1, fg=cor3)
label_data_nascimento.place(x=50,y=60)

cal_data_nasc = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2024)
cal_data_nasc.place(x=190, y=60)

#Label Idade usuario
label_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_anos.place(x=60, y=135)
label_anos_text = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_anos_text.place(x=60, y=175)

label_mes = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_mes.place(x=150, y=135)
label_mes_text = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_mes_text.place(x=150, y=175)

label_dia = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_dia.place(x=240, y=135)
label_dia_text = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 20 bold'), bg=cor1, fg=cor3)
label_dia_text.place(x=240, y=175)


# Criando botão para calcular

btn_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief="raised", overrelief='ridge', font=('Ivi 10 bold'), bg=cor1, fg=cor3)
btn_calcular.place(x=70, y=225)
janela.mainloop()