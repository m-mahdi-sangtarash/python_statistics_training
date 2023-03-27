import statistics as ss

data1 = [0, -1, 3, 4, 3, 4, 0, 5, 8, 9, -4, 0, 4, 5]
data2 = [456.7, 547.8, 926.6, 236.1, 543, 439]

print("mean data 1: ", ss.mean(data1))
print("mean data 2: ", ss.mean(data2))
print("harmonic mean data 1: ", ss.harmonic_mean(data1))
print("harmonic mean data 2: ", ss.harmonic_mean(data2))
print("median data 1: ", ss.median(data1))
print("median data 2: ", ss.median(data2))
print("variance data 1: ", ss.pvariance(data1))
print("variance data 2: ", ss.pvariance(data2))
print("std data 1: ", ss.pstdev(data1))
print("std data 2: ", ss.pstdev(data2))