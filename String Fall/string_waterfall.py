import time


def test(string):
    i = 0
    x = 0
    for i in range(len(string)):
        for x in range(len(string)):
            if i == x:
                print('>\ '+string[i]+' \<', end='')
            else:
                print('~', end='')
        time.sleep(0.25)
        print('')


print('\nReady...')
string = input('\nInput String : ')
string = string.replace(' ', '_')
print('\n')
test(string)
input()
