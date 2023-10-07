import unittest
from src.structures.gramatic import Gramatic


class MyTestCase(unittest.TestCase):

    def test_me_gusta(self):
        gr = Gramatic()
        input_1 = 'Me gusta que'
        input_2 = 'Me gusta'
        input_3 = 'Me'
        input_4 = 'mE gusta que la historia...'
        input_5 = 'Me gust aa'
        input_6 = 'Me gustaa que'

        self.assertEqual(gr.checkGramatic(input_1.split()), True)
        self.assertEqual(gr.checkGramatic(input_2.split()), False)
        self.assertEqual(gr.checkGramatic(input_3.split()), False)
        self.assertEqual(gr.checkGramatic(input_4.split()), True)
        self.assertEqual(gr.checkGramatic(input_5.split()), False)
        self.assertEqual(gr.checkGramatic(input_6.split()), False)

    def test_no_gusta(self):
        gr2 = Gramatic()
        input_1 = 'No me gusta que'
        input_2 = 'No me '
        input_3 = 'No'
        input_4 = 'No me gusta los finales'
        input_5 = 'No me gust aa'
        input_6 = 'No me gustaa que'

        self.assertEqual(gr2.checkGramatic(input_1.split()), True)
        self.assertEqual(gr2.checkGramatic(input_2.split()), False)
        self.assertEqual(gr2.checkGramatic(input_3.split()), False)
        self.assertEqual(gr2.checkGramatic(input_4.split()), True)
        self.assertEqual(gr2.checkGramatic(input_5.split()), False)
        self.assertEqual(gr2.checkGramatic(input_6.split()), False)

    def test_multiple_answers(self):
        gr3 = Gramatic()
        input_1 = 'Me guartaria que fuera diferente'
        input_2 = 'Excelente historia'
        input_3 = 'Para nada ma llamó la...'
        input_4 = 'Buena historia'
        input_5 = 'Interesante'
        input_6 = 'Muy buena'

        self.assertEqual(gr3.checkGramatic(input_1.split()), False)
        self.assertEqual(gr3.checkGramatic(input_2.split()), False)
        self.assertEqual(gr3.checkGramatic(input_3.split()), False)
        self.assertEqual(gr3.checkGramatic(input_4.split()), False)
        self.assertEqual(gr3.checkGramatic(input_5.split()), False)
        self.assertEqual(gr3.checkGramatic(input_6.split()), False)


if __name__ == '__main__':
    unittest.main()