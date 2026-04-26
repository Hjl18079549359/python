"""
需求：
    问1,2,3,4能组合成的四位数有几张情况，按照5个一行输出
要求：
    1，要求同时包含1,2,3,4这四个数字

    2，要求数字1和3不能挨着

    3，数字4不能开头

    4,5行代码搞定
"""
count=0
for s in [str(i) for i in range(1234,4322)]:
    if'1'in s and '2'in s and '3'in s and '4'in s and s[0]!='4' and '13' not in s and '31' not in s:
        count+=1
        print(s, end='\n' if count%5==0 else '\t')

print("*"*50)

print([int( s) for s in [str(i) for i in range(1234,4322)]if'1'in s and '2'in s and '3'in s and '4'in s and s[0]!='4' and '13' not in s and '31' not in s])