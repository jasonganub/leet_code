def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    num_hash = {}
    st = []
    result = []

    for i in nums:
        # while the st has an item and the last item is less than current item
        while len(st) and st[-1] < i:
            # add it to num hash and remove it from st
            num_hash[st.pop()] = i
        st.append(i)

    for i in findNums:
        result.append(num_hash.get(i, -1))
    return result


findNums = [4,1,2]
nums = [1,3,4,2]
#nums = [6,5,4,3,2,1,7]
print(nextGreaterElement(findNums=findNums, nums=nums))