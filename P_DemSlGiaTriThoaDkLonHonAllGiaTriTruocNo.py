L = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
count = sum(1 for i in range(1, len(L)) if all(L[i] > x for x in L[:i]))
print("Số lượng giá trị thỏa điều kiện là: ", count)

