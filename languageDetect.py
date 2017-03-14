import neuralNetwork as nn
import os, random, math,pickle
def random_line(file_name):
        total_bytes = os.stat(file_name).st_size 
        random_point = random.randint(0, total_bytes)
        file = open(file_name)
        file.seek(random_point)
        file.readline() # skip this line to clear the partial line
        return file.readline()

def normalize(word):
	word = word.lower()
        modWord = []
        word = word[:10]
        if len(word)<10:
            for c in range(10-len(word)):
                word+=chr(0)
        for ch in word:
            modWord.append(ord(ch)*.01)
	return modWord

def genDataArrs(trainingNum=100):
    fe= "english.txt"
    fs="spanish.txt"
    spanish = []
    english = []
    for c in range(trainingNum):
        spanish.append(random_line(fs))
        english.append(random_line(fe))
    outputArr = []
    normArr = []
    for word in english:
        outputArr.append([1,0])
        normArr.append(normalize(word))
    for word in spanish:
        outputArr.append([0,1])
        normArr.append(normalize(word))
    return zip(normArr,outputArr)

def getAllData(fileName, indvOut):
	lines = []
	out = []
	for line in open(fileName):
		lines.append(normalize(line.rstrip('\n')))
		out.append(indvOut)
	return zip(lines,out)
		
netarr = [10,15,2]
learningRate=.01
net = pickle.load(open("spanishEnglish.pkl"))
net.learningRate =.01
c=0
data = genDataArrs(500)

while c<200:
    for a,b in data:
        net.train(a,b)
    c+=1
os.remove("spanishEnglish.pkl")
output = open('spanishEnglish.pkl', 'wb')
pickle.dump(net, output)

print net.predict(normalize("rocks"))
print net.predict(normalize("Usted"))
print net.predict(normalize("shopping"))
