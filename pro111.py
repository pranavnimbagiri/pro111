import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
df=pd.read_csv("proj.csv")
data=df["reading_time"].tolist()
figure=ff.create_distplot([data],["scores"],show_hist=False)

#figure.show()
mean=statistics.mean(data)
sd=statistics.stdev(data)
print(mean)
print(sd)

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

meanlist=[]
for i in range(0,1000):
    setofmeans=randomsetofmean(100)
    meanlist.append(setofmeans)
standarddeviation=statistics.stdev(meanlist)
mean1=statistics.mean(meanlist)
print(standarddeviation)
print(mean1)

firstSDstart,firstSDend=mean-standarddeviation,mean+standarddeviation
secondSDstart,secondSDend=mean-(2*standarddeviation),mean+(2*standarddeviation)
thirdSDstart,thirdSDend=mean-(3*standarddeviation),mean+(3*standarddeviation)

fig=ff.create_distplot([meanlist],["proj"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[firstSDstart,firstSDstart],y=[0,0.17],mode="lines",name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[secondSDstart,secondSDstart],y=[0,0.17],mode="lines",name="sd 2 start"))
fig.add_trace(go.Scatter(x=[secondSDend,secondSDend],y=[0,0.17],mode="lines",name="sd 2 end"))
fig.add_trace(go.Scatter(x=[thirdSDstart,thirdSDstart],y=[0,0.17],mode="lines",name="sd 3 start"))
fig.add_trace(go.Scatter(x=[thirdSDend,thirdSDend],y=[0,0.17],mode="lines",name="sd 3 end"))

#fig.show()

df=pd.read_csv("proj.csv")
data=df["reading_time"].tolist()
meanofsampling1=statistics.mean(data)
print(meanofsampling1)

fig=ff.create_distplot([meanlist],["studentmarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsampling1,meanofsampling1],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="standard deviation 1 start"))

df=pd.read_csv("proj.csv")
data=df["reading_time"].tolist()
meanofsampling2=statistics.mean(data)
print(meanofsampling1)

fig=ff.create_distplot([meanlist],["studentmarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsampling2,meanofsampling2],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[firstSDend,firstSDend],y=[0,0.17],mode="lines",name="standard deviation 1 start"))

#figure.show()
df=pd.read_csv("proj.csv")
data=df["reading_time"].tolist()
meanofsampling3=statistics.mean(data)
print(meanofsampling1)

fig=ff.create_distplot([meanlist],["studentmarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsampling3,meanofsampling3],y=[0,0.17],mode="lines",name="mean of sample"))
fig.add_trace(go.Scatter(x=[secondSDend,secondSDend],y=[0,0.17],mode="lines",name="standard deviation 1 start"))

fig.add_trace(go.Scatter(x=[thirdSDend,thirdSDend],y=[0,0.17],mode="lines",name="standard deviation 1 start"))

zscore=(meanofsampling1-mean1)/standarddeviation
print(zscore)
zscore=(meanofsampling2-mean1)/standarddeviation
print(zscore)
zscore=(meanofsampling3-mean1)/standarddeviation
print(zscore)
#fig.show()
