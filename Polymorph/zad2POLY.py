class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        if not self.words:
            self.words.append(word)
        else:
            if len(' '.join(self.words + [word])) <= self.width:
                self.words.append(word)
            else:
                print(' '.join(self.words))
                self.words = [word]
    def end(self):
        if self.words:
            print(' '.join(self.words))
            self.words = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        if not self.words:
            self.words.append(word)
        else:
            if len(' '.join(self.words + [word])) <= self.width:
                self.words.append(word)
            else:
                line = ' '.join(self.words)
                print(line.rjust(self.width))
                self.words = [word]
    def end(self):
        if self.words:
            line = ' '.join(self.words)
            print(line.rjust(self.width))
            self.words = []
# Ваш код

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
