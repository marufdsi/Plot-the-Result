import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from copy import deepcopy as copy
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.backends.backend_pdf import PdfPages
# %matplotlib inline

pd_graph_list = pd.read_csv('GraphList.csv')
graphs = pd_graph_list['GraphName'].values.tolist()
n = len(graphs)
print(graphs)
pp = PdfPages('Legacy Modularity Per Iteration.pdf')
for i in range(n):
    fig = plt.figure()
    graphName = 'LegacyModularity\PerIteration' + "\ ".strip() + graphs[i] + '.csv'
    legacy_modularity = pd.read_csv(graphName)
    legacy_modularity[['Modularity']].plot(kind='line', ylim=(0, 1.1), figsize=(20, 7), title='Legacy Modularity Per Iteration for ' + graphs[i], color='tomato')
    plt.xlabel('Iteration')
    plt.ylabel('Modularity')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Legacy Modularity Per Move.pdf')
for i in range(n):
    graphName = 'LegacyModularity\PerMove' + "\ ".strip() + graphs[i] + '.csv'
    legacy_modularity = pd.read_csv(graphName)
    legacy_modularity[['Modularity']].plot(kind='bar', ylim=(0, 1.1), figsize=(20, 7), title='Legacy Modularity Per Move for ' +graphs[i] , color='tomato')
    plt.xlabel('Move')
    plt.ylabel('Modularity')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Legacy Time Complexity Per Iteration.pdf')
for i in range(n):
    graphName = 'LegacyTimeComplexity\PerIteration' + "\ ".strip() + graphs[i] + '.csv'
    legacy_time_complexity = pd.read_csv(graphName)
    legacy_time_complexity[['Time']].plot(kind='line', figsize=(20, 7), title='Legacy Time Per Iteration for ' + graphs[i], color='orange')
    plt.xlabel('Iteration')
    plt.ylabel('Time in MS')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Legacy Time Complexity Per Move.pdf')
for i in range(n):
    graphName = 'LegacyTimeComplexity\PerMove' + "\ ".strip() + graphs[i] + '.csv'
    legacy_time_complexity = pd.read_csv(graphName)
    legacy_time_complexity[['Time']].plot(kind='bar', figsize=(20, 7), title='Legacy Time Per Move for ' + graphs[i], color='navy')
    plt.xlabel('Move')
    plt.ylabel('Time in MS')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Modularity Per Iteration.pdf')
for i in range(n):
    graphName = 'Modularity\PerIteration' + "\ ".strip() + graphs[i] + '.csv'
    modularity = pd.read_csv(graphName)
    modularity[['Modularity']].plot(kind='line', ylim=(0, 1.1), figsize=(20, 7), title='Modularity Per Iteration for ' + graphs[i], color='tomato')
    plt.xlabel('Iteration')
    plt.ylabel('Modularity')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Modularity Per Move.pdf')
for i in range(n):
    graphName = 'Modularity\PerMove' + "\ ".strip() + graphs[i] + '.csv'
    modularity = pd.read_csv(graphName)
    modularity[['Modularity']].plot(kind='bar', ylim=(0, 1.1), figsize=(20, 7), title='Modularity Per Move for ' +graphs[i] , color='tomato')
    plt.xlabel('Move')
    plt.ylabel('Modularity')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Time Complexity Per Iteration.pdf')
for i in range(n):
    graphName = 'TimeComplexity\PerIteration' + "\ ".strip() + graphs[i] + '.csv'
    time_complexity = pd.read_csv(graphName)
    time_complexity[['Time']].plot(kind='line', figsize=(20, 7), title='Time Per Iteration for ' + graphs[i], color='orange')
    plt.xlabel('Iteration')
    plt.ylabel('Time in MS')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()

pp = PdfPages('Time Complexity Per Move.pdf')
for i in range(n):
    graphName = 'TimeComplexity\PerMove' + "\ ".strip() + graphs[i] + '.csv'
    time_complexity = pd.read_csv(graphName)
    time_complexity[['Time']].plot(kind='bar', figsize=(20, 7), title='Time Per Move for ' + graphs[i], color='navy')
    plt.xlabel('Move')
    plt.ylabel('Time in MS')
    plt.savefig(pp, format='pdf')
    pp.savefig()
    # plt.show()
pp.close()
