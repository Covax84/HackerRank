n = int(input())
contacts = dict()
for i in range(n):
    data = input().split()
    contacts[str(data[0])] = data[1]

while True:
    try:
        name = input()
        if name in contacts.keys():
            print('{}={}'.format(name, contacts.get(name)))
        else:
            print('Not found')
    except EOFError:
        break
