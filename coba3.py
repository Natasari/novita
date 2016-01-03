import random
import math

NUM_CLUSTERS = 3
TOTAL_DATA = 150
SETOSA_SAMPLE = 15 
VERSICOLOR_SAMPLE = 80
VIRGINICA_SAMPLE= 120 
#BIG_NUMBER = math.pow(100, 100)

SAMPLES = [
            [5.1,3.5,1.4,0.2],    #setosa
            [4.9,3.0,1.4,0.2], 
            [4.7,3.2,1.3,0.2], 
            [4.6,3.1,1.5,0.2], 
            [5.0,3.6,1.4,0.2], 
            [5.4,3.9,1.7,0.4], 
            [4.6,3.4,1.4,0.3],
            [5.0,3.4,1.5,0.2],
            [4.4,2.9,1.4,0.2],
            [4.9,3.1,1.5,0.1],
            [5.4,3.7,1.5,0.2],
            [4.8,3.4,1.6,0.2],
            [4.8,3.0,1.4,0.1],
            [4.3,3.0,1.1,0.1],
            [5.8,4.0,1.2,0.2],
            [5.7,4.4,1.5,0.4],
            [5.4,3.9,1.3,0.4],
            [5.1,3.5,1.4,0.3],
            [5.7,3.8,1.7,0.3],
            [5.1,3.8,1.5,0.3],
            [5.4,3.4,1.7,0.2],
            [5.1,3.7,1.5,0.4],
            [4.6,3.6,1.0,0.2],
            [5.1,3.3,1.7,0.5],
            [4.8,3.4,1.9,0.2],
            [5.0,3.0,1.6,0.2],
            [5.0,3.4,1.6,0.4],
            [5.2,3.5,1.5,0.2],
            [5.2,3.4,1.4,0.2],
            [4.7,3.2,1.6,0.2],
            [4.8,3.1,1.6,0.2],
            [5.4,3.4,1.5,0.4],
            [5.2,4.1,1.5,0.1],
            [5.5,4.2,1.4,0.2],
            [4.9,3.1,1.5,0.1],
            [5.0,3.2,1.2,0.2],
            [5.5,3.5,1.3,0.2],
            [4.9,3.1,1.5,0.1],
            [4.4,3.0,1.3,0.2],
            [5.1,3.4,1.5,0.2],
            [5.0,3.5,1.3,0.3],
            [4.5,2.3,1.3,0.3],
            [4.4,3.2,1.3,0.2],
            [5.0,3.5,1.6,0.6],
            [5.1,3.8,1.9,0.4],
            [4.8,3.0,1.4,0.3],
            [5.1,3.8,1.6,0.2],
            [4.6,3.2,1.4,0.2],
            [5.3,3.7,1.5,0.2],
            [5.0,3.3,1.4,0.2],
            [7.0,3.2,4.7,1.4],#versicolor
            [6.4,3.2,4.5,1.5],
            [6.9,3.1,4.9,1.5],
            [5.5,2.3,4.0,1.3],
            [6.5,2.8,4.6,1.5],
            [5.7,2.8,4.5,1.3],
            [6.3,3.3,4.7,1.6],
            [4.9,2.4,3.3,1.0],
            [6.6,2.9,4.6,1.3],
            [5.2,2.7,3.9,1.4],
            [5.0,2.0,3.5,1.0], 
            [5.9,3.0,4.2,1.5],
            [6.0,2.2,4.0,1.0],
            [6.1,2.9,4.7,1.4],
            [5.6,2.9,3.6,1.3],
            [6.7,3.1,4.4,1.4],
            [5.6,3.0,4.5,1.5],
            [5.8,2.7,4.1,1.0],
            [6.2,2.2,4.5,1.5],
            [5.6,2.5,3.9,1.1],
            [5.9,3.2,4.8,1.8],
            [6.1,2.8,4.0,1.3],
            [6.3,2.5,4.9,1.5],
            [6.1,2.8,4.7,1.2],
            [6.4,2.9,4.3,1.3],
            [6.6,3.0,4.4,1.4],
            [6.8,2.8,4.8,1.4],
            [6.7,3.0,5.0,1.7],
            [6.0,2.9,4.5,1.5],
            [5.7,2.6,3.5,1.0],
            [5.5,2.4,3.8,1.1],
            [5.5,2.4,3.7,1.0],
            [5.8,2.7,3.9,1.2],
            [6.0,2.7,5.1,1.6],
            [5.4,3.0,4.5,1.5],
            [6.0,3.4,4.5,1.6],
            [6.7,3.1,4.7,1.5],
            [6.3,2.3,4.4,1.3],
            [5.6,3.0,4.1,1.3],
            [5.5,2.5,4.0,1.3],
            [5.5,2.6,4.4,1.2],
            [6.1,3.0,4.6,1.4],
            [5.8,2.6,4.0,1.2],
            [5.0,2.3,3.3,1.0],
            [5.6,2.7,4.2,1.3],
            [5.7,3.0,4.2,1.2],
            [5.7,2.9,4.2,1.3],
            [6.2,2.9,4.3,1.3],
            [5.1,2.5,3.0,1.1],
            [5.7,2.8,4.1,1.3],
            [6.3,3.3,6.0,2.5],#virginica
            [5.8,2.7,5.1,1.9],
               [7.1,3.0,5.9,2.1], 
               [6.3,2.9,5.6,1.8], 
               [6.5,3.0,5.8,2.2], 
               [7.6,3.0,6.6,2.1], 
               [4.9,2.5,4.5,1.7], 
               [7.3,2.9,6.3,1.8], 
               [6.7,2.5,5.8,1.8], 
               [7.2,3.6,6.1,2.5], 
               [6.5,3.2,5.1,2.0], 
               [6.4,2.7,5.3,1.9], 
               [6.8,3.0,5.5,2.1],
               [5.7,2.5,5.0,2.0], 
               [5.8,2.8,5.1,2.4], 
               [6.4,3.2,5.3,2.3], 
               [6.5,3.0,5.5,1.8], 
               [7.7,3.8,6.7,2.2], 
               [7.7,2.6,6.9,2.3], 
               [6.0,2.2,5.0,1.5], 
               [6.9,3.2,5.7,2.3], 
               [5.6,2.8,4.9,2.0], 
               [7.7,2.8,6.7,2.0], 
               [6.3,2.7,4.9,1.8], 
               [6.7,3.3,5.7,2.1],
               [7.2,3.2,6.0,1.8], 
               [6.2,2.8,4.8,1.8], 
               [6.1,3.0,4.9,1.8], 
               [6.4,2.8,5.6,2.1], 
               [7.2,3.0,5.8,1.6], 
               [7.4,2.8,6.1,1.9], 
               [7.9,3.8,6.4,2.0], 
               [6.4,2.8,5.6,2.2], 
               [6.3,2.8,5.1,1.5], 
               [6.1,2.6,5.6,1.4], 
               [7.7,3.0,6.1,2.3], 
               [6.3,3.4,5.6,2.4],
               [6.4,3.1,5.5,1.8], 
               [6.0,3.0,4.8,1.8], 
               [6.9,3.1,5.4,2.1], 
               [6.7,3.1,5.6,2.4], 
               [6.9,3.1,5.1,2.3], 
               [5.8,2.7,5.1,1.9], 
               [6.8,3.2,5.9,2.3], 
               [6.7,3.3,5.7,2.5], 
               [6.7,3.0,5.2,2.3], 
               [6.3,2.5,5.0,1.9], 
               [6.5,3.0,5.2,2.0], 
               [6.2,3.4,5.4,2.3],
               [5.9,3.0,5.1,1.8]
]

data = []
centroids = []

class DataPoint:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def set_a(self, a):
        self.a = a
    
    def get_a(self):
        return self.a
    
    def set_b(self, b):
        self.b = b
    
    def get_b(self):
        return self.b

    def set_c(self, c):
        self.c = c
    
    def get_c(self):
        return self.c

    def set_d(self, d):
        self.d = d
    
    def get_d(self):
        return self.d
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber

class Centroid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def set_a(self, a):
        self.a = a
    
    def get_a(self):
        return self.a
    
    def set_b(self, b):
        self.b = b
    
    def get_b(self):
        return self.b

    def set_c(self, c):
        self.c = c
    
    def get_c(self):
        return self.c

    def set_d(self, d):
        self.d = d
    
    def get_d(self):
        return self.d

def initialize_centroids():
    centroids.append(Centroid(SAMPLES[SETOSA_SAMPLE][0], SAMPLES[SETOSA_SAMPLE][1], SAMPLES[SETOSA_SAMPLE][2], SAMPLES[SETOSA_SAMPLE][3]))
    centroids.append(Centroid(SAMPLES[VERSICOLOR_SAMPLE][0], SAMPLES[VERSICOLOR_SAMPLE][1], SAMPLES[VERSICOLOR_SAMPLE][2], SAMPLES[VERSICOLOR_SAMPLE][3]))
    centroids.append(Centroid(SAMPLES[VIRGINICA_SAMPLE][0], SAMPLES[VIRGINICA_SAMPLE][1], SAMPLES[VIRGINICA_SAMPLE][2], SAMPLES[VIRGINICA_SAMPLE][3]))
    
    print "Centroids initialized at:"
    print "Centroids 1 kelas Setosa", (centroids[0].get_a(), centroids[0].get_b(), centroids[0].get_c(), centroids[0].get_d())
    print "Centroids 2 kelas Versicolor", (centroids[1].get_a(), centroids[1].get_b(), centroids[1].get_c(), centroids[1].get_d())
    print"Centroids 3 kelas Virginica", (centroids[2].get_a(), centroids[2].get_b(), centroids[2].get_c(), centroids[2].get_d())
    print("\n")
    return

def initialize_datapoints():
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1], SAMPLES[i][2], SAMPLES[i][3])
        
        if(i == SETOSA_SAMPLE):
            newPoint.set_cluster(0)
        elif(i == VERSICOLOR_SAMPLE):
            newPoint.set_cluster(1)
        elif(i == VIRGINICA_SAMPLE):
            newPoint.set_cluster(2)
        else:
            newPoint.set_cluster(None)
            
        data.append(newPoint)
    
    return

def get_distance(dataPointA, dataPointB,dataPointC, dataPointD, centroidA, centroidB, centroidC, centroidD ):
         return math.sqrt(math.pow((centroidA - dataPointA), 2) + math.pow((centroidB - dataPointB), 2) + math.pow((centroidC - dataPointC), 2) + math.pow((centroidD - dataPointD), 2))

def recalculate_centroids():
    totalA = 0
    totalB = 0
    totalC = 0
    totalD = 0
    totalInCluster = 0
    
    for j in range(NUM_CLUSTERS):
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                totalA += data[k].get_a()
                totalB += data[k].get_b()
                totalC += data[k].get_c()
                totalD += data[k].get_d()
                totalInCluster += 1
        
        if(totalInCluster > 0):
            centroids[j].set_a(totalA / totalInCluster)
            centroids[j].set_b(totalB / totalInCluster)
            centroids[j].set_c(totalC / totalInCluster)
            centroids[j].set_d(totalD / totalInCluster)
    
    return

def update_clusters():
    isStillMoving = 0
    
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(NUM_CLUSTERS):
            distance = get_distance(data[i].get_a(), data[i].get_b(),data[i].get_c(), data[i].get_d(), centroids[j].get_a(), centroids[j].get_b(), centroids[j].get_c(), centroids[j].get_d())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        
        data[i].set_cluster(currentCluster)
        
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1
    
    initialize_centroids()
    
    initialize_datapoints()
    
    while(isStillMoving):
        recalculate_centroids()
        isStillMoving = update_clusters()
    
    return

def print_results():
    for i in range(NUM_CLUSTERS):
        print("\n")
        #print("Cluster ke", i+1)
        if(i==0):
            print "Cluster ke", i+1 ,"Kelas Setosa"
            print("\n")
            for j in range(TOTAL_DATA):
                if(data[j].get_cluster() == i):
                    print "Data" ,j+1,"->", (data[j].get_a(),data[j].get_b(), data[j].get_c(), data[j].get_d())
                    #print("\n")
        if(i==1):
            print "Cluster ke", i+1, "Kelas Versicolor"
            print("\n")
            for j in range(TOTAL_DATA):
                if(data[j].get_cluster() == i):
                    print "Data",j+1,"->", (data[j].get_a(),data[j].get_b(), data[j].get_c(), data[j].get_d())
                    #print("\n")
        if(i==2):
            print "Cluster ke" ,i+1 ,"Kelas Virginica"
            print("\n")
            for j in range(TOTAL_DATA):
                if(data[j].get_cluster() == i):
                    print "Data", j+1,"->", (data[j].get_a(),data[j].get_b(), data[j].get_c(), data[j].get_d())
                    #print("\n")
    print("\n") 
    return

perform_kmeans()
print_results()