a = []
b = [3, 5, 7]
c = ['enjoy', 'python', 'life' ]

d = ['test', 42, '56', b]

print(a)
print(b)
print(c)
print(d)

print('a의길이:', len(a))
print('b의 길이:', len(b))
print('c의 길이:', len(c))
print('d의 길이:', len(d))

print(b[0])
print(b[2])
print(b[-1])

b[0] = 3000

print(b[0])
print(b)

print(3 in b)

print('python' in c)

if 'life' in c:
    print('life is beautiful!')

for word in c:
    print(word)

for i in range(len(c)):
    print(i, c[i])

print(b)
b.append(100)
print(b)


mylist = []
for number in range(50):
    if number % 3 == 0:
        mylist.append(number)

print(mylist)
# 1

data1 = [4, 29, 41, 92, 70, 60, 43, 54, 56, 49, 77, 10, 14, 46, 52, 20, 40, 64, 93, 70, 0, 91, 20, 59, 54,
         93, 46, 89, 11, 75, 50, 16, 97, 55, 11, 32, 1, 7, 36, 55, 13, 19, 89, 96, 88, 14, 26, 2, 63, 44]
data1_unique = []
for number in data1:
    if number not in data1_unique:
        data1_unique.append(number)

print(data1_unique)
print(len(data1_unique))
print(len(data1))

# 2
for number in data1_unique :
   n = len(data1_unique)
   for i in range(0, n):
       for j in range(0, n-i-1):
           if  data1_unique[j] > data1_unique[j+1]:
               data1_unique[j], data1_unique[j+1] = data1_unique[j+1], data1_unique[j]

print(data1_unique)

# 3
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