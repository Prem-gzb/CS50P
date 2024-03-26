def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # using the remove prefix method to remove the dollar sign
    cost_without_dollar_sign = d.removeprefix('$')
    return float(cost_without_dollar_sign)



def percent_to_float(p):
    # using the remove suffix method to remove the % sign
    p_withhout_percent_sign = p.removesuffix('%')
    p = float(p_withhout_percent_sign)/100
    return p


main()