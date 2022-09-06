import numpy
def out_iqr(df , column):
    q25, q75 = numpy.quantile(df[column], 0.25), numpy.quantile(df[column], 0.75)
    # calculate the IQR
    iqr = q75 - q25
    # calculate the outlier cutoff
    cut_off = iqr * 1.5
    # calculate the lower and upper bound value
    lower, upper = q25 - cut_off, q75 + cut_off
    print('The IQR is',iqr)
    print('The lower bound value is', lower)
    print('The upper bound value is', upper)
    df1 = df[(df[column] > upper)  | (df[column] < lower)]
    print('Total number of outliers are', len(df1))
    return df1

# Q1 = data.quantile(q=.25)
# Q3 = data.quantile(q=.75)
# IQR = data.apply(stats.iqr)

# #only keep rows in dataframe that have values within 1.5*IQR of Q1 and Q3
# data_clean = data[~((data < (Q1-1.5*IQR)) | (data > (Q3+1.5*IQR))).any(axis=1)]
