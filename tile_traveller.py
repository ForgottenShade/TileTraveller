acc = 1
position = 'a0'

def buildGrid(pos,d):
    newpos = ''

    arra = ['x',' ','_x_',' ','x']
    arrb = ['x',' ','-x-','|','x']
    arrc = ['x','|','x','|','x']

    if d == 'n':
        if pos[0] != 'a':
            newpos = chr(ord(pos[0]) - 1)
            newpos += pos[1]
            print(newpos)
    #if d == 'e':

    #if d == 's':

    #if d == 'w':

    print(arra)
    print(arrb)
    print(arrc)

while acc == 1:
    dirin = input('direction')
    buildGrid('b0',dirin)