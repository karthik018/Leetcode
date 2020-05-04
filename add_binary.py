a = input()
b = input()

a_l = len(a)
b_l = len(b)

i = a_l-1
j = b_l-1

res = ""
carry = 0
while i >= 0 and j >= 0:
    if a[i] == b[j] == '1':
        res += str(carry)
        carry = 1
    else:
        res += str(int(a[i]) ^ int(b[j]) ^ carry)
        carry = 0

    i -= 1
    j -= 1

while i >= 0:
    if a[i] == str(carry) == '1':
        res += '0'
        carry = 1
    else:
        res += str(int(a[i]) + carry)
        carry = 0

    i -= 1
   
while j >= 0:
    if b[j] == str(carry) == '1':
        res += '0'
        carry = 1
    else:
        res += str(int(b[j]) + carry)
        carry = 0

    j -= 1
    
if carry == 1:
    res += str(carry)

res = res[::-1]
print(res)
    

