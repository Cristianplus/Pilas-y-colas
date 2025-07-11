"""
Ejercicio
"""

#Pila/Stack (LIFO)

stack = []

#Push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

#Pop
stack_item = stack[len(stack)-1]
print(stack_item)
print(stack)