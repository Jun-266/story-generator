from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State


class Automaton:
    def __init__(self):
        self.createAutomaton()
        self.aut = None

    def createAutomaton(self):
        q0=State('q0')
        q1=State('q1')
        q2=State('q2')
        q3=State('q3')
        q4=State('q4')
        q5=State('q5')
        q6=State('q6')
        q7=State('q7')
        q8=State('q8')
        q9=State('q9')
        q10=State('q10')
        q11=State('q11')
        q12=State('q12')
        q13=State('q13')
        q14=State('q14')
        q15=State('q15')
        q16=State('q16')
        q17=State('q17')
        q18=State('q18')
        q19=State('q19')
        self.aut=DeterministicFiniteAutomaton( 
            states={q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19}, 
            input_symbols={"1","2","3"}, 
            start_state=q0,
            final_states={q4,q7,q9,q10,q11})
        
        df=self.aut
        df.add_transitions([(q0,"1",q1), 
                            (q0,"2",q2), 
                            (q0,"3",q3), 
                            (q1,"1",q4),
                            (q1,"2",q5),
                            (q1,"3",q6),
                            (q2,"1",q7),
                            (q2,"2",q8),
                            (q2,"3",q9),
                            (q3,"1",q10),
                            (q3,"2",q11),
                            (q3,"3",q12),
                            (q5,"1",q13),
                            (q5,"2",q14),
                            (q5,"3",q19),
                            (q6,"1",q13),
                            (q6,"2",q14),
                            (q6,"3",q19),
                            (q8,"1",q15),
                            (q8,"2",q16),
                            (q8,"3",q19),
                            (q12,"1",q17),
                            (q12,"2",q18),
                            (q12,"3",q19)])
        
    def checkText(self,chain):
        return self.aut.accepts(chain)
        

