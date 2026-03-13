a = 10
b = 20

c = a
a = b
b = c

print(f"A: {a}, B: {b}")



a2 = 10
b2 = 20

a2, b2 = b2, a2
print(f"A: {a2}, B: {b2}")