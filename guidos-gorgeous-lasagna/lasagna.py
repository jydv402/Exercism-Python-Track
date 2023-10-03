"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40 #Expected time of preparation

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining.

    :param number_of_layers: int - number of layers.
    :return: int - preparation time based on the number of layers.

    Function that takes in the number of layers as parameter and 
    returns the preparation time in minutes with respect to the 
    number of layers present in the Lasagna.
    """
    return number_of_layers * 2  # Each layer takes 2 minutes

    
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - elapsed bake time.
    :return: int - total elapsed time in minutes.

    Function that takes in two parameters: the number of layers and
    the elapsed bake time and returns the total elapsed time
    in minutes needed to prepare the Lasagna.
    """
    return preparation_time_in_minutes(
        number_of_layers) + elapsed_bake_time  # Calculates the total elapsed time
