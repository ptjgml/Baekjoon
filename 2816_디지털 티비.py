# 문제
# 2012년 12월 31일 새벽 4시부터 지상파 아날로그 TV방송이 종료되었다. TV를 자주보는 할머니를 위해서, 상근이네 집도 디지털 수신기를 구입했다.

# 원래 상근이네 집에는 KBS1과 KBS2만 나왔다. 할머니는 두 방송만 시청한다. 이제 디지털 수신기와 함께 엄청난 양의 채널을 볼 수 있게 되었다.  하지만, 할머니는 오직 KBS1과 KBS2만 보려고 한다. 따라서, 상근이는 채널 리스트를 조절해 KBS1을 첫 번째로, KBS2를 두 번째로 만들려고 한다.

# 티비를 켜면 디지털 수신기는 시청 가능한 채널 리스트를 보여준다. 모든 채널의 이름은 서로 다르고, 항상 KBS1과 KBS2를 포함하고 있다. 상근이는 이 리모콘을 이용해서 리스트의 순서를 바꾸는 법을 알아냈다. 리스트의 왼편에는 작은 화살표가 있고, 이 화살표는 현재 선택한 채널을 나타낸다. 가장 처음에 화살표는 제일 첫 번째 채널을 가리키고 있다.

# 다음과 같은 네 가지 버튼을 이용해서 리스트의 순서를 바꿀 수 있다. 각각은 1번부터 4번까지 번호가 적혀져있는 버튼이다.

# 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
# 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
# 현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
# 현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)
# 화살표가 채널 리스트의 범위를 넘어간다면, 그 명령은 무시한다.

# 현재 채널 리스트의 순서가 주어졌을 때, KBS1를 첫 번째로, KBS2를 두 번째로 순서를 바꾸는 방법을 구하는 프로그램을 작성하시오. 방법의 길이는 500보다 작아야 한다. 두 채널을 제외한 나머지 채널의 순서는 상관없다.

# 입력
# 첫째 줄에 채널의 수 N이 주어진다. (2 ≤ N ≤ 100)

# 다음 N개 줄에는 채널의 이름이 한 줄에 하나씩 주어진다. 채널의 이름은 최대 10글자이고, 알파벳 대문자와 숫자로만 이루어져 있다.

# 이미 KBS1이 첫 번째에, KBS2가 두 번째에 있는 입력은 주어지지 않는다.

# 출력
# 상근이가 눌러야 하는 버튼을 순서대로 공백없이 출력한다.

# 예제 입력 1 
# 3
# MBC
# KBS1
# KBS2
# 예제 출력 1 
# 33
# 예제 입력 2 
# 4
# ABC1
# ABC02
# KBS2
# KBS1
# 예제 출력 2 
# 11144411144
# 예제 입력 3 
# 4
# ABC1
# ABC02
# KBS2
# KBS1
# 예제 출력 3 
# 33144413


N = int(input())
channels = [input().strip() for _ in range(N)]

result = []
cursor = 0  # 현재 화살표 위치

# KBS1을 0번으로 옮기기
kbs1_idx = channels.index("KBS1")

# 화살표를 kbs1 위치까지 이동
result.append("1" * kbs1_idx)
cursor = kbs1_idx

# KBS1을 위로 옮기기
for _ in range(kbs1_idx):
    # swap 채널
    channels[cursor], channels[cursor - 1] = channels[cursor - 1], channels[cursor]
    cursor -= 1
    result.append("4")

# KBS2 위치 다시 찾기
kbs2_idx = channels.index("KBS2")

# 화살표를 kbs2 위치까지 이동
result.append("1" * (kbs2_idx - cursor))
cursor = kbs2_idx

# KBS2를 1번 인덱스로 옮기기
for _ in range(kbs2_idx - 1):
    channels[cursor], channels[cursor - 1] = channels[cursor - 1], channels[cursor]
    cursor -= 1
    result.append("4")

print("".join(result))
