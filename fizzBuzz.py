"""FizzBuzz"""
def main() :
    "FizzBuzz"
    num = int(input())
    for i in range(1, num + 1) :
        if not i % 5 and not i % 3 :
            print("FizzBuzz")
        elif not i % 5 :
            print("Buzz")
        elif not i % 3 :
            print("Fizz")
        else :
            print(i)
main()
