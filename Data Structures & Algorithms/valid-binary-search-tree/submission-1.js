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
    constructor(){
        this.arr = []
    }

    isValidBST(root) {
        this.rec(root)
        console.log(this.arr)
        if(this.arr.length == 1){
            return true
        }

        for(let i = 0; i < this.arr.length - 1; i++){
            if(this.arr[i] < this.arr[i + 1]) continue;
            return false
        }   
        return true
    }     

    rec(root){
        let resL
        let resR
        if(root.left) resL = this.rec(root.left)
        this.arr.push(root.val)
        if(root.right) resR = this.rec(root.right)
    }
}
