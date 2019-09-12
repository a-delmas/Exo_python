integers = [1, 5, 34, 34932, 32423]
# for value in integers:
#     print(value)
# for i in range(len(integers)):
#     print(integers[i])
# for i in range(-1, -len(integers),-1):
#     print(integers[i])
for i in range(len(integers)):
    print(integers[len(integers)-i-1])