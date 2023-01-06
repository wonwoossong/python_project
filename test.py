n_lst=list(range(1,31))
print(n_lst)

for i in range(28):
    lst=int(input())
    n_lst.remove(lst)
print(min(n_lst))
print(max(n_lst))