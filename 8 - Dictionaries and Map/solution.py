n = int(input())

phone_book = {}

for i in range(n):
    entry = str(input()).split(' ')
    name = entry[0]
    phone = int(entry[1])
    phone_book[name]=phone

for i in range(n):
    name = str(input())
    if name in phone_book:
        phone=phone_book[name]
        print(str(name)+'='+str(phone))
    else:
        print('Not found')
