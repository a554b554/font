import numpy as np
import scipy
import json
from scipy.optimize import minimize
def parsefile(filename):
    userlist=[]
    imglist=[]
    records=[] #records=[(ai,bi,ci,qi)...] ai := idx of first font; bi := idx of second font ci:= user id; qi := user's choice, 1 denotes chose first
    with open(filename) as f:
        for line in f:
            # print(line)
            l = json.loads(line)
            for record in l.keys():
                r = json.loads(record)
                if r['id'] not in userlist:
                    userlist.append(r['id'])
            for record in l.keys():
                r = json.loads(record)
                for keys,vals in r.items():
                    if keys == 'id':
                        continue
                    pair = keys.split('_')
                    a1 = int(pair[0])
                    b1 = int(pair[1])
                    if a1 not in imglist:
                        imglist.append(a1)
                    if b1 not in imglist:
                        imglist.append(b1)
                    c1 = userlist.index(r['id'])
                    d1 = 0
                    if(vals=='up'):
                        d1 = 1
                    records.append((a1,b1,c1,d1))
        # print(records)
        # print(userlist)
    return records, userlist, imglist

def parseLineFile(filename):
    userlist=[]
    records=[]
    imglist=[]

    with open(filename) as f:
        # initialize userlist
        for line in f:
            ss = line.split()
            username = ss[-1]
            if username not in userlist:
                userlist.append(username)
            a1 = int(ss[2])
            b1 = int(ss[3])
            if a1 not in imglist:
                imglist.append(a1)
            if b1 not in imglist:
                imglist.append(b1)
            c1 = userlist.index(username)
            d1 = 0
            if(ss[-2]=='a'):
                d1=1
            records.append((a1,b1,c1,d1))

    #check image interity
    for i in range(len(imglist)):
        if i not in imglist:
            print("miss image: "+str(i))
            exit(1)
    return records,userlist

def initilizeProb(imglist,userlist):
    # x0 = [np.random.randint(0,100) for i in range(len(imglist))]
    x0 = [50]*len(imglist)
    x0 = x0+[0.8]*len(userlist)
    # print(x0)
    bnd=[]
    for i in range(len(imglist)):
        bnd.append((0,100))
    for i in range(len(userlist)):
        bnd.append((-1, 1))
    return x0, tuple(bnd)

def fun(x, records, userlist, imglist):  #args(records, userlist, imglist, imgidxmap)
    ans=0
    imgN = len(imglist)
    userN = len(userlist)
    for r in records:
        vi = r[0]
        vj = r[1]
        # print(vi,vj)
        # if(vi==0 and vj ==1):
        #     print(r)
        if r[3]==1:
            ans = ans - np.log(1./(1+np.exp(x[imgN+r[2]]*(x[vj]-x[vi]))))
            # print(np.log(1./(1+np.exp(x[imgN+r[2]]*(x[vj]-x[vi])))))
        elif r[3]==0:
            ans = ans - np.log(1-(1./(1+np.exp(x[imgN+r[2]]*(x[vj]-x[vi])))))
            # if(vi==0 and vj ==1):
            #     print(x[vi])
            #     print(np.log(1-(1./(1+np.exp(x[imgN+r[2]]*(x[vj]-x[vi]))))))
    # print(ans)
    return ans

def printresult(x, userlist, imglist):
    for i in range(len(imglist)):
        print('img'+str(imglist[i])+': '+ str(x[i]))
    for i in range(len(userlist)):
        print(userlist[i]+': '+str(x[i+len(imglist)]))

def writeresult(x, userlist, imgidx, f):
    for i in range(len(imgidx)):
        f.write('img'+str(imgidx[i])+': '+ str(x[i])+'\n')
    for i in range(len(userlist)):
        f.write('worker '+userlist[i]+': '+str(x[i+len(imgidx)])+'\n')


if __name__ == '__main__':
    records,userlist = parseLineFile('recordA.txt')
    # print(records,len(records))
    # print(userlist,len(userlist))
    f=open('idx_a','r')
    idx = f.read()
    idx = idx.split()
    idx = list(map(int,idx))
    f.close()

    x0, bnd = initilizeProb(idx, userlist)
    res = minimize(fun, x0, args=(records, userlist, idx), bounds=bnd, options={'disp':True, 'maxiter':100000}, method='L-BFGS-B')
    print(res.x)
    ff = open('optresult.txt','w')
    # f.write(res.x)
    writeresult(res.x, userlist, idx, ff)
    ff.close()

    # print(x0, bnd, imgidxmap)
    # print('optimizing...')
    # print(imglist[2])
    # print(fun(x0,records,userlist,imglist,imgidxmap))
    # x0[0] = x0[0]+ 0.1
    # print(fun(x0,records,userlist,imglist,imgidxmap))
    # res = minimize(fun, x0, args=(records, userlist, imglist, imgidxmap), bounds=bnd, options={'disp':True})
    # print(res.x)
    # print(res.x[imgidxmap[220]])
    # printresult(res.x, userlist, imglist)
