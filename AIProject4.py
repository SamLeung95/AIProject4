
# coding: utf-8

# In[103]:

def getdistance(centroid, point):
    return math.sqrt(((centroid[0]-point[0])**2)+((centroid[1]-point[1])**2))


#loop through for range 0 to cluster size and compare current data to centroids with root((datax-x)^2+(datay-y)^2)
#have variable keep num that it is closest to
#after loop, append data to temp clusters list with index of that variable
#repeat until all datapoints are in cluster list
def getclusters(centroids, points):
    clusters=[]
    #print ("centroids:", centroids, "\n\n")
    for x in range(len(centroids)):
        clusters.append([])
        #make temp list cluster number size to put clusters in {clusters} equal to centroids
        #loop for range in 0 to data size
    for x in range(len(points)):
        closest_centroid=0
        for y in range(1, len(clusters)):
            closest_distance=getdistance(centroids[closest_centroid], points[x])
            temp_distance=getdistance(centroids[y], points[x])
            if temp_distance<closest_distance:
                closest_centroid=y
        clusters[closest_centroid].append(points[x])
        #print("clusters:",clusters, "point:",points[x], "centroid:", centroids[closest_centroid], "index:", closest_centroid, "\n")
    return clusters
        


# In[104]:

def main():
    
    if len(sys.argv)==3:
       
        if os.path.isfile(sys.argv[2]) and sys.argv[1].isdigit():
            
            fig = plt.figure()

            points=[]
            final_clusters=[]

            cluster_amt=int(sys.argv[1])
            points_file = open(sys.argv[2], 'r')
                
            for line in points_file:
                line=line.strip(' \t\n\r()')
                points.append(list(int(x) for x in re.split(' |, |,',line)))
            
            unique_points=[];
            
            
            for x in range(0,len(points)):
                if points[x] not in unique_points:
                    unique_points.append(points[x])
            
            unique_points_amt=len(unique_points);
            
            if int(sys.argv[1])<=unique_points_amt:
                    
                centroids=[]

                #select random centroids of amount cluster size
                centroids_index=random.sample(range(len(unique_points)), cluster_amt)        
                #copy those out of data list and into new centroid list
                for x in range(cluster_amt):
                    centroids.append(unique_points[centroids_index[x]])

                #now centroid and data is separate

                done=False

                #Set while done is false
                #done will be set to true at beginning of loop start, but in loops later on
                #if centroids dont match, then set to false after

                while done==False:
                    done=True
                    clusters=[cluster_amt]
                    clusters=getclusters(centroids, points) 
                    #make temp list cluster number size to put clusters in {clusters}
                    #call cluster function and return list to temp cluster list
                    new_centroid=[]

                    #set newcentroid list
                    #loop through temp cluster list size
                    for group in range(len(clusters)):
                        xsum=0
                        ysum=0

                        for pnt in clusters[group]:
                            xsum+=pnt[0]
                            ysum+=pnt[1]
                            
                        #get mean of each cluster
                        # append each to newcentroids
                        xmean=xsum/len(clusters[group])
                        ymean=ysum/len(clusters[group])

                        new_centroid.append([xmean,ymean])
                        
                    #compare new and old centroids
                    #if centroid is different
                    #set done to false
                    #set centroids equal to newcentroids
                    if new_centroid!=centroids:
                        done=False
                        centroids=new_centroid

                    else:
                        final_clusters=clusters

                #Display graph
                markers=['1', 'v', 'h','2','o','^','<','>','p','s','x','+','d']
                colors=['b', 'c', 'y', 'm', 'r']
                for group_num in range(len(final_clusters)):
                    for pnt in final_clusters[group_num]:
                        plt.scatter(pnt[0], pnt[1], marker=markers[group_num%len(markers)], c=colors[group_num%len(colors)])


                plt.show()
            
            else:
                print("Amount of clusters can not be more than the amount of unique points.")
        
        else:
            print("Invalid command arguments")

    else:
        print("Invalid amount of command arguments")
        
    


# In[101]:

import sys
import random
import math
import matplotlib.pyplot as plt
import os.path
import re

main()


# In[ ]:




# In[ ]:



