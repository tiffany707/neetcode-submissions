class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let p1 = 0;
        let p2 = heights.length;
        let max = 0;
        while (p2 > p1){
            let area = (p2-p1) * Math.min(heights[p1], heights[p2])
            if (area > max){
                max = area
            }
            
            if(heights[p1] < heights[p2]){
               p1 ++ 
            }
            else{
                p2 --
            }
        }
        return max
        

    }
}
