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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let res = this.transversal(root, 0, k)
        return res[1]
        
    }

    transversal(root, count , k){
        if(root == null){
            return [0 + count, null]
        }
        console.log(root.val)
        let l = this.transversal(root.left, count ,k) 
        let m = [l[0] + 1, l[1]]
        console.log(m)
        let r = this.transversal(root.right, m[0], k) 
        if(l[1] != null){
            r[1] = l[1]
        }
        else if( m[0] == k){
            r[1] = root.val
        }
        return r 
    }
}
