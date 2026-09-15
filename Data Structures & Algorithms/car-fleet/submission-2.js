class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let arr = position.map((key, index) => [key, speed[index]])
        arr = arr.sort((a, b) => a[0]-b[0])
        arr = arr.map(key => ((target - key[0])/key[1]))
        console.log(arr)

        let curr = -Infinity
        let res = 0
        for(let key of position){
            let val = arr.pop()
            if ( val <= curr){
                console.log(val)
            }
            else{
                curr = val
                res ++
            }
        }
        return res
    }
}
