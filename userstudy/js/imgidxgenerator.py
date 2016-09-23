

if __name__ == '__main__':
    totalimg = 3721
    centerimg = 1860
    idx = []
    for i in range(-30,31,20):
        for j in range(-30,31,20):
            # print(i,j)
            # idx.appen(j+i*305)
            print(j+30+(i+30)*61, end=" ")
