import matplotlib as mpl
mpl.use('Agg')
# import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns



def graphIt():
	baseFile = "data.csv"

	# reads the data from file
	df = pd.read_csv(baseFile)

	# remove data 
	dfX = pd.DataFrame(df, columns = ['x'])
	xList = dfX.values.tolist()
	dfY = pd.DataFrame(df, columns = ['y'])
	yList = dfY.values.tolist()
	dfZ = pd.DataFrame(df, columns = ['z'])
	zList = dfZ.values.tolist()

	print(df)



	# use the data to make a graph

	plt.scatter(xList,yList, color='blue')
	# plt.plot(xList,yList)

	# super crazy graph
	# plt.figure(figsize=(10,8), dpi= 72)
	# sns.pairplot(df)


	plt.savefig('graphs/graph03.png')

