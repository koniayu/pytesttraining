#! /usr/bin/env python
#coding=utf-8

import random

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return random.choice([nums,None,10])
    #return nums

nums = [5,2,45,6,8,2,1]

print(bubble_sort(nums))