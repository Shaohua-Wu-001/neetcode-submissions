class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Area = width * min(h1, h2)
        # i.e. Area = (j - i) * min(heights[i], heights[j])
        
        # 該初始化的變數為以下
        left, right = 0, len(heights)-1
        max_area = 0

        # 一樣為 two pointer 解題法

        while left < right:
            width = right - left #底邊

            if heights[left] < heights[right]:
                curr_heights = heights[left]
                current_area = width*curr_heights
                left += 1

            else:
                curr_heights = heights[right]
                current_area = width*curr_heights
                right -= 1
            
            max_area = max(max_area, current_area)

        return max_area