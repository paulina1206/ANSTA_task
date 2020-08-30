"""ZADANIE 2.
Podana jest lista zawierająca elementy o wartościach 1-n.
Napisz funkcję, która sprawdzi, jakich elementów brakuje:
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]"""


def missing_values(number_list, n):
    """
    Takes in a list and an integer and returns a list with missing elements.
    :param number_list: list containing elements with values 1 to n
    :param n: integer, range to which the list will be checked
    :return: list with missing elements
    """
    missing_number = []
    for number in range(1, n + 1):
        if number not in number_list:
            missing_number.append(number)
    return missing_number


if __name__ == '__main__':
    print(missing_values([2, 3, 7, 4, 9], 10))
