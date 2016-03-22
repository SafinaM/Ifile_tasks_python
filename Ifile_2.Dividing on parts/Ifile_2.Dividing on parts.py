#Task: to divide vector size on equal parts.
size = 0
while(size == 0):
    try:
        size = int (input ("Enter the size of vector: "))
    except:
        print("The number is not integer.")
M = 0
while(M == 0):
    try:
        M = int(input ("Enter the integer number of parts M < size: "))
    except:
        print("The number is not integer.")
if size > M+1:
    if size % M == 0:
        part = size/M
        for k in range (0, M):
            print("Part: ", k+1, ": ")
            for i in range(int(k*part), int((k+1)*part), int(part-1)):
                print(i," ")
    else:
        diff = size % M
        if diff % 2 == 0:
            i = 0
            part = (size - diff) / M
            for k in range(0, M):
                print("Part: ", k+1, ": ")
                i = int(k*part+diff/2)
                while( i < int((k + 1)*part + diff / 2)):
                    print(int(i), " ")
                    if M< size/2 or part != 1:
                        i += part - 1
                    else:
                        print(int(i), " ")
                        break
        else:
            diff += 1
            divided = size - diff
            while(divided % M != 0 or divided > 0):
                diff += 2
                divided = size - diff
            if(divided > 0):
                part = (size - diff) / M
                for k in range(0, M):
                    print("Part: ", k+1, ": ")
                    for i in range(int(k*part + diff/2), int((k+1)*part+diff/2+1), int(part - 1)):
                        print(i, ": ")
            else:
                print("The process with such numbers is not possible.")
else:
    print("The process with such numbers is not possible.")
