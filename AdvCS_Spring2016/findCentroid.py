__author__ = 'becca.elenzil'

import pygame
import math
import random
import sys
import time


WIDTH = 1400
HEIGHT = 800

clock = pygame.time.Clock()

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def distanceToCentroids(centroids,p):
    distArray = []
    for centroid in centroids:
        distArray.append(distance(p,centroid))
    i = distArray.index(min(distArray))
    return i


def generateCentroids(n,w,h):
    c = []
    for i in range(n):
        c.append(point(random.randrange(w),random.randrange(h)))
        #print c[i].x,c[i].y
    return c

def generatePoints(n,w,h):
    p = []
    for i in range(n):
        p.append(point(random.randrange(w),random.randrange(h)))
    return p

def calculateCentroids(groupedPoints):
    centroids = []
    for pointsList in groupedPoints:
        centroidX = 0
        centroidY = 0
        for p in pointsList:
            centroidX += p.x
            centroidY += p.y
        if len(pointsList) > 0:
            centroidX = centroidX/len(pointsList)
            centroidY = centroidY/len(pointsList)
        centroids.append(point(centroidX,centroidY))
    return centroids

COLORS = [[255,0,0],[255,128,0],[255,255,0],[0,255,0],
          [0,255,255],[0,0,255],[128,0,255],[255,0,255],[255,0,128],
            [255,153,153],[255,204,153],[255,255,153],[153,255,153],
          [153,255,255],[153,153,255],[255,153,255],[255,153,204]]

# Set the height and width of the screen
size = [WIDTH,HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Centroid Visualization")

done = False
numCentroids = 10
numPoints = 1000

centroids = generateCentroids(numCentroids,WIDTH,HEIGHT)
points = generatePoints(numPoints,WIDTH,HEIGHT)
grouped = False

groupedPoints = []
for k in range(numCentroids):
    groupedPoints.append([])

pygame.init()

time.sleep(1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if grouped == True:
        centroids = calculateCentroids(groupedPoints)

    groupedPoints = []
    for k in range(numCentroids):
        groupedPoints.append([])

    for p in points:
        centroidIndex = distanceToCentroids(centroids,p)
        groupedPoints[centroidIndex].append(p)
        grouped = True

    #Draw
    #fill screen with black
    screen.fill([0,0,0])

    #draw centroids
    i = 0
    for centroid in centroids:
        color = COLORS[i]
        pygame.draw.circle(screen, color, (centroid.x,centroid.y), 5)
        i+=1

    #draw points and lines
    k = 0
    for pointsList in groupedPoints:
        color = COLORS[k]
        for p in pointsList:
            pygame.draw.line(screen, color, [p.x,p.y], [centroids[k].x,centroids[k].y])
            pygame.draw.circle(screen, color, (p.x,p.y), 2)
        k += 1

    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

pygame.quit()