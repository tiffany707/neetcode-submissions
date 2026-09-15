class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if(this.keyStore.has(key)){
            this.keyStore.get(key).push([value, timestamp])
        }
        else{
            this.keyStore.set(key,[[value, timestamp]])
        }
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        
        let arr = this.keyStore.get(key)
        if(!arr) return ""
        let l = 0
        let r = arr.length - 1
        let m = Math.floor((l+r)/2)
        let res = ""
        
        while(l <= r){
           
            if(arr[m][1] <= timestamp ){
                res = arr[m][0]
                l = m + 1
                
            }
            else{
                r = m - 1
            }
            m = Math.floor((l+r)/2)
        }
        
        return res
    }
}
