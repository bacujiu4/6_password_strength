

def get_password_strength(password):
    pass


if __name__ == '__main__':
    s = 'megaPaSSw#$Ord'
    for symbol in s:
        print('isupper', symbol, s.isupper())
        print('islower', symbol, s.islower())
        print(symbol, s.isprintable())
