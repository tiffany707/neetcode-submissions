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
     * @return {number}
     */
    goodNodes(root) {
        return this.rec(root, -Infinity)
    }

    rec(root, max){
        let resL = 0
        let resR = 0
        if(root.val >= max){
            
            max = root.val
            console.log("PREMAX", max)
            if(root.left) resL = this.rec(root.left, max)
            if(root.right) resR =  this.rec(root.right, max)
            console.log("CURR", root.val)
            console.log("MAX", max)
        console.log(resL + resR + 1)
            return resL + resR + 1
        }
        else{
            if(root.left) resL = this.rec(root.left, max)
            if(root.right) resR =  this.rec(root.right, max)
            console.log("CURR", root.val)
            console.log("MAX", max)
        console.log(resL + resR)
            return resL + resR
        }
        
    }
}
