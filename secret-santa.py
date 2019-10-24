#
# Secret Santa
#    Given N people, assign each person a 'designated gift recipient'(TM).
#    - everyone should receive exactly one gift
#    - no one should be their own designated gift recipient
#
# (a.k.a. Generate a random cycle of length N)
#

import itertools
import random
import pprint


class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


def getGiftRecipients(names: tuple) -> dict:
    p = list( itertools.permutations(names) )
    cycle = random.choice(p)
    
    x_gives_to_y = {}
    for i in range(len(names)):
        x_gives_to_y[ cycle[i-1].email ] = cycle[i].name

    return x_gives_to_y


def main():
    people = (
                Person('Ixxxx',  'ixxx@gmail.com'),
                Person('Mxxxx',  'mxxx@gmail.com'),
                Person('Vxxxx',  'vxxx@gmail.com'),
                Person('Axxxx',  'axxx@gmail.com'),
                Person('Lxxxx',  'lxxx@gmail.com')
             )
    recipients = getGiftRecipients(people)
    pprint.pprint(recipients)
    

main()

# TO DO:
#   inform everyone of their designated gift recipient by email
