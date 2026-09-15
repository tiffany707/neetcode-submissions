/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */

    isValidBST(root) {
        return this.rec(root, -Infinity, Infinity)
    }   

    rec(root, left, right){
        let resL = true
        let resR = true
        if(root.val > left && root.val < right){
            if(root.left)  resL = this.rec(root.left, left, root.val)
            if(root.right)  resR = this.rec(root.right, root.val, right)
            return resL && resR
        }
        else{
            return false
        }
    }
}
