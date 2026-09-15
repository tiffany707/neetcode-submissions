class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
    
        
        let l = 1;
        let r = Math.max(...piles);
        let m = Math.floor((r+l) / 2)
        
        while(l < r){
            
            let count = h;
            for(let i = 0; i < piles.length; i++){
                count -=  Math.ceil(piles[i] / m)
                
            }
        
            if(count >= 0){
                r = m;
            }
            else{
                l = m + 1
            }

            m = Math.floor((r+l) / 2)
           
           
               
            
        }
        return r

    }
}
