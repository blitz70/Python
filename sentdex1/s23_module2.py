#   23. Module Import Syntax

import statistics as s
from statistics import median, stdev as d, variance as v

list = [1,12,67,2,3,7,9,7,4]

print('mean:',      s.mean(list))
print('median:',    median(list))
print('stdev:',     d(list))
print('variance:',  v(list))
