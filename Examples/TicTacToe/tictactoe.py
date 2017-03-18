import neuralNetwork as nn
import os, random
import pickle
nnarr = [9,27,9]
learningRate=.01
net = pickle.load(open("ticTacToe.pkl"))
learningRate = .001
#net = nn.network(nnarr, learningRate)
winner = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
board= [0,0,0,0,0,0,0,0,0]
playerMoves = []
def gamePlayerEncoder(num=1,training=True):
        playerIn = raw_input("enter move ")
        board[int(playerIn)]=num
        outTrain = [0,0,0,0,0,0,0,0,0]
        outTrain[int(playerIn)]=1
	if training:
		return outTrain
def boardPrinter():
        print str(board[0])+str(board[1])+str(board[2])
        print str(board[3])+str(board[4])+str(board[5])
        print str(board[6])+str(board[7])+str(board[8])
def checkWin():
        for poss in winner:
                if board[poss[0]] == board[poss[1]] and board[poss[1]]==board[poss[2]] and not board[poss[1]]==0:
                        print "WINNER IS "+str(board[poss[0]])
			if board[poss[0]]==1:
				for a in correct1:
					correct.append(a)
			return [0,0,0,0,0,0,0,0,0]
	zeros = 0
	for pos in board:
		if(pos==0):
			zeros+=1
	if zeros ==0:
		for c in correct1:
                	correct.append(c)
		return [0,0,0,0,0,0,0,0,0]
	return board
def netPlay(net,num):
	modBoard =board
	if num ==1:
		modBoard = [1 if p == 2 else p*2 for p in modBoard]
	predict=net.predict(modBoard)
	print predict
	c=0
	maxI=0
	maxV=predict[0]
	for spc in predict:
		if maxV<spc:
			maxV=spc
			maxI=c
		c+=1
	if board[maxI]==0:
		board[maxI]=num
	else:
		pass
		#randomSelect(num)
	return maxI
def randomSelect(num =1):
	selection = random.randint(0,8)
	if board[selection]==0:
		board[selection]=num
		outTrain = [0,0,0,0,0,0,0,0,0]
       	 	outTrain[selection]=1
		if num == 1:
			correct1.append(outTrain)
	else:
		randomSelect()

correct1 = []
correct2 = []
correct=[]
boards =[]
gathering = True
c = 0

while gathering:
	boardPrinter()
	#randomSelect()
	netPlay(net,1)
	#gamePlayerEncoder(training=False)
	board=checkWin()
	boardPrinter()
	if sum(board) != 0:
		#randomSelect(2)
		#correct.append()
		gamePlayerEncoder(2)
		boards.append(board)
		#netPlay(net,2)
		board=checkWin()
	if sum(board) == 0:
		#gameCount = int(raw_input("play Again (0 yes, 1 no)"))
		if c == 25:
			gathering =False
		c+=1
'''
print "TRAINING NOW"
trainingSet=[]
correctSet =[]
for b in boards:
	trainingSet.append(b)
for c in correct:
	correctSet.append(c)
correctSet = [[a*1.0 for a in correct] for correct in correctSet]
trainingSet = [[a*1.0 for a in correct] for correct in trainingSet]
tc = 0
while tc < 100:
	for a,b in zip(trainingSet,correctSet):
		net.train(a,b)
	tc+=1

print "PREDICTION "+str(net.predict([1,1,0,2,0,0,0,0,0]))
os.remove("ticTacToe.pkl")
output = open('ticTacToe.pkl', 'wb')
pickle.dump(net, output)
'''
