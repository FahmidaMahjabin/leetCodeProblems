# binary search 
# input = list in ascending order, and a target 
# output = index of the target value 
# step1:list e jodi 1 er cheye beshi element thake then,



def findTargetIndex(numbers, target):
    if len(numbers) == 0:
        return -1

    else:
        return binarySearch(numbers, 0, len(numbers) - 1, target)
        
# function = binary Search
#     step1.1:lowerLimit = 0 and upperLimit = last index and   mid index ber korbo 
# step2:jodi mid index er value target er value same hoy then mid index return korbo 
# step3:jodi same na hoy then , target choto hole , left side e search korbo where lowerLimit = lowerLimit and upper = mid-1
# step4:target boro hole right side e search korbo, right side e search korbo where lowerLimit = mid+ 1 upper = last index
def binarySearch(array, lowerLimit, upperLimit, target):
    if lowerLimit > upperLimit:
        return -1
    else:

        midIndex = (lowerLimit + upperLimit) // 2
        if array[midIndex] == target:
            return midIndex 
        elif array[midIndex] > target:
            upperLimit = midIndex -1
            return binarySearch(array, lowerLimit, upperLimit, target)
        else:
            lowerLimit = midIndex + 1
            return binarySearch(array, lowerLimit, upperLimit, target)
nums = [-1,0,3,5,9,12]

print(findTargetIndex(nums, 9))