"""Seven"""
x = int(input())
last_di = [7, 9, 3, 1]
position = x % 4
if not position:
    print(last_di[3])
elif position :
    print(last_di[position - 1])
