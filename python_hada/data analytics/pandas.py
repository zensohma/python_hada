import pandas as pd
# Membuat Series dari list
s = pd.Series([10, 20, 30, 40])
print(s)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# Series dengan index custom
s_custom = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s_custom)
# Output:
# a    10
# b    20
# c    30
# dtype: int64

# Akses nilai
print(s_custom['b'])  # 20
print(s_custom[['a', 'c']])  # Series dengan nilai a dan c
