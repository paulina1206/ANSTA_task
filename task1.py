"""ZADANIE 1.
Generator kodów pocztowych, który przyjmuje 2 stringi: "79-900" i "80-155"
i zwraca listę kodów pomiędzy nimi."""

def postcode_generator(postcode_start, postcode_end):
    """
    Takes in two strings and returns a list.
    :param postcode_start: string, postcode in format "DD-DDD"
    :param postcode_end: string, postcode in format "DD-DDD"
    :return: postcodes list between given codes
    """

    postcode_start = int(postcode_start.replace("-", ""))
    postcode_end = int(postcode_end.replace("-", ""))
    postcodes = []
    for code in range(postcode_start + 1, postcode_end):
        postcodes.append(f"{str(code)[:2]}-{str(code)[2:]}")
    return postcodes


if __name__ == '__main__':
    print(postcode_generator("79-900", "80-155"))
