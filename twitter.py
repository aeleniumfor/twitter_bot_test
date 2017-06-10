#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Twitter用
import tweepy
import time
import numpy as np
import sqlite3

def db_connect():
    db = sqlite3.connect('../token.db')
    db_data = db.cursor()
    db_data= db_data.execute("select * from ttoken;")
    db_ret = db_data.fetchall()
    db.close()
    return db_ret

acctoken=db_connect()

time_list = np.random.randint(300,1000,size=100)
twitt_list = ["やべー","かっこいい","おなか減った","やったー","あ","コート返してほしい...",
              "おいしそう","美味","パケット...","数学...","fedora","なる","あのネクタイほしい",
              "アニメ見よ...","眠たい...","眠い","マックに行きたい","楽しい!!","オフ","オン"]

consumer_key=acctoken[0][0]
consumer_secret= acctoken[0][1]
token= acctoken[0][2]
tokensecret= acctoken[0][3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, tokensecret)
api = tweepy.API(auth)

for i in range(10):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, tokensecret)
    api = tweepy.API(auth)
    randomv = np.random.choice(time_list)
    random_comment = np.random.choice(twitt_list)
    print(str(randomv)+"秒停止")
    api.update_status(random_comment)
    time.sleep(randomv)