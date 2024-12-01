import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def read_dataset(): #导入社交网络数据
    #两个社交网络数据集可选:karate_edge.csv,dolphin_edge.csv

    # 任务1.1 从CSV文件中读取网络数据，构建numpy数组，并计算图中节点总数
    pass

    num_nodes = len(np.unique(np.concatenate((karate_dataset[:,0], karate_dataset[:,1]))))
    G = nx.Graph()

    #任务1.2：使用numpy数组为netwokx无向图对象增加节点和边
    pass

    G.to_undirected()

    """ 可视化社交网络 """
    plt.figure()

    # 任务1.3：使用networkx对象的draw方法将图可视化
    pass

    plt.show()
    return G

def community_NMF(G,k, epoch=100): #epoch为迭代次数
    n = len(G.nodes())  # number of nodes

    # 任务2.1 构建图的邻接矩阵并转化为numpy数组
    print("邻接矩阵\n", nx.adjacency_matrix(G))
    pass

    print("邻接矩阵数组为\n",adj)
    H = np.random.random((n, k))

    for i in range(epoch):
    #任务2.2 实现NMF分解算法
        pass

    return soft_max(H)

def soft_max(z):
    #任务2.3 根据特征矩阵Z计算节点所属社区
    pass
    return a

def np_modularity(pred, cluster):
    num_edges = sum(sum(pred)) / 2
    k1 = np.sum(pred, axis=1)
    k2 = k1.reshape(k1.shape[0], 1)
    k1k2 = k1 * k2
    B = pred - (k1k2 / (2 * num_edges))
    result = np.dot(cluster, np.transpose(cluster))
    result = np.dot(B, result)
    sum_result = np.trace(result)
    Q = sum_result / (2*num_edges)
    print("模块度:",Q)
    return Q

def visualize_community(G, k, pred):
    #3.1 输出每个社区成员
    for i in range(k):
        pass
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G,
            pos,
            node_color='c',
            with_labels=True
            )
    color_list = ["pink", "orange","green","yellow","black","purple"]
    # 3.2 为每个社区节点打上指定颜色
    for i in range(k):
        pass
    plt.show()
if __name__ == "__main__":
    #导入社交网络数据,构建图结构
    G = read_dataset()
    #设置社区数量
    k = 4
    #执行社区发现模型
    H = community_NMF(G, k)
    #提取社区发现结果
    pred = np.argmax(H, axis=1)
    #输出并可视化社区发现结果
    visualize_community(G, k, pred)
    #计算模块度
    cluster_matrix = np.zeros(shape=(len(G.nodes), k))
    cluster_matrix[np.arange(len(G.nodes)), pred] = 1
    adj = nx.adjacency_matrix(G).toarray()
    np_modularity(adj, cluster_matrix)
