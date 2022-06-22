nums1=[1, 2]
nums2=[41,5]
nums1.extend(nums2)
nums1.sort()
print(nums1)
print(len(nums1) / 2)
if len(nums1) / 2 == int(len(nums1) / 2):
    k = int(len(nums1) / 2 - 1)
    z = int(len(nums1) / 2)
    median = (nums1[k] + nums1[z]) / 2
    print (median)
else:
    z = int(len(nums1) / 2 )
    median = nums1[z]
    print (median)
