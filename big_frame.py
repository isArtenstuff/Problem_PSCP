"""Big Frame"""
n_1 = input().strip()
n_2 = input().strip()
n_3 = input().strip()
n_4 = input().strip()
n_5 = input().strip()
maxx_length = max(len(n_1), len(n_2), len(n_3), len(n_4), len(n_5))
all_space = maxx_length + 4
first_line = "*" * all_space
print(first_line)
print("* " + n_1 + (" " * (maxx_length - len(n_1))) + " *")
print("* " + n_2 + (" " * (maxx_length - len(n_2))) + " *")
print("* " + n_3 + (" " * (maxx_length - len(n_3))) + " *")
print("* " + n_4 + (" " * (maxx_length - len(n_4))) + " *")
print("* " + n_5 + (" " * (maxx_length - len(n_5))) + " *")
print(first_line)
