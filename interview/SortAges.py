from typing import List


"""
    reference: https://blog.csdn.net/chenjun5845209/article/details/8062327
"""
class Solution:
    def sortAges(self, ages: List):
        if not ages:
            return None

        time_of_age = [0] * 100
        for i in ages:
            time_of_age[i] += 1

        index = 0
        for i in range(len(time_of_age)): # 执行100次
            for j in range(time_of_age[i]): # 执行time_of_age数组元素的次数
                ages[index] = i
                index += 1
        return ages


if __name__ == '__main__':
    ages = [25, 20, 23, 40, 31]
    test = Solution()
    print(test.sortAges(ages))