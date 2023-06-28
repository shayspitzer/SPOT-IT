from itertools import combinations
from random import randint


def sum_triples(triples):  # meant to take the sum of each triple in a deck
    n = len(triples[0]) - 1
    sums = []
    for i in range(0, len(triples) - 2, 3):
        t1 = triples[i]
        t2 = triples[i + 1]
        t3 = triples[i + 2]
        tsum = 0
        for j in range(n):
            t = t1[j] + t2[j] + t3[j]
            tsum += t
        sums.append(tsum % n)
    return sums


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

    def make_tricap(self, s):  # make a complete cap of at most size n
        n = self.n
        cards = self.cards
        cap = []
        k1 = randint(0, n ** 2 + n - 1)
        card1 = cards[k1]
        cap.append(card1)
        cards.remove(card1)
        k2 = randint(0, n ** 2 + n - 2)
        card2 = cards[k2]
        cap.append(card2)
        cards.remove(card2)

        ints = set(card1).intersection(set(card2))

        for card in cards:
            if len(cap) == s:
                break
            if len(set(card).intersection(ints)) < 1:
                for thing in cap:
                    ints = ints.union(set(card).intersection(set(thing)))
                cap.append(card)
        cards.append(card1)
        cards.append(card2)
        return cap

    def find_triples(self):
        cards = self.cards
        triples = []
        for (c, d, e) in combinations(cards, 3):
            (x, y, z) = (set(c), set(d), set(e))
            if len(x & y & z) == 1:
                triples.append(list(x))
                triples.append(list(y))
                triples.append(list(z))
        return triples
