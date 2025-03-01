"""""
WAP for reverse string by more than 3 way

"""
# For reverse 1st way Extended Slice Method [start,stop,step]

x = 'abcderfghijkl'
print(x[::-1])

# taking reverse by one step gap

print(x[::-2])

# taking the string from 0 to last by gap of 2

print(x[::2])

# taking reverse of string excluding first two elements

y = x.replace(x[0:2],'', 1) # Replacing the first two elements
print(x[0:2]+y[::-1])


# 2nd way using reversed()

print(''.join(reversed(x)))


# 3rd Way using looping method

i = len(x)-1
newstr = ''
while i>=0:
    newstr +=x[i]
    i = i-1
print(newstr)


# For list using slice

a = [8,1,2,3,4,5,6,7]

print(a[::-1])

