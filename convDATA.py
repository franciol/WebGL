import os
import numpy as np
import itertools


def convertDATA(file, file2):
    points_index = ''
    triangles_def = ''
    vertex_count = 0

    cur = os.getcwd()
    F = open(cur+"/"+file, 'r')
    latitude = F.readline()
    longitude = F.readline()
    n_points = F.readline()

    lat = [float(x) for x in latitude.split()]
    lng = [float(x) for x in longitude.split()]
    n_p = [float(x) for x in n_points.split()]
    points = [[float(x) for x in line.split()] for line in F]

    new_res = np.array(points)
    new_res = (new_res - np.min(new_res))/np.ptp(new_res)

    res1 = []
    for dx_i, i in enumerate(new_res):
        for dx_j, j in enumerate(i):
            res1.append([float(dx_j/(n_p[0]-1)), j, float(dx_i/(n_p[1]-1))])

    
    F.close()

    F = open(cur+'/'+file2, 'r')
    n_p1 = int(F.readline())
    points = []
    lat1 = []
    lng1 = []
    for i in range(n_p1):
        tmp = F.readline().split()
        lat1.append(abs(float(tmp[1])-lat[1])/abs(lat[0]-lat[1]))
        lng1.append(abs(float(tmp[0])-lng[1])/abs(lng[0]-lng[1]))

    F.close()

    
    
    s = 0
    
    for dx_i, i in enumerate(res1):
        s+=1
        points_index += ((" %f, %f, %f,\n" % (i[2], i[1], i[0])))
        
    for i in range(len(lat1)):
        points_index += ((" %f, %f, %f,\n" % (lng1[i], 1.0, lat1[i])))
        

    for i in range(int(n_p[1]-1)):
        for j in range(int(n_p[0]-1)):
            vertex_count += 6
            triangles_def += ("%d, %d, %d, %d, %d, %d,\n" % ((n_p[0]*i+j), (n_p[0]*i+j+1), (n_p[0]*(
                i+1)+j), (n_p[0]*i+j+1), (n_p[0]*(i+1)+j), (n_p[0]*(i+1)+j+1)))

    for i in range(s,s+n_p1-2):
        vertex_count += 3
        triangles_def += ("%d, %d, %d,\n" % (i,i+1,i+2))
        print(("%d, %d, %d,\n" % (i,i+1,i+2)))

    vertex_count += 3
    triangles_def += ("%d, %d, %d,\n" % (s+n_p1-2,s+n_p1-1,s))
    vertex_count += 3
    triangles_def += ("%d, %d, %d,\n" % (s+n_p1-1,s,s+1))
   

    F = open('vars.js', 'w')

    F.write('const positions1 = [\n')
    F.write(points_index)
    F.write(']\n')

    F.write('const idx_pontos = [\n')
    F.write(triangles_def)
    F.write(']\n')


    F.write('const vertexCount1 = %d;\n' % vertex_count)
    print((lat[0],lat[1]), (lng[0],lng[1]))
    print(n_p)


convertDATA("SP.pto", "SP.ctr")
