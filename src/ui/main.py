import re
from model.story import story_description
from model.story import path_1, path_2, path_3
from model.TextProcessor import TextProcessor

welcome_message = '¡Bienvenido al programa!'

description = '''
    Este programa sigue la historia de un caballero que busca rescatar a su princesa.
    Puedes modificar nombres y alterar el flujo de algunos eventos de la historia.
'''

yes_options = ['Si', 'si', 'sí', 'Sí', 'SI']
no_options = ['No', 'no', 'NO']

regex = r'((S|s)(I|i|í))|((N|n)(O|o))'
regex_path = r'(C|c)amino\s?[123]:?\s?.*'
regex_opt=r'[1|2]{1}'


def view_2():
    print('Antes de continuar...')
    stop = False
    while not stop:
        option = input('¿Quieres ser el caballero de esta historia?: ')
        match_obj = re.match(regex, option)
        if match_obj is not None:
            my_tuple = match_obj.span()
            f_option = option[my_tuple[0]:my_tuple[1]]
            if f_option in yes_options:
                pass
            elif f_option in no_options:
                stop = True
                print('De acuerdo. Continuemos...')
            else:
                print('Por favor, escribe una opción valida.')
        else:
            print('Por favor, escribe una opción valida.')

    print(story_description)
    stop = False
    while not stop:
        print(TextProcessor.printParts())
        option = input('¿Cuál camino deseas elegir?(Ej: Camino 1): ')
        match_obj = re.match(regex_path, option)
        if match_obj is not None:
            my_tuple = match_obj.span()
            f_option = option[my_tuple[0]:my_tuple[1]]
            if f_option in path_1|path_2|path_3:
                TextProcessor.developStory(f_option)  
            else:
                print('Por favor, escribe una opción valida.')
        else:
            print('Por favor, escribe una opción valida.')

        conti=False
        while not conti:
            option = input('''
                        Opciones de configuración de las historia:
                        1. Leer historia
                        2. Cambiar nombre de personajes
                        ''')
        
            if re.match(regex_opt, option) is not None:
                if option == 1:
                    print(TextProcessor.readStory())
                else:
                    current=input('Digite el nombre actual del personaj')
                    new=input('Digite el nuevo nombre')
                    TextProcessor.useTransducer(current,new)
                
                conti=True
            else:
                print('Esta entrada no es valida')
        
        if TextProcessor.checkStory():
            stop = True


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
                view_2()
            elif f_option in no_options:
                stop = True
                option = input('¿Quieres agregar algún comentario')
                match_obj = re.match(regex, option)
                if match_obj is not None:
                    my_tuple = match_obj.span()
                    f_option = option[my_tuple[0]:my_tuple[1]]
                    if f_option in yes_options:
                        conti = False
                        while not conti:
                            suggestion = input('Escriberlo en estos formatos: (Me gustaría que...) o (No me gustó...)')
                            if TextProcessor.grammarProcessor(suggestion):
                                print('Gracias por la sugerencia')
                            else:
                                print('La entrada es inválida')

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
