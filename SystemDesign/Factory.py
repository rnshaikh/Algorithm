class FrenchLocalizer:
    
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
                             
    
    def localize(self, msg):
        return self.translations.get(msg, msg)
        

class SpanishLocalizer:
    
    def __init__(self):
        self.translations =  {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
                             
    def localize(self, msg):
        return self.translations.get(msg, msg)
                             

class EnglishLocalizer:
    
    def __init__(self):
        pass
    
    def localize(self, msg):
        return msg
        
        
def factory(language="english"):
    localizer = {
        "english": EnglishLocalizer,
        "spanish": SpanishLocalizer,
        "french": FrenchLocalizer
    } 
    return localizer[language]()
        


e = factory("english")
s = factory("spanish")
f = factory("french")

msges= ["car", "bike", "cycle"]

for msg in msges:
    print(e.localize(msg))
    print(s.localize(msg))
    print(f.localize(msg))
