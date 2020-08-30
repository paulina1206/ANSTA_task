"""ZADANIE 3.
Należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5.
Dane wynikowe muszą być typu decimal."""


def list_generator(min=2, max=5.5, step=0.5):
    """
    Takes in three decimals and returns a list with numbers.
    :param min: float, first number in list
    :param max: float, last number in list
    :param step: float, step between numbers
    :return: list of numbers between min and max with step
    """
    decimals = []
    while min <= max:
        decimals.append(float(min))
        min += step
    return decimals


if __name__ == '__main__':
    print(list_generator())
