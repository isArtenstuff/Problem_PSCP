"""cyan's password"""
def main():
    """cyan's password"""
    name = input()
    sur = input()
    age = input()
    if len(name) >= 5 and len(sur) >= 5 :
        print(name[:2] + sur[-1] + age[-1])
    else :
        print(name[0] + age + sur[-1])
main()
