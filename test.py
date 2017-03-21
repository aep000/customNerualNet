import neuralNetwork as nn

netarr = [2,2]
testInpts = [[10.0,2.0], [5.0,5.0], [5.0,6.0], [4.0,3.0], [1.0,2.0] ]
outs = [[1.0/12,1.0/12],[1.0/10,1.0/10],[1.0/11,1.0/11],[1.0/7,1.0/7],[1.0/3,1.0/3]]
learningRate =.001
net = nn.network(netarr,learningRate)
c=0
while c<20000:
        for a,b in zip(testInpts,outs):
                net.train(a,b)
        c+=1
correct = 0.0
testInpts = [[11.0,3.0],[7.0,3.0]]
outs = [[1.0/14],[1.0/10]]
for a,b in zip(testInpts,outs):
        pos=net.predict(a)
        if pos[0]>.5 and b[0]==1:
                correct+=1.0
        if pos[0]<.5 and b[0]==0:
                correct+=1.0
        print str(a)+" EXPECTED"+str(b)+" OUT "+str(pos)
print correct/len(outs)

