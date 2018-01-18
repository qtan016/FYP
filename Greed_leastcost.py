# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 04:50:45 2017

@author: quanquan
"""

import random

def getMatrix():
    mat = [[0x1b,0x80,0x80,0x9b],[0x80,0x40,0x40,0xc0],[0x40,0x20,0x20,0x60],[0x20,0x10,0x10,0x30],\
           [0x10,0x08,0x08,0x18],[0x08,0x04,0x04,0x0c],[0x04,0x02,0x02,0x06],[0x02,0x01,0x01,0x03],\
           [0x9b,0x1b,0x80,0x80],[0xc0,0x80,0x40,0x40],[0x60,0x40,0x20,0x20],[0x30,0x20,0x10,0x10],\
           [0x18,0x10,0x08,0x08],[0x0c,0x08,0x04,0x04],[0x06,0x04,0x02,0x02],[0x03,0x02,0x01,0x01],\
           [0x80,0x9b,0x1b,0x80],[0x40,0xc0,0x80,0x40],[0x20,0x60,0x40,0x20],[0x10,0x30,0x20,0x10],\
           [0x08,0x18,0x10,0x08],[0x04,0x0c,0x08,0x04],[0x02,0x06,0x04,0x02],[0x01,0x03,0x02,0x01],\
           [0x80,0x80,0x9b,0x1b],[0x40,0x40,0xc0,0x80],[0x20,0x20,0x60,0x40],[0x10,0x10,0x30,0x20],\
           [0x08,0x08,0x18,0x10],[0x04,0x04,0x0c,0x08],[0x02,0x02,0x06,0x04],[0x01,0x01,0x03,0x02]]
    s_mat = []
    
    # converting the hexadecimals to a 32 by 32 bit matrix
    for i in range(len(mat)):
        s = ''
        for j in range(len(mat[0])):
            temp = bin(mat[i][j])[2:].zfill(8)
            s = s + temp
        s_mat.append(list(s))
     
    for i in range(len(s_mat)):
        for j in range(len(s_mat[0])):
            s_mat[i][j] = int(s_mat[i][j])
    
    s_mat = [list(a) for a in zip(*s_mat)] # transpose the matrix
    
    #for i in range(len(s_mat)): #printing of bit matrix
    #              print(s_mat[i])
    return s_mat
    

def find2tuples(matrix,removal):
    # this function calculates the number of 2 tuples for a matrix
    # initialization
    res = []
    dic = dict()
    
    # put the rows with ones in the same list
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                temp.append(j)
        res.append(temp)    # res shows the columns of each row that has a 1
    # Printing the rows
    #for i in res:
    #    print(i)    
    for i in range(len(res)):
        for j in range(len(removal)):
            if set(removal[j]) <= set(res[i]):
                for k in range(len(removal[j])):
                    res[i].remove(removal[j][k])
    for tup in res:
        if len(tup) >= 3:
            for i in range(len(tup)-1):
                for j in range(i+1,len(tup)):
                            if (tup[i],tup[j]) in dic.keys():
                                dic[(tup[i],tup[j])] = dic[(tup[i],tup[j])] + 1
                            else:
                                dic[(tup[i],tup[j])] = 1
        elif len(tup) == 2:
            if (tup[0],tup[1]) in dic.keys():
                dic[(tup[0],tup[1])] = dic[(tup[0],tup[1])] + 1
            else:
                dic[(tup[0],tup[1])] = 1
        else:
            continue
    keys = [k for k, v in dic.items() if v == 1]
    for x in keys:
        del dic[x]
    return dic
    

def find3tuples(matrix,removal):
    # initialization
    res = []
    dic = dict()
    
    # put the rows with ones in the same list
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                temp.append(j)
        res.append(temp)
    
    for i in range(len(res)):
        for j in range(len(removal)):
            if set(removal[j]) <= set(res[i]):
                for k in range(len(removal[j])):
                    res[i].remove(removal[j][k])
    
    
    for tup in res:
        if len(tup) >= 4:
            for i in range(len(tup)-2):
                for j in range(i+1,len(tup)-1):
                    for m in range(j+1,len(tup)):
                            if (tup[i],tup[j],tup[m]) in dic.keys():
                                dic[(tup[i],tup[j],tup[m])] = dic[(tup[i],tup[j],tup[m])] + 1
                            else:
                                dic[(tup[i],tup[j],tup[m])] = 1
        elif len(tup) == 3:
            if (tup[0],tup[1],tup[2]) in dic.keys():
                dic[(tup[0],tup[1],tup[2])] = dic[(tup[0],tup[1],tup[2])] + 1
            else:
                dic[(tup[0],tup[1],tup[2])] = 1
        else:
            continue
    keys = [k for k, v in dic.items() if v == 1]
    for x in keys:
        del dic[x]
    return dic
   

def find4tuples(matrix,removal):

    # initialization
    res = []
    dic = dict()
    
    # put the rows with ones in the same list
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                temp.append(j)
        res.append(temp)
    
    for i in range(len(res)):
        for j in range(len(removal)):
            if set(removal[j]) <= set(res[i]):
                for k in range(len(removal[j])):
                    res[i].remove(removal[j][k])
    
    
    for tup in res:
        if len(tup) >= 5:
            for i in range(len(tup)-3):
                for j in range(i+1,len(tup)-2):
                    for m in range(j+1,len(tup)-1):
                        for n in range(m+1,len(tup)):
                            if (tup[i],tup[j],tup[m],tup[n]) in dic.keys():
                                dic[(tup[i],tup[j],tup[m],tup[n])] = dic[(tup[i],tup[j],tup[m],tup[n])] + 1
                            else:
                                dic[(tup[i],tup[j],tup[m],tup[n])] = 1
        elif len(tup) == 4:
            if (tup[0],tup[1],tup[2],tup[3]) in dic.keys():
                dic[(tup[0],tup[1],tup[2],tup[3])] = dic[(tup[0],tup[1],tup[2],tup[3])] + 1
            else:
                dic[(tup[0],tup[1],tup[2],tup[3])] = 1
        else:
            continue
    keys = [k for k, v in dic.items() if v == 1]
    for x in keys:
        del dic[x]
    return dic

    
def leastcost(d,tuplesize,removal,mat):
    least = list()
    for tup in d:
        removal.append(tup)
        leastcost = 100
        if tuplesize == 2:
            temp = find2tuples(mat,removal)
        elif tuplesize == 3:
            temp = find3tuples(mat,removal)
        elif tuplesize == 4:
            temp = find4tuples(mat,removal)
            
        if len(temp) < leastcost:
            leastcost = len(temp)
            least = [tup]
        elif len(temp) == leastcost:
            least.append(tup)
            
        removal.remove(tup)
    return least
        

def greed(mat,removal):
    while True: 
        """if find5tuples(mat,removal):
            d = find5tuples(mat,removal)
            x = random.choice(list(d))
            removal.append(d[x]) """
        if find4tuples(mat,removal):
            d = find4tuples(mat,removal)
            d = leastcost(d,4,removal,mat)
            x = random.choice(list(d))
            removal.append(x)
        elif find3tuples(mat,removal):
            d = find3tuples(mat,removal)
            d = leastcost(d,3,removal,mat)
            x = random.choice(list(d))
            removal.append(x)
            
        elif find2tuples(mat,removal):
            d = dict((k, v) for k, v in find2tuples(mat,removal).items() if v >= 3)
            if d:
                d = leastcost(d,2,removal,mat)
                x = random.choice(list(d))
                removal.append(x)
            else:
                d2 = find2tuples(mat,removal)
                x = random.choice(list(d2))
                removal.append(x)
        else:
            return verification_code(mat,removal)
    
def contains(small, big):
    for i in range(len(small)):
        if small[i] in big:
            continue
        else:
            return False
    return True


def verification_code(s_mat,saved):
    """
        This function will help to calculate the number of XORs required
    """

                                       
    ################### CALCULATING THE NUMBER OF XORS SAVED ####################
    l2 = list()
    l3 = list()
    l4 = list()
    for t in saved:
        if len(t) == 2:
            l2.append(list(t))
        elif len(t) == 3:
            l3.append(list(t))
        elif len(t) == 4:
            l4.append(list(t))
    for t4 in l4:
        for t3 in l3:
            if contains(t3,t4):
                t4.remove(t3[0])
                t4.remove(t3[1])
                t4.remove(t3[2])
                t4.append(set(t3))
    for t4 in l4:
        for t2 in l2:
            if contains(t2,t4):
                t4.remove(t2[0])
                t4.remove(t2[1])
                t4.append(set(t2))
    for t3 in l3:
        for t2 in l2:
            if contains(t2,t3):
                t3.remove(t2[0])
                t3.remove(t2[1])
                t3.append(set(t2))
    XOR_saved = 0
    for temp in l2:
        #print(temp)
        XOR_saved = XOR_saved + len(temp) - 1
    for temp in l3:
        #print(temp)
        XOR_saved = XOR_saved + len(temp) - 1
    for temp in l4:
        #print(temp)
        XOR_saved = XOR_saved + len(temp) - 1
                                   
    # initialization
    res = []
    # put the rows with ones in the same list
    for i in range(len(s_mat)):
        temp = []
        for j in range(len(s_mat)):
            if s_mat[i][j] == 1:
                temp.append(j)
        res.append(temp)
    
    ### ORIGINAL COUNTER ###
    count = 0
    for row in res:
        count = count + len(row) - 1
    
    
    new = dict()
    for tup in saved:
        new[tup] = 0
    # putting them in sets 
    for i in range(len(res)):
        for j in range(len(saved)):
            if set(res[i]) >= set(saved[j]):
                new[saved[j]] = new[saved[j]] + 1
                for k in saved[j]:
                    res[i].remove(k)
                res[i].append(saved[j])
       
    
    XOR = 0
    for i in range(len(res)):
        if len(res[i]) > 1:
            XOR = XOR + len(res[i]) -1
        else:
            XOR = XOR + 1
    if XOR_saved + XOR < 108:
        print(saved)
    return XOR_saved + XOR                


def main():
    mat = getMatrix()
    removal =[]
    x = greed(mat,removal) 
       
    print(x)
    print("program ended")
    #a2 = find2tuples(mat,removal)
    #for key,value in a2.items():
    #    if value >= 2:
    #        print(key,value)
    #find3tuples(mat,removal)
    #find4tuples(mat,removal)
    #find5tuples(mat,removal)
    #verification_code(mat,removal)
    
    
    
if __name__ == '__main__':
    main()



