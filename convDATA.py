import os
import numpy as np
import itertools

def convertDATA(file):
    cur = os.getcwd()
    F = open(cur+"/"+file, 'r')
    latitude = F.readline()
    longitude = F.readline()
    n_points = F.readline()

    

    lat = [float(x) for x in latitude.split()]
    lng = [float(x) for x in longitude.split()]
    n_p = [float(x) for x in n_points.split()]

    points = [[float(x) for x in line.split()] for line in F]
    
    maxHeight = -10e99
    minHeight = 10e99
    for i in points:
        
        if(max(i)>maxHeight):
            maxHeight = max(i)
        elif(min(i)<minHeight):
            minHeight = min(i)
    
    new_res = np.array(points)
    new_res = (new_res - np.min(new_res))/np.ptp(new_res)


    res1 = []

    for dx_i, i in enumerate(new_res):
       for dx_j, j in enumerate(i):
            res1.append([float(dx_j/(n_p[0]-1)), j, float(dx_i/(n_p[1]-1))])

    res1 = np.array(res1)
    print(len(res1),len(res1[0]))


    G = open(cur+"/res",'w')
    G.write("Lista de Pontos\n")
    for dx_i, i in enumerate(res1):
        G.write(" %f, %f, %f,\n" % (i[0],i[1],i[2]))
    G.close()
    
    n_vextex_point = 0
    G = open(cur+"/res_idx",'w')
    G.write("Index de Pontos\n")
    for i in range(int(n_p[1]-1)):
        for j in range(int(n_p[0]-1)):
            n_vextex_point += 1
            if(i+2 >= n_p[1] and j+2 >= n_p[0]):
                G.write("%d, %d, %d, %d, %d, %d\n" % ( (n_p[0]*i+j),(n_p[0]*i+j+1),(n_p[0]*(i+1)+j),(n_p[0]*i+j+1), (n_p[0]*(i+1)+j) , (n_p[0]*(i+1)+j+1) ))
            else:
                G.write("%d, %d, %d, %d, %d, %d,\n" % ( (n_p[0]*i+j),(n_p[0]*i+j+1),(n_p[0]*(i+1)+j),(n_p[0]*i+j+1), (n_p[0]*(i+1)+j) , (n_p[0]*(i+1)+j+1) ))

    G.close()

    G = open(cur+"/res_VertexCount",'w')
    G.write("VextexCount: %d\n" % (n_vextex_point*6))
    G.close()

    F.close()
convertDATA("SP.pto")