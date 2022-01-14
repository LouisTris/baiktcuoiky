def demkytutrongten():
    count_lower = 0
    for c in s:
        if c.islower():
            count_lower += 1
    print("Xuất tên sinh viên:", s .title())
    print("Số ký tự trong tên:", count_lower)
s = str(input("Nhập tên của sinh viên: "))
demkytutrongten()

n=int(input("Nhập số ký tự trong tên = "))

d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)