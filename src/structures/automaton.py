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
            input_symbols={"a","b","c"}, 
            start_state=q0,
            final_states={q4,q7,q9,q10,q11})
        
        df=self.aut
        df.add_transitions([(q0,"a",q1), 
                            (q0,"b",q2), 
                            (q0,"c",q3), 
                            (q1,"a",q4),
                            (q1,"b",q5),
                            (q1,"c",q6),
                            (q2,"a",q7),
                            (q2,"b",q8),
                            (q2,"c",q9),
                            (q3,"a",q10),
                            (q3,"b",q11),
                            (q3,"c",q12),
                            (q5,"a",q13),
                            (q5,"b",q14),
                            (q5,"c",q19),
                            (q6,"a",q13),
                            (q6,"b",q14),
                            (q6,"c",q19),
                            (q8,"a",q15),
                            (q8,"b",q16),
                            (q8,"c",q19),
                            (q12,"a",q17),
                            (q12,"b",q18),
                            (q12,"c",q19)])
        
    def checkText(self,chain):
        return self.aut.accepts(chain)
        

