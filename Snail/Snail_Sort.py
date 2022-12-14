# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# M = [[1, 2, 3, 4, 5], 
#      [6, 7, 8, 9, 10], 
#      [11, 12, 13, 14, 15], 
#      [16, 17, 18, 19, 20], 
#      [21, 22, 23, 24, 25]]
M = [[1, 2, 3, 4, 5, 6], 
[20, 21, 22, 23, 24, 7], 
[19, 32, 33, 34, 25, 8], 
[18, 31, 36, 35, 26, 9], 
[17, 30, 29, 28, 27, 10], 
[16, 15, 14, 13, 12, 11]]

def snail(M):
    K = []
    while M != []:
        n = len(M)
        K.append(M.pop(0))
        k = [row[n-1] for row in M]
        K.append(k)
        for i in M:
            i.pop(-1)  
        if M != []:
            k = M[-1][::-1]
            K.append(k)
            M.pop(-1)
            k = [row[0] for row in M]
            K.append(k[::-1])
            for i in M:
                i.pop(0)  

    K = sum(K, [])
        
    return K

print(snail(M))