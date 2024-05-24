while True:
    a = int(input())
    if a < 25:
        print("Higher")
        continue
    if a > 25:
        print("Lower")
        continue
    if a == 25:
        print("Good")
        break