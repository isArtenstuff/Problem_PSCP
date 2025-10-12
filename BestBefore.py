"""Best Before"""
n = int(input())
list_exp = []
for i in range(n):
    exp = input()
    list_exp.append(exp)
    two_front = [list_exp[i][:2]]
print(two_front)