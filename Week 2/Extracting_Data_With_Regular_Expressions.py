import re
file_name = input('Enter File Name: ')
with open(file_name) as f:
    s = 0
    for line in f:
        val = re.findall('[0-9]+', line)
        if len(val)>0:
            s = s+ sum([int(x) for x in val])
    print(s)

## Testcases
# 1. Input : regex_sum_42.txt
#    Output: 445833
# 2. Input : regex_sum_189811.txt
#    Output: 371775