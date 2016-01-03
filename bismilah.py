import csv
import random
import math
import operator

def SetData(filename, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    #print dataset
	    z=30
	    for x in range(len(dataset)):
	        for y in range(4):
	           dataset[x][y] = float(dataset[x][y])
	           #print dataset[x][y]
	        if x < 30:
	           #print dataset[x]
	           testSet.append(dataset[x])
	           #z=z+1
	        else:
	           trainingSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	akar = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	
	akar= pow(distance, 0.5)
	return akar

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	#print length
	#print k
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))

	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		#print neighbors[x]
		#print neighbors[x][-1]
		response = neighbors[x][-1]
		#print response 
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	#print classVotes
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	wrong = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
		else:
			wrong += 1
	print 'benar', correct 
	print 'salah', wrong
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	
	SetData('iris.data', trainingSet, testSet)
	print 'Train set: ', len(trainingSet)
	print 'Test set: ' , len(testSet)
	# generate prediction
	predictions=[]
	k = input('Input nilai k: ')
	
	for x in range(len(testSet)):
		#print 'ini', testSet[x]
		#print 'itu', trainingSet
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		#print result
		predictions.append(result)
		
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	#print 'ini', x
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()