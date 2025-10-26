"""Sequence X"""

num = int(input())
N_NUM = num
J_NUM = num-2
for i in range(1,num+1):
    print("   "*(num-i),end="")
    for j in range(1,i+1):
        if i == 1:
            print(f"{j:02}",end="")
        else:
            print(f"{j:02}",end=" ")
    for j in range(i-1,0,-1):
        if j == 1:
            print(f"{j:02}",end="")
        else:
            print(f"{j:02}",end=" ")
    print()
for _ in range(1,num):
    print("   "*_,end="")
    for i in range(1,N_NUM):
        if N_NUM-1 == 1:
            print(f"{i:02}",end="")
            continue
        print(f"{i:02}",end=" ")
    for i in range(J_NUM,0,-1):
        if i == 1:
            print(f"{i:02}",end="")
            continue
        print(f"{i:02}",end=" ")
    J_NUM -= 1
    N_NUM -= 1
    print()
