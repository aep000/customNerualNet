import random
import math
import numpy as np

#Defines the attributes of a neuron Probably very memory intensive
class neuron:
	def __init__(self, inputNodes):
		self.inpts = inputNodes
		self.inpts.append(inputNode(1))
		self.weights =[]
		self.output = 0
		for inp in inputNodes:
			self.weights.append(random.random())	
	def weightSum(self):
		for a,b in zip(self.weights,self.inpts):
			weightedVals = [ a*b.output for a,b in zip(self.weights,self.inpts)]
		return sum(weightedVals)
	


	def runNeuron(self):
		sm = self.weightSum()
		out = 1/(1+math.exp(-sm))
		self.output = out
		return out
	def backProp(self, error,learningRate):
		errors = [weight*(self.output*(1-self.output))*error for weight in self.weights]
		
		self.weights= [ weight + learningRate * error * inp.output for inp,err,weight in zip(self.inpts,errors,self.weights)]
		
		for inp,err in zip(self.inpts,errors):
			inp.backProp(err,learningRate)

class inputNode:
	def __init__(self, val=0):
		self.output = val
	def output(self):
		return self.output
	def setOutput(self, val):
		self.output = val
	def backProp(self, error, learningRate):
		pass
	def runNeuron(self):
		pass

class network:
	def __init__(self, netArray,learningRate):
		self.net = []
		c = 1
		c2 = 0
		self.net.append([])
		self.learningRate =learningRate
		while c2<netArray[0]:
			self.net[0].append(inputNode())
			c2+=1
		for layer in netArray[1:]:
			self.net.append([])
			c1 = 0 
			while c1<layer:
				self.net[c].append(neuron(self.net[c-1]))
				c1+=1
			c+=1
	def train(self, idata, expectedOut):
		for inp,data in zip(self.net[0],idata):
			inp.setOutput(data)
		for layer in self.net:
			for neuron in layer:
				neuron.runNeuron()
		for a,b in zip(expectedOut,self.net[len(self.net)-1]):
			b.backProp(a-b.output,self.learningRate)
					
		
	def predict(self, inputs):
		for inp,data in zip(self.net[0],inputs):
                        inp.setOutput(data)
		for layer in self.net:
                                for neuron in layer:
                                        neuron.runNeuron()
		outs = []
		for out in self.net[len(self.net)-1]:
			outs.append(out.output)
		return outs
