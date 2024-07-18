array=[2200,2350,2600,2130,2190]

print(array)

x=array[1]-array[0]
print(x)

print(array[0]+array[1]+array[2])

print(2000 in array)

array.append(1980)


print(array[3]-200)

print(array)


heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)

heros.insert(3,"black panther")
print(heros)

heros[1:3]=['doctor strange']               #kinda replace 
print(heros)

heros.sort()
print(heros)


a=int(input("enter the no. upto which odd number is required"))

b=[]

for i in range(1,a):
    if i%2==1:
        b.append(i)

print(b)
