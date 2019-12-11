from re import finditer

numnberOfPasswords = 0

for i in range(353096,843212):
    digits = [int(numb) for numb in str(i)]
    if (any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', str(i))) and digits == sorted(digits)):
        numnberOfPasswords+=1
print(numnberOfPasswords))
