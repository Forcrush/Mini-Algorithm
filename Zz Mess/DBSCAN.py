import numpy as np
import matplotlib.pyplot as plt
import math
import time


UNCLASSIFIED = False
NOISE = 0


# 4个高斯核生成数据  
def generate_data():
    N = 500         # 样本数目   
    mu1 = [0, 35]  
    mu2 = [30, 40]  
    mu3 = [20, 20]  
    mu4 = [45, 15]  
    sigma = np.matrix([[30, 0], [0, 30]])  # 协方差矩阵  
    alpha = [0.1, 0.2, 0.3, 0.4]         # 混合项系数  

    X = np.zeros((N, 2))       # 初始化X，2行N列。2维数据，N个样本  
    X = np.matrix(X)
    
    # 生成数据，根据alpha概率生成
    threshold_1 = alpha[0] / (alpha[0] + alpha[1] + alpha[2] + alpha[3])
    threshold_2 = (alpha[0] + alpha[1]) / (alpha[0] + alpha[1] + alpha[2] + alpha[3])
    threshold_3 = (alpha[0] + alpha[1] + alpha[2]) / (alpha[0] + alpha[1] + alpha[2] + alpha[3])
    for i in range(N):  
        if np.random.random(1) < threshold_1:  # 生成0-1之间随机数
            X[i, :] = np.random.multivariate_normal(mu1, sigma, 1)     # 用第一个高斯模型生成2维数据
        elif threshold_1 <= np.random.random(1) < threshold_2:
            X[i, :] = np.random.multivariate_normal(mu2, sigma, 1)      # 用第二个高斯模型生成2维数据  
        elif threshold_2 <= np.random.random(1) < threshold_3:
            X[i, :] = np.random.multivariate_normal(mu3, sigma, 1)      # 用第三个高斯模型生成2维数据  
        else:  
            X[i, :] = np.random.multivariate_normal(mu4, sigma, 1)      # 用第四个高斯模型生成2维数据  
    return X  


def dist(a, b):
    """
    输入：向量A, 向量B
    输出：两个向量的欧式距离
    """
    return math.sqrt(np.power(a - b, 2).sum())


def eps_neighbor(a, b, eps):
    """
    输入：向量A, 向量B
    输出：是否在eps范围内
    """
    return dist(a, b) < eps


def region_query(data, pointId, eps):
    """
    输入：数据集, 查询点id, 半径大小
    输出：在eps范围内的点的id
    """
    nPoints = data.shape[1]
    seeds = []
    for i in range(nPoints):
        if eps_neighbor(data[:, pointId], data[:, i], eps):
            seeds.append(i)
    return seeds


def expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
    """
    输入：数据集, 分类结果, 待分类点id, 簇id, 半径大小, 最小点个数
    输出：能否成功分类
    """
    seeds = region_query(data, pointId, eps)
    if len(seeds) < minPts: # 不满足minPts条件的为噪声点
        clusterResult[pointId] = NOISE
        return False
    else:
        clusterResult[pointId] = clusterId # 划分到该簇
        for seedId in seeds:
            clusterResult[seedId] = clusterId

        while len(seeds) > 0: # 持续扩张
            currentPoint = seeds[0]
            queryResults = region_query(data, currentPoint, eps)
            if len(queryResults) >= minPts:
                for i in range(len(queryResults)):
                    resultPoint = queryResults[i]
                    if clusterResult[resultPoint] == UNCLASSIFIED:
                        seeds.append(resultPoint)
                        clusterResult[resultPoint] = clusterId
                    elif clusterResult[resultPoint] == NOISE:
                        clusterResult[resultPoint] = clusterId
            seeds = seeds[1:]
        return True


def dbscan(data, eps, minPts):
    """
    输入：数据集, 半径大小, 最小点个数
    输出：分类簇id
    """
    clusterId = 1
    nPoints = data.shape[1]
    clusterResult = [UNCLASSIFIED] * nPoints
    for pointId in range(nPoints):
        point = data[:, pointId]
        if clusterResult[pointId] == UNCLASSIFIED:
            if expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
                clusterId = clusterId + 1
    return clusterResult, clusterId - 1


def plotFeature(data, clusters, clusterNum):
    nPoints = data.shape[1]
    matClusters = np.mat(clusters).transpose()
    fig = plt.figure()
    scatterColors = ['black', 'blue', 'green', 'yellow', 'red', 'purple', 'orange', 'brown']
    ax = fig.add_subplot(111)
    for i in range(clusterNum + 1):
        colorSytle = scatterColors[i % len(scatterColors)]
        subCluster = data[:, np.nonzero(matClusters[:, 0].A == i)]
        ax.scatter(subCluster[0, :].flatten().A[0], subCluster[1, :].flatten().A[0], c=colorSytle, s=25, alpha=0.5)


def main():
    dataSet = generate_data()
    dataSet = dataSet.transpose()
    # print(dataSet)
    clusters, clusterNum = dbscan(dataSet, 6, 25) # eps minpts
    print("cluster Numbers =", clusterNum)
    # print(clusters)
    plotFeature(dataSet, clusters, clusterNum)
    plt.show()


main()
