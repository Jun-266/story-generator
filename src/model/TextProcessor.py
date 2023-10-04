from src.structures.automaton import Automaton
from src.structures.gramatic import Gramatic
from src.structures.regular_expression import RegularExpression
from src.structures.transducer import Transcuder


class TextProcessor:

    def __init__(self):
        self.df = Automaton()
        self.gr = Gramatic()
        self.gr = RegularExpression()
        self.gr = Transcuder()

    def process_automaton(self):
        df1 = self.df
        if self.df.checkText(""):
            print("Finale reached")
        else:
            print("No reached")
