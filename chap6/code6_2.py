import random

top = -1
stack = []

def push(data) :
    top += 1
    stack[top] = data

def pop(data) :
    top -=1
    stack[top] = data

def printStack(stack) :
    for str in stack :
        print(f'{str} >>', end=' ')

stackAry = ['orange','green','blue','purple','red','yello']
random.shuffle(stackAry)

printStack(stackAry)


