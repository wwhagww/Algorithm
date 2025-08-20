# 15678 연세워터파크
from heapq import heappop, heappush
N, D = map(int, input().split())
arr = list(map(int, input().split()))

positive_idx = []
for i in range(N):
    if arr[i] > 0:
        positive_idx.append(i)
len_pos = len(positive_idx)

# 최소 양수 노드 2개는 보장됨
if len(positive_idx) <= 1:
    print(max(arr))
    exit()


# 첫번째 양수 노드부터 시작
cur_idx = 0
cur = positive_idx[0]
score = arr[cur]

score_max = 0

visited = [False]*N
while True:
    if cur_idx+1 >= len_pos:
        # 마지막 양수 노드까지 순회 완료
        score_max = max(score_max, score)
        break

    # 다음 양수 노드 정의해주기
    nxt_idx = cur_idx + 1
    nxt = positive_idx[nxt_idx]

    # 다음 양수 노드까지 한번에 갈 수 있으면
    if nxt - cur <= D:
        # 그냥 가기
        score += arr[nxt]
        cur_idx =  nxt_idx; cur = nxt
        continue

    que = [(0, cur)]
    while que:
        cost, node = heappop(que)
        if node == nxt: 
            # 다음 양수 노드 도달하면 
            # 비용는 빼주고 양수 노드 값은 더해주기
            # score - cost 는 항상 양수 보장됨
            score_max = max(score_max, score)
            score += arr[nxt] - cost
            cur_idx = nxt_idx; cur = nxt
            break

        if visited[node]: continue
        visited[node] = True
        
        # 다음 갈수있는 노드 순회
        for n in range(node+1, min(node+D+1, nxt+1)):
            # 이미 방문했다는건 최솟값 아니라는 뜻
            if visited[n]: continue
            # 다음 노드가 양수 노드면 비용에 포함되면 안됨
            new_cost = cost + max(0, -arr[n])
            # 현재까지 얻은 점수보다 비용이 큰 경우는 무시
            if score - new_cost <= 0: continue
            heappush(que, (new_cost, n))
    else: # 다음 양수 노드 도달 못하면 초기화
        score_max = max(score_max, score)
        score = arr[nxt] 
        cur_idx = nxt_idx; cur = nxt
print(score_max)