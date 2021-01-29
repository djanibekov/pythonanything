class Roman():
    def __init__(self):
        self.r_1000 = ['','M', 'MM', 'MMM']
        self.r_100 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        self.r_10 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        self.r_1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']


arabic = input()
arabic_list = list(arabic)
length = len(arabic)

r_numbers = Roman()
holder = [r_numbers.r_1000, r_numbers.r_100, r_numbers.r_10, r_numbers.r_1]
holder = holder[4-length:]


actual_roman_number = ''
for i in range(length):
    value = arabic_list[i]
    actual_roman_number += holder[i][int(value)]

print(actual_roman_number)
