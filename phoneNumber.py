"""Phone number"""
phone = input()
want = input()
if len(phone) == 9 :
    if want == "Domestic" :
        print(f"{phone[0]} {phone[1:5]} {phone[5:]}")
    elif want == "International" :
        print(f"+66 {phone[1:5]} {phone[5:]}")
if len(phone) == 10 :
    if want == "Domestic" :
        print(f"{phone[:2]} {phone[2:6]} {phone[6:]}")
    elif want == "International" :
        print(f"+66{phone[1]} {phone[2:6]} {phone[6:]}")
