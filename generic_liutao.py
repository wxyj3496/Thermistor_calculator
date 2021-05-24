# define the generic function of liutao
# is_number : Determine whether the string is a number

import re


def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)

    if result:
        return True
    else:
        return False


def main():
    a = is_number('a')
    b = is_number('1.11')
    print(a)
    print(b)


if __name__ == '__main__':
    main()
