from _typeshed import Self
from string import punctuation

class Analyser().
    def __init__(self, s):
        for c in punctuation:
            s = s.lower()
            S= s.replace(c, '')
            self.words = s.solit()
    def no_of_words (self):
        return len(self.words)

    def starts with(self, s):
        return len([w for w in self.words
             if w[:len(s)]==s])
    def no_with_length(self, n):
             if len(w)==n])

s = "This is a string to analyse."
analyse = Analyser(s)
print (analyse.words)
print("NUmber of words:", analyse.no_of_words())
print("Number of words starting with 't':",
     analyse.starts_with('t'))
print("Number of 4-letter words:",
     analyse.no_with_length(4))                      
       