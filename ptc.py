# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    Bank = ''.join(input())
    if(re.match(r'^[456]', Bank) and
      (re.match(r'([\d]{4}-){3}[\d]{4}$', Bank) or
      re.match(r'[\d]{16}', Bank)) and not
      re.search(r'(\d)\1{3,}', Bank.replace('-', ''))):
        print('Valid')
    else:
        print('Invalid')