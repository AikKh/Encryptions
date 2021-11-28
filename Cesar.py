alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
key = int(input('Key:'))
str1 = input()
res = ''

for i in str1:
    if i == ' ':
        res+=' '
        continue
    
    res += alpha[(alpha.find(i) + (key + 1)) % len(alpha)]
    
print('Result: "' + res + '"')

