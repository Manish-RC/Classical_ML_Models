"""
Z-score is measure of population of datapoints that come under a particular region. This region can be represented using a standarised normal distribution.
It is nesscary to be a standarised distribution because in nomal distribution can can have a mean of any value.But in Standardised nor. dist.,
we have a mean of zero and a max stadnard deviation of +/-3.

"""
def z_score(df.column,point):
    mean=sum(df.column)/len(df.column)
    sd = np.std(df.column, ddof=1)
    point=(point-mean)/sd
    z__score=1.79*point
    print("the z-score is",z__score)
    
"""
The formula takes two parameters:

data and
ddof is a value of degrees of freedom. We apply 1, since we are calculating the standard deviation for a sample (rather than an entire population)
"""