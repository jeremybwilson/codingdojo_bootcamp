for num in range(0,4):
  print num

def find_minimum(nums):
  min = nums[0]
  for idx in range(1,len(nums)):
    if nums[idx] < min:
      min = nums[idx]
  print min

find_minimum([55,12,-5])