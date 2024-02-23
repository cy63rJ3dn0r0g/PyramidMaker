
def pyramidPrint(symbol):
    if len(symbol) != 1:
        raise Exception(" 'symbol' need to be string of 1.")
    for i in range(1,11):
        spaces = ' ' * (10 - i)
        symbols = symbol * (2 * i - 1)
        print(spaces + symbols)

symbol = input("Enter a symbol: ")
print('You have choosen an ' + symbol + ' for a shape.')
pyramidPrint(symbol)
