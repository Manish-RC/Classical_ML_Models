import numpy as np
from sklearn.neighbors import LocalOutlierFactor
def lof(df,col1,col2):
    c = np.column_stack((df[col1], df[col2]))
    clf = LocalOutlierFactor(n_neighbors=2)
    clf.fit_predict(c)