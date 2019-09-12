maliste = [0, 11, 12, 30, 34, 48, 66]
# mynumber = 9
# cpt = 0
# for i in range(len(maliste)):
#     if maliste[i] > mynumber:
#         cpt += 1
# print(cpt)

                # for i in range(len(maliste)):
                #     if maliste[i] < maliste[i+1]:
                #         print("True")
                #     else:
                #         print("False")

# is_ordered = True

# for i in range(len(maliste)-1):
#     if maliste[i] > maliste[i+1]:
#         is_ordered = False

# print(is_ordered)

mynumber = 9
# for i in range(len(maliste)):
#     if mynumber == maliste[i]:
#         print([i])
#     else:
#         print(False)

is_found = False

for i in range(len(maliste)):
    if maliste[i] > mynumber:
        is_found = False

print(is_found)
    print(maliste.index(mynumber))