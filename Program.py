import random
from collections import defaultdict

class MarkovTextGenerator:
    def __init__(self, text, order=2):
        self.text = text
        self.order = order
        self.ngrams = defaultdict(list)
        self.build_ngrams()

    def build_ngrams(self):
        words = self.text.split()
        for i in range(len(words) - self.order):
            ngram = tuple(words[i:i + self.order])
            self.ngrams[ngram].append(words[i + self.order])

    def generate_text(self, length):
        current_ngram = random.choice(list(self.ngrams.keys()))
        generated_text = ' '.join(current_ngram)
        for i in range(length - self.order):
            next_word = random.choice(self.ngrams[current_ngram])
            generated_text += ' ' + next_word
            current_ngram = tuple(generated_text.split()[-self.order:])
        return generated_text

text = "This is an example of a Markov text generator. It is written in Python."
gen = MarkovTextGenerator(text)
print(gen.generate_text(10))
