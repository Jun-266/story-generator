story_description = '''
    Historia: El Caballero y el Rescate de su Amada
    Eres Sir William, un valiente caballero en busca de su amada, Lady Eleanor, 
    quien ha sido secuestrada por un malvado mago llamado Malachar. 
    Tu misión es rescatarla y devolverla a salvo a tu lado. 
    Tienes tres caminos por delante:
'''

path_1 = ['Camino 1', 'camino 1', 'Camino1', 'camino1', 'Camino 1:', 'camino 1:']
path_2 = ['Camino 2', 'camino 2', 'Camino2', 'camino2', 'Camino 2:', 'camino 2:']
path_3 = ['Camino 3', 'camino 3', 'Camino3', 'camino3', 'Camino 3:', 'camino 3:']

choices = {}

import re
my_string = 'No'
regex = r'(N|n)(O|o)'
match_object = re.match(regex, my_string)
# print(match_object)
# match_object = re.search(regex, my_string)
# my_tuple = match_object.span()
# print(match_object)
# print(my_string[my_tuple[0]:my_tuple[1]])
