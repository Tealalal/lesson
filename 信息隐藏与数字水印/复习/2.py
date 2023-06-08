strs="BUPT2023"
def generateMatrix():

    ascii=""
    for i in strs:
        ascii +=str(ord(i))

    print(strs+"的ASCII是"+ascii)

    Matrix = [[]]

    for i in range(8):
        temp = bin(ord(strs[i])).replace('0b','').zfill(8)
        Matrix.append([])
        for j in range(8):
            Matrix[i].append(int(temp[j]))
    return Matrix

if __name__ == '__main__':
    m = generateMatrix()
    ms = ''
    for i in range(8):
        for j in range(8):
            ms += str(m[i][j])
        ms+='\n'
    print(ms)
