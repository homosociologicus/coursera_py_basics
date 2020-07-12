nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums = []
i, j = 0, 0
for _ in range(len(nums1) + len(nums2)):
    if i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    elif j < len(nums2):
        nums.append(nums2[j])
        j += 1
    elif i < len(nums1):
        nums.append(nums1[i])
        i += 1
print(' '.join(map(str, nums)))
