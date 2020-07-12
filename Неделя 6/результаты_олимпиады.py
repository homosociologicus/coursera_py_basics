class student:
    name = ''
    mark = 0
n = int(input())
st_list = []
for _ in range(n):
    data = input().split()
    st = student()
    st.name = data[0]
    st.mark = int(data[1])
    st_list.append(st)
st_list.sort(key=lambda st: st.mark, reverse=True)
for st in st_list:
    print(st.name)
