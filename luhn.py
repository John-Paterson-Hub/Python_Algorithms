# 1) if the number already contains the check digit, drop that digit from the payload. The check digit is most often the last digit. 
# 2) With the payload start with the rightmost digit. Moving left double the value of every second digit left (including the rightmost digit)
# 3) Sum the values of the resulting digits.
# 4) The check digit is calculated by 10 - (s mod 10) . This is the least number (possibly zero) that must be added to s to make it a
#       multiple of 10. Other valid formulas giving the same value are (10 - s)mod 10 and 10[s/10] - s.

# ----------------------------------------------------------
# |             | 7 |  9  | 9 | 2 | 7 | 3 | 9 |  8  | 7 | 1 |
# -----------------------------------------------------------
# | Multipliers | 1 |  2  | 1 | 2 | 1 | 2 | 1 |  2  | 1 | 2 |
# -----------------------------------------------------------
# |             | = |  =  | = | = | = | = | = |  =  | = | = |
# -----------------------------------------------------------
# |             | 7 | 18  | 9 | 4 | 7 | 6 | 9 | 16  | 7 | 2 |
# -----------------------------------------------------------
# |    Sum      | 7 | 9   | 9 | 4 | 7 | 6 | 9 | 7   | 7 | 2 |
# |   Digits    |   |(1+8)|   |   |   |   |   |(1+6)|   |   |
# -----------------------------------------------------------

# The sum of the resulting digits is 67
# The check digit is equal to 10 - (67 mod 10) = 3
# This makes the full account number read 79927398713

# Example for valitating check digit
#     1) Drop the check digit (last digit) of the number to validate 79927398713 -> 7992739871
#     2) Calculate the check digit (See above)
#     3) Compare your result with the original check digit. If both numbers match result is valid
#       (e.g. (givenCheckDigit = calculatedCheckDigit) <=> (isValidCheckDigit) )

# def luhn(payload):




def luhn(data):
    result = []
    for d in str(data):
        result.append (int(d))
    print(result)
    size = len(result)

    if (size % 2) == 0:
        size = int(size/2)
        holding =[]
        for i in range(size):
            holding.append(1)
            holding.append(2)
        print(holding)
    elif (size % 2) != 0:
        size = int((size-1)/2)
        holding =[]
        for i in range(size):
            holding.append(2)
            holding.append(1)
        holding.append(2)
        print(holding)

    size = len(result)
    sumdigit = []
    allsum = 0

    for i in range(size):
        sum = result[i] * holding[i]
        if sum > 9:
            sum = (sum - 10) + 1
        sumdigit.append(sum)
        allsum += sum

    print(sumdigit)
    print(allsum)

    checkdigit = size - (allsum % size)
    if checkdigit == 10:
        checkdigit = 'X'

    print(checkdigit)


# returns check digit for even amount of numbers
payload = 7992739871
luhn(payload)

# returns X for check digit being 10
payload = 5928745923
luhn(payload)

# returns check digit for odd amount of numbers
payload = 508284305
luhn(payload)


