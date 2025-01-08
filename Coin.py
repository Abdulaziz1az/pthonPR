import random
# The Coin class simulates a coin that ca n be flipped
class Coin:
    def __init__(self):
        self.___sideup = "Head"

    # The toss method generates a random number
    # in the range of 0 through 1 if the number is 0 then sid is set to Head
    # otherwise, sideup is set ot "Tails"
    def toss(self):
        if random.radnint(0,1) == 0:
            self.___sideup = "Head"
        else:
            self.___sideup = "Tails"
