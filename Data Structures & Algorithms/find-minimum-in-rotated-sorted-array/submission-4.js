class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0
        let r = nums.length - 1
        let m = Math.floor((l+r) / 2)

        while(l < r){
    
            if(nums[r] < nums[m]){
                l = m + 1
            }
            else{
                r = m
            }
           
            m = Math.floor((l+r) / 2)
        }

        return nums[r]
    }
}
