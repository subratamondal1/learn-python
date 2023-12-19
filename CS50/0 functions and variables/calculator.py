x: int|float = float(input("What's x? "))
y: int|float = float(input("What's y? "))

z: int|float = round(x+y)

print(f"{z:,}")