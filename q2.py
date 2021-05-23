
import math
import os
import random
import re
import sys
import string

def contains(pw, criteria):
    return len(set.intersection( set(pw) , set(criteria))) > 0


def minchar(n, password):
    count = 0 
    criterias = [string.ascii_lowercase, string.ascii_uppercase, string.digits,     string.punctuation]  

    for criteria in criterias:
        if not contains(password, criteria):
            count += 1
    
    if len(password) < 8:
        missing = 8 - len(password)
        return max(count, missing)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minchar(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
