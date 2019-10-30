name = "everything_trivia"

class Thing:
    def __init__(self, title, link, short_desc, long_desc, tags):
        self.title = title
        self.wikipedia_link = link
        self.short_description = short_desc
        self.long_description = long_desc
        self.tags = {}
    
    def __str__(self):
        output = f'{self.title}: {self.short_description}, {self.long_description}, {self.wikipedia_link}'
        output += '\n' + str(self.tags)

class PublicFigure(Thing):
    def __init__(self, title: str, link: str, short_desc: str, long_desc: str, tags: {}, predcessor = None, successor = None):
        Thing.__init__(self, title, link, short_desc, long_desc, tags)
        self.successor = successor
        self.predcessor = predcessor
