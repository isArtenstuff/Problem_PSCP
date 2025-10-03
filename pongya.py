"""พูดอะไรดี เลข หรือ โป้ง ?"""
x = int(input())
def what_should_say():
    """Pong or num"""
    if 1 <= x <= 100_000 :
        if not x % 3 or str(x).endswith("3"):
            print("PONG")
        else :
            print(x)
what_should_say()
