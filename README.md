# SPOT-IT
Shay Spitzer
shay.spitzer@gmail.com

The class SpotIt is designed to generate SPOT-IT decks of prime order n. SPOT-IT decks consist of
n ** 2 + n + 1 symbols (symbols are integers here) across n ** 2 + n + 1 cards that satisfy the following axioms:
1. Each symbol appears on n + 1 cards
2. Each card contains n + 1 symbols
3. Each pair of cards share exactly 1 symbol
If we view cards as lines and symbols as points, note that these axioms describe a finite projective plane of order n.

The class SpotIt permutes the symbols in such a way that the axioms are met. Though there is likely a more efficient way
to make a deck, the exercise here was to implement the mathematical intuition that I had for the problem.

The file main.py includes an example of how to use the program. Changing the value of n to any prime number will
produce the corresponding deck. I'm also working on several methods to examine triples (sets of 3 cards with the same
symbol in common) and caps (sets of cards containing no triples, term adapted from finite geometry). The method
make_tricap() returns a complete cap; that is, a cap such that including any additional card will create a triple.
The cap will consist of at most n cards, still figuring out how to precisely construct maximal caps (largest possible 
cap for a given deck).
