chaine = str(input())
new_str_ = ""
str_len = len(chaine)

for i in range(1, str_len + 1):
    new_str_ += chaine[str_len - i]
print(new_str_)