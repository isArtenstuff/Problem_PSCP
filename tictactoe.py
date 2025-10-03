"""Tic Tac Toe"""
line_1 = input()
line_2 = input()
line_3 = input()
if line_1 == "OOO" or line_2 == "OOO" or line_3 == "OOO":
    print("O WIN")
elif line_1 == "XXX" or line_2 == "XXX" or line_3 == "XXX":
    print("X WIN")
elif line_1[0] == "O" and line_2[1] == "O" and line_3[2] == "O":
    print("O WIN")
elif line_1[0] == "X" and line_2[1] == "X" and line_3[2] == "X":
    print("X WIN")
elif line_1[2] == "O" and line_2[1] == "O" and line_3[0] == "O":
    print("O WIN")
elif line_1[2] == "X" and line_2[1] == "X" and line_3[0] == "X":
    print("X WIN")
elif line_1[0] == "O" and line_2[0] == "O" and line_3[0] == "O":
    print("O WIN")
elif line_1[0] == "X" and line_2[0] == "X" and line_3[0] == "X":
    print("X WIN")
elif line_1[1] == "O" and line_2[1] == "O" and line_3[1] == "O":
    print("O WIN")
elif line_1[1] == "X" and line_2[1] == "X" and line_3[1] == "X":
    print("X WIN")
elif line_1[2] == "O" and line_2[2] == "O" and line_3[2] == "O":
    print("O WIN")
elif line_1[2] == "X" and line_2[2] == "X" and line_3[2] == "X":
    print("X WIN")
else:
    print("DRAW")
