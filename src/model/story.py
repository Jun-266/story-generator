story_part1 = '''
    Historia: El Caballero y el Rescate de su Amada
    Eres Sir William, un valiente caballero en busca de su amada, Lady Eleanor, 
    quien ha sido secuestrada por un malvado mago llamado Malachar. 
    Tu misión es rescatarla y devolverla a salvo a tu lado. 
    Tienes tres caminos por delante:
'''

choices = {}

import re
my_string = 'No'
regex = r'(N|n)(O|o)'
match_object = re.match(regex, my_string)
print(match_object)
# match_object = re.search(regex, my_string)
# my_tuple = match_object.span()
# print(match_object)
# print(my_string[my_tuple[0]:my_tuple[1]])
