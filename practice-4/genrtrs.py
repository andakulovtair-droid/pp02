
def simple_gen():
    yield 1
    yield 2
    yield 3

print("Simple generator:")
for x in simple_gen():
    print(x)

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

print("\nCount to 5:")
for x in count_up_to(5):
    print(x)

def squares(n):
    for i in range(n):
        yield i * i

print("\nSquares:")
for x in squares(5):
    print(x)