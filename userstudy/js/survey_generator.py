import json
import numpy as np
import random

def pair_generator(length, pair_size):
    pairidx=[]
    paircount=[0]*length
    for i in range(length):
        while 1:
            if paircount[i] >= pair_size:
                break
            idx = np.random.randint(0,length)
            if idx == i:
                continue
            elif paircount[idx] >= pair_size:
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

def loadpairidx(filename):
    pairidx=[]
    with open(filename) as fp:
        for line in fp:
            pair = line.split()
            pairidx.append((int(pair[0]), int(pair[1])))
    return pairidx

def generate_survey(samples, pairidx, question_per_survey, idx0):
    surveys=[]
    # print(len(pairidx))
    assert(len(pairidx)%question_per_survey==0)
    num_of_survey = int(len(pairidx)/question_per_survey)
    paircount=0
    for i in range(num_of_survey):
        surveyJSON={}
        surveyJSON['title'] = 'Tell us, which one is more similar to characters in the center?'
        surveyJSON['pages'] = []
        for j in range(question_per_survey):
            page={}
            page['name'] = 'page'+str(j+1)
            page['questions'] = []
            q1 = {}
            q1['type'] = 'html'
            q1['html'] = '<img src="./Mturk/'+str(samples[pairidx[paircount][0]])+'.png" width="200px" /><p>'
            q1['html'] = q1['html']+ '<img src="./Mturk/'+str(idx0)+'.png" width="200px" /><p>'
            q1['html'] = q1['html']+ '<img src="./Mturk/'+str(samples[pairidx[paircount][1]])+'.png" width="200px" />'
            page['questions'].append(q1)
            q2={}
            q2['type'] = 'radiogroup'
            q2['name'] = str(pairidx[paircount][0])+'_'+str(pairidx[paircount][1])
            paircount = paircount + 1
            q2['choices'] = ['up', 'down']
            q2['isRequired'] = True
            page['questions'].append(q2)
            surveyJSON['pages'].append(page)

        page={}
        page['name'] = 'last'
        page['questions'] = []
        q1={}
        q1['type'] = 'comment'
        q1['name'] = 'id'
        q1['title'] = 'Your ID'
        page['questions'].append(q1)
        surveyJSON['pages'].append(page)
        surveys.append(surveyJSON)
    return surveys




if __name__ == '__main__':
    samples = loadsampleidx('index3')
    idx0 = 1860 #len(pair)=845 #len(samples)=169
    pairidx = loadpairidx('taskpair3')
    random.shuffle(pairidx)
    # print(pairidx)
    # print(len(pairidx))
    # print('"\'\'"')
    surveys = generate_survey(samples, pairidx, 17, idx0)
    print(json.dumps(surveys))






# print(samples)
# taskpair=[]
# pidx = pair_generator(len(samples), 8)
# for pair in pidx:
#     print(samples[pair[0]], samples[pair[1]])


# print(np.random.randint(0,2))
# samples = np.random.randint(0,440,80)
# print(samples)


# print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
