import os
import sys
import json
import logging
from collections import namedtuple


"""
Setting up logger
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s -%(lineno)s: \t%(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)



def get_path(name = None):
    basepath = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(basepath, "..", "app_data", name))


def write_to_file(name = 'final_disbursement.json', data = None):
    full_path = get_path(name = name)
    try:
        with open(full_path, 'w') as file_handler:
            json.dump(data, file_handler)
        return True
    except Exception as e:
        logger.warning(e)
        return False

def read_from_file(name = None):
    full_path = get_path(name)
    if os.path.isfile(full_path):
        try:
            with open(full_path, 'r') as file_handler:
                return json.load(file_handler)
        except Exception as e:
            logger.warning(e)
            return None
    logger.warning('File doesnt exist')
    return {}

def to_json(arr = None):
    dic = {}
    for traveler in arr:
        dic[traveler.name] = traveler.owns_to
    return dic

def disbursement(arr = None):
    if arr:
        arr = get_most_spent_order(arr = arr)
        total_spent = get_total_spent(arr = arr)

        """
        array is not empty so there should be no ZeroDivisionError
        """
        average = total_spent / len(arr)
        disbursement_helper(arr = arr, average = average)
        json_data = to_json(arr)
        logger.info(json_data)
        write_to_file(name = 'final_disbursement.json', data = json_data)
        return json_data
    return None

def get_most_spent_order(arr = None):
    """
    This will return array in reversed order highest to lowest
    """
    return sorted(arr, key=lambda x : x.total, reverse=True)

def get_total_spent(arr = None):
    """
    This will return a total spent by all travelers
    """
    return sum(list(traveler.total for traveler in arr))

def disbursement_helper(arr = None, average = 0):
    pool = 0
    visited = 0
    current = 0
    for traveler in arr:
        current += 1
        amount_to_pay_back = average - traveler.total
        if traveler.name == 'Nyk':
            print('Nyk amount_to_pay_back {}'.format(amount_to_pay_back))
        if amount_to_pay_back > 0:
            
            pool = amount_to_pay_back
            traveler.total += amount_to_pay_back
            visited = pay_back_to(arr = arr[visited:current], traveler = traveler, average = average, pool = pool)

    return True


def pay_back_to(arr = None, traveler = None, average = 0, pool = 0):
    """
    We will record how many travelers were visited,
    so we dont have to visit them again
    """
    visited = 0
    for getter in arr:
        """
        only proceed if getter is expecting to get some money back
        """

        if traveler.name == 'Nyk':
            print('Nyk will pay {}'.format(getter.name))

        if getter.total > average:
            visited += 1
            exchange = average + pool - getter.total

            if traveler.name == 'Nyk':
                print('Nyk exchange {}'.format(exchange))

            if exchange >= 0:
                """
                pool has more than getter needs
                """
                pay = pool - exchange
                if traveler.name == 'Nyk':
                    print('Nyk pay {}'.format(pay))
                pool -= pay
                getter.total -= pay
                traveler.set_own_to(name = getter.name, amount = round(pay, 2))
            else:
                """
                pool has less than getter needs
                """
                if traveler.name == 'Nyk':
                    print('Nyk pool {}'.format(pool))
                getter.total -= pool
                traveler.set_own_to(name = getter.name, amount = round(pool, 2))
                pool = 0
            if pool <= 0:
                """
                return if pool is empty, but first
                check whether last getter got all the money back
                """
                if getter.total > average:
                    visited -= 1
                    return visited
                return visited