"""แปลงอุณหภูมิ"""
tem = float(input())
or_unit = input()
want_unit = input()
def change_unit():
    """Have"""
    c = 0
    if or_unit == "F" :
        c = (tem - 32) * 5 / 9
    elif or_unit == "K" :
        c = tem - 273.15
    elif or_unit == "R" :
        c = (tem * 5) / 9 - 273.15
    elif or_unit == "C" :
        c = tem
    return c
def show_output(c):
    """Want"""
    output = 0
    if want_unit == "F" :
        output = c * 9 / 5 + 32
    elif want_unit == "K" :
        output = c + 273.15
    elif want_unit == "R" :
        output = (c + 273.15) * 9 / 5
    elif want_unit == "C" :
        output = c
    print(f"{output:.2f}")
show_output(change_unit())
