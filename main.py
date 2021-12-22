from blackjack import BlackJack


def should_hit(player_cards, dealer_card):
    """
    De functie should_hit bepaalt of je nog een kaart wilt krijgen.

    `player_cards` zijn jouw huidige kaarten, bijvoorbeeld ['A', 9]
    (je hebt een Aas en een 9 in je hand). `dealer_card` is de laatst
    getrokken kaart van de dealer voor zijn set kaarten, bijvoorbeeld
    'Q' (de dealer heeft een vrouw).

    Lees verder README.md voor de regels van deze variatie op Blackjack!

    Args:
        player_cards: list[int | str], jouw huidige kaarten
        dealer_card: int | str, de kaart van de dealer

    Returns:
        True als je nog een kaart wilt (hit), False voor passen
    """
    return True


# Simuleer het spel, zet verbose op True om het spelverloop te printen
BlackJack.simulate_games(should_hit, 10000, verbose=False)
