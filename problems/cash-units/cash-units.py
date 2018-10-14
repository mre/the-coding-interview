denominations = [ 500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def cash_units(input_value):
    result = {}
    remaining_value_in_cents = input_value * 100

    for denomination in denominations:
        denomination_in_cents = denomination * 100

        count = int(remaining_value_in_cents / denomination_in_cents)
        result[denomination] = count
        
        remaining_value_in_cents = remaining_value_in_cents - (denomination_in_cents * count)
    return result

result = cash_units(1972.78)

assert(result[500] == 3);
assert(result[200] == 2);
assert(result[100] == 0);
assert(result[50] == 1);
assert(result[20] == 1);
assert(result[10] == 0);
assert(result[5] == 0);
assert(result[2] == 1);
assert(result[1] == 0);
assert(result[0.5] == 1);
assert(result[0.2] == 1);
assert(result[0.1] == 0);
assert(result[0.05] == 1);
assert(result[0.02] == 1);
assert(result[0.01] == 1);
