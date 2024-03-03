#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:27:32 2024

@author: mcerdeiro
"""


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

#%%
data = pd.read_csv('taylor_album_songs.csv')

data.describe()
data.head()


#%%
"""['album_name', 'ep', 'album_release', 'track_number', 'track_name',
       'artist', 'featuring', 'bonus_track', 'promotional_release',
       'single_release', 'track_release', 'danceability', 'energy', 'key',
       'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
       'liveness', 'valence', 'tempo', 'time_signature', 'duration_ms',
       'explicit', 'key_name', 'mode_name', 'key_mode', 'lyrics']
"""
#%%
data.columns
sel_columns = ['loudness', 'danceability', 'energy', 'valence', 'acousticness', 'speechiness']

data_sel  = data[sel_columns].dropna()
X=data_sel.values
#%%
plt.scatter(X[:, 1], X[:,4])
#%%
sns.pairplot(data_sel)
plt.savefig('pairplot_taylor')
#%%
pca = PCA(n_components=2)

pca.fit(X)


print(pca.components_)
XX = pca.fit_transform(X)
plt.scatter(X[:,0], X[:,4])
plt.scatter(XX[:,0], XX[:,1])


