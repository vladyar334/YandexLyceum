n, x, y = [int(i) for i in input().split(" ")]
count_ = 0
for i in range(1, n + 1):
    if x == y and str(i).count(str(x)) == len(str(i)):
        count_ += 1
    if x != y and str(i).count(str(x)) + str(i).count(str(y)) == len(str(i)):
        count_ += 1
print(count_)
