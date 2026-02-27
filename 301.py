n = input().strip()
for ch in n:
    if ch not in "02468":
        print("Not Valid")
        break
else:
        print("Valid")
