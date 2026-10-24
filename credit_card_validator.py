credit_card_number = input("Hello, Kindly Enter Card details to verify\n")

credit_card_array = []
for digit_char in credit_card_number:
    credit_card_array.append(int(digit_char))

def get_credit_card_type(card_array):
    first_digit = card_array[0]

    if first_digit == 4:
        return "Visa Card"

    if first_digit == 5:
        return "MasterCard"

    if first_digit == 3 and card_array[1] == 7:
        return "American Express Card"

    if first_digit == 6:
        return "Discover Card"

    return "Invalid Card"

def check_card_validity(card_array):
    total= 0
    array_length = len(card_array)

    for index in range(array_length - 1):
        current_digit = card_array[index]
        position_from_right = array_length - 1 - index

        if position_from_right % 2 == 1:
            current_digit = current_digit * 2

            if current_digit > 9:
                current_digit = current_digit - 9
        total = total + current_digit

    return total % 10 == 0

credit_card_type = get_credit_card_type(credit_card_array)
credit_card_length = len(credit_card_array)
is_card_valid = check_card_validity(credit_card_array)

if credit_card_length < 13 or credit_card_length > 16:
    is_card_valid = False

if is_card_valid and credit_card_type!= "Invalid Card":
    validity_status = "Valid"

else:
    validity_status = "Invalid"

print("********************************")
print("**Credit Card Type: " + credit_card_type)
print("**Credit Card Number: " + credit_card_number)
print("**Credit Card Digit Length: " + str(credit_card_length))
print("**Credit Card Validity Status: " + validity_status)
print("********************************")
