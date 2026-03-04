class Dictionary:
    def __init__(self):
        #creo un dizionario vuoto
        self.dict={}

    def addWord(self,alien_word, translation):
        #assegno alla parola aliena contenuta nel dizionario la sua traduzione
        #traduco ma lo tengo per me, l'utente non lo vede
        self.dict[alien_word.lower()] = translation.lower()


    def translate(self,alien_word):
        #gli do la parola aliena e mi restituisce la traduzione
        return self.dict.get(alien_word.lower())


    def translateWordWildCard(self):
        pass