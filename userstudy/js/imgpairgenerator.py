import numpy as np
def pair_generator(length, pair_size):
    pairidx=[]
    paircount=[0]*length
    print('length', length)
    for i in range(length):
        while 1:
            if paircount[i] >= pair_size:
                break
            idx = np.random.randint(0,length)
            print(i, paircount[i])
            if idx == i:
                continue
            elif paircount[idx] >= pair_size:
                continue
            elif (i, idx) in pairidx:
                continue
            elif (idx, i) in pairidx:
                continue
            else:
                pairidx.append((i,idx))
                paircount[i] = paircount[i] + 1
                paircount[idx] = paircount[idx] + 1
    return pairidx

def loadsampleidx(filename):
    f = open(filename)
    st = f.read()
    st = st.split()
    f.close()
    samples = list(map(int,st))
    return samples


if __name__ == '__main__':
    samples = loadsampleidx('index3')
    pid = pair_generator(len(samples), 10)
    print(len(pid), pid)
