"""Stair"""

def main():
    """PSCP - Stair"""
    y = int(input())
    n = int(input())

    heights = []
    x = 0
    for i in range(n):
        x += i
        heights.append(int(input()))

    for height in heights:
        if height > y:
            print("NO")
            return

    steps = 0
    current_pos = 0

    while current_pos < n:
        total_height = 0
        next_pos = current_pos
        while next_pos < n and total_height + heights[next_pos] <= y:
            total_height += heights[next_pos]
            next_pos += 1
        if next_pos == current_pos:
            print("NO")
            return

        current_pos = next_pos
        steps += 1

    print(steps)

main()
