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
     * @return {number[]}
     */
    rightSideView(root) {
        if(!root){
            return []
        }
        let currArr = [root]
        let nextArr = []
        let res = []
        console.log(currArr)
        console.log(nextArr)



        while (currArr.length || nextArr.length){
            let node 
            while(currArr.length){
                if(currArr.length == 1){
                    node = currArr.shift()
                    res.push(node.val)
                    if(node.left){
                        nextArr.push(node.left)
                    }
                    if(node.right){
                        nextArr.push(node.right)
                    }
                }
                else{
                    node = currArr.shift()
                     if(node.left){
                        nextArr.push(node.left)
                    }
                    if(node.right){
                        nextArr.push(node.right)
                    }
                }
                console.log(node.val)
            }

            while(nextArr.length){
                if(nextArr.length == 1){
                    node = nextArr.shift()
                    res.push(node.val)
                     if(node.left){
                        currArr.push(node.left)
                    }
                    if(node.right){
                        currArr.push(node.right)
                    }
                }
                else{
                    node = nextArr.shift()
                    if(node.left){
                        currArr.push(node.left)
                    }
                    if(node.right){
                        currArr.push(node.right)
                    }
                }
                 console.log(node.val)
            }
        }
        return res
    }
}
