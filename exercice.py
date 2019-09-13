# maliste = [0, 11, 12, 30, 34, 48, 66]
# # mynumber = 9
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

# mynumber = 9
# # for i in range(len(maliste)):
# #     if mynumber == maliste[i]:
# #         print([i])
# #     else:
# #         print(False)

# is_found = False

# for i in range(len(maliste)):
#     if maliste[i] > mynumber:
#         is_found = False

# print(is_found)
#     print(maliste.index(mynumber))

            # resultat = 0
            # for i in range(len(maliste)):
            #     if maliste[i]%n == 0:
            #         resultat += i
            # print(str(i) + "est divisible par" + "n")
            #     else:
            # print(str(i) + "n'est pas divisible par" + "n")

# l = []
# nb_elements = 9
# import random
# for i in range(nb_elements):
#     l.append(random.randint (1, 100))
# print(l)

l1 = [2, 4, 9, 10, 5, 12]
l2 = []

                                # for i in range(len(l1)):
                                #     if l1[i] % 2 == 0: 
                                #         print(i,"pair")
                                #     else:
                                #         print(i,"impair") 

                                # for i in range(len(l2)):
                                #     l2.append(l1[i] == "pair")
                                #     print(l2)
                                    
                                #     l1.pop(l2 = l1[-1])
                                #     print(l2)

                                #                 # if l1[i] == "pair":
                                #                 #     print(i)
                                #                 # else:
                                #                 #     print(a.pop[i])

for i in l1:
    if i % 2 != 0:
        l2.append(i)
        l1.remove(i)

for i in range(len(l1)):
    if l1[i] % 2 = 0:
        l2.append(l1[i])

for i in range(len([l2])):
    l1.remove(l2[i])

print(l1)
print(set(l2))