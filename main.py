def solve(N,K,categories,cooking_times):
    category_times={}
    for i in range(N):
        category=categories[i]
        time=cooking_times[i]
        if category not in category_times or time < category_times[category]:
            category_times[category]=time
    if len(category_times)<K:
        return -1
    total_time=sum(sorted(category_times.values())[:K])
    return total_time


T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    categories=list(map(int,input().split()))
    cooking_times=list(map(int,input().split()))
    result = solve(N,K,categories,cooking_times)
    print("Minimum Time required to have the meal",result)
    