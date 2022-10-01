
from pandas_ods_reader import read_ods
import pandas
from pylr2 import regress2
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
base_path ="OC1 SMA.ods"

sheet_index = 1
df = read_ods(base_path , sheet_index )


n_and_p=df.to_numpy()

n=n_and_p[:,0]
p=n_and_p[:,1]


results = regress2(n, p, _method_type_2="reduced major axis")


olr_slope, olr_intercept, olr_r, olr_p, olr_std_err = stats.linregress(n, p)

plt.figure(1)
plt.plot(n, p, 'o')



r=results.get('r')
slope=results.get('slope')
intercept=results.get('intercept')


X=np.arange(35)
plt.plot(X, X*slope + intercept, 'r', label='MODEL II regression')

plt.plot(X, X*olr_slope + olr_intercept, 'g', label='olr regression')
plt.title('Graph of MODEL II regression')
plt.legend(loc='upper left')
plt.xlabel('NITRATE_NITRITE_UMOL/KG')
plt.ylabel('PHOSPHATE_UMOL/KG')

print('slope of model 2:',slope,'intercept of model 2:',intercept,'model 2 r squre:',r)

print('slope of olr:',slope,'intercept of olr:',intercept,'olr r squre:',olr_r)