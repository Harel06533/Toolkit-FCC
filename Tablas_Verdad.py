import tkinter as ttk
from tkinter import messagebox

expression = ''

def NEW_TTG_WIN():
  
  #====== VARIABLES =====#
  inputText = ttk.StringVar()

  #===== FUNCIONES CALCULADORA =====#

  #Quitar expresiones
  def clearExpression():
    global expression
    expression = ''
    inputText.set('')
    
  #Generar expresión
  def varButtonClick(var):
    global expression
    expression = expression + var
    inputText.set(expression)
  
  #Eliminar caracteres
  def deleteButtonClick():
    global expression 
    try:
      expression = expression.rstrip(expression[-1])
      inputText.set(expression)
    except IndexError:
      messagebox.showwarning(title='CUIDADO', message='No puedes seguir borrando')


  #Checar variables y extensión
  def checkVar():
    if 'p' in expression and not 'q' in expression and not 'r' in expression and not 's' in expression:
      return 1
    elif 'p' in expression and 'q' in expression and not 'r' in expression and not 's' in expression:
      return 2
    elif 'p' in expression and 'q' in expression and 'r' in expression and not 's' in expression:
      return 3
    elif 'p' in expression and  'q' in expression and 'r' in expression and 's' in expression:
      return 4

    else:
      return 0 #Error

  #Evaluar expresión:
  def getValueAndEvaluate():
    expType = checkVar()
    prop = valueInput.get()
    print(prop)
    if not prop:
      messagebox.showerror(title='ERROR', message='No hay proposición a evaluar')
    elif expType == 0:
      messagebox.showerror(title='ERROR', message='Es necesario utilizar el órden alfabético de "p, q, r, s"')
    elif expType == 1:
      operacion = fragmentar(prop)                           #Fragmentar la expresion de entrada
      PrintOneVar(operacion)
    elif expType == 2:
      operacion = fragmentar(prop)                           #Fragmentar la expresion de entrada
      PrintTwoVar(operacion)
    elif expType == 3:
      operacion = fragmentar(prop)                           #Fragmentar la expresion de entrada
      PrintTreeVar(operacion)
    elif expType == 4:
      operacion = fragmentar(prop)                           #Fragmentar la expresion de entrada
      PrintTreeVar(operacion)
    elif expType == 5:
      operacion = fragmentar(prop)                           #Fragmentar la expresion de entrada
      PrintFiveVar(operacion)



  
  #===== VENTANA PRINCIPAL =====#
  ttg = ttk.Toplevel()
  ttg.geometry('550x400')
  ttg.title('Calculadora de Tablas de Verdad')
  ttg.resizable(False, False)
  ttg.iconbitmap('Assets\Iteso_logo.ico')
  ttg.config(bg='#fbfbfb')

  #===== ELEMENTOS =====#
  
  #Char
  pText = 'p'
  qText = 'q'
  rText = 'r'
  sText = 's'
  negText = '~'
  andText = '^'
  orText = 'V'
  ifText = '>' #Implicación
  onlyifText = '<' #Doble Implicación
  acText = 'AC'
  delText = 'DEL'
  lparText = '('
  rparText = ')'
  equalText = 'Evaluar Expresión'

  #Tkinter
  insertFrame = ttk.Frame(ttg, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
  valueInput = ttk.Entry(insertFrame, font=('Verdana', 11), textvariable=inputText, width=50, bg='#eee', bd=0, justify='left')
  warnLabel = ttk.Label(ttg, font=('Verdana', 11), text=f'{andText} = AND\n{orText} = OR\n{negText} = NOT\n{ifText} = IMPLICACIÓN\n{onlyifText} = DOBLE IMPLICACIÓN', bg='#fbfbfb' )

  #===== BOTONES =======#

  #Botones de Variables
  pButton = ttk.Button(ttg, text= pText, font=('Verdana',11), height=2, width=6, command= lambda:varButtonClick(pText)) # p
  qButton = ttk.Button(ttg, text= qText, font=('Verdana',11), height=2, width=6, command= lambda:varButtonClick(qText)) # q
  rButton = ttk.Button(ttg, text= rText, font=('Verdana',11), height=2, width=6, command= lambda:varButtonClick(rText)) # r 
  sButton = ttk.Button(ttg, text= sText, font=('Verdana',11), height=2, width=6, command= lambda:varButtonClick(sText)) # s

  #Operadores
  negButton = ttk.Button(ttg, text= negText, font=('Verdana',11),height=2, width=6,bg='#bf8eed', command= lambda:varButtonClick(negText)) # ~
  andButton = ttk.Button(ttg, text= andText, font=('Verdana',11), height=2, width=6, bg='#bf8eed', command= lambda:varButtonClick(andText)) # ^
  orButton = ttk.Button(ttg, text= orText, font=('Verdana',11), height=2, width=6, bg='#bf8eed', command= lambda:varButtonClick(orText)) # v
  ifButton = ttk.Button(ttg, text= ifText, font=('Verdana',11), height=2, width=6, bg='#bf8eed', command= lambda:varButtonClick(ifText))# ->
  onlyIfButton = ttk.Button(ttg, text= onlyifText, font=('Verdana',11), height=2, width=6, bg='#bf8eed', command= lambda:varButtonClick(onlyifText))# <->

  #Formato
  acButton = ttk.Button(ttg, text= acText, font=('Verdana',11), height=2, width=6, bg='#ff9999', command= clearExpression) # AC
  delButton = ttk.Button(ttg, text= delText, font=('Verdana',11), height=2, width=6, bg='#ff9999', command= deleteButtonClick) # DEL
  lParButton = ttk.Button(ttg, text= lparText, font=('Verdana',11), height=2, width=6, bg='#44ff88', command= lambda:varButtonClick(lparText)) # (
  rParButton = ttk.Button(ttg, text= rparText, font=('Verdana',11), height=2, width=6, bg='#44ff88', command= lambda:varButtonClick(rparText)) # )
  evalButton = ttk.Button(ttg, text= equalText, font=('Verdana',11), height=2, width=34, bg='#ff9999', command=getValueAndEvaluate) # =

  #====== ACOMODO ======#

  #Elementos
  insertFrame.pack(side='top')
  valueInput.grid(padx=0, pady=0)
  valueInput.pack(ipady=10)
  warnLabel.pack(side='bottom')

  #Variables
  pButton.place(x=65, y=80)
  qButton.place(x=130, y=80)
  rButton.place(x=195, y=80)
  sButton.place(x=260, y=80)

  #Operadores
  negButton.place(x=65, y=145)
  andButton.place(x=130, y=145)
  orButton.place(x=195, y=145)
  ifButton.place(x=260, y=145)
  onlyIfButton.place(x=325, y=145)

  #Formato
  acButton.place(x=325, y=80)
  delButton.place(x=390, y=80)
  lParButton.place(x=390, y=145)
  rParButton.place(x=390, y=210)
  evalButton.place(x=65, y=210)


# ========== OPERACIONES LÓGICAS ============= #

def separateExpression(express):
  text = ''
  for i in express:
    text = text + i + '\t' 
  return text

def oneVarExpression(operacion_fin, booleanos):
  text = ''
  for p in booleanos:   
    text = text + '{}'.format(p) + '\t'
    for i in range(0, len(operacion_fin)):
      text = text + '\t' + f'{eval(operacion_fin[i])}' 
    text = text + '\n'    
  return text                      #Generar tabla de verdad de las variables

def operaciones(opera):    
    #Cambia los > por sus equivalentes lógicos, es decir, p > q = ~ p v q
    for i in opera:
        if i.find(">") != -1:                   #Recorre el arreglo hasta encontrar >, si no lo encuentra imprime -1
            posi = i.find(">")                  #Determinar la posision de >
            conjunto = i[posi-1:posi+2]         #Encontrando la posiscion de sus variables
            opera[opera.index(i)] = opera[opera.index(i)].replace(conjunto,"~"+i[posi-1]+"v"+i[posi+1]) # Transformando a su equivalente

    #Cambia los > por sus equivalentes lógicos, es decir, p < q = (p > q) ^ (q > p)=(~ p v q) ^ (~ q v p)
    for i in opera:
        if i.find("<") != -1:                   #Recorre el arreglo hasta encontrar <, si no lo encuentra imprime -1
            posi = i.find("<")                  #Determinar la posision de <
            conjunto = i[posi-1:posi+2]         #Encontrando la posiscion de sus variables
            opera[opera.index(i)] = opera[opera.index(i)].replace(conjunto,"(~"+i[posi-1]+"v"+i[posi+1]+") ^ (~"+i[posi+1]+"v"+i[posi-1]+")")   # Transformando a su equivalente

    #Agrega espacios entre todos los caracteres de la operación
    for i in range (len(opera)):                #Recorrer todas las posiciones de la lista
        conjunto = ""                           #Declarando conjunto
        for j in opera[i]:                      #Recorriendo cada arreglo
            conjunto = conjunto + j + " "       #Agregando un espacio despues de cada caracter para que quede todo separado
        opera[i] = conjunto                     #Guardando lo obtenido en conjunto

    #Cambia cada uno de los signos por su operador lógico correspondiente      
    for i in range (0,len(opera)):                      #Recorrer cada posicion de la lista
        opera[i] = opera[i].replace("~","not")          #Reemplazar su simbolo a su equivalente logico en python
        opera[i] = opera[i].replace("^","and")          #Reemplazar su simbolo a su equivalente logico en python
        opera[i] = opera[i].replace("v","or")           #Reemplazar su simbolo a su equivalente logico en python

    return(opera)                                       #Retornar opera

def fragmentar(expresion):
    #Variables
    opera = []        #Contiene las operaciones
    opera_2 = []      #Lista final para pulir todo
    frase = expresion.replace(" ","")   #Quitando los espacios para poder determinar las letras mas adelante   

    while (len(frase) != 1 and not frase.isdigit()):  #Verificando que sea mas de un caracter y no contenga numeros

        # Encontrar y cambiar los ~, ya sé que los siguientes 3 pueden ser función
        for i in range(0,len(frase)-1):                 #Recorriendo cada posision del arreglo
            if (frase[i] == "~" and frase[i+1].isalnum() and frase[i:i+2] not in opera):      #Obteniendo las posiciones de las variables
                opera.append(frase[i:i+2])
        frase = simplificar(opera,frase)                                                      #Llamada a la funcion simplificar

        #Encontrar "^" & "v",es decir los operadores de conjunción y disyunción
        for i in range(1,len(frase)-1):                                                         #recorrer cada posision de la expresion
            if ((frase[i] == "^" or frase[i] == "v") and frase[i+1].isalnum() and frase[i-1].isalnum() and frase[i-1:i+2] not in opera): #Encontrando or y and y separando sus variables
                opera.append(frase[i-1:i+2])                                              #Colocandola en el arreglo
        frase = simplificar(opera,frase)                                                  #Llamada a la funcion simplificar

        #Encontrar > que en este caso representa condicional
        for i in range(1,len(frase)-1):                                                     #Recorriendo cada posision del arreglo
            if (frase[i] == ">" and frase[i+1].isalnum() and frase[i-1].isalnum() and frase[i-1:i+2] not in opera): #Encontrando > y sus variables
                opera.append(frase[i-1:i+2])                                              #Guardando todo en la lista
        frase = simplificar(opera,frase)                                                  #Llamando a la funcion simplificar

        #Encontrar < que en este caso representa bidireccional
        for i in range(1,len(frase)-1):                                                     #Recorrer cada posision del arreglo
            if (frase[i] == "<" and frase[i+1].isalnum() and frase[i-1].isalnum() and frase[i-1:i+2] not in opera):          #Encontrando < y sus variables
                opera.append(frase[i-1:i+2])                                              #Guardandolo en la lista
        frase = simplificar(opera,frase)                                                  #Llamando a la funcion simplificar

        #Eliminar parentesis y agregarlos a la lista
        for i in range(1,len(frase)-1):                                                     #Recorrer cada posision del arreglo
            if (frase[i].isdigit() and frase[i-1] == "(" and frase[i+1] == ")"):            #Encontrando parentesis
                opera[int(frase[i])] = "(" + opera[int(frase[i])] + ")"                 #Agregando
                frase = frase.replace(frase[i-1:i+2], " " + frase[i] + " ", 1)              #Eliminando
        frase = frase.replace(" ","")                                                       #Eliminando espacios

    # Cambia los números por la operación para crear la lista opera_2
    for i in opera:                                                     #Recorrer cada posision de la lista
        frase = i                                                         #Colocarlo en frase
        for j in frase:                                                   #Recorrer cada posision del arreglo
            if j.isdigit():                                               #Verificando
                if len(opera_2) >= int(j):                              #Comparando
                    frase = frase.replace(j,opera_2[int(j)])            #Si la condicion se cumple remplazar los valores
                else:    
                    frase = frase.replace(j,opera[int(j)])              #Reemplazar el valor en opera si no
        opera_2.append(frase)                                           #Colocar frase en la ultima posision del arreglo

    return(opera_2)

    #opera_2 regresa la expresion fragmentada en partes.

    

# Reduce las operaciones 
def simplificar(opera,frase):
    for i in range(0,len(opera)):                       #Recorrer las posiciones de opera
        if(opera[i] in frase):                          
            frase = frase.replace(opera[i],str(i))      #Reemplazar la posicion de opera por la de i en frase
    return(str(frase))                                  #Retornar frase como valor tipo cadena

#Funcion para cuando hay una sola variable
def PrintOneVar(operacion): 
  
    booleanos = [False, True]                              #Valores booleanos
    print('p\t', end ='')                                   #Encabezado de variables
    for i in range(len(operacion)):                         #Recorre las posiciones de operacion
        print (f"{operacion[i]}", end = '\t')               #Encabezado de preposiciones
    print()                                                 #Enter
    print('-'*25*len(operacion))                            #Linea divisora
    operacion_fin = operaciones(operacion)                  #Llamada a la funcion operacion para la conversion de caracteres a caracteres logicos
    
    for p in booleanos:                                     #Generar tabla de verdad de las variables
        print('{}'.format(p), end = '\t')                   #Imprimir valor booleano
        for i in range(0,len(operacion_fin)):               #Recorrer preposiciones
            print (f"{eval(operacion_fin[i])}", end='\t')      #Imprimir
        print()                                             #Enter
    return operacion_fin

def PrintTwoVar(operacion):
    
    booleanos = [False, True]                              #Valores booleanos
    print('\t')                                             #Encabezado de variables
    print('p \t q \t', end ='')                        
    for i in range(len(operacion)):                          #Recorre las posiciones de operacion
        print (f"{operacion[i]}", end = '\t')                #Encabezado de preposiciones
    print()                                                 #Enter
    print('-'*25*len(operacion))                            #Linea divisora
    operacion_fin = operaciones(operacion)                  #Llamada a la funcion operacion para la conversion de caracteres a caracteres logicos 
    for p in booleanos:                                     #Recorrer variables
        for q in booleanos:                                 #Recorrer variables
            print('{} \t {}'.format(p,q), end = '\t')       #Imprimir valor booleano
            for i in range(0,len(operacion_fin)):           #Recorrer preposiciones
                print (f"{eval(operacion_fin[i])}", end='\t')      #Imprimir
            print()                                             #Enter
    return operacion_fin


def PrintTreeVar(operacion):

  booleanos = [False, True]                               #Valores booleanos
  print('p \t q \t r \t', end ='')                        #Encabezado de variables
  for i in range(len(operacion)):                         #Recorre las posiciones de operacion
    print (f"{operacion[i]}", end = '\t')                  #Encabezado de preposiciones
  print()
  print('-'*25*len(operacion))                              #Linea divisora
  operacion_fin = operaciones(operacion)                #Llamada a la funcion operacion para la conversion de caracteres a caracteres logicos 
  for p in booleanos:                                         #Recorrer variables                                   
    for q in booleanos:                                     #Recorrer variables
        for r in booleanos:                                     #Recorrer variables
            print('{} \t {} \t {}'.format(p,q,r), end = '\t') #Imprimir valor booleano
            for i in range(0,len(operacion_fin)):
                print (f"{eval(operacion_fin[i])}", end='\t') #Imprimir valor booleano
            print()
  return operacion_fin
        

def PrintFourVar(operacion):
  
  booleanos = [False, True]                              #Valores booleanos
  print('p \t q \t r \t s \t', end ='')                       #Encabezado de variables
  for i in range(len(operacion)):                        #Recorre las posiciones de operacion
    print (f"{operacion[i]}", end = '\t')                #Encabezado de preposiciones
  print()
  print('-'*25*len(operacion))                             #Linea divisora
  operacion_fin = operaciones(operacion)                #Llamada a la funcion operacion para la conversion de caracteres a caracteres logicos     
  for p in booleanos:                                         #Recorrer variables 
    for q in booleanos:                                         #Recorrer variables 
        for r in booleanos:                                         #Recorrer variables 
            for s in booleanos:                                         #Recorrer variables 
                print('{} \t {} \t {} \t {}'.format(p,q,r,s), end = '\t')#Imprimir valor booleano
                for i in range(0,len(operacion_fin)):
                    print (f"{eval(operacion_fin[i])}", end='\t')       #Imprimir valor booleano
                print()
  return operacion_fin
def PrintFiveVar(operacion):
 
  booleanos = [False, True]                              #Valores booleanos
  print('p \t q \t r \t s \t t \t', end ='')            #Encabezado de variables
  for i in range(len(operacion)):                        #Recorre las posiciones de operacion
    print (f"{operacion[i]}", end = '\t')                #Encabezado de preposiciones
  print()
  print('-'*25*len(operacion))                             #Linea divisora
  operacion_fin = operaciones(operacion)                #Llamada a la funcion operacion para la conversion de caracteres a caracteres logicos                                        #linea divisora
  for p in booleanos:                                        #Recorrer variables 
    for q in booleanos:                                        #Recorrer variables 
        for r in booleanos:                                        #Recorrer variables 
            for s in booleanos:                                        #Recorrer variables 
                for t in booleanos:                                        #Recorrer variables 
                    print('{} \t {} \t {} \t {} \t {}'.format(p,q,r,s,t), end='\t')#Imprimir valor booleano
                    for i in range(0,len(operacion_fin)):
                        print (f"{eval(operacion_fin[i])}", end='\t')       #Imprimir valor booleano
                    print()
  return operacion_fin

