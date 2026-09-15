class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionaryOfDictionaries = {}
        for key in strs:
            dictionary = {}
            isDict = False
            
            for key2 in key:
                dictionary[key2] = 1 + dictionary.get(key2, 0)
                
            for dict in dictionaryOfDictionaries:
                if dictionaryOfDictionaries[dict][0] == dictionary:
                    isDict = True
                    temp = dictionaryOfDictionaries[dict][1]
                    temp.append(key)
                    print("temp", temp)
                    dictionaryOfDictionaries[dict] = [dictionary, temp]
                    
            if isDict == False:
                dictionaryOfDictionaries[key] = [dictionary, [key]]
            
            
            # tempList = dictionaryOfDictionaries.get(key, [])
            # print("hi", tempList)
            # dictionaryOfDictionaries[dictionary] = tempList.append(key)
            # print("bye",dictionaryOfDictionaries[dictionary] )
        list = []
        for key in dictionaryOfDictionaries:
            list.append(dictionaryOfDictionaries[key][1])
        return list