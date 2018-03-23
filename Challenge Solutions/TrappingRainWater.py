class Solution1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curmax = 0
        prevmaxpos = 0
        ret = 0
        for i in range(len(height)):
            if height[i] >= curmax:
                for j in range(prevmaxpos, i):
                    ret += curmax - height[j]
                prevmaxpos = i
                curmax = height[i]

        curmax = 0
        prevmaxpos = len(height) - 1
        for i in range(len(height) - 1, -1, -1):
            if height[i] > curmax:
                for j in range(prevmaxpos, i, -1):
                    ret += curmax - height[j]
                prevmaxpos = i
                curmax = height[i]

        return ret


class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(height)):
            leftmax = i
            rightmax = i

            for lp in range(i):
                if height[lp] > height[leftmax]:
                    leftmax = lp

            for rp in range(i,len(height)):
                if height[rp] > height[rightmax]:
                    rightmax = rp

            ret += min(height[leftmax], height[rightmax]) - height[i]

        return ret

class Solution3:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0:
            return 0
        ret = 0
        lmaxs = [height[0]]
        rmaxs = [height[-1]]

        for i in range(1, len(height)):
            lmaxs.append(max(lmaxs[i - 1], height[i]))

        for i in range(2, len(height) + 1):
            print(height[-i])
            print(rmaxs[i - 2])
            print(rmaxs)
            rmaxs.append(max(rmaxs[i - 2], height[-i]))

        rmaxs.reverse()

        for i in range(len(height)):
            #print(lmaxs[i])
            #print(rmaxs[i])
            ret += min(lmaxs[i], rmaxs[i]) - height[i]

        return ret

class Solution4:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ret = 0

        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break;
                dist = i - stack[-1] - 1
                level = min(height[i], height[stack[-1]]) - height[top]
                ret += level * dist
            stack.append(i)

        return ret

class Solution5:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        ret = 0
        while left < right:
            if leftmax < rightmax:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ret += leftmax - height[left]
                    left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ret += rightmax - height[right]
                    right -= 1

        return ret
