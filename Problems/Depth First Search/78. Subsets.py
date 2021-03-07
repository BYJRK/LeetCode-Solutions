# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(cur=[], idx=0):
            # 这里的 .copy() 如果不加，在后续 cur.pop() 后
            # 已经添加的 cur 都是指向同一个引用，会跟着变，最终全变成 []
            res.append(cur.copy())

            # idx 指的是 i 从 nums 的第几个数字开始看
            # i 则是当前已经指到了哪一位，所以这里的递归调用传递的是 i + 1
            # 比如看完了 1，要看 2 和 3，那在这个循环中，idx + 1 的值是不变的
            # 改变的是 i 的值
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        dfs()

        return res

    def subsets_v2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            tmp = []
            # 这里要准备一个 tmp，之后再把它追加到 res 后面
            # 如果直接对 res 进行修改，会导致每次循环都让 res 的内容变长
            # 以至于永远无法遍历到结尾，造成死循环
            for r in res:
                tmp.append(r + [n])
            res.extend(tmp)
        return res


s = Solution()
print(s.subsets_v2([1, 2, 3]))
