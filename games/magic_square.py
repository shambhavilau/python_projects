'''
    sum = n(n^2 +1)/2
    # Steps
    1. in any magic square, 1 is located at position (n/2,n-1)
    2. position of 1 = (n/2,n-1) = (p,q), then next number 2 is located at (p-1,q+1) position
       if calculated row becomes - then replace it with value n-1 and if column becomes n then replace it with 0
    3. if calculated position already contains a number then, decrement column by 2 and increment row by 1
    4. if row position becomes -1 and columns becomes n then replace with (0,n-2)
'''

n = int(input("Enter degree of magic square: "))


def magic_square(n):
    # inserting blank entries in magic square
    magicSq = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSq.append(l)
    '''magic = [0 for i in range(3)] this will insert 0 in list 3 times like [0,0,0]
    magic = [[0 for i in range(3)] for j in range(3)] this will insert 0 in list 9 times i.e create 3 sublist with 3 0's
    like [[0,0,0],[0,0,0],[0,0,0]]
    '''

    i = n//2
    j = n-1
    num = n * n
    count = 1
    while count <= num:
        if i == -1 and j == n:      # Condition 4
            j = n-2
            i = 0
        else:
            if j == n:      # Column value is exceeding
                j = 0

            if i < 0:       # Row is becoming -1
                i = n-1

        if magicSq[i][j] != 0:
            j = j-2
            i = i+1
            continue
        else:
            magicSq[i][j] = count
            count += 1

        i = i-1     # Condition 1
        j = j+1
    # printing the magic square
    for i in range(n):
        for j in range(n):
            print(magicSq[i][j], end=" ")
        print()
    print("The sum of each row / column/ diagonal is: ", int((n*(n**2 + 1))/2))


magic_square(n)
