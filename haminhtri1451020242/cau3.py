t = str(input("Nhập tên đầy đủ của bạn"))
print("Tên đầy đủ của bạn là: ",t);
def demkytufullname():
    count_lower1 = 0
    for c in s:
        if c.islower():
            count_lower1 += 1

    count_lower2 = 0
    for c in n:
        if c.islower():
            count_lower2 += 1
    count_lower3 = 0
    for c in x:
        if c.islower():
            count_lower3 += 1
    print("Xuất tên sinh viên:",x .title() + s .title() + n .title())
    print("Số ký tự trong tên:", count_lower3)
    print("Số ký tự trong tên đệm:", count_lower1)
    print("Số ký tự trong tên:", count_lower2)

x = str(input("Nhập họ của sinh viên: "))
s = str(input("Nhập tên đệm của sinh viên: "))
n = str(input("Nhập tên của sinh viên: "))
demkytufullname()

def soThuanNghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;


n = (input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", soThuanNghich(n));