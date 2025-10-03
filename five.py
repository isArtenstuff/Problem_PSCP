"""fiveX"""
x = int(input())
def main() :
    """five"""
    output = ""
    for i in range(1, x + 1) :
        if  not i % 5 :
            output += "X"
        else :
            output += "*"
    print(output)
main()
