function = find out the first bad version 
input = integerNumber, n (total number of versions ), isBadVersion() that checks whether the version is bad or not 
output = first bad version  
step1: midVersion = n// 2 and check whether it's bad version or not 
step2: if badVersion i.e returns true then firstBadversion = midVersion 
    stpe2.1:midversion k abar devide korbo and check whether is't bad 
step3:if false then , midVersion = last half er mid 
    step3.1:check mid badVersion kina

def findFirstBadVersion(n):
    lowerLimit = 0
    midVersion = (lowerLimit + n)// 2
    if isBadVersion(midVersion):
        firstBadVersion = midVersion 
        lowerLimit = midVersion 
        midVersion = (firstBadVersion + lowerLimit) // 2
        if isBadVersion(midVersion):
            

