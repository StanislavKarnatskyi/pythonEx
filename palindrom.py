st = input()
st = st.lower()
print(st)
st1 = ""

for i in range(1, len(st)+1):
    st1 += st[-i]

print(st1)


if st == st1:
    print("Palindrom")
else:
    print("Isn't palidnrom")