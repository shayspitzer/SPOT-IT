from spot_it import SpotIt

order = 7
Deck = SpotIt(order)
print(f"Cards in SPOT-IT deck of order {order}:", Deck.cards)
size = 8
cap = Deck.make_tricap(size)
print(f"Example cap of size {len(cap)}:", cap)
