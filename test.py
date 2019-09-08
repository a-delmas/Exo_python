# n = 100
# stars = ""
# for i in range(n):
#     for nb_spaces in range(n-i-1):
#         stars = stars + " "
#     for nb_stars in range(2*i-1):
#         stars = stars + "*"
#     stars = stars +"\n"
# print(stars)

# temp = 18
# if temp < 20 :
#     print("J'ai froid")
# elif temp > 30 :
#     print("J'ai chaud")
# else :
#     print("Je suis bien")

# for i in range(100):
#     if i % 2 == 0: 
#         print(i,"pair")
#     else:
#         print(i, "impair") 

for i in range(10):
    print("Table de "+ str(i))
    for j in range(10):
       print(str(i) + "*" + str(j) + "=" + str(i*j))