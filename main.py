from spot_it import SpotIt
from pprint import pprint
from itertools import combinations

order = 7
deck = SpotIt(order)   # make deck of order 7 (contains 57 cards)
print(f"Cards in SPOT-IT deck of order {order}:", deck.cards)
size = 8
stuff = deck.make_tricap_super_capadds(size, True)  # make cap of size 8
cap = stuff[0]
deps = stuff[1]
print(f"\n Example cap of size {len(cap)}:", cap)
print(f"\n Dependencies (card, true sum, false sum):")
pprint(deps)













