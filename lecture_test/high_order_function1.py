def greeting(name):
    return lambda  greetings : print(greetings, name)

greet_function = greeting('Tom')
greet_function('What is up, ')
