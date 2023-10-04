
welcome_message = '¡Bienvenido al programa!'

description = '''
    Este programa sigue la historia de un caballero que busca su princesa perdida.
    Puedes modificar nombres y el flujo de algunos eventos de la historia.
'''


def view_1(name):
    print('Bienvenido ' + name)
    print(description)


def start():
    print(welcome_message)
    name = input('Por favor digita tu nombre: ')
    print()
    view_1(name)
