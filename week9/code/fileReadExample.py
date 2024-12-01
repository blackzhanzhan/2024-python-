fin=open("../data/monday.txt")

data=fin.readlines()

fout=open("../data/monday_copy.txt","wt")
datalist=[10,20,320,600]
datalist=[str(data) + "\n" for data in datalist]

