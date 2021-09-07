# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 02:56:52 2021

@author: Pano
"""
from kaggle.api.kaggle_api_extended import KaggleApi
import os
from path import Path
from zipfile import ZipFile
import pandas as pd
api = KaggleApi()
api.authenticate()

print(api.competitions_list(search='mnist'))
competitionName=str(api.competitions_list(search='mnist')[0])

print("Working Directory: ",os.getcwd())

location=r'C:\Users\Pano\Desktop\Kaggle\Competitions\MNIST'
locationPath=Path(location)

api.competition_download_files(competitionName,path=locationPath)


zipFile = ZipFile(location+'\\'+competitionName+'.zip')
zipFile.extractall(location+r'\datasets') 
zipFile.close()


df_train=pd.read_csv(location+r'\datasets\train.csv')
df_test=pd.read_csv(location+r'\datasets\train.csv')
df_sampleSubmission=pd.read_csv(location+r'\datasets\sample_submission.csv')