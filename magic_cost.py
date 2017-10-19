from datetime import datetime


def magic_cost():
    now = datetime.now()
    magic_factor = float(now.day % 10 + now.hour)
    return magic_factor
