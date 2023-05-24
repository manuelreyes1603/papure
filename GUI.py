from tkinter import *
import tkinter as tk
from MatrizNumpy import *

root = Tk()
root.title("Calculadora de Matrices")
root.geometry('450x600')
root.minsize(width ="450", height = "600")
root.maxsize(width ="600", height = "900")
root.configure(bg = "wheat")
matriz1 = []
matriz2 = []
scalar = 0

#------------Funciones------------#
def reiniciar_programa():
    '''
    Función que rompe el programa y crea uno nuevo
    Params:
    Returns:
    '''
    # Destruir la ventana principal
    root.destroy()

    # Crear una nueva ventana
    crear_ventana()

def crear_ventana():
    '''
    Función que regenera todo el código en caso de reiniciar
    Params:
    Returns:
    '''
    global root
    global opcion_seleccionada2
    global matriz1, matriz2
    root = Tk()
    root.title("Calculadora de Matrices")
    root.geometry('450x600')
    root.minsize(width ="450", height = "600")
    root.maxsize(width ="600", height = "900")
    root.configure(bg = "wheat")

    matriz1 = []
    matriz2 = []

    opcion_seleccionada2 = IntVar()

    #Texto selecciona una operación                 
    cuadro2 = LabelFrame(root, bg = "wheat", text= "Selecciona un Método")
    cuadro2.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)
    #Botones para nuestras operaciones (solo se selecciona uno) row 8-10
    opcion_opera1 = tk.Radiobutton(cuadro2, text= "Suma", bg = "wheat", variable = opcion_seleccionada2,value = 1)
    opcion_opera1.grid(column = 0, row = 0, sticky = W, padx = 6, pady = 5)
    opcion_opera2 = tk.Radiobutton(cuadro2, text= "Multiplicar por Escalar", bg = "wheat", variable = opcion_seleccionada2,value = 2)
    opcion_opera2.grid(column = 1, row = 0, sticky = W, padx = 6, pady = 5)
    opcion_opera3 = tk.Radiobutton(cuadro2, text= "Mínimo", bg = "wheat", variable = opcion_seleccionada2,value = 3)
    opcion_opera3.grid(column = 0, row = 1, sticky = W, padx = 6, pady = 5)
    opcion_opera4 = tk.Radiobutton(cuadro2, text= "Inversa", bg = "wheat", variable = opcion_seleccionada2,value = 4)
    opcion_opera4.grid(column = 1, row = 1, sticky = W, padx = 6, pady = 5)
    opcion_opera5 = tk.Radiobutton(cuadro2, text= "Determinante", bg = "wheat", variable = opcion_seleccionada2,value = 5)
    opcion_opera5.grid(column = 0, row = 2, sticky = W, padx = 6, pady = 5)
    opcion_opera6 = tk.Radiobutton(cuadro2, text= "Transpuesta", bg = "wheat", variable = opcion_seleccionada2,value = 6)
    opcion_opera6.grid(column = 1, row = 2, sticky = W, padx = 6, pady = 5)
    operacionelegido_Button = Button(root, text = 'Siguiente', command = operacion)
    operacionelegido_Button.grid(column = 0, row = 3, sticky = W, padx = 6, pady = 5)

    otra_matriz_Button = Button(root, text = 'Salir', command = quit)
    otra_matriz_Button.grid(column = 0, row = 15, sticky = N, padx = 5, pady = 5)


    boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar_programa)
    boton_reiniciar.grid(column = 1, row = 15, sticky = W, padx = 5, pady = 5)



#Operacion elegida
def operacion():
    '''
    Función que almacena los datos de los tkinter.Entry de las matrices
    Params:
    Returns:
    '''
    elegido = opcion_seleccionada2.get()
    if elegido not in range(1,7):
        return

    calcular= Button(root, text = 'Calcular', command = calcula)
    calcular.grid(column = 0, row = 8, sticky = W, padx = 5, pady = 5)

    if elegido == 1:
        crearmatriz1()
        crearmatriz2()
    elif elegido == 2:
        crearmatriz1()
        crearescalar()
    else:
        crearmatriz1()

def imprimir_resultado(resultado:object):
    '''
    Función que imprime el resultado obtenido del método elegido
    Params:
    resultado = object
    Returns:
    '''
    frame1 = Frame(root)
    frame1.grid(column = 0, row = 9, padx = 10, pady = 10)
    dimension = resultado.setdi()

    for i in range(dimension[0]):
        for j in range(dimension[1]):
            salida = Label(frame1, width = 5, text = resultado.get()[i][j])
            salida.grid(column = j, row = i)

def calcula():
    '''
    Función que detecta la opción elegida, genera la matriz NxM con las entradas deseadas
    Params:
    Returns:
    '''
    elegido = opcion_seleccionada2.get()

    if len(matriz1) != 0:
        for i, renglon in enumerate(matriz1):
            for j, columna in enumerate(renglon):
                matriz1[i][j] = int(matriz1[i][j].get() )

    if len(matriz2) != 0:
        for i, renglon in enumerate(matriz2):
            for j, columna in enumerate(renglon):
                matriz2[i][j] = int(matriz2[i][j].get())

    matriz1_np = MatrizNumpy(matriz1)

    if elegido == 1:
        matriz2_np = MatrizNumpy(matriz2)

        if matriz1_np.setdi()[0] != matriz2_np.setdi()[0] or matriz1_np.setdi()[1] != matriz2_np.setdi()[1]:
            frame = Frame(root, bg = "red")
            frame.grid(column = 0, row = 9, padx = 10, pady = 10)

            error_label = Label(frame, text = "Error: Matrices de dimensiones distintas") 
            error_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)
        else:
            resultado = matriz1_np.suma(matriz2_np)

    elif elegido == 2:
        resultado = matriz1_np.prod_escalar(scalar)
    elif elegido == 3:
        resultado = MatrizNumpy([[matriz1_np.minimo().tolist()]])
    elif elegido == 4:
        if matriz1_np.setdi()[0] != matriz1_np.setdi()[1]:
            frame = Frame(root, bg = "red")
            frame.grid(column = 0, row = 9, padx = 10, pady = 10)

            error_label = Label(frame, text = f"Error: No es una matriz cuadrada") 
            error_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)            
        elif matriz1_np.determinante().tolist() == 0:
            frame = Frame(root, bg = "red")
            frame.grid(column = 0, row = 9, padx = 10, pady = 10)

            error_label = Label(frame, text = f"Error: La determinante de la matriz es {0}, por tanto, no existe la inversa") 
            error_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)
        
        else:
            resultado = matriz1_np.inversa()
    elif elegido == 5:
        if matriz1_np.setdi()[0] != matriz1_np.setdi()[1]:
            frame = Frame(root, bg = "red")
            frame.grid(column = 0, row = 9, padx = 10, pady = 10)

            error_label = Label(frame, text = f"Error: No es una matriz cuadrada") 
            error_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)   
        else:
            resultado = MatrizNumpy([[matriz1_np.determinante().tolist()]])
    elif elegido == 6:
        resultado = matriz1_np.transpuesta()

    try: 
        imprimir_resultado(resultado)
    except:
        return

def crearescalar():
    ''''
    Función que crea el espacio para clickear el guardado del escalar deseado
    Params:
    Returns:
    '''
    frame = Frame(root, bg = "wheat")
    frame.grid(column = 0, row = 6, padx = 10, pady = 10)

    escalar_label = Label(frame,text="Ingrese el Escalar:", bg = "wheat") 
    escalar_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)

    escalar_entry = Entry(frame)
    escalar_entry.grid(column = 1, row = 0, sticky = W, pady = 5)

    escalar_Button = Button(frame, text = 'Subir Escalar', command = lambda: obten_escalar(escalar_entry.get()))
    escalar_Button.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

def obten_escalar(escalar):
    '''
    Función que actualiza el escalar del tkinter por un entero int
    Params:
    escalar = object
    Returns:
    '''
    global scalar
    scalar = int(escalar)

def crearmatriz1():
    '''
    Crea el espacio para introducir la dimensión de la matriz 1 junto con su botón de guardado
    Params:
    Returns:
    '''
    frame = Frame(root, bg = "wheat")
    frame.grid(column = 0, row = 4, padx = 10, pady = 10)

    tamaño_matriz_label = Label(frame,text="Ingrese el Tamaño de la Matriz 1 (mxn):", bg = "wheat") 
    tamaño_matriz_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)

    tamaño_matriz_entry = Entry(frame)
    tamaño_matriz_entry.grid(column = 1, row = 0, sticky = W, pady = 5)

    agregar_matriz1_Button = Button(frame, text = 'Subir Matriz', command = lambda: muestramatriz1(tamaño_matriz_entry.get()))
    agregar_matriz1_Button.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

def muestramatriz1(tamaño_matriz):
    '''
    Función que crea los espacios para introducir los elementos de la matriz, además, guarda los object tk.entry en una lista
    Params:
    tamaño_matriz = str
    Returns:
    '''
    frame = Frame(root)
    frame.grid(column = 0, row = 5, padx = 10, pady = 10)
    dimension1 = tamaño_matriz.split('x')

    for i in range(int(dimension1[0])):
        sub = []
        for j in range(int(dimension1[1])):
            entrada = Entry(frame, width = 5)
            entrada.grid(column = j, row = i)
            sub.append(entrada)
        matriz1.append(sub)
    


def crearmatriz2():
    '''
    Crea el espacio para introducir la dimensión de la matriz 2 junto con su botón de guardado
    Params:
    Returns:
    '''
    frame = Frame(root, bg = "wheat")
    frame.grid(column = 0, row = 6, padx = 10, pady = 10)

    tamaño_matriz_label = Label(frame,text="Ingrese el Tamaño de la Matriz 2 (mxn):", bg = "wheat") 
    tamaño_matriz_label.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)

    tamaño_matriz_entry = Entry(frame)
    tamaño_matriz_entry.grid(column = 1, row = 0, sticky = W, pady = 5)

    agregar_matriz2_Button = Button(frame, text = 'Subir Matriz', command = lambda: muestramatriz2(tamaño_matriz_entry.get()))
    agregar_matriz2_Button.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

def muestramatriz2(tamaño_matriz):
    '''
    Función que crea los espacios para introducir los elementos de la matriz, además, guarda los object tk.entry en una lista
    Params:
    tamaño_matriz = str
    Returns:
    '''
    frame = Frame(root)
    frame.grid(column = 0, row = 7, padx = 10, pady = 10)
    dimension2 = tamaño_matriz.split('x')

    for i in range(int(dimension2[0])):
        sub = []
        for j in range(int(dimension2[1])):
            entrada = Entry(frame, width = 5)
            entrada.grid(column = j, row = i)
            sub.append(entrada)
        matriz2.append(sub)


#-----------Interfaz-----------#
#Variable donde se guarda la opción de método elegida
opcion_seleccionada2 = IntVar()

#Texto selecciona una operación                 
cuadro2 = LabelFrame(root, bg = "wheat", text= "Selecciona un Método")
cuadro2.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)
#Botones para nuestras operaciones (solo se selecciona uno) row 8-10
opcion_opera1 = tk.Radiobutton(cuadro2, text= "Suma", bg = "wheat", variable = opcion_seleccionada2,value = 1)
opcion_opera1.grid(column = 0, row = 0, sticky = W, padx = 6, pady = 5)
opcion_opera2 = tk.Radiobutton(cuadro2, text= "Multiplicar por Escalar", bg = "wheat", variable = opcion_seleccionada2,value = 2)
opcion_opera2.grid(column = 1, row = 0, sticky = W, padx = 6, pady = 5)
opcion_opera3 = tk.Radiobutton(cuadro2, text= "Mínimo", bg = "wheat", variable = opcion_seleccionada2,value = 3)
opcion_opera3.grid(column = 0, row = 1, sticky = W, padx = 6, pady = 5)
opcion_opera4 = tk.Radiobutton(cuadro2, text= "Inversa", bg = "wheat", variable = opcion_seleccionada2,value = 4)
opcion_opera4.grid(column = 1, row = 1, sticky = W, padx = 6, pady = 5)
opcion_opera5 = tk.Radiobutton(cuadro2, text= "Determinante", bg = "wheat", variable = opcion_seleccionada2,value = 5)
opcion_opera5.grid(column = 0, row = 2, sticky = W, padx = 6, pady = 5)
opcion_opera6 = tk.Radiobutton(cuadro2, text= "Transpuesta", bg = "wheat", variable = opcion_seleccionada2,value = 6)
opcion_opera6.grid(column = 1, row = 2, sticky = W, padx = 6, pady = 5)
operacionelegido_Button = Button(root, text = 'Siguiente', command = operacion)
operacionelegido_Button.grid(column = 0, row = 3, sticky = W, padx = 6, pady = 5)

otra_matriz_Button = Button(root, text = 'Salir', command = quit)
otra_matriz_Button.grid(column = 0, row = 15, sticky = N, padx = 5, pady = 5)


boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar_programa)
boton_reiniciar.grid(column = 1, row = 15, sticky = W, padx = 5, pady = 5)

root.mainloop()