import xgboost as xgb
import numpy as np
data = np.random.rand(5,10)
# print(data)
label = np.random.randint(2, size=5)
# print label
param = {'bst:maxdepth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic'}
dtrain = xgb.DMatrix(data, label=label)
