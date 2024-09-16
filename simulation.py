import random
from matka import matka
from tqdm.autonotebook import tqdm # For displaying progress bars while running simulations 


class game: 
    def __init__(self) -> None:
        self.bettingRange = list(range(100))
        self.wins = 0
        self.losses = 0
        self.oddsFor = 90  # Amount won for a correct bet
        self.oddsAgainst = 1  # Amount lost for an incorrect bet
        self.sims = None

    def simulate(self, n):
        self.sims = n
        Matka = matka()
        
        for _ in tqdm(range(n)):
            bet = random.choice(self.bettingRange)
            
            Matka.drawMorningPatti()
            Matka.drawEveningPatti()
            Matka.getJodi()

            if Matka.jodi == bet:
                self.wins += 1
            else:
                self.losses += 1

            Matka.reset()

    def results(self):
        winRate = self.wins / self.sims
        lossRate = self.losses / self.sims
        totalWinnings = self.wins * self.oddsFor
        totalLosses = self.losses * self.oddsAgainst
        returnPerUnit = (totalWinnings - totalLosses) / self.sims

        print(f"""
                win rate: {winRate}
                loss rate: {lossRate}
                total winnings (in unit currency): {totalWinnings}
                total losses (in unit currency): {totalLosses}
                return per unit currency bet: {returnPerUnit}
            """)
if __name__ == '__main__':
    kalyan = game()             # Initializing 'game' object
    kalyan.simulate(1000000)       # Setting the number of simulations
    kalyan.results()            # Displaying the Results






if __name__ == '__main__':

    kalyan = game()             # Initializing 'game' object
    kalyan.simulate(1000000)    # Setting the number of simulations
    kalyan.results()            # Displaying the Results
