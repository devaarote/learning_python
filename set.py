s1={1,2,3,4}
s2=set([3,4,5,6,7])

print(s1)
print(s2)

print(type(s2))

inter=s1|s2
print("Intersection",inter)

union=s1&s2
print("union",union)

diff=s1-s2
print("diference",diff)


fs1=frozenset(s2)
print(fs1)
print(type(fs1))




