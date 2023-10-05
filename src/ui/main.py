import re

welcome_message = '¡Bienvenido al programa!'

description = '''
    Este programa sigue la historia de un caballero que busca rescatar a su princesa.
    Puedes modificar nombres y alterar el flujo de algunos eventos de la historia.
'''

yes_options = ['Si', 'si', 'sí', 'Sí', 'SI']
no_options = ['No', 'no', 'NO']

regex = r'((S|s)(I|i|í))|((N|n)(O|o))'


def menu():
    pass


def view_1(name):
    print('Bienvenido ' + name)
    print(description)
    stop = False
    while not stop:
        option = input('¿Te interesa seguir con la aventura?: ')
        match_obj = re.match(regex, option)
        if match_obj is not None:
            my_tuple = match_obj.span()
            f_option = option[my_tuple[0]:my_tuple[1]]
            if f_option in yes_options:
                menu()
            elif f_option in no_options:
                stop = True
                print('Gracias por usar el programa 😊')
            else:
                print('Por favor, escribe una opción valida.')
        else:
            print('Por favor, escribe una opción valida.')


def start():
    print(welcome_message)
    name = input('Por favor digita tu nombre: ')
    print()
    view_1(name)
