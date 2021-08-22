import random


def pick_Card():
    cards=["Diamond","Spades","Hearts","Clubs"]
    ranks=[2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    card=random.choice(cards)
    rank=random.choice(ranks)
    return(f"The '{rank}' of the '{card}'")

print(pick_Card())