from itertools import combinations
from random import randint, shuffle
from collections import deque


class SpotIt:
    def __init__(self, n):
        self.n = n
        self.cards = self.make_deck()

    def make_deck(self):  # creates spot it deck
        n = self.n
        k = n ** 2 + n + 1
        p = 1
        cards = []
        parts = []              # breaks symbols into subsets to permute in different patterns
        for i in range(1, n + 2):
            parts.append(list(range(p, p + n)))
            p += n
        for i in range(1, n + 2):
            cards.append([0] + parts[i - 1])
        r = n
        part = 0
        num = 0
        while r < k - 1:
            for j in range(r - (n - 1), r + 1):
                cards.append([parts[part][num]])
            num += 1
            r += n
        part += 1
        q = n + 1
        p = 0
        while q < k:
            cards[q].append(parts[part][p])
            q += 1
            p = (p + 1) % n
        indexes = []
        for i in range(n):
            indexes.append(i)
        perms = []
        counter = 0
        for j in range(n):   # framework for permuting symbols
            perms.append(list([(x + counter) % n for x in indexes]))
            counter += 1
        step = 1
        while step < n: # permute symbols according to list above
            mod = 0
            counter_ = 0
            part += 1
            q_ = n + 1
            while q_ < k:
                i = perms[counter_][mod]
                cards[q_].append(parts[part][i])
                q_ += 1
                mod = (mod + 1) % n
                if mod == 0:
                    counter_ = (counter_ + step) % n
            step += 1
        return cards

    def find_triples(self):   # find all triples in the deck
        cards = self.cards    # a triple is a set of 3 cards that all share one symbol (integer)
        triples = []
        for (c, d, e) in combinations(cards, 3):    # just checks every combination of 3 cards
            (x, y, z) = (set(c), set(d), set(e))    # largely used for smaller decks due to time complexity
            if len(x & y & z) == 1:
                triples.append(list(x))
                triples.append(list(y))
                triples.append(list(z))
        return triples

    def make_tricap(self, s):   # make a complete cap of at most size n
        n = self.n              # (a cap is a set of cards with no triples)
        cards = deque(self.cards)   # uses deques for faster pops and insertion
        shuffle(cards)              # randomizes deck for selection of first 2 cards
        cap = deque()

        card1 = cards.pop()         # the selection of the first 2 cards is arbitrary
        cap.append(card1)           # (the relationship between any 2 cards is equivalent)
        card2 = cards.pop()
        cap.append(card2)

        ints = set(card1).intersection(set(card2))  # keep track of intersections between cards
        for card in cards:          # each card added to the cap cannot contain the intersection
            if len(cap) == s:       # of any 2 cards in the cap
                break
            if len(set(card).intersection(ints)) < 1:
                for thing in cap:
                    ints = ints.union(set(card).intersection(set(thing)))   # add intersections of new card w/ old cards
                cap.append(card)
        cards.append(card1)     # returns deck to its original state (for running many trials)
        cards.append(card2)
        return cap
