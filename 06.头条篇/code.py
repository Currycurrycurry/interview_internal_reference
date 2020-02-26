
# 6.1.1
def sqrtKind(nums):
    nums = set(map(abs,nums))
    return len(nums)

nums = [1,2,3,-1,-2,-3]
print(sqrtKind(nums))

# 6.1.2 ???
def walkKind(n):
    pass

# 6.1.3 
import heapq
def kMaxNum(nums, k):
    minQueue = []
    for i in nums:
        if len(minQueue) == k:
            if i > min(minQueue):
                heapq.heappop(minQueue)
                heapq.heappush(minQueue, i)
        else:
            heapq.heappush(minQueue, i)
    return min(minQueue)
nums = [1,2,3,4,5]
print(kMaxNum(nums, 2))

# 6.1.4

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPath(root):
    pass






