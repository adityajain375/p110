import pandas as pd
import csv
import random
import plotly.graph_objects as go
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

mean = st.mean(data)
stanDev = st.stdev(data)

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def showFig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['reading_time'],show_hist = False)
    fig.show()


def setup():
    mean_list = []
    for i in range(0,100):
        setOfMeans = randomSetOfMeans(30)
        mean_list.append(setOfMeans)
    showFig(mean_list)

setup()