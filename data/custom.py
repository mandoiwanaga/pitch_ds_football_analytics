import numpy as np

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

