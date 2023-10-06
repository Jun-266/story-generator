import re
import unittest
from src.structures.regular_expression import regular_expressions
from src.ui.main import yes_options, no_options


class MyTestCase(unittest.TestCase):

    def test_yes_option(self):
        re_for_yes = regular_expressions['yes_or_no']
        input_1 = 'Si me gustaría continuar la historia'
        input_2 = 'si quiero continuar con la historia.'
        input_3 = 'Si, estoy de acuerdo'
        input_4 = 'siiiiiiiiiiiii'
        input_5 = 'Sí mi loco'
        input_6 = 'sí, está bien'
        input_7 = 'SI VOY A CONTINUAR'

        match_obj_1 = re.match(re_for_yes, input_1)
        match_obj_2 = re.match(re_for_yes, input_2)
        match_obj_3 = re.match(re_for_yes, input_3)
        match_obj_4 = re.match(re_for_yes, input_4)
        match_obj_5 = re.match(re_for_yes, input_5)
        match_obj_6 = re.match(re_for_yes, input_6)
        match_obj_7 = re.match(re_for_yes, input_7)

        my_tp_1 = match_obj_1.span()
        my_tp_2 = match_obj_2.span()
        my_tp_3 = match_obj_3.span()
        my_tp_4 = match_obj_4.span()
        my_tp_5 = match_obj_5.span()
        my_tp_6 = match_obj_6.span()
        my_tp_7 = match_obj_7.span()

        process_str_1 = input_1[my_tp_1[0]: my_tp_1[1]]
        process_str_2 = input_2[my_tp_2[0]: my_tp_2[1]]
        process_str_3 = input_3[my_tp_3[0]: my_tp_3[1]]
        process_str_4 = input_4[my_tp_4[0]: my_tp_4[1]]
        process_str_5 = input_5[my_tp_5[0]: my_tp_5[1]]
        process_str_6 = input_6[my_tp_6[0]: my_tp_6[1]]
        process_str_7 = input_7[my_tp_7[0]: my_tp_7[1]]

        self.assertEqual(process_str_1 in yes_options, True)
        self.assertEqual(process_str_2 in yes_options, True)
        self.assertEqual(process_str_3 in yes_options, True)
        self.assertEqual(process_str_4 in yes_options, True)
        self.assertEqual(process_str_5 in yes_options, True)
        self.assertEqual(process_str_6 in yes_options, True)
        self.assertEqual(process_str_7 in yes_options, True)

    def test_no_option(self):
        re_for_no = regular_expressions['yes_or_no']
        input_1 = 'no me gustaría continuar la historia'
        input_2 = 'No quiero continuar con la historia.'
        input_3 = 'NO estoy de acuerdo'
        input_4 = 'nooooooooooooo'
        input_5 = 'No, no voy a continuar'
        input_6 = 'no me parece bien'
        input_7 = 'NO VOY A SEGUIR'

        match_obj_1 = re.match(re_for_no, input_1)
        match_obj_2 = re.match(re_for_no, input_2)
        match_obj_3 = re.match(re_for_no, input_3)
        match_obj_4 = re.match(re_for_no, input_4)
        match_obj_5 = re.match(re_for_no, input_5)
        match_obj_6 = re.match(re_for_no, input_6)
        match_obj_7 = re.match(re_for_no, input_7)

        my_tp_1 = match_obj_1.span()
        my_tp_2 = match_obj_2.span()
        my_tp_3 = match_obj_3.span()
        my_tp_4 = match_obj_4.span()
        my_tp_5 = match_obj_5.span()
        my_tp_6 = match_obj_6.span()
        my_tp_7 = match_obj_7.span()

        process_str_1 = input_1[my_tp_1[0]: my_tp_1[1]]
        process_str_2 = input_2[my_tp_2[0]: my_tp_2[1]]
        process_str_3 = input_3[my_tp_3[0]: my_tp_3[1]]
        process_str_4 = input_4[my_tp_4[0]: my_tp_4[1]]
        process_str_5 = input_5[my_tp_5[0]: my_tp_5[1]]
        process_str_6 = input_6[my_tp_6[0]: my_tp_6[1]]
        process_str_7 = input_7[my_tp_7[0]: my_tp_7[1]]

        self.assertEqual(process_str_1 in no_options, True)
        self.assertEqual(process_str_2 in no_options, True)
        self.assertEqual(process_str_3 in no_options, True)
        self.assertEqual(process_str_4 in no_options, True)
        self.assertEqual(process_str_5 in no_options, True)
        self.assertEqual(process_str_6 in no_options, True)
        self.assertEqual(process_str_7 in no_options, True)


if __name__ == '__main__':
    unittest.main()
