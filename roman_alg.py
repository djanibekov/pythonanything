

roman_numbers1 = ['I', 'X', 'C', 'M']
roman_numbers2 = ['V', 'L', 'D', 'M']

arabic_number = input()
length = len(arabic_number)
arabic_number = int(arabic_number)
roman_number = ''

while(length > 0):
    rank = pow(10, length-1)
    rank_number = arabic_number // rank
    if(rank_number < 4):
        roman_number = roman_number + rank_number*roman_numbers1[length-1]
    elif(rank_number > 5):
        roman_number = roman_number + (rank_number-5)*roman_numbers2[length-1] + roman_numbers1[length-1]

    length = length - 1

print(roman_number)