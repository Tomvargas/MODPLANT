import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import time
import serial
import threading
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
import pymysql

def arduino():
	
	Registro = {}
	Registro2 = []

	arduino = serial.Serial(port='COM12', baudrate=int(9600), timeout=2)
	C = 1
	inicio = False
	while not (inicio or C > 7):
	    line = arduino.readline()  # EN ESTA PARTE SE LEE TODA LA INFORMACION QUE NOS TRASNMITE LA PLACA ARDUINO MEGA
	    conversion = str(line.decode('ascii', errors='replace'))

	    conversion2 = str(line)

	    Registro[C] = conversion
	    Registro2.append(conversion)

	    C = C + 1

	posicion = 0
	while posicion < len(Registro2):
	    if Registro2[posicion] == "":
	        Registro2.pop(posicion)
	    else:
	        posicion = posicion + 1

	Registro2 = [x.replace("\r\n", "") for x in Registro2]
	arduino.close()
	return Registro2
	

def dato():
        try:
                Registrodata=arduino()
        except:
                Registrodata=["5.7", "27", "38", "15", "10"]
                messagebox.showerror("Error!!","La coneccion con arduino ha fallado\nVerifique si el módulo está conectado.\nSe mostraran datos de ejemplo...")
        return Registrodata
	

def about_us():
    ven=Toplevel()
    ven.title("About us")
    ven.resizable(False, False)
    ven.iconbitmap(r'images/descarga_gMJ_icon.ico')
    tex="Este programa sirve para poder monitorear parámetros\nclimaticos por medio de graficos y tablas decomparación\n"
    Label(ven, text="").pack()
    l1=Label(ven, text=tex, height=0, width=50)
    l1.pack()
    #ttk.Button(ven, text="Cerrar",command=exit).pack()
    Button(ven, text="Close", command=ven.destroy).pack()
    Label(ven,text="").pack()

def presentarIntegrantes():
    ven=Toplevel()
    ven.title("Developers")
    ven.resizable(False, False)
    ven.iconbitmap(r'images/descarga_gMJ_icon.ico')
    tex="\n TOMÁS VARGAS DROUET\n ARTURO NEGREIROS SAMANEZ \n"
    l1=Label(ven, text=tex, height=0, width=50)
    l1.pack()
    Button(ven, text="Close", command=ven.destroy).pack()
    Label(ven,text="").pack()


def datos_tr():
    live = Toplevel()
    #root.get_themes()     #-------------Returns a list of all themes that can be set
    #root.set_theme("plastik")   #----------------------------Sets an available theme

    #----------------DIMENSION Y WIDGETS DE LA VENTANA------------------------------
    #===============================================================================
    live.geometry("800x500")
    live.title("DATOS EN TIEMPO REAL")
    live.iconbitmap(r'images/descarga_gMJ_icon.ico')
    bg_image1=PhotoImage(file="images/BG.png")
    Label(live, image=bg_image1).place(x=0, y=0, relwidth=1, relheight=1)
    live.resizable(False, False)#-----------------Bloquear redimencion de la ventana

    #-------------------------------BARRA DE MENU-----------------------------------
    #===============================================================================
    menubar = Menu(live)
    live.config(menu=menubar)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Exit", command=live.destroy)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us", command=about_us)
    subMenu.add_command(label="Desarrolladores", command=presentarIntegrantes)
    Registrodata=dato()

    Txx="HORA DE OBTENCIÓN "+time.strftime("%H:%M")
    text = Label(live, font =('arial', 12, 'bold'),fg='white' ,text=Txx, bg="#6fd54d")#color del header bg="#2ca3d7"
    text.pack(ipady=20)
    #Registrodata.pop(0)
    print(Registrodata)
    
    Registro=[Registrodata[0],Registrodata[1],Registrodata[2],Registrodata[3],Registrodata[4]]#---------------------------( 0-PH  1-LLUVIA  2-NIVEL_LLUVIA )
    
    print(Registro)


    #crear graficos de cada sensor
    Registro=np.array(Registro)

    def ph():
        fig, ax = pyplot.subplots()

        size = 0.3

        cmap = pyplot.get_cmap("tab20c")
        outer_colors = cmap(np.arange(6)*4)

        ax.pie(Registro[0].flatten(), radius=0.8, colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'))

        ax.set(aspect="equal", title='DATOS DE PH')
        pyplot.savefig('images/temp/dataPH.png', transparent=True,dpi=50, quality=100)

    def salData():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ('#a12ef2', '#e2e00b', '#70f528' ,'#23cdeb', '#a42ff5', '#e03232')#-------------------------cambiarrrrr
        #inner_colors = ('#6eeb67', '#e0df54', '#9eee72' ,'#71d2e3', '#c27cf2', '#df7070')

        ax.pie(Registro[2].flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='white'))

        #ax.pie(valtemp.sum()/len(valtemp), radius=1-size, colors=inner_colors,
        #       wedgeprops=dict(width=size, edgecolor='white'))

        ax.set(aspect="equal", title='SALINIDAD')
        pyplot.savefig('images/temp/datasal.png', transparent=True,dpi=50, quality=100)#---------------------------------------------------
    
    def nivel():#BARRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        '''fig, ax = pyplot.subplots()

        size = 0.3
        outer_colors = ('#f2662a', '#e2e00b', '#70f528' ,'#23cdeb', '#a42ff5', '#e03232')

        ax.pie(Registro[4], radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        ax.set(aspect="equal", title='NIVEL DE AGUA')
        pyplot.savefig('images/temp/dataNIV.png', transparent=True,dpi=50, quality=100)'''
        fig, ax1 = pyplot.subplots()        

        bins = ['agua','','']
        ax1.bar(bins, Registro[4],color='#f2662a')
        ax1.set_title('NIVEL DEL AGUA')

        pyplot.savefig('images/temp/dataNIV.png', transparent=True, dpi=46, quality=100)

    def temperatura():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ('#e2e00b', '#70f528' ,'#23cdeb', '#a42ff5','#f2662a', '#e03232')

        ax.pie(Registro[1], radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        ax.set(aspect="equal", title='TEMPERATURA')
        pyplot.savefig('images/temp/dataTEMP.png', transparent=True,dpi=50, quality=100)

    def humedad():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ( '#70f528' ,'#23cdeb','#e2e00b', '#a42ff5','#f2662a', '#e03232')

        ax.pie(Registro[3], radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        ax.set(aspect="equal", title='HUMEDAD')
        pyplot.savefig('images/temp/dataHUM.png', transparent=True,dpi=50, quality=100)

    ph()
    nivel()
    salData()
    temperatura()
    humedad()

    

    #------------------------------------------------ PH

    PHIMAGE=PhotoImage(file='images/temp/dataPH.png')
    Label(live,image=PHIMAGE).place(x=0 ,y=70+10)
    TX1=str(Registro[0])
    Label(live, text=TX1, font=(18)).place(x=310 ,y=107)


    TEMPIMAGE=PhotoImage(file='images/temp/dataTEMP.png')
    Label(live,image=TEMPIMAGE).place(x=250+250 ,y=70+10)
    TX3=str(int(Registro[2]))+' °C'
    Label(live, text=TX3, font=(18)).place(x=480,y=107)

    
    HUMIMAGE=PhotoImage(file='images/temp/dataHUM.png')
    Label(live,image=HUMIMAGE).place(x=350-100 ,y=270)
    TX4=str(int(Registro[3]))+' %'
    Label(live, text=TX4, font=(18)).place(x=315+80 ,y= 200)

    NIVIMAGE=PhotoImage(file='images/temp/dataNIV.png')
    Label(live,image=NIVIMAGE).place(x=10 ,y=265)
    TX2=str(int(Registro[4]))+' Cm.'
    Label(live, text=TX2, font=(18)).place(x=310,y=147)



    SALIMAGES=PhotoImage(file='images/temp/datasal.png')
    Label(live,image=SALIMAGES).place(x=250+250 ,y=270)
    TXS=str(int(Registro[1]))+' %'
    Label(live, text=TXS, font=(18)).place(x=480,y=107+40)

        

    ppp=PhotoImage(file="images/trdataa.png") 
    Label(live, image=ppp).place(x=300+60, y=100)

    ttk.Button(live, text='cerrar', command=live.destroy).place()


    live.mainloop()
