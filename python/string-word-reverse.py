# "india is my country" > "country my is india"
str1 = "india is my country"
str1 = str1.split()

print(" ".join(str1[::-1]))
str1.reverse()
print(" ".join(str1))
