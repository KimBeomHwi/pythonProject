data2 = ['business', 'switch', 'letters', 'agonizing', 'irate', 'strange', 'light', 'bone', 'clover', 'locket',
         'knock', 'part', 'throne', 'announce', 'mitten', 'claim', 'impartial', 'structure', 'vessel', 'homely',
         'arrange', 'ticket', 'growth', 'quarrelsome', 'satisfying', 'avoid', 'panoramic', 'perfect', 'beautiful', 'escape',
         'daily', 'subtract', 'knowledgeable', 'argument', 'butter', 'invincible', 'rhetorical', 'overflow', 'humor', 'tease',
         'noxious', 'crime', 'truculent', 'shake', 'bridge', 'bulb', 'phobic', 'icky', 'immense', 'space']

def third_sort(arr):
    for a, p in enumerate(arr):
        for b, q in enumerate(arr):
            if a != b:
                if len(p) < len(q):
                    arr[a], arr[b] = arr[b], arr[a]

    n = len(arr[a])
    data_A = []
    data_B = []
    for c in range(1, n+1):
        for d, f in enumerate(arr):
            if len(f) == c:
                data_A.append(f)
            elif len(f) != c:
                continue
        data_A.sort()
        data_B.extend(data_A)
        data_A.clear()
    print(data_B)

print(third_sort(data2))
