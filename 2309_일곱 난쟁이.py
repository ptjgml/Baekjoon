# 문제
# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 
# 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 
# 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

# 입력
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

# 출력
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

def find(one, two, sumV):
    if stack[0] >= sumV:
        return
    while two < 9:
        stack.append(height[two])

        if sum(stack) == sumV:                
            b = height.pop(two)     # 두번째 난쟁이부터 pop해야 인덱스 에러 안남
            a = height.pop(one)
            return a+b
        
        else:
            stack.pop()     
            two += 1

height = [int(input()) for _ in range(9)]
sumV = sum(height) - 100   # 일곱 난쟁이가 아닌 난쟁이들의 키의 합

stack = []

for i in range(8):
   if i+1 < 9: 
        stack.append(height[i])     # 일곱 난쟁이가 아닌 첫번째 후보 난쟁이의 키 stack에 넣어줌
        result = find(i,i+1,sumV)   
        if result == sumV:          # 후보 난쟁이들의 키가 sumV와 같다면 그만 찾기
            break
        else:
            stack.pop()     # 첫번째 후보의 키 stack에서 제거 
            

height.sort()
for k in height:
    print(k)

