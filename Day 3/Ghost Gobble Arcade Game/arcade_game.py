def eat_ghost(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active == True and touching_ghost == True:
        return True
    elif touching_ghost == False:
        return False
    return False


def score(touching_power_pellet, touching_dot):
    """
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet == True or touching_dot == True


def lose(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    return touching_ghost == True and power_pellet_active == False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if lose(power_pellet_active, touching_ghost) == True:
        return False
    return has_eaten_all_dots
