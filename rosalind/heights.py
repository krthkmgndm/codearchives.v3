################ PROBLEM SOLNS ###################
def fibo(**kwargs):
    f, o = file_open("fibo")
    n = kwargs.get('n', int(f.readline()))
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n=n-1)+fibo(n=n-2)

def bins():
    f = open("datasets/rosalind_bins.txt", "r")
    n = f.readline().strip("\n")
    m = f.readline().strip("\n")
    arr = f.readline().strip("\n").split()
    nums = f.readline().strip("\n").split()
    o = open("outputs/rosalind_bins.txt", "w")

    for i in nums:
        low = 0
        high = int(n) - 1
        mid = 0
        sent = False

        while low <= high:
            mid = (high + low) // 2

            if arr[mid] < i:
                low = mid + 1
            elif arr[mid] > i:
                high = mid - 1
            else:
                o.write(str(mid+1)+" ")
                sent = True
                break
        if not sent:
            o.write("-1 ")

    o.close()

def ins():
    swaps = 0
    f,o = file_open("ins")
    n = int(f.readline())
    ls = [int(i) for i in f.readline().split()]
    for i in range(1, n):
        k = i
        while k > 0 and ls[k-1] > ls[k]:
            temp = ls[k]
            ls[k] = ls[k-1]
            ls[k-1] = temp
            swaps += 1
            k -= 1

    o.write(str(swaps))
    o.close()

def mer(**kwargs):
    # Parameterization
    ls = kwargs.get('ls', [])
    f, o = file_open("mer")
    n = kwargs.get('n', int(f.readline().strip("\n")))
    a = kwargs.get('a', [int(i) for i in f.readline().strip("\n").split()])
    m = kwargs.get('m', int(f.readline().strip("\n")))
    b = kwargs.get('b', [int(i) for i in f.readline().strip("\n").split()])

    # Logic
    if not a:
        return ls+b
    elif not b:
        return ls+a
    elif a[0] < b[0]:
        ls.append(a[0])
        ls = mer(ls = ls, n = n-1, a = a[1:], m = m, b = b)
    else:
        ls.append(b[0])
        ls = mer(ls = ls, n = n, a = a, m = m-1, b = b[1:])

    for i in ls:
        o.write(str(i)+" ")
    o.close()

    return ls


def deg():
    f, o = file_open("deg")
    mn = f.readline().strip("\n").split()
    deg = [0] * int(mn[0])
    for i in range(int(mn[1])):
        edge = f.readline().strip("\n").split()
        deg[int(edge[0])-1] += 1
        deg[int(edge[1])-1] += 1

    for vertex in deg:
        o.write(str(vertex)+" ")
    o.close()

def ddeg():
    f, o = file_open("ddeg")
    mn = f.readline().strip("\n").split()
    deg = [0] * int(mn[0])
    final = [0] * int(mn[0])
    edges = {}
    for i in range(int(mn[0])):
        edges[i] = []
    for i in range(int(mn[1])):
        edge = f.readline().strip("\n").split()
        deg[int(edge[0])-1] += 1
        edges[int(edge[0])-1].append(int(edge[1]) - 1)

        deg[int(edge[1])-1] += 1
        edges[int(edge[1])-1].append(int(edge[0]) - 1)

    for vertex, neighbors in edges.items():
        for edge in neighbors:
            final[vertex] += deg[edge]

    for vertex in final:
        o.write(str(vertex)+" ")
    o.close()

################ FILE HELPER ###################
def file_open(name):
        return open("datasets/rosalind_"+name+".txt", "r"), open("outputs/rosalind_"+name+".txt", "w")


################ MAIN RUN ###################
if __name__ == '__main__':
    # fibo()
    # bins()
    # ins()
    mer()
    # deg()
    # ddeg()
