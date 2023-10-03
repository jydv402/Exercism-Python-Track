def exchange_money(budget, exchange_rate):
    """
    Function to return the value of exchanged currency

    eg: exchange_money(127.5, 1.2) = 106.25

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Function to return the amount left of your total budget

    eg: get_change(127.5, 120) = 7.5

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Function to return the total money you will obtain from the booth after exchange

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    Function to return the number of bills you will receive

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget, denomination):
    """
    Function to return the leftover bills that cannot be exchanged

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Function to return the maximum value you can get taking into consideration the exchange commission

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    
    new_exchange_rate = exchange_rate + exchange_rate * spread / 100
    new_exchanged_money = exchange_money(budget, new_exchange_rate)
    money_not_exchanged = get_leftover_of_bills(new_exchanged_money, denomination)

    return int(new_exchanged_money - money_not_exchanged)