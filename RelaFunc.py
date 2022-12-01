import tkinter as ttk

def NEW_RF_WIN():

  # =============== VARIABLES ================#
  inputBrackets = ttk.StringVar()

  # ================ FUNCIONES ================#
    
  def normalizePairs(string):
    normalizeString = string
    return normalizeString

  def checkTransitive():
    print("WIP")

  def checkSimetric():
    print("WIP")

  def checkReflex():
    print("WIP")
  
  def newWindow():
    stringToEval = relationEntry.get()
    normalizedString = normalizePairs(stringToEval)

    result = ttk.Toplevel()
    result.geometry = ('700x500')
    result.title('Evaluación de la Relación')
    result.resizable(False, False)
    result.iconbitmap('Assets\Iteso_logo.ico')
    result.config(bg='#fbfbfb')
    resultLabel = ttk.Label(result, text= normalizedString, font=('Verdana', 11), bg= '#fbfbfb')

    resultLabel.pack()

  # ================ VENTANA PRINCIPAL ==============#
  ref = ttk.Toplevel()
  ref.geometry('500x300')
  ref.title('Relaciones y Funciones')
  ref.resizable(False, False)
  ref.iconbitmap('Assets\Iteso_logo.ico')
  ref.config(bg='#fbfbfb')

  # ================= ELEMENTOS =================#

  #Labels
  titleLabel = ttk.Label(ref, text='Relaciones y Funciones', font=('Verdana', 15), bg='#fbfbfb')
  warnLabel = ttk.Label(ref, text='Introduzca los pares de la forma "(a,b)\nSeparados por una coma."', font=('Verdana', 11), bg='#fbfbfb')

  #Entrys
  relationEntry = ttk.Entry(ref, textvariable=inputBrackets, font=('Verdana', 11), bg='#ccc', fg='#0f0f0f')


  #Botones
  evaluateButton = ttk.Button(ref, text='Evaluar', font=('Verdana', 11), command=newWindow)

  #Acomodo 
  titleLabel.pack()
  relationEntry.pack()
  warnLabel.pack()
  evaluateButton.pack(side='bottom')
  