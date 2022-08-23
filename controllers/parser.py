import nltk

VERB_FORMS = ['VB', 'VBD', 'VBZ', 'VBP', 'VBN', 'VBZ']

class Parser(object):
    def __init__(self):
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        self.generic_error = "Uhm I do not understand. Just tell me what to do."

    def handle_input(self, tagged_words):
        sentence_parts = {}
        for pos in tagged_words:
            sentence_parts[pos[1]] = pos[0]
        print(sentence_parts)

        if sentence_parts.get('PRP'):
            return f"{sentence_parts.get('PRP')} refuses"

        verb = ''
        for form in VERB_FORMS:
            if verb == '':
                verb = sentence_parts.get(form, '')
        print(verb)


    def make_proper(self, user_input):
        user_input = user_input.lower()
        if user_input.split(' ')[0] != 'i':
            user_input = f"i {user_input}"

        return user_input

    def parse_input(self, user_input):
        user_input = self.make_proper(user_input)
        tokens = nltk.word_tokenize(user_input)
        tagged = nltk.pos_tag(tokens)[1:]
        self.handle_input(tagged)

if __name__ == "__main__":
    parser = Parser()
    print(parser.parse_input(input("test> ")))

### DEVLOG; currently theres a bug where if it gets a sentence with 2 nouns itll overwite the Game Object with the second noun
