from itertools import combinations
from random import randint, shuffle


def get_more_dependencies(cap, capadds): # used in get_tricap_super_capadds()
    mults = []
    for i in range(len(capadds)):
        cardd = capadds[i]
        card_count_t = 0
        card_count_f = 0
        for num in cardd:
            count = -1
            in_cap = False
            for card in capadds:  # checks how many times each number in the card occurs on cards in capadds
                if num in card:
                    count += 1
            for ccard in cap:     # checks if each number in card appears on some card in the cap
                if num in ccard:
                    in_cap = True
                    break
            if in_cap:
                card_count_t += count   # counts each number that appears in the cap
            else:
                card_count_f += count   # counts each number that does not appear in the cap
        this_tuple = (cardd, card_count_t, card_count_f)
        mults.append(this_tuple)
    return mults


class SpotIt:
    def __init__(self, n):
        self.n = n
        self.cards = self.make_deck()
        self.inc = self.incidence()

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

    def incidence(self):   # creates an incidence matrix for projective plane order n
        n = self.n
        cards = self.cards
        k = n ** 2 + n + 1
        inc = []
        for card in cards:
            inc_card = []
            for j in range(k):
                if j in card:
                    inc_card.append(1)
                else:
                    inc_card.append(0)
            inc.append(inc_card)
        return inc

    def make_complete_tricap(self, s):   # make a complete cap of at most size n
        n = self.n              # (a cap is a set of cards with no triples)
        cards = self.cards
        shuffle(cards)              # randomizes deck for selection of first 2 cards
        cap = []

        card1 = cards.pop()         # the selection of the first 2 cards is arbitrary
        cap.append(card1)           # (the relationship between any 2 cards is equivalent)
        card2 = cards.pop()
        cap.append(card2)

        ints = set(card1).intersection(set(card2))  # keep track of intersections between cards
        for card in cards:                 # each card added to the cap cannot contain the intersection
            if len(cap) == s:                # of any 2 cards in the cap
                break
            if len(set(card).intersection(ints)) < 1:
                for thing in cap:
                    ints = ints.union(set(card).intersection(set(thing)))   # add intersections of new card w/ old cards
                cap.append(card)
        cards.append(card1)     # returns deck to its original state (for running many trials)
        cards.append(card2)
        return cap

    def make_tricap_super_capadds(self, s, max):   # int s, boolean max
        cards = self.cards       # uses true/false sums from get_more_dependencies() to construct a cap
        n = self.n
        k = n ** 2 + n + 1
        shuffle(cards)
        cap = []
        card1 = cards.pop()
        cap.append(card1)
        card2 = cards.pop()
        cap.append(card2)
        ints = set(card1).intersection(set(card2))
        current_capsize = 2
        capadds_deps = {}
        while current_capsize < s:
            capadds = []          # keeps track of capadds at each step
            for card in cards:    # makes a random cap if size 5 before making more complex decisions
                if len(set(card).intersection(ints)) < 1:
                    if len(cap) == current_capsize:
                        capadds.append(card)
                    else:
                        for thing in cap:
                            ints = ints.union(set(card).intersection(set(thing)))
                        cap.append(card)
            if current_capsize >= 5:
                dependencies = get_more_dependencies(cap, capadds)
                dependencies.sort(key=lambda a: a[1])   # sort dependencies by size of true sum
                capadds_deps[current_capsize] = dependencies
                if max:
                    next_card = dependencies[0][0]
                else:
                    try:
                        next_card = dependencies.pop()[0]
                    except IndexError:
                        break
                for thing in cap:
                    ints = ints.union(set(next_card).intersection(set(thing)))
                cap.append(next_card)
            current_capsize += 1
        cards.append(card1)
        cards.append(card2)
        return cap, capadds_deps


