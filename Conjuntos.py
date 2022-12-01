#Módulos de los conjuntos
import tkinter as ttk

#Función para brindar la información principal de la ventana 'CONJUNTOS'

def NEW_TDCWINDOW_SET():
    #GLOBALS
  A_List = []
  B_List = []
  C_List = []

  #Nested
  def getValueFromEntrys(): #Función que se encargará de dar presentación a la  lista, y debuggear cualquier posible caso
    #Obtención de los valores
    selectedValue1 = Get_Value1.get()
    selectedValue2 = Get_Value2.get()
    opValue1 = []
    opValue2 = []
    returnedValue = '' #Valor que retornará de las funciones
    insertNum = ''
    option = defaultValue.get()
    aVal = A_Value.get()
    bVal = B_Value.get()
    cVal = C_Value.get()
    
    A_List.clear()
    B_List.clear() #LIMPIA LAS LISTAS AL MOMENTO DE SER EJECUTADAS
    C_List.clear()

    ListA = aVal.split(",")
    ListB = bVal.split(",")
    ListC = cVal.split(",")

    #Limpiar espacios y juntar
    #Lista A
    for i in ListA: #Si existen espacios cómas
      for j in i:
        if j != ',' or j != '\0':
          A_List.append(i)

      #LISTA B                              
    for i in ListB: #Si existen espacios cómas
      for j in i:
        if j != ',' or j != '\0':
          B_List.append(i)

      #LISTA C
    for i in ListC: #Si existen espacios cómas
      for j in i:
        if j != ',' or j != '\0':
          C_List.append(i)

    #Encontrar repetidos
      #LISTA A

    print(A_List)
    print(B_List) #Debug
    print(C_List)
    print(selectedValue1, selectedValue2)
    print(option)
  
    #REASIGNAR VALORES DEPENDIENDO DE LA ENTRADA DE DATOS
      #VALOR 1 (IZQUIERDA)
    if selectedValue1 == 'A' or selectedValue1 == 'a':
      opValue1 = A_List
    elif selectedValue1 == 'B' or selectedValue1 == 'b':
      opValue1 = B_List
    elif selectedValue1 == 'C' or selectedValue1 == 'c':
      opValue1 = C_List
      #VALOR 2 (DERECHA)
    if selectedValue2 == 'A' or selectedValue2 == 'a':
      opValue2 = A_List
    elif selectedValue2 == 'B' or selectedValue2 == 'b':
      opValue2 = B_List
    elif selectedValue2 == 'C' or selectedValue2 == 'c':
      opValue2 = C_List
  
    #DETERMINAR LA OPERACIÓN A REALIZAR
    if option == 'Unión':
      returnedValue = UNION('Unión', opValue1, opValue2)
    elif option == 'Intersección':
      returnedValue = INTERSEC('Intersección', opValue1, opValue2)
    elif option == 'Diferencia':
      returnedValue = DIFERENCIA('Diferencia', opValue1, opValue2)
    elif option == 'Dif. Simétrica':
      returnedValue = SIMDIFER('Diferencia Simétrica', opValue1, opValue2)

    #MOSTRAR EL RESULTADO EN UNA PANTALLA NUEVA
    displayWin = ttk.Toplevel()
    displayWin.geometry('400x260')
    displayWin.config(background='#fbfbfb')
    displayWin.title('Resultado')
    displayWin.resizable(False, False)
    displayWin.iconbitmap('Assets\Iteso_logo.ico')
    operandLabel = ttk.Label(displayWin, font=('Verdana', 14), bg='#fbfbfb', text= f"{selectedValue1.capitalize()} {option} {selectedValue2.capitalize()}").place(x= 148, y=2)
    resultLabel = ttk.Label(displayWin,font=('Verdana', 12), bg='#bfbfbf',  text = f"[{returnedValue}]").place(x = 110, y = 80)

  #FUNCIONES QUE OPERAN, UTILIZAN LOS MISMOS PARÁMETROS Y RETORNAN UNA MISMA VARIABLE
  def UNION(strName, firstList, sndList): #El valor de string es solo para debugs
    finalValue, newList, finalList = '', [], []
    #Crear la nueva lista con los valores
    for i in firstList:
      newList.append(i)
    for i in sndList:
      newList.append(i)

    for item in newList:
      if item not in finalList:
        finalList.append(item)

    finalValue = ", ".join(finalList)
    print(finalList, strName)
    return finalValue #Poder retornar el valor del string final para mostrarlo en una pantalla nueva

  def INTERSEC(strName, firstList, sndList):
    finalValue, newList, finalList = '', [], []
    #Crear la nueva lista con los valores
    for i in firstList:
      for j in sndList:
        if i == j:
          newList.append(i)
    
    for item in newList:
      if item not in finalList:
        finalList.append(item)
    

    #Checar si SÍ hay valores existentes 
    if finalList:
      finalValue = ", ".join(finalList)
    else:
      finalValue = 'NO HAY INTERSECCIÓN'
    

    print(finalList, strName)
    return finalValue #Poder retornar el valor del string final para mostrarlo en una pantalla nueva

  def DIFERENCIA(strName, firstList, sndList):
    finalValue, newList, finalList = '', [], []
    for i in firstList:
      if i in sndList: #Si el número se repite en la segunda lista
        continue
      else:
        newList.append(i)
    
    for item in newList:
      if item not in finalList:
        finalList.append(item)

    #Checar si SÍ hay valores existentes
    if finalList: 
      finalValue = ', '.join(finalList)
    else:
      finalValue = 'NO EXISTE DIFERENCIA'

    print(finalList, strName)
    return finalValue #Poder retornar el valor del string final para mostrarlo en una pantalla nueva

  def SIMDIFER(strName, firstList, sndList):
    finalValue, newList, finalList = '', [], []
    for i in firstList:
      if i in sndList: #Si el número se repite en la segunda lista
        continue
      else:
        newList.append(i)
    for i in sndList: #La diferencia simétrica es la unión de las diferencias (A-B)U(B-A), por lo que se evalúan ambas
      if i in firstList: #Si el número se repite en la primera lista
        continue
      else:
        newList.append(i) #Se unen la diferencia de la primera con la de la segunda
    #Checar si SÍ hay valores existentes
    for item in newList:
      if item not in finalList:
        finalList.append(item)

    if finalList: 
      finalValue = ', '.join(finalList)
    else:
      finalValue = 'NO EXISTE DIFERENCIA SIMÉTRICA'
    print(finalList, strName)
    return finalValue #Poder retornar el valor del string final para mostrarlo en una pantalla nueva


    #Configuración del Top Level
  tdc = ttk.Toplevel()
  tdc.geometry('550x400')
  tdc.config(background='#fbfbfb')
  tdc.title('Teoría de Conjuntos')
  tdc.iconbitmap('Assets\Iteso_logo.ico')
  tdc.resizable(False, False)

#VARIABLES
  defaultValue = ttk.StringVar(tdc)
  defaultValue.set('Opción')
  operands = ['Unión','Intersección', 'Diferencia', 'Dif. Simétrica']
 
    #Entry y Botones

  #//LABELS
  labelA = ttk.Label(tdc, text='Conjunto A = ', bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f').grid(row=0)
  labelB = ttk.Label(tdc, text='Conjunto B = ', bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f').grid(row=1)
  labelC = ttk.Label(tdc, text='Conjunto C = ', bg='#fbfbfb', font=('Verdana', 15), foreground= '#0f0f0f' ).grid(row=2)
  informLabel = ttk.Label(tdc, text='*Introduzca los elementos\nseparados por cómas.\nLea el manual de usuario\nsi no sabe cómo funciona',
  bg='#fbfbfb', font=('Verdana', 8), fg='#0f0f0f').grid(row=0, column=3)

  #ENTRY
  A_Value = ttk.Entry(tdc, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')
  B_Value = ttk.Entry(tdc, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')
  C_Value = ttk.Entry(tdc, bg='#ccc', font=('Verdana',11), fg='#0f0f0f')

  Get_Value1 = ttk.Entry(tdc, bg='#ccc', font=('Verdana',8), fg='#0f0f0f')
  Get_Value2 = ttk.Entry(tdc, bg='#ccc', font=('Verdana',8), fg='#0f0f0f')

  #BOTONES Y OPCIONES
  evaluateButton = ttk.Button(tdc,text='Evaluar', font=('Verdana',11))
  
  opSelector = ttk.OptionMenu(tdc, defaultValue, *operands)

    #Acoplamientos
  A_Value.grid(row=0, column = 2)
  B_Value.grid(row=1, column =2)
  C_Value.grid(row = 2, column =2)
  evaluateButton.place(x=248, y=350)
  opSelector.place(x=235, y = 250)
  Get_Value1.place(x =35, y=250)
  Get_Value2.place(x =370, y=250)

  
  #EVENTOS
  evaluateButton.config(command=getValueFromEntrys)

