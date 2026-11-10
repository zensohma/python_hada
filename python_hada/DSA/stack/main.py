stack = []

# push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# peek
topElement = stack[-1] # ngambil element paling akhir
print("Peek: ", topElement)

# pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after pop
print("Stack after pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))