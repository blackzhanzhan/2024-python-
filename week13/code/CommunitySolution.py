import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def read_dataset(): #导入社交网络数据
    #两个社交网络数据集可选:scholat_edge.csv,scholat_edge.csv
    karate_dataset = np.loadtxt("../data/karate_edge.csv", delimiter=',', dtype=int)
    #karate_dataset = np.loadtxt("scholat_edge.csv", delimiter=',', dtype=int)
    print("数据集为：\n",karate_dataset)
    num_nodes = len(np.unique(np.concatenate((karate_dataset[:,0], karate_dataset[:,1]))))

    G = nx.Graph()
    G.add_nodes_from(np.arange(num_nodes))
    G.add_edges_from(karate_dataset)
    G.to_undirected()

    """ 可视化社交网络 """
    plt.figure()
    nx.draw(G,
            nx.spring_layout(G),
            node_color='c',
            with_labels=True
            )
    plt.show()
    return G

def community_NMF(G,k, epoch=100): #epoch为迭代次数
    n = len(G.nodes())  # number of nodes
    print("邻接矩阵\n", nx.adjacency_matrix(G))
    adj = nx.adjacency_matrix(G).toarray()
    print("邻接矩阵数组为\n",adj)
    H = np.random.random((n, k))
    for i in range(epoch):
        H_numerator = np.dot(adj, H)
        H_denominator = np.dot(H, np.dot(H.T, H)) + 1e-10
        H = H * (H_numerator / H_denominator)
    return soft_max(H)

def soft_max(z):
    t = np.exp(z)
    a = t / np.sum(t, axis=1).reshape(-1,1)
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
    for i in range(k):
        print("社区{}的成员为：{}".format(i+1, np.where(pred==i)[0]))
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G,
            pos,
            node_color='c',
            with_labels=True
            )
    color_list = ["pink", "orange","green","yellow","black","purple"]
    for i in range(k):
        nx.draw_networkx_nodes(G, pos= pos, nodelist = np.where(pred == i)[0], node_color= color_list[i])
    plt.show()
if __name__ == "__main__":
    #导入社交网络数据,构建图结构
    G = read_dataset()
    #设置社区数量
    k = 2
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
