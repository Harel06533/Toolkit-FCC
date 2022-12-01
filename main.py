#===== TOOLKIT FCC VERSIÓN FINAL =====#
#        - Harel Olguín 
#        - Omar Ponce
#        - Kevin González

import tkinter as ttk
import Tablas_Verdad as tot
import Conjuntos as cnj
import Series as sr
import RelaFunc as rf

#//CONFIGURACIÓN DE LA VENTANA PRINCIPAL
root = ttk.Tk()
root.geometry('1000x600')
root.iconbitmap('Assets\Iteso_logo.ico')
root.config(
     bg = '#fbfbfb'
)
root.title('ToolPack FCC v.3.1')
root.resizable(False, False) #Ancho y Altura

welcomeMessage = ttk.Label(root, text = '!Bienvenido! al Toolkit FCC v.3.1(FINAL)')
welcomeMessage.pack(anchor=ttk.CENTER)
welcomeMessage.config(
     fg = 'black',
     font = ("Verdana", 25),
     bg = '#cfcfcf',
     borderwidth=3
)

selecMessage = ttk.Label(root, text = 'Seleccione la opción que le interese')
selecMessage.config(
     fg = 'black',
     font = ("Verdana", 12),
     bg = 'white'
)
selecMessage.pack()


# --BOTONES Y SELECCIÓN --

     #VARIABLES Y EVENTOS 
ttgButton = ttk.Button(root, text = 'Tablas de Verdad', height=4, width=15, command=tot.NEW_TTG_WIN)
tdcButton = ttk.Button(root, text = 'Teoría de Conjuntos', height=4, width=15, command=cnj.NEW_TDCWINDOW_SET)  
seriesButton = ttk.Button(root, text = 'Sucesiones', height=4, width=15, command= sr.NEW_SR_WIN)
refButton = ttk.Button(root, text= 'Relaciones y Funciones', height=4, width=17, command= rf.NEW_RF_WIN)
exitButton = ttk.Button(root, text= 'Salir', highlightcolor='#000', height=2, width=7, command=root.quit)

     #ACOPLAMIENTOS
ttgButton.pack(padx= 0, pady= 0)
tdcButton.pack(padx= 0, pady= 20)
seriesButton.pack(padx= 0, pady= 25)
refButton.pack(padx= 0, pady= 30)
exitButton.pack(side=ttk.BOTTOM)


root.mainloop()