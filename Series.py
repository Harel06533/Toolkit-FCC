import tkinter as ttk
from tkinter import messagebox

def NEW_SR_WIN():
  #Funciones
  def getValues():
    sumatoria = 0
    multiplicatoria = 1
    limSVal = limSupEnt.get()
    limIVal = limInfEnt.get()
    formulaVal = formulaEnt.get()
    print(limSVal)
    print(limIVal)
    print(formulaVal)
    
    #Checa que se evalúe en 'k', y que el límite inferior sea menor que el superior
    if not formulaVal or not limIVal or not limSVal:
      messagebox.showwarning(title='ERROR', message='Entradas insuficientes')
    elif not 'k' in formulaVal:
      messagebox.showwarning(title='ERROR', message='Evalúa en "k" minúscula')
    elif 'k' not in formulaVal or int(limIVal) > int(limSVal): #Checar que las entradas sean válidas
      messagebox.showwarning(title='ERROR', message='Entrada inválida')
    else:
  
      #Ventana
      resultWin = ttk.Toplevel()
      resultWin.geometry('1000x600')
      resultWin.title('Resultado de la Sucesión')
      resultWin.resizable(True, False)
      resultWin.iconbitmap('Assets\Iteso_logo.ico')
      resultWin.config(bg='#fbfbfb')
      
      #Frame
      frame = ttk.Frame(resultWin)
      frame.pack(fill='both', expand=1)
      frame.config(bg='#fbfbfb')

      #Canvas
      canvas = ttk.Canvas(frame)
      canvas.pack(side= 'left', fill='both', expand= 1)
      canvas.config(bg='#fbfbfb')

      #Scroll
      scrollL = ttk.Scrollbar(frame, orient='vertical', command = canvas.yview)
      scrollL.pack(side='right', fill= 'y')

      #Config 
      canvas.config(yscrollcommand = scrollL.set)
      canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox("all")))

      #Segundo Frame
      sndFrame = ttk.Frame(canvas)
      canvas.create_window((0, 0), window = sndFrame, anchor='nw')
      sndFrame.config(bg='#fbfbfb')

      titLabel = ttk.Label(sndFrame, text = f'Evaluando {formulaVal}\nDesde {limIVal} hasta {limSVal}', bg='#fbfbfb', font = ('Verdana', 15), fg='#0f0f0f')
      titLabel.pack()

      for ins in range(int(limIVal), int(limSVal) + 1):
        eachValue = formulaVal.replace('k', str(ins))
        actualVal = eval(eachValue)
        eValueLabel = ttk.Label(sndFrame, text = f"{eachValue} = {actualVal}", bg='#fbfbfb', font=('Verdana', 10), foreground= '#0f0f0f')
        eValueLabel.pack()
        sumatoria += actualVal
        multiplicatoria = multiplicatoria * actualVal
    opLabel = ttk.Label(canvas, text = f"Sumatoria = {sumatoria}\nMultiplicatoria = {multiplicatoria}", font=('Verdana', 13), bg='#fbfbfb', foreground= '#0f0f0f')
    opLabel.place(x=250, y=24)

    

  #Ventana principal
  srs = ttk.Toplevel()
  srs.geometry('500x300')
  srs.title('Series y Sucesiones')
  srs.resizable(False, False)
  srs.iconbitmap('Assets\Iteso_logo.ico')
  srs.config(bg='#fbfbfb')

  #Labels
  informLabel = ttk.Label(srs, text='*Introduzca la fórumula en\nfunción de "k" minúscula,\npor ejemplo:\n1/k, k*2, 2/(k+1).\nEs importante respetar jerarquía de\noperaciones.\nEjemplo:\nk+1*k+2 no es igual a\n(k+1)*(k+2)',
  bg='#fbfbfb', font=('Verdana', 8), fg='#0f0f0f')
  limSupLab = ttk.Label(srs, text='Limite superior = ', bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f')
  limInfLab = ttk.Label(srs, text='Limite inferior = ', bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f')
  formulaLab = ttk.Label(srs, text='Formula = ' ,bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f')

  #Entrys
  limSupEnt = ttk.Entry(srs, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')
  limInfEnt = ttk.Entry(srs, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')
  formulaEnt = ttk.Entry(srs, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')

  #Grids/Place Labels
  informLabel.place(x=240, y=0)
  limSupLab.grid(row=1, column=1)
  limInfLab.grid(row = 3, column = 1)
  formulaLab.grid(row = 5, column= 1)

  #Grids/Place Entrys
  limSupEnt.grid(row=2, column=1)
  limInfEnt.grid(row = 4, column = 1)
  formulaEnt.grid(row = 6, column= 1)

  #Botones
  evalButton = ttk.Button(srs, text='Evaluar', font=('Verdana',11))
  evalButton.place(x = 50, y = 200)
  evalButton.config(command = getValues)