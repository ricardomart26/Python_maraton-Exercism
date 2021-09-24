
# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME=40

# TODO: consider defining the 'PREPARATION_TIME' constant 
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME=2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(time):

    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time
    pass

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def	preparation_time_in_minutes(layers):

    """layers = numero de layers
    
    :elaped ... = tempo no forno
    """
    if layers == 0:
        return 0
    elif layers > 0:
        return (layers * PREPARATION_TIME)

# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    
    """layers = numero de layers
    
    :elaped ... = tempo no forno
    """
    return elapsed_bake_time + preparation_time_in_minutes(layers)
