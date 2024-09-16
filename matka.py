import random

class matka():


        def __init__(self):
                self.morningPatti = []
                self.eveningPatti = []
                self.open = None
                self.close = None
                self.jodi = None


        def drawMorningPatti(self):

                for i in range(3):
                        n = random.choice([x for x in range(10)])
                        self.morningPatti.append(n)
        
        def drawEveningPatti(self):

                for i in range(3):
                        n = random.choice([x for x in range(10)])
                        self.eveningPatti.append(n)


        def getJodi(self):
                
                if len(self.morningPatti) != 0:
                        mp = sum(self.morningPatti)
                       

                if len(self.eveningPatti) != 0:
                        ep = sum(self.eveningPatti)
                      
                lastDigitMp = str(mp)[-1]
                lastDigitEp = str(ep)[-1]

                jodi = lastDigitMp  + lastDigitEp
                self.jodi = int(jodi)
                

        def reset(self):
                self.morningPatti = []
                self.eveningPatti = []
                self.open = None
                self.close = None
                self.jodi = None


                








