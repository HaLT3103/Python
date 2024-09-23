N = 10004
par = [i for i in range(N)]
rankz = [0] * N

def init():
    global par, rankz
    for i in range(N):
        par[i] = i
        rankz[i] = 0

def find(u):
    global par
    if par[u] != u:
        par[u] = find(par[u])
    return par[u]

def join(u, v):
    global par, rankz
    u = find(u)
    v = find(v)
    if u == v:
        return
    if rankz[u] == rankz[v]:
        rankz[u] += 1
    if rankz[u] < rankz[v]:
        par[u] = v
    else:
        par[v] = u

def main():
    init()
    Q = int(input())
    for _ in range(Q):
        u, v, t = map(int, input().split())
        if t == 1:
            join(u, v)
        else:
            u = find(u)
            v = find(v)
            if u == v:
                print(1)
            else:
                print(0)

if __name__ == "__main__":
    main()
