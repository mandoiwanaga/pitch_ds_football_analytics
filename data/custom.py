import numpy as np
import scipy

def variance(sample):
    """
    Calculate variance of a sample. After learn.co
    """
    sample_mean = np.mean(sample)
    return sum([(i - sample_mean)**2 for i in sample])

def sample_variance(sample1, sample2):
    """
    Calculate sample variance. After learn.co
    """
    n_1, n_2 = len(sample1), len(sample2)
    var_1, var_2 = variance(sample1), variance(sample2)
    return (var_1 + var_2)/((n_1 + n_2)-2)

def twosample_tstatistic(sample1, sample2):
    exp_mean, sample2_mean = np.mean(sample1), np.mean(sample2)
    samp_var = sample_variance(sample1, sample2)
    n_e, n_c = len(sample1), len(sample2)
    num = exp_mean - sample2_mean
    denom = np.sqrt(samp_var * ((1/n_e)+(1/n_c)))
    return num / denom

def one_sample_ttest(sample, popmean, alpha):
    """Calculate t-value and p-value and return each"""
    
    # Population  
    mu = popmean
    
    # Sample mean (x̄) using NumPy mean()
    sample_mean = np.mean(sample)
    
    # Sample Stadard Deviation (sigma) using Numpy
    sample_std = np.std(sample, ddof=1)
    
    # Degrees of freedom
    degrees_freedom = len(sample) - 1
    
    
    #Calculate the critical t-value
    t_crit = scipy.stats.t.ppf(1-alpha, df=degrees_freedom)
    
    #Calculate the t-value and p-value      
    t_val, p_val = scipy.stats.ttest_1samp(a=sample, popmean=mu)
    
    #return results
    #if t-value is greater than t-critical than you can reject the null hypothesis
    #if p-value is less than alpha than you can reject the null hypothesis
    if t_val > t_crit and p_val < alpha:
        print("Null Hypothesis rejected. ", "t-value: ", t_val, "p-value: ", p_val)
    else:
        print("Null Hypothesis true. ", "t-value: ", t_val, "p-value: ", p_val)
    return t_val, p_val 