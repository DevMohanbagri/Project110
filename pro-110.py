import plotly.figure_factory as pff
import plotly.graph_objects as go
import random
import statistics
import csv
import pandas as pd 

df = pd.read_csv('medium_data.csv')

data = df['responses'].tolist()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)

print('Mean = ',population_mean)
print('StDev = ',stdev)

#function to get the mean of given data samples
def random_set_of_mean(counter):

    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print('Mean of sampling distribution', mean)
    fig = pff.create_distplot(
        [df],
        ['temp'],
        show_hist = False
    )
   
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines", name = "MEAN"))

    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    show_fig(mean_list)
