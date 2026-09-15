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
            let min = Math.min(nums[l], nums[m], nums[r]);
            if(min == nums[r]){
                l = m + 1
            }
            else if (min == nums[m]){
                r = m
            }
            else{
                return nums[l] 
            }
            m = Math.floor((l+r) / 2)
        }

        return nums[r]
    }
}
