todo=[]

def doSomething(tasks):
    todo.append(tasks)
    print("Added tasks "+tasks)

def printTodo(todo):
    print("todo list: ")
    i=1
    for task in todo:
        print(i,task)
        i+=1
        
def deleteSomething(todo,num):
    todo.pop(num)
    print("deleting something")
        
doSomething("buy milk")
doSomething("buy car")
doSomething("buy house")
doSomething("buy tank")

printTodo(todo)
deleteSomething(todo,1)
printTodo(todo)