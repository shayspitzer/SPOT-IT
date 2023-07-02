from spot_it import SpotIt

order = 7
Deck = SpotIt(order)   # make deck of order 7 (contains 57 cards)
print(f"Cards in SPOT-IT deck of order {order}:", Deck.cards)
size = 8
cap = Deck.make_tricap(size)  # make cap of at most size 8
print(f"Example cap of size {len(cap)}:", cap)

