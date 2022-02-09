


# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# function = getFirstBadVersion 
# input = n where n is the version 
# output = first bad version , isBadVersion() that returns true if it's a bad version else false
# step1:define lower = 0 and upper = n 
# step2: lower > upper na howa porjonto 
#     step2.1: mid = (lower+upper) /2 ber korbo and check korbo j eta bad version kina 
#     step2.2: jodi badVersion hoy then first bad version mid er age pabo 
#         step2.2.1:upper hobe mid-1 and save the firstBadVersion 
#     step2.3:jodi badVersion na hoy then first bad version mid er porer part e pabo 
#         step2.3.1: lower = mid+1 
# step3: return firstBadVersion 

def getFirstBadVersion(n):
    lower = 0
    upper = n 
    while lower <= upper:
        return binarySearch(lower, upper, isBadVersion)

def binarySearch(lower, upper, versionChecker):
    mid = (lower + upper) // 2
    if versionChecker(mid):
        firstBadVersion = mid 
        upper = mid -1
    else:
        lower = mid + 1
    return firstBadVersion

def getFirstBadVersion(n):
    lower = 0
    upper = n 
    while lower <= upper:
        mid = (lower + upper) // 2
        if isBadVersion(mid):
            firstBadVersion = mid 
            upper = mid -1
        else:
            lower = mid + 1
    return firstBadVersion