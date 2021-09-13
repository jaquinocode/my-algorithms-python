def are_transactions_possible(cust_payments):
    register = {
        20: 0,
        10: 0,
        5: 0,
    }
    for payment in cust_payments:
        try:
            give_change(payment, register)
        except ValueError as change_not_possible_error:
            return False
    return True


def give_change(payment, register):
    change_to_give = payment - 5
    register[payment] += 1

    for bill in register.keys():
        while can_pay(bill, change_to_give, register):
            # pay person with the bill
            register[bill] -= 1
            change_to_give -= bill

    if change_to_give != 0:
        raise ValueError(
            "There is still change that needs to be given. Change not possible."
        )


def can_pay(bill, change_to_give, register):
    return register[bill] >= 1 and bill <= change_to_give


inputs = [
    [5, 5, 5],
    [10, 5, 5],
    [5, 5, 10],
]
for numbers in inputs:
    print(f"in: {numbers}")
    print(f"out: {are_transactions_possible(numbers)}\n")
