class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        answers = []

        for i in range(len(temperatures) -1 , -1, -1):
            print(answers)
            print("hi", arr)
            flag = False
            if arr == []:
                answers.append(0)
                arr.append((temperatures[i], i))
            else:
                top = arr[len(arr) - 1]
                while arr != [] and top[0] <= temperatures[i]:
                    arr.pop()
                    if arr != []:
                        top = arr[len(arr) - 1]
                    else:
                        answers.append(0)
                        arr.append((temperatures[i], i))
                        flag =  True
                        break
                if not flag:
                    answers.append(top[1] - i)
                    arr.append((temperatures[i], i))
        answers.reverse()
        print(answers)
        return answers
                

            