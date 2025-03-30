
def get_ways(n,i,ans, final_ans):
    if i == n:
        final_ans.append(ans)
        return
    if i > n:
        return
    for j in range(1,7):
        get_ways(n, i+j, ans+str(j), final_ans)

final_ans = []
get_ways(3,0,'', final_ans)
print(final_ans)