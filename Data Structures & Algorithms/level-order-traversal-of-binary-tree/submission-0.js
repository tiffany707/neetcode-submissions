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
     * @return {number[][]}
     */
    
    levelOrder(root) {
         if(root == null) return []
        
         let deque = new Deque();
         deque.pushBack(root)
    
         let result = []

         while(deque.size() > 0){
            let arr = []
            let len = deque.size()
            for(let i = 0; i < len; i++){
                let frontVal = deque.popFront()
                if(frontVal.left) deque.pushBack(frontVal.left)
                if(frontVal.right) deque.pushBack(frontVal.right)

                arr.push(frontVal.val);
            }
            result.push(arr)

         }  
        return result

    }
}
