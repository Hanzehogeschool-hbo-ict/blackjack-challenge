# DIT BESTAND HOEFT NIET TE WORDEN AANGEPAST,
# dit is de blackjack simulator.
# pas het bestand main.py

# reused and refactored from https://www.kaggle.com/alexisbcook/blackjack-microchallenge
import random


class BlackJack:
    def __init__(self, player_agent, verbose=False):
        self.phit = player_agent
        # Backwards compatibility with old call signature of should_hit
        self.verbose = verbose
        self.player_cards = []
        self.dealer_cards = []

    @staticmethod
    def simulate_games(hit_function, nr_of_games, verbose=False):
        blackjack = BlackJack(hit_function, verbose=verbose)
        dealer_wins = 0
        player_wins = 0

        for i in range(0, nr_of_games):
            if blackjack.play() > 0:
                player_wins += 1
            else:
                dealer_wins += 1

        percentage_player_wins = int((player_wins / nr_of_games) * 100)
        print(f"Player wins: {percentage_player_wins} %")
        print(f"Dealer wins: {100-percentage_player_wins} %")

    @staticmethod
    def deal():
        return random.choice(list(range(2, 11)) + ["A", "J", "Q", "K"])

    def log(self, msg):
        if self.verbose:
            print(msg)

    @property
    def player_total(self):
        return self.card_total(self.player_cards)

    @property
    def dealer_total(self):
        return self.card_total(self.dealer_cards)

    @staticmethod
    def card_total(cards, ace_counts=False):
        tot = 0
        aces = 0
        for c in cards:
            if c == "A":
                aces += 1
            elif c in list("JQK"):
                tot += 10
            else:
                tot += c
        # tot is now the total of non-ace cards
        tot = tot + aces
        # tot is now the smallest possible total
        # Looping here isn't strictly necessary because we'll never count more
        # than one ace as high. But hey, we're future-proofed in case we ever
        # want to implement 31.
        high_aces = 0
        for _ in range(aces):
            if (tot + 10) <= 21:
                tot += 10
                high_aces += 1
        if ace_counts:
            return tot, (aces - high_aces), high_aces
        return tot

    def player_hits(self):
        return self.phit(self.player_cards, self.dealer_cards[0])

    def play(self):
        self.player_cards = [self.deal(), self.deal()]
        self.log(f"Speler start met {self.player_cards} (totaal = {self.player_total})")
        self.dealer_cards = [self.deal()]
        self.log(f"Dealer start met {self.dealer_cards}")

        self.log("\n__Spelers beurt__\n")
        while self.player_hits():
            self.player_cards.append(self.deal())
            self.log(
                f"Speler vraagt een kaart en krijgt {self.player_cards[-1]}. (totaal = {self.player_total})"
            )
            if self.player_total > 21:
                self.log("De speler is dood! De dealer wint.")
                return -1
        self.log("De speler past")

        self.log("\n__Dealers beurt__\n")
        while True:
            self.dealer_cards.append(self.deal())
            self.log(
                f"Dealer vraagt een kaart en krijgt {self.dealer_cards[-1]}. (totaal = {self.dealer_total})"
            )
            if self.dealer_total > 21:
                self.log("De dealer is dood! De speler wint.")
                return 1
            # Stand on 17
            elif self.dealer_total >= 17:
                self.log("De dealer past.")
                if self.dealer_total >= self.player_total:
                    self.log(
                        "De dealer wint. {} >= {}".format(
                            self.dealer_total,
                            self.player_total,
                        )
                    )
                    return -1
                else:
                    self.log(
                        "De speler wint. {} > {}".format(
                            self.player_total,
                            self.dealer_total,
                        )
                    )
                    return 1
