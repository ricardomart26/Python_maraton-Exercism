def estimate_value(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - estimated value of the foreign currency you can receive
    """
    return budget // exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging
    """
    return budget - exchanging_value


def get_value(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money
    """
    return budget // denomination
        

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get
    """
    if denomination >= budget:
        return 0
    exchange_fee = (exchange_rate * spread) / 100
    exchange_fee += exchange_rate

    money = estimate_value(budget, exchange_fee)
    denomination = estimate_value(denomination, exchange_fee)
    return money - denomination



def unexchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - unexchangeable value
    """
    return denomination - 4

print(exchangeable_value(127.25, 1.20, 10, 20))
# print(estimate_value(100, 1.32))
print(exchangeable_value(127.25, 1.20, 10, 5))
print(exchangeable_value(127.25, 1.20, 10, 100))
# print(unexchangeable_value(127.25, 1.20, 10, 20))
# print(unexchangeable_value(127.25, 1.20, 10, 5))