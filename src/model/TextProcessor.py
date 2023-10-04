import structures.Automaton as Automaton, structures.Gramatic as Gramatic, structures.RegularExpression as RegularExpression, structures.Transducer as Transducer
class TextProcessor:

    def __init__(self):
        self.df= Automaton()
        self.gr= Gramatic()
        self.gr= RegularExpression()
        self.gr= Transducer()

    def processAutomaton(self):
        df1=self.df
        if(self.df.checkText("")):
            print("Finale reached")
        else:
            print("No reached")


