def isPrime(num):
    if num <= 1:
        return False
    else:
        if num == 2:
            return True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def solution(nums):
    answer = 0

    numList = []
    newNum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                newNum = nums[i]+nums[j]+nums[k]
                numList.append(newNum)
    
    for num in numList:
        answer += isPrime(num)
    return answer

nums = [1,2,7,6,4]
print(solution(nums))