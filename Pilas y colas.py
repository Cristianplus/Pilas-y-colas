"""
Ejercicio
"""

#Pila/Stack (LIFO)

stack = []  #Creación de lista para simular una pila

#Push: añadir elementos a la pila
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

#Pop: eliminar el último elemento añadido
stack_item = stack[len(stack)-1] 
del stack[len(stack)-1] #Eliminamos un elemento dependiendo (-n) de la longitud de la pila
print(stack_item)
print(stack)

print(stack.pop()) #Eliminamos el último elemento añadido
print(stack)

print("--------------------")

#Cola /Queue (FIFO)

queue = []  #Creación de lista para simular una cola

#Añadir elementos a la cola
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
print(queue)

#Eliminar el primer elemento añadido
queue_item = queue[0] 
del queue[0] 
print(queue_item)
print(queue)

print(queue.pop(0))  #Eliminamos el primer elemento añadido
print(queue)

"""
Extra
"""

#Web

def navigation_web():

    stack = []
    
    while True:
        action = input("introduce una url o inserta los comandos 'atras' , 'adelante' o 'salir': ")

        if action == "salir":
            print("Has salido de la navegación web.")
            break
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        elif action == "adelante":
            print("No puedes avanzar, no hay páginas adelante.")
            continue
        else:
            stack.append(action)
        
        if len(stack) > 0:
            print(f"Estás en la página web: https://{stack[len(stack)-1]}")
        else:
            print("Inicio.")

#navigation_web() 

def shared_printed():

    queue = []

    while True:
        action = input("añade un documento o selecciona las opciones 'imprimir' o 'salir': ")

        if action == "salir":
            print("Has terminado con las impresiones.")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"imprimiendo documento: {queue.pop(0)}.pdf")
            else:
                print("No hay documentos disponibles para imprimir.")
        else:
            queue.append(action)

        print(f"Documentos en espera: {queue}")

shared_printed()