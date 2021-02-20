# Take input from the user using input function (remember the datatype of the input data)!
# For now, you can assume that input wil only be numbers, there will be no character input.

# Initializing temporary variables to store intermediate data might be useful!

# Remember to keep track of sums of alternate digits starting from the end!
# Make sure you account for the case where the product of a digit might exceed 10!

# Check the different length and numeric constraints for each individual card type!
# And finally, don't forget to account for invalid card numbers!

# Last step, print the card type using the print function.
# You can just print the card type in all caps, for example, INVALID or AMEX or VISA or MASTERCARD


card_no = input("Enter credit/debit card number: ")

# function to create a list of digits in a number
def toDigit(number):
    digit = [int(x) for x in number]
    return digit

# store digits of car_no in a list
card_digits = toDigit(card_no)

# reverse the list
digits_reversed = card_digits[::-1]

# list of alternate digits starting from the end
alt_digits = digits_reversed[1::2]

# multiply each digit by two and store in list
times_two = [digit*2 for digit in alt_digits]

# sum of numbers which were doubled 
sum_of_digits = 0 
sum_of_num = 0
for num in times_two:
    num = str(num)
    for digit in num:
        sum_of_digits += int(digit)        

alt_digits_2 = digits_reversed[0::2]

sum_ = 0
for digit in alt_digits_2:
    sum_ += digit

# final sum of digits after necessary processing 
end_sum = sum_ + sum_of_digits

# checking validity of card number
if end_sum % 10 != 0:
    print("INVALID\n")

# checking card type
if ((len(card_no) == 15) and (card_no[0] == '3') and ((card_no[1] in {'4', '7'}))):
    print("AMEX\n")
elif ((len(card_no) == 16) and (card_no[0] == '5') and (card_no[1] in {'1', '2', '3', '4', '5'})):
    print("MASTERCARD\n")
elif ((len(card_no) in {13, 16}) and card_no[0] == '4'):
    print("VISA\n")