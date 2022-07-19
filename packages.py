import numpy as np

# a =np.array([[11,23,256],
#               [859,4587,1000]])

# b =np.array([[10,365,425],
#              [125,859,500]])
             
# c = a+b
# print(*c)                                                   # [ 12  59 612] [1427 5446 5785]                               
# e = a-b
# print(*e)                                                     # [  10  -13 -100] [  291  3728 -3785]
# print(*e)                                                     
# v = a*b
# print(*v)                                                       # [   11   828 91136] [ 487912 3940233 4785000]

# u = a/b
# print(*u)                                                         # [11.          0.63888889  0.71910112] [1.51232394 5.33993015 0.20898642]

# print(*5*b)                                                         # [   5  180 1780] [ 2840  4295 23925]

# print(b**5)                                                           # [      1  759375 9765625] [ 24300000 184528125 503284375]

# c = np.array([[10,20,33],
#               [40,50,60]])
# print(c**5)
# print(630**5)


# x =np.array([[11,23,256],
#               [859,4587,1000]])

# y =np.array([[10,365,425],
#              [125,859]])

# print(x+y)                                          # ValueError: operands could not be broadcast together with shapes (2,3) (2,)


''' By default identity matrix is float'''
# r = np.eye(2)                                         # [[1. 0.]
# h = np.eye(2,dtype=int)
# g = np.eye(3,dtype=bool)
# print(h)
# print(r)                                              # [0. 1.]]
# print(g)


# t = np.array([c for c in range(0,17,2)])
# g= t.reshape(3,3)
# print(g)


# k = np.array([[1.2,25.3,56.9],
#               [45.1,50.0,0.00]])
# f = k.astype('int')
# print(f)                                        #To convert the list of array nto int type.


# a = np.array([[1,0,0],
#               [0,1,0],
#               [0,0,1]])
# b = a.astype('bool')
# print(b)                                     # To convert the numpy arrays into bool values


# v = np.array([[1,23,56.2],
#               [8988,0,859],
#               [452,1.023,1]])
# x = v.astype('bool')
# print(x)                                        # Doubt session


# j = np.array([[10,23,154],
#               [45,569,145]])
# l = np.array([[45,78,96],
#                [125,458,23.3]])                 # [[ 10.   23.  154.   45.   78.   96. ],
# d =np.hstack([j,l])                             #        [ 45.  569.  145.  125.  458.   23.3]]
# print(d)                               


# o = np.array([[10,23,154],
#               [45,569,145]])
# q = np.array([[45,78,96],
#              [125,458,23.3]])
# t = np.vstack([o,q])
# print(t)



# r= ([g for g in range(0,101,3)])
# u = np.array(r)
# print(u)                                         # [ 0  3  6  9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99]
 

# y = np.array([10,20,30,40,50])
# m = np.array([10,50,30,20,40])
# w = np.array(np.where(y==m))
# print(w)                                            # [[0 2]]


# l = np.full([3,3],10)
# print(l)

# h = np.zeros([3,3])
# i = np.array(h,dtype=int)
# print(i) 
                                          

# z = np.array([[1,2,3],
#               [6,7,8],
#               [80,14,2.3]])   
# s = np.array([[12.3,45.3,78],
#               [48,78,96.3],
#                [123,456,789]])    
# b = z@s                                  
# print(b)
# v = np.matmul(z,s)
# print(v)                                       # Matrix multiplication.


# g = np.array([[1,2,3],
#              [4,5,6],
#               [7,8,9]])
# x = g.T
# print(x)                                  #  rows will be columns and columns will be rows


# print(dir(np))