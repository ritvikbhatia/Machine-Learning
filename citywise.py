import json
f=open("C:\\Users\\Ritvik\\Documents\\file1.json","r")
d=f.readlines()
a=json.loads(d[0])
f.close()
inp='Gurgaon'
h={}
t=[]
for i in range(76):
    resultsshown=int(a[i]['results_shown'])
    resultsstart=int(a[i]['results_start'])-1
    for j in range(resultsstart,resultsshown):
        user=a[i]['restaurants'][j]['restaurant']['user_rating']
        city=a[i]['restaurants'][j]['restaurant']['location']['city']
        score=int(user['votes'])*float(user['aggregate_rating'])
        name=a[i]['restaurants'][j]['restaurant']['name']
        h[score]=name
        city = city.encode('ascii', 'ignore').decode('ascii')
        if(city==inp):
            t.append(score)

top=sorted(t,reverse=True)[:5]
for i in range(5):
    print(h[top[i]],":",top[i])
