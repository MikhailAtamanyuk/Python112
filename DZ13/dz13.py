import re

s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированны максимумы ежемесячных осадков."
print(s)
reg = "[\d\/+^,]{10,14}"

print(re.findall(reg, s))
print()
# _________________________________________________________
def valid_pass(pasword):
    return re.findall(r"[\w+-_@\d]{6,18}", pasword)


print(valid_pass("my-p@ssw0rd"))