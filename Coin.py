import random
# The Coin class simulates a coin that ca n be flipped
class Coin:
    def __init__(self):
        self.__sideup = "Head"

    # The toss method generates a random number
    # in the range of 0 through 1 if the number is 0 then sid is set to Head
    # otherwise, sideup is set ot "Tails"
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    # returns the value
    def get_sidup(self):
        return self.__sideup
# The main function
def main():
    # object  from the Coin class
    my_coin = Coin()

    # display the side of the coin that is facing up 
    print("This side is up :", my_coin.get_sidup())
    # Toss the coin 
    print("I am tossing the coin...")
    # display the side fo the coin that is facing up
    for count in range(10):
         my_coin.toss()
         print("This side is up: ", my_coin.get_sidup())
# Call the function 
main()