# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:31:56 2017

@author: lenny
"""
# import your dependencies
# I recommend using spyder from Anaconda to run such ML programs 
import numpy as np
from lightfm.datasets import  fetch_movielens
from lightfm import LightFM

# fetch data and format it
data = fetch_movielens(min_rating=5.0)

# printing training and testing data
print(repr(data['train']))
print('\n')
print(repr(data['test']))

# create model
model = LightFM(loss='warp')

# train model
model.fit(data['train'], epochs=30, num_threads=2)


def sample_recommendation(model, data, user_ids):
    # number of users and movies in trainng data
    n_users, n_items, = data['train'].shape

    # generate recommendations for each user we input
    for user_id in user_ids:
        # movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies our model predicts  they will like
        scores = model.predict(user_id, np.arange(n_items))
        # ranking from most liked to least liked
        top_items = data['item_labels'][np.argsort(-scores)]

        # printing results
        print('user %s' % user_id)
        print('  known positives:')

        for x in known_positives[:5]:
            print('       %s ' % x)

        print('  recommended')

        for x in top_items[:5]:
            print('     %s' % x)


sample_recommendation(model,data, [4, 20, 5])
            