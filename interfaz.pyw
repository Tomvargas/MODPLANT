import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import time
import serial
import threading
import tkinter.messagebox
from tkinter import *
import tkinter as ttk
from ttkthemes import themed_tk as tk
import pymysql
import time



'''Registro2=['21.34', '21.34', '21.34', '21.34', '21.34', '21.34', '21.34','91', '91', '92', '91', '91', '93', '93','22', '22', '22', '22', '22', '22','65', '65', '65', '65', '65', '65','1533', '1532', '1532', '1531', '1532', '1532','1023', '1023', '1023', '1023', '1023', '1023']
DATA=Registro2'''

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

def Present_Grafic():

    #===================================================================================
    ############################### nombres de listas ################################
    #===================================================================================
    
    phdata=[5.4,6.7,5.5,6.6,7.4,8.9]

    listasal=[30,60,50,30,20,80]

    listatemp=(20, 13, 18, 21, 21, 22)

    listah=(34, 23,55, 66, 34, 78)

    nldata=[10,9,8,10,13,15]

    lldata=[1,1,1,0,1,1]
    

    #----------------------------------------------------------------------------------------------------------

    listaph=np.array(phdata)
    sumph = 0
    for t in listaph:
        sumph = sumph + float(t)

    phdata_prom=sumph/len(listaph)
    #phdata_prom="{0:.2f}".format(promPH1)
    #---------------------------------------------------------

    sali=np.array(listasal)#--------------salinidad
    sumsal = 0
    for t in sali:
        sumsal = sumsal + float(t)

    listasal_prom=sumsal/len(sali)
    #listasal_prom="{0:.2f}".format(promsal)

    #---------------------------------------------------------

    valtemp=np.array(listatemp)
    sumt = 0
    for t in listatemp:
            sumt = sumt + float(t)

    listatemp_prom=sumt/len(valtemp)
    #listatemp_prom="{0:.2f}".format(promtemp)

    #---------------------------------------------------------
    valh=np.array(listah)
    sumh = 0
    for t in valh:
        sumh = sumh + float(t)

    listah_prom=sumh/len(valh)
    #listah_prom="{0:.2f}".format(promh)
    #---------------------------------------------------------

    vall=np.array(lldata) #--- luvia

    #---------------------------------------------------------
    valln=np.array(nldata)
    sumln = 0
    for t in valln:
        sumln = sumln + float(t)
    nldata_prom=sumln/len(valln)
    #nldata_prom="{0:.2f}".format(promlln)

    #---------------------------------------------------------


    #listaNIV=np.array(listaNIV)

    #================================================================================
    # /*------------------------CREACION DE LA VENTANA GRAFICOS-------------------/*
    #===============================================================================
    root = Toplevel()
    #root.get_themes()     #-------------Returns a list of all themes that can be set
    #root.set_theme("plastik")   #----------------------------Sets an available theme
    bg_image=PhotoImage(file="images/newBG1.png")
    ttk.Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)
    root.resizable(False, False)#-----------------Bloquear redimencion de la ventana

    #-------------------------------BARRA DE MENU-----------------------------------
    #===============================================================================
    menubar = Menu(root)
    root.config(menu=menubar)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Exit", command=root.destroy)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us", command=about_us)
    subMenu.add_command(label="Desarrolladores", command=presentarIntegrantes)
    #----------------DIMENSION Y WIDGETS DE LA VENTANA------------------------------
    #===============================================================================
    root.geometry("1000x600")
    root.title("Estadisticas")
    root.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Txx="GRAFICAS DE DATOS"
    text = Label(root, font =('arial', 16, 'bold'),fg='white' ,text=Txx, bg="#65dc40")#color del header bg="#2ca3d7"
    text.pack(ipady=30)

    #==================================================FUNCION Graica de Promedios
    def promedios():
        data=[phdata_prom,listasal_prom,listatemp_prom,listah_prom,nldata_prom]
        data=np.array(data)
        labels = 'PH', 'SALINIDAD', 'TEMPERATURA', 'HUMEDAD', 'NIVEL DEL AGUA'
        col=('#0da0c1','#e39106','#25b413','#700f9e','#e82626')#,'#e7ea0e')
        #_,_, texto= pyplot.pie(data,colors=col,labels=len,autopct='%1.1f%%')
        figg, axx=plt.subplots()
        axx.pie(data,colors=col, labels=labels)
        print(data)
        
        _,_, texto= axx.pie(data,colors=col,autopct=lambda p: '{0:.2f}%'.format(p/100*data.sum()))
        for tex in texto:
                tex.set_color('white')
        
        axx.axis('equal')
        pyplot.title('PROMEDIOS')
        #pyplot.show()
        pyplot.savefig('images/data.png', transparent=True, dpi=60, quality=100)
        

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        '''sizes=[phdata_prom, listasal_prom, listatemp_prom, listah_prom, nldata_prom]
                                sizes=np.array(sizes)
                                labels = 'PH', 'SALINIDAD', 'TEMPERATURA', 'HUMEDAD', 'NIVEL DEL AGUA'
                                #sizes = [15, 30, 45, 10, 10]
                                #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
                                print(sizes)
                                fig1, ax1 = plt.subplots()
                                _,_,ax1.pie(sizes, labels=labels, autopct=lambda p: '{0:.2f}%'.format(p/100*sizes.sum()))
                                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                                ax1.set(title='PROMEDIOS')
                                pyplot.savefig('images/data.png', transparent=True, dpi=60, quality=100)'''
    #===========================================================FUNCION Graica de PH

    def PhData():
        fig, ax = pyplot.subplots()

        size = 0.3

        cmap = pyplot.get_cmap("tab20c")
        outer_colors = cmap(np.arange(6)*4)
        #inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

        ax.pie(listaph.flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        #ax.pie(listaph.sum()/len(listaph), radius=1-size, colors=inner_colors,
        #       wedgeprops=dict(width=size, edgecolor='w'))

        ax.set(aspect="equal", title='DATOS DE PH')
        pyplot.savefig('images/data2.png', transparent=True,dpi=50, quality=100)


    def salData():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ('#f2662a', '#e2e00b', '#70f528' ,'#23cdeb', '#a42ff5', '#e03232')#-------------------------cambiarrrrr
        #inner_colors = ('#6eeb67', '#e0df54', '#9eee72' ,'#71d2e3', '#c27cf2', '#df7070')

        ax.pie(sali.flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='white'))

        #ax.pie(valtemp.sum()/len(valtemp), radius=1-size, colors=inner_colors,
        #       wedgeprops=dict(width=size, edgecolor='white'))

        ax.set(aspect="equal", title='SALINIDAD')
        pyplot.savefig('images/datasal.png', transparent=True,dpi=50, quality=100)

    def TempData():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ('#f2662a', '#e2e00b', '#70f528' ,'#23cdeb', '#a42ff5', '#e03232')
        #inner_colors = ('#6eeb67', '#e0df54', '#9eee72' ,'#71d2e3', '#c27cf2', '#df7070')

        ax.pie(valtemp.flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='white'))

        #ax.pie(valtemp.sum()/len(valtemp), radius=1-size, colors=inner_colors,
        #       wedgeprops=dict(width=size, edgecolor='white'))

        ax.set(aspect="equal", title='TEMPERATURA')
        pyplot.savefig('images/data3.png', transparent=True,dpi=50, quality=100)

    def HumeData():
        fig, ax = pyplot.subplots()

        size = 0.3

        outer_colors = ('#cc1b50','#700f9e','#2d45c4','#41be06','#df8908','#e82626')
        #inner_colors = ('#df8f3b','#700f9e','#2d45c4','#41be06','#df8908','#e82626')

        ax.pie(valh.flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        '''ax.pie(valh.sum()/len(valh), radius=1-size, colors=inner_colors,
                                       wedgeprops=dict(width=size, edgecolor='w'))
                        '''
        ax.set(aspect="equal", title='HUMEDAD')
        pyplot.savefig('images/data4.png', transparent=True,dpi=50, quality=100)


    def nivelData():
        '''fig, ax = pyplot.subplots()
                        
        size = 0.3

        outer_colors = ('#700f9e','#2d45c4','#cc1b50','#41be06','#df8908','#e82626')#------------cambarrr
        #inner_colors = ('#df8f3b','#700f9e','#2d45c4','#41be06','#df8908','#e82626')

        ax.pie(valln.flatten(), radius=0.8, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'))

        '''#ax.pie(valh.sum()/len(valh), radius=1-size, colors=inner_colors,
        #wedgeprops=dict(width=size, edgecolor='w'))
        '''
        ax.set(aspect="equal", title='NIVEL DEL AGUA')'''
        fig, ax1 = pyplot.subplots()
        

        bins = [1, 2, 3, 4, 5, 6]
        ax1.bar(bins, valln)
        ax1.set_title('NIVEL DEL AGUA')

        pyplot.savefig('images/dataNIV.png', transparent=True, dpi=50, quality=100)


    strt1=str(valtemp[0])+'°C'
    strt2=str(valtemp[1])+'°C'
    strt3=str(valtemp[2])+'°C'
    strt4=str(valtemp[3])+'°C'
    strt5=str(valtemp[4])+'°C'
    strt6=str(valtemp[5])+'°C'
    #strt=str(promtemp)+'°C Temp prom.'

    strh1=str(valh[0])+'%'
    strh2=str(valh[1])+'%'
    strh3=str(valh[2])+'%'
    strh4=str(valh[3])+'%'
    strh5=str(valh[4])+'%'
    strh6=str(valh[5])+'%'
    #strh=str(promh)+'  Hum prom.'

    str1=str(listaph[0])
    str2=str(listaph[1])
    str3=str(listaph[2])
    str4=str(listaph[3])
    str5=str(listaph[4])
    str6=str(listaph[5])
    #strph=str(promPH1)+'  PH prom.'

    strNIV1=str(valln[0])+'cm'
    strNIV2=str(valln[1])+'cm'
    strNIV3=str(valln[2])+'cm'
    strNIV4=str(valln[3])+'cm'
    strNIV5=str(valln[4])+'cm'
    strNIV6=str(valln[5])+'cm'

    strsal1=str(sali[0])+'%'
    strsal2=str(sali[1])+'%'
    strsal3=str(sali[2])+'%'
    strsal4=str(sali[3])+'%'
    strsal5=str(sali[4])+'%'
    strsal6=str(sali[5])+'%'

    '''
    nivelData()
    pniv=PhotoImage(file="images/dataNIV.png")
    Label(root,image=pniv).place(x=675+25,y=300)

    
    '''




    # /*----------------------------grafico de datos------------------------------/*

    #==============================================================================
    #--------------------------------- grafico de ph ------------------------------
    PhData()
    phot2=PhotoImage(file="images/data2.png")
    Label(root,image=phot2).place(x=675+25,y=95)


    #==============================================================================
    #---------------------------- grafico de temperatura --------------------------
    TempData()
    phot4=PhotoImage(file="images/data3.png")
    Label(root,image=phot4).place(x=85-15+25,y=95)


    #==============================================================================
    #------------------------------ grafico de salinidad ----------------------------
    salData()
    



    #==============================================================================
    #------------------------------ grafico de nivel de agua-----------------------
    nivelData()


    '''    '''

    #==============================================================================
    #------------------------------ grafico de humedad ----------------------------

    HumeData()
    phot5=PhotoImage(file="images/data4.png")
    Label(root,image=phot5).place(x=290+60+20+25,y=95)

    #==============================================================================
    #------------------------------ grafico de promedios --------------------------



    promedios()
    phot=PhotoImage(file="images/data.png")
    Label(root,image=phot).place(x=600,y=300-20)

    '''Label(root, text='PH').place(x=656,y=410+5)
                Label(root, text='Intensidad lluvia').place(x=656,y=442+5)
                Label(root, text='nivel de agua').place(x=656,y=474+5)
            '''


    phot12=PhotoImage(file="images/colorph.png")
    Label(root,image=phot12).place(x=315+330+75,y=124)


    phott=PhotoImage(file="images/colortemp.png")
    Label(root,image=phott).place(x=50-15+75,y=114+10)

    phott1=PhotoImage(file="images/colortemp.png")
    Label(root,image=phott1).place(x=50-15+25,y=250+60)

    '''photh=PhotoImage(file="images/colorhum.png")
                Label(root,image=photh).place(x=330+125,y=114+10)'''


    potsal=PhotoImage(file='images/datasal.png')
    Label(root, image=potsal).place(x=80-50, y=250+60)

    photh=PhotoImage(file="images/colorhum.png")
    Label(root,image=photh).place(x=330+75,y=114+10)

    potniv=PhotoImage(file='images/dataNIV.png')
    Label(root, image=potniv).place(x=290+60+20-70, y=250+60)

    '''phot3=PhotoImage(file="images/colorprom.png")
                ph3=Label(root,image=phot3).place(x=600+75,y=370)'''

    def on_closing():
        root.destroy()

    ttk.Button(root, text='cerrar', command=on_closing).place(x=460, y=550)

    #------------------------------------------------------------------------------------ Label ph

    Label(root, text=str1).place(x=654+50+70,y=116+15)
    Label(root, text=str2).place(x=654+50+70,y=142+15)
    Label(root, text=str3).place(x=654+50+70,y=167+15)
    Label(root, text=str4).place(x=654+50+70,y=194+15)
    Label(root, text=str5).place(x=654+50+70,y=221+15)
    Label(root, text=str6).place(x=654+50+70,y=248+15)

    #-----------------------------------------------------------------------------------Label temp
    

    Label(root, text=strt1).place(x=354-250-15+70,y=116+15-1)
    Label(root, text=strt2).place(x=354-250-15+70,y=142+15-3)
    Label(root, text=strt3).place(x=354-250-15+70,y=167+15-1)
    Label(root, text=strt4).place(x=354-250-15+70,y=194+15)
    Label(root, text=strt5).place(x=354-250-15+70,y=221+15-1)
    Label(root, text=strt6).place(x=354-250-15+70,y=248+15-1)

    #-----------------------------------------------------------------------------------Label nivel agua
    '''
    Label(root, text=strNIV1).place(x=305+60+20,y=116+15+220)
    Label(root, text=strNIV2).place(x=305+60+20,y=142+15+220)
    Label(root, text=strNIV3).place(x=305+60+20,y=167+15+220)
    Label(root, text=strNIV4).place(x=305+60+20,y=194+15+220)
    Label(root, text=strNIV5).place(x=305+60+20,y=221+15+220)
    Label(root, text=strNIV6).place(x=305+60+20,y=248+15+220)

    '''

    #-----------------------------------------------------------------------------------Label salinidad
    '''photh1=PhotoImage(file="images/colorhum.png")
                Label(root,image=photh1).place(x=330+75,y=116+15+220)'''
    phosall=PhotoImage(file="images/colortemp.png")
    Label(root,image=phosall).place(x=354-250-65,y=116+15+216)

    Label(root, text=strsal1).place(x=354-250-15,y=116+15+220)
    Label(root, text=strsal2).place(x=354-250-15,y=142+15+220)
    Label(root, text=strsal3).place(x=354-250-15,y=167+15+220)
    Label(root, text=strsal4).place(x=354-250-15,y=194+15+220)
    Label(root, text=strsal5).place(x=354-250-15,y=221+15+220)
    Label(root, text=strsal6).place(x=354-250-15,y=248+15+220)

    #-----------------------------------------------------------------------------------Label humedad
    Label(root, text=strh1).place(x=305+60+20+70,y=116+15)
    Label(root, text=strh2).place(x=305+60+20+70,y=142+15)
    Label(root, text=strh3).place(x=305+60+20+70,y=167+15)
    Label(root, text=strh4).place(x=305+60+20+70,y=194+15)
    Label(root, text=strh5).place(x=305+60+20+70,y=221+15)
    Label(root, text=strh6).place(x=305+60+20+70,y=248+15)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()




def niveles():
    print("niveles xd")


#======================================================================================================
#                                 ---- VENTANA PRICIPAL ----
#======================================================================================================
index = tk.ThemedTk()
index.get_themes()     #-------------Returns a list of all themes that can be set
index.set_theme("plastik")  #----------------------------Sets an available theme
bg11_image=PhotoImage(file="images/newBG2.png")
ttk.Label(index, image=bg11_image).place(x=0, y=0, relwidth=1, relheight=1)
index.resizable(False, False)
index.geometry("500x300")
index.title("MOD PLANT")
index.iconbitmap(r'images/descarga_gMJ_icon.ico')


from opc import cmpdata
from trdata import datos_tr

ttk.Button(index, text='Estadistias', command=Present_Grafic).place(x=30+45+15, y=100)

ttk.Button(index, text='Comparaion de valores', command=cmpdata).place(x=150+10+15, y=100)

ttk.Button(index, text='Valores actuales', command=datos_tr).place(x=270+40+15, y=100)

#-------------------------------BARRA DE MENU-----------------------------------
#===============================================================================
menubar = Menu(index)
index.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=index.destroy)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)
subMenu.add_command(label="Desarrolladores", command=presentarIntegrantes)

Txx="MOD-PLANT"
text = Label(index, font =('arial', 16, 'bold'),fg='white' ,text=Txx, bg="#6fd54d")#color del header
text.pack(ipady=10)




#ttk.Button(index, text='indicaciones', command=niveles).place(x=150+55, y=200-30)

index.mainloop()
