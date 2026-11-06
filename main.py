binary_num = input("Enter a binary number: ")
resultnum = 0
exponent = 0
for i in binary_num[0:-1]:
    if i == '1':
        resultnum += 2 ** exponent
    exponent += 1
print("The decimal equivalent of", binary_num, "is", resultnum)