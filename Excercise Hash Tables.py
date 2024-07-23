# nyc=[]
# with open('nyc_weather.csv','r') as f:
#     for line in f:
#         token=line.split(',')
#         temp=int(token[1])
#         nyc.append(temp)

# print(nyc)    

# print("average of 1st week ",(sum(nyc[0:7])/7))   

# print("maximum temp from",max(nyc[0:10]))

# nyc={}
# with open('nyc_weather.csv','r') as f:
#     for line in f:
#         token=line.split(',')
#         date=token[0]
#         temp=int(token[1])
#         nyc[date]=temp

# print(nyc)        
# print(nyc['Jan 9'])
# print(nyc['Jan 4'])

poem={}
with open("poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n','')
            if token in poem:
                poem[token]+=1
            else:
                poem[token]=1

print(poem)                