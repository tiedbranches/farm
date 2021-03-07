import pandas as pd
#import seaborn as sns
import numpy as np



df = pd.read_table("C:/Users/tiedbranches/Downloads/glove.6B.50d.txt/glove_6B_50d.txt", delimiter=" ", header=None, index_col=0, quoting=3)


words = set(df.index)
print(len(words))

print("happy" in words)

whatever = ["happy", "sad","rich", "poor", "important", "unimportant","good", "bad", "evil","healthy", "ill","high", "low", "up", "down",
            "conscious", "unconscious", #            "rational", "emotional","more", "less",#          "idealistic", "down-to-earth", "practical",
            "unknown", "known",
            "finished", "incomplete", "complete",
            "positive", "negative",
            "big", "small", "little", "enormous",
            "beginning", "end",
            "future", "past",
            "spirit", "body",
            #          "sky", "ground",
            #           "heavenly", "hell", "salvation",
            "virtuous", "sinful",
            #           "central", "peripheral",
            #           "urban", "rural",
            "active", "passive",
            "hot", "cold",

            "loud", "quiet",
            #          "expensive", "cheap", "costly",
            "normal", "eccentric", "strange",
            "front", "back",
            "on", "off"
            ]


def norm(df):
    b = np.linalg.norm(df)
    print("NORM: ",b)
    return b

a=df.loc[whatever].dot(df.loc["up"] - df.loc["down"])  # .sort_values()
print(type(a))

#lens = (df**2).sum(axis=1).sort_values()
dfsq = (df**2)
dfsq_ad = (df**2).sum(axis=1)
#print("DF: ",df)
print("DFSQ: ",dfsq.loc["the"])

print("The value: 24.679304")

line = dfsq.loc["the"]
sum = 0
for i in line:
    index=1
    sum += line[index]
    index +=1
    print(sum)


