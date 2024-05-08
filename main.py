print("conflict1")
for i in range(8):
    print("word")
a, b = 9, 8
print("conflict2")
if a > b:
    print("a bigger than b")
elif b > a:
    print("b bigger than a")
else:
    print("a equal to b")
print("conflict3")