import re
from src.model.story import story_description, story, knight, lady, villain
from src.model.story import path_1_opt, path_2_opt, path_3_opt
from src.structures.transducer import replace_name
from src.model.text_processor import TextProcessor

welcome_message = '¡Bienvenido al programa!'


description = '''
    Este programa sigue la historia de un caballero que busca rescatar a su princesa.
    Puedes modificar nombres y alterar el flujo de algunos eventos de la historia.
'''

yes_options = ['Si', 'si', 'sí', 'Sí', 'SI']
no_options = ['No', 'no', 'NO']

regex = r'((S|s)(I|i|í))|((N|n)(O|o))'
regex_path = r'(C|c)amino\s?[123]:?\s?.*'
regex_opt = r'1{1}|2{1}'


def view_2(txtp, name):
    print('Antes de continuar...')
    
    stop = False
    while not stop:
        option = input('¿Quieres ser el caballero de esta historia?: ')
        match_obj = re.match(regex, option)
        if match_obj is not None:
            my_tuple = match_obj.span()
            f_option = option[my_tuple[0]:my_tuple[1]]
            if f_option in yes_options:
                r_name = replace_name(name, knight)
                new_story = story.format(r_name, lady, villain)
                print(new_story)
                stop = True
            elif f_option in no_options:
                stop = True
                print(story_description)
                print('De acuerdo. Continuemos...')
            else:
                print('Por favor, escribe una opción valida.')
        else:
            print('Por favor, escribe una opción valida.')

    stop = False
    while not stop:
        next = False
        while not next:
            print(txtp.print_parts())
            option = input('¿Cuál camino deseas elegir?(Ej: Camino 1): ')
            match_obj = re.match(regex_path, option)
            if match_obj is not None:
                my_tuple = match_obj.span()
                f_option = option[my_tuple[0]:my_tuple[1]]
                if f_option in path_1_opt:
                    next = True
                    txtp.develop_story(f_option)
                elif f_option in path_2_opt:
                    next = True
                    txtp.develop_story(f_option)
                elif f_option in path_3_opt:
                    next = True
                    txtp.develop_story(f_option)
                else:
                    print('Por favor, escribe una opción valida.')
            else:
                print('Por favor, escribe una opción valida.')

        print(txtp.read_story())
        
        if txtp.check_story():
            stop = True


def view_1(name):
    print('Bienvenido ' + name)
    print(description)
    stop = False
    while not stop:
        txtp = TextProcessor()
        option = input('¿Te interesa seguir con la aventura?: ')
        match_obj = re.match(regex, option)
        if match_obj is not None:
            my_tuple = match_obj.span()
            f_option = option[my_tuple[0]:my_tuple[1]]

            if f_option in yes_options:
                view_2(txtp, name)
            elif f_option in no_options:
                stop = True
                option = input('¿Quieres agregar algún comentario? ')
                match_obj = re.match(regex, option)

                if match_obj is not None:
                    my_tuple = match_obj.span()
                    f_option = option[my_tuple[0]:my_tuple[1]]

                    if f_option in yes_options:
                        conti = False

                        while not conti:
                            suggestion = input('Escribelo en estos formatos: (Me gusta que...) o (No me gusta...)')

                            if txtp.grammar_processor(suggestion):
                                print('Gracias por la sugerencia')
                                conti = True
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
