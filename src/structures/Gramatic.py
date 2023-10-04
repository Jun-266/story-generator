from pyformlang.cfg import CFG
class Gramatic:
    def __init__(self) -> None:
        self.gr=None
        self.initiGramatic()

    
    def initiGramatic(self):
        self.gr=CFG.from_text("""
            S -> NP VP
            NP -> Det N
            Det -> el | la | un | una
            N -> caballero | princesa | dragón | castillo
            VP -> V NP
            V -> salvó | atacó | mató | escapó""")
    
    def checkGramatic(self, chain):
        return self.gr.contains(chain)
