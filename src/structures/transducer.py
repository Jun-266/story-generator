from pyformlang.fst import FST

transducer = FST()


def replace_name(username, name_to_replace):
    i = 0
    transducer.add_start_state('q' + str(i))

    if len(username) < len(name_to_replace):
        while i < len(name_to_replace):

            if i < len(username):
                transducer.add_transition('q' + str(i), name_to_replace[i], 'q' + str((i + 1)),
                                          [username[i]])
            else:
                transducer.add_transition('q' + str(i), name_to_replace[i], 'q' + str((i + 1)),
                                          [''])

            i += 1
    else:
        while i < len(username):

            if i < len(name_to_replace):
                transducer.add_transition('q' + str(i), name_to_replace[i], 'q' + str((i + 1)),
                                          [username[i]])
            else:
                transducer.add_transition('q' + str(i), 'epsilon', 'q' + str((i + 1)),
                                          [username[i]])

            i += 1

    transducer.add_final_state('q' + str(i))

    if len(list(transducer.translate(name_to_replace))[0]) == 0:
        return 'No hay coincidencias'
    else:
        return ''.join(list(transducer.translate(name_to_replace))[0])
