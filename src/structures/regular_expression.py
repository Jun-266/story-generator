
import re


class RegularExpression:

    def checkAnswer(chain, chain2):
        return re.search(chain, chain2)



regular_expressions = {
    'yes_or_no': r'((S|s)(I|i|í))|((N|n)(O|o))',
    'path_choice': r'(C|c)amino\s?[123]:?\s?.*',
}
