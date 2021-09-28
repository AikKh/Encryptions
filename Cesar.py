# Cesar encryption algorithm. Changes for test new Git tool.
alpha = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Key:'))
str1 = input()
res = ''

for i in str1:
    if i == ' ':
        res+=' '
        continue
    
    res += alpha[(alpha.find(i) + key) % len(alpha)]
    
print('Result: "' + res + '"')

