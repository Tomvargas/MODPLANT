from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
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
import time
from trdata import dato


#en caso de conexion exitosa muestra los datos reales
# si la conexion falla se muestra datos ficticios
data1=dato()

data1.insert(0,time.strftime("%H:%M:%S"))


class App(Frame):
    data=data1
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        #tv.tag_configure('even', background='#65dc40')
        tv['columns'] = ('Hora', 'Estadoactual', 'Recomendado')
        tv.heading("#0", text='Variable', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Hora', text='Hora')
        tv.column('Hora', anchor='center', width=100)
        tv.heading('Estadoactual', text='Estado actual')
        tv.column('Estadoactual', anchor='center', width=100)
        tv.heading('Recomendado', text='Estado recomendado')
        tv.column('Recomendado', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):

        self.treeview.insert('', 'end', text="PH", values=(data1[0],data1[1], '6.6'))

        self.treeview.insert('', 'end', text="SALINIDAD", values=(data1[0],data1[2], '30%'))

        self.treeview.insert('', 'end', text="TEMPERATURA", values=(data1[0],data1[3], '30° - 35°'))#3

        self.treeview.insert('', 'end', text="HUMEDAD", values=(data1[0],data1[4], '13%'))

        self.treeview.insert('', 'end', text="NIVEL DEL AGUA", values=(data1[0],data1[5], '10 cm'))
        self.treeview.tag_configure('even', background='#65dc40')


def main():
    root1 = Tk()
    root1.iconbitmap(r'images/descarga_gMJ_icon.ico')
    root1.geometry("600x200")
    root1.title("Comparacion")
    App(root1)
    Button(root1, text="Verificar Valores", bg='#65dc40', fg='White').grid()
    root1.mainloop()
if __name__ == '__main__':
    main()

def cmpdata():
    main()