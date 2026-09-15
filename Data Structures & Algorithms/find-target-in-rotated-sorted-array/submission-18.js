class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length - 1;
        let m = Math.floor((l+r)/ 2);

        while( l <= r ){
            console.log(m)
            if(target == nums[m]){
                return m
            }

           //left
            if(nums[l] <= nums[m]){
                if(target < nums[m] && target >= nums[l]){
                    r = m - 1
                }
                else{
                    l = m + 1
                }
            }
            else{
                if(target > nums[m] && target <= nums[r]){
                    l = m + 1
                }
                else{
                    r = m - 1
                }
            }
           //right
           m = Math.floor((l+r)/ 2);
        }
        return -1
    }
}
