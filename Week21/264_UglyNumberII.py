#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Here is the detailed explanation:
    https://leetcode.com/discuss/58186/elegant-c-solution-o-n-space-time-with-detailed-explanation
    In a short:
    1. Each number is generated by a former number multiplied by 2, 3 or 5.
       That's saying, next_num = min(x * 2, y * 3, z * 5)
       where x, y, z is an pre existing number.
    2. When we find a next_num, we update the x(maybe y or z at the same time)
    """
    def nthUglyNumber(self, n):
        if n <= 0:
            return
        ugly_nums = [1] * n
        l_2, l_3, l_5 = 0, 0, 0
        for i in range(1, n):
            v_2 = ugly_nums[l_2] * 2
            v_3 = ugly_nums[l_3] * 3
            v_5 = ugly_nums[l_5] * 5
            ugly_nums[i] = min(v_2, v_3, v_5)
            if ugly_nums[i] == v_2:
                l_2 += 1
            if ugly_nums[i] == v_3:
                l_3 += 1
            if ugly_nums[i] == v_5:
                l_5 += 1

        return ugly_nums[-1]

"""
-9
0
1
160
"""