"""docstring"""
def main():
    """docstring"""
    price = float(input())
    atleast_pro = float(input())
    discount = float(input())
    sugguest_food = float(input())

    if price >= atleast_pro:
        cost_no_add = price * (1 - discount/100)
    else:
        cost_no_add = price
    total = price + sugguest_food

    if total >= atleast_pro:
        cost_with_add = total * (1 - discount/100)
    else:
        cost_with_add = total
    difference = cost_with_add - cost_no_add

    if difference < 0:
        print(f"Yes {abs(difference):.3f}")
    elif difference > 0:
        print(f"No {difference:.3f}")
    else:
        print("Yes")

main()
