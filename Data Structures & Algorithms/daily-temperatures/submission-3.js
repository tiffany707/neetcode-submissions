class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let result = new Array(temperatures.length).fill(0)
        let stack = []


        for(const [i, temp] of temperatures.entries()){
            console.log(`${stack} and ${result}`)
            while(stack && temperatures[stack[stack.length - 1]] < temp){
                const popped = stack.pop()
                result[popped] = i - popped
            }
            stack.push(i)

        }

        return result
    }
}
