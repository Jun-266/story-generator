from pyformlang.fst import FST
class Transcuder:
    def __init__(self):
        self.tr=FST()
    

    def checkChain(self,chainA,story):
        self.tr.add_transition([('q0',chainA[0],'q1',[chainA[1]])])
        story = "".join(list(self.tr.translate(story))[0])
        return story
