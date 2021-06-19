
import numpy as np
def hill_enc(M,string):
    M=np.array([[17,17,5],[21,18,21],[2,2,19]])
    no_space=string.replace(" ","")
    string_upper=no_space.upper()
    length_string=len(string_upper)
    if length_string%3!=0:
        padding=3-(length_string%3)
#        padding_size=length_string+padding
        res=string_upper+"X"*(padding)
#        print(res)
#        for i in range(0,len(res),3):
    else:
        res=string_upper
    
    str_dict = {}
    result_dict={}
    j = 0
    k=0
    for i in range(0, len(res), 3):
        str_dict[j] = [ord(res[i])-65, ord(res[i+1])-65, ord(res[i+2])-65]
        
#            str_dict[j] = [res[i:i+3]]
#            split=[res[i:i+3]]
#            str_dict[j].append(split)
#            str_dict += str(split)
#            print(split)
        j += 1
    for k in range(len(str_dict)):     
        array1=np.array(str_dict[k])
        result=np.matrix.round(np.matmul(array1,M))%26
        l=0
        result_dict[k]=chr(result[l]+65)+chr(result[l+1]+65)+chr(result[l+2]+65)
    v=''.join(result_dict.values())
    return v
    
        
#        print(result_dict.values())
    
#            print(array1)
#        print(str_dict)
#        print(split[0])
#        for i in split:
#            print(i)
#            for j in i:
##                print(ord(j))
#                for_matrix=ord(j)-65
#                print(for_matrix)
#                for k in range(3):
#                    mat1=[for_matrix]
#                print(k)
#                    
##                l.append([for_matrix])
##                print(M.dot(mat1))
##            print(mat1)
##        for k in for_matrix:
##            l.append[k]
##        print(l)
#                

#    print(M)
#    np.linalg.inv(M)
#    np.linalg.det(M)
def hill_dec(M,string):
    M=([[17,17,5],[21,18,21],[2,2,19]])
    no_space=string.replace(" ","")
    string_upper=no_space.upper()
    
    Minv=np.linalg.inv(M)
    Mdet=np.linalg.det(M)
    Madj = Mdet*Minv
    Madj26 = Madj%26
    Mod26invTable = {}
    for m in range(26):
      for minv in range(26):
        if (m*minv)%26==1:
          Mod26invTable[m] = minv
    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
        Mdet26inv = Mod26invTable[Mdet26]
#    else:
#        Mdet26inv = -1
#    Mcheck=np.matrix.round(np.matmul(M,Minv))
#    print(Mcheck)
   
    Minv26=(Mdet26inv*Madj26)%26
#    Minv266_ceil=np.ceil(Minv26)
#    Minv26_int=Minv26.astype(int)
    Mcheck=np.matrix.round(np.matmul(M,Minv26))%26 #identity matrix not coming
    print(Mcheck)
#    print(Minv26)
#    print(Mdet26inv)
    
    if len(string)%3!=0:
        padding=3-(len(string)%3)
#        padding_size=length_string+padding
        res=string_upper+"X"*(padding)
#        print(res)
#        for i in range(0,len(res),3):
    else:
        res=string_upper
        
    str_dict = {}
    result_dict={}
    j = 0
    k=0
    for i in range(0, len(res), 3):
        str_dict[j] = [ord(res[i])-65, ord(res[i+1])-65, ord(res[i+2])-65]
        j += 1
    for k in range(len(str_dict)):     
        array1=np.array(str_dict[k])
        result=np.matrix.round(np.matmul(array1,Minv26))%26
        print(array1)
        l=0
        result_dict[k]=chr(int(result[l])+65)+chr(int(result[l+1])+65)+chr(int(result[l+2])+65)
    v=''.join(result_dict.values())
    return v
#    print("For testing")
#    print(Minv)
#    print(Mdet)
#    print(Madj)
#    print(Madj26)
#    print(Mdet26)
#    print(Mdet26inv)
#    print(Minv26)
#    print(Minv26_int)
#    print(np.int_(Minv26))
#    print(Minv266_ceil)
        
