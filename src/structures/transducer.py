from pyformlang.fst import FST

transducer = FST()

my_name = 'Jun'
name_to_r = 'Pepe'
i = 0
transducer.add_start_state('q' + str(i))
while i < len(name_to_r):

    if i < len(my_name):
        transducer.add_transition('q' + str(i), name_to_r[i], 'q' + str((i + 1)), [my_name[i]])
    else:
        transducer.add_transition('q' + str(i), name_to_r[i], 'q' + str((i + 1)), [''])

    i += 1

transducer.add_final_state('q' + str(i))
print(''.join(list(transducer.translate('Pepe'))[0]))







transducer.add_transition('q0', 'a', 'q1', ['x'])
transducer.add_transition('q1', 'a', 'q2', ['x'])
transducer.add_transition('q1', 'b', 'q2', ['y'])
transducer.add_transition('q2', 'a', 'q2', ['x'])
transducer.add_transition('q2', 'b', 'q2', ['y'])
transducer.add_transition('q2', 'b', 'q3', ['y'])

transducer.add_start_state('q0')
transducer.add_final_state('q3')

print(''.join(list(transducer.translate('ababb'))[0]))
