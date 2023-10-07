from pyformlang.cfg import CFG


class Gramatic:
    def __init__(self) -> None:
        self.gr = self.initiGramatic()
        
    def initiGramatic(self):
        gr=CFG.from_text("""
             S -> n S | o | B
             B -> m B | e | C 
             C -> g C | u C | s C | t C| a | E
             E -> q E | u E | e""")
        return gr


    def checkGramatic(self, chain):
        if(len(chain)>=3):
            for i in range(3):
                if self.gr.contains(chain[i])!= True:
                    return False
            return True
        else:
            return False
