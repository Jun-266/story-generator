from src.structures.automaton import Automaton
from src.structures.gramatic import Gramatic
from src.structures.regular_expression import regular_expressions
from src.structures.transducer import replace_name
import re


class TextProcessor:
    state = ""

    def __init__(self):
        self.df = Automaton()
        self.gr = Gramatic()
        self.options = self.create_options()
        self.parts = self.create_parts()
        self.story = ""
        self.state = ""

    def process_automaton(self, selections):
        if self.df.checkText(selections):
            print("Finale reached")
        else:
            print("No reached")

    def create_options(self):
        return {"1": "La Búsqueda en el Bosque Encantado",
                "2": "La Búsqueda en el Castillo Oscuro",
                "3": "La Búsqueda en las Montañas Heladas",
                "11": "Enfrentar al guardián del bosque",
                "12": "Resolver enigma",
                "13": "Ignorar el bosque y buscar pistas en el pueblo",
                "121": "Luchar contra Malachar",
                "122": "Infiltrarse en el escondite",
                "131": "Luchar contra Malachar",
                "132": "Infiltrarse en el escondite",
                "21": "Escapar de las trampas y laberintos que hay en el castillo.",
                "22": "Descifrar los pergaminos antiguos",
                "23": "Luchar contra el mejor sirviente de Malachar.",
                "221": "Luchar contra Malachar",
                "222": "Rescatar a Lady Eleanor a escondidas",
                "31": "Sobrevivir a una tormenta de nieve mortal.",
                "32": "Superar un laberinto de hielo que oculta la guarida de Malachar.",
                "33": "Aliarte con un grupo de nómadas locales",
                "331": "Infiltrarte como sirviente.",
                "332": "Pelear contra Malachar"}

    def create_parts(self):
        return {"1": "Dentro del Bosque Encantado, te encuentras con tres desafíos. ¿Cómo decides abordarlos?",
                "11": '''
                     El guardián mágico resulta ser invencible, y no puedes avanzar.
                     Tu búsqueda en el Bosque Encantado termina en fracaso y desesperanza.
                     ''',
                "12": "Resuelves el enigma antiguo y descubres el escondite de Malachar.",
                "13": "La criatura misteriosa del bosque te guía hasta el escondite de Malachar.",
                "121": "Después de una dura batalla, logras rescatar a Lady Eleanor y regresas juntos a salvo.",
                "122": '''
                     Logras infiltrarte en el castillo y rescatar a Lady Eleanor mientras Malachar está distraído.
                     Escapan juntos y regresan a salvo.
                     ''',
                "131": "Después de una dura batalla, logras rescatar a Lady Eleanor y regresas juntos a salvo.",
                "132": '''
                     Logras infiltrarte en el castillo y rescatar a Lady Eleanor mientras Malachar está distraído.
                     Escapan juntos y regresan a salvo.
                     ''',
                "2": "Decides investigar el Castillo Oscuro, el hogar de Malachar, directamente. ¿Qué haces a "
                     "continuación?",
                "21": "No logras escapar de las trampas. Mueres en una de ellas",
                "22": "Descifras los pergaminos antiguos y encuentras el escondite de Malachar. ",
                "23": "Luchas contra el mejor sirviente de Malachar, pero mueres en el intento",
                "221": "Tras una feroz lucha, rescatas a Lady Eleanor y regresas juntos a salvo.",
                "222": "Rescatas a Lady Eleanor mientras Malachar está distraído.",
                "3": "Decides buscar a Malachar en las peligrosas Montañas Heladas, donde se dice que tiene su "
                     "guarida. ¿Qué acción tomas?",
                "31": "No logras sobrevivir a la tormenta de nieve mortal",
                "32": "No logras superar el laberinto de hielo y mueres por hipotermia",
                "33": "Te alías con los nómadas locales, quienes te guían hasta la guarida de Malachar.",
                "331": "Logras infiltrarte en la guarida y rescatar a Lady Eleanor mientras Malachar está "
                       "distraído." + "\n" + "Escapan juntos y regresan a salvo.",
                "332": "Después de una dura batalla, con ayuda de los nomadas, logras rescatar a Lady Eleanor y "
                       "regresas juntos a salvo."}

    def print_parts(self):
        temp = self.state
        msg = ""
        print(temp)
        if re.match(r"[0-9]?$", temp) is not None:
            for i in range(1, 4):
                temp = temp + str(i)
                msg = msg + "Camino " + str(i) + ": " + self.options[temp] + "\n"
                temp = self.state
        else:
            for i in range(1, 3):
                temp = temp + str(i)
                msg = msg + "Camino " + str(i) + ": " + self.options[temp] + "\n"
                temp = self.state

        return msg

    def develop_story(self, answer):
        ans = answer.split()
        self.state = self.state + ans[1]
        self.story = self.story + self.parts[self.state] + "\n"

    def check_story(self):
        return self.df.checkText(self.state)

    def read_story(self):
        return self.story

    """
    def useTransducer(self,current,new):
        chain={current,new}
        self.story = Transcuder.checkChain(chain,self.story)

        for key, values in self.parts.items:
            self.parts[key] = Transcuder.checkChain(chain,values)
        
        for key, values in self.options.items:
            self.options[key] = Transcuder.checkChain(chain,values)
    """

    def grammar_processor(self, text):
        new_text = text.lower()
        return self.gr.checkGramatic(new_text.split())
