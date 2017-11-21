'''
Created on 08-Nov-2017

@author: advai
'''
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from sklearn import datasets
from sklearn.cross_validation import StratifiedKFold
from sklearn.svm import SVC
from sklearn import metrics
import os
import numpy as np
from model import PaperData
import gensim
import experiment
def load_vec(d, data, use_pkl=False, file_name=None):
    # print("call get_document_vec")
    return d.get_document_vec(data, file_name)

from learners import SK_SVM
learner = [SK_SVM][0]

word_src = "word2vecs_models"
myword2vecs = [os.path.join(word_src, i) for i in os.listdir(word_src)
                   if "syn" not in i]

def run_tuning_SVM(word2vec_src, repeats=1,fold=10,tuning=True):
  print("# word2vec:", word2vec_src)
  word2vec_model = gensim.models.Word2Vec.load(word2vec_src)
  data = PaperData(word2vec=word2vec_model)
  train_pd = load_vec(data, data.train_data, file_name=False)
  test_pd = load_vec(data, data.test_data, file_name=False)
  learner = [SK_SVM][0]
  goal = {0: "PD", 1: "PF", 2: "PREC", 3: "ACC", 4: "F", 5: "G", 6: "Macro_F",
          7: "Micro_F"}[6]
  F = {}
  clfs = []
  for i in xrange(repeats):  # repeat n times here
    kf = StratifiedKFold(train_pd.loc[:, "LinkTypeId"].values, fold,shuffle=True)
    print kf
    for train_index, tune_index in kf:
        train_data = train_pd.ix[train_index]
        tune_data = train_pd.ix[tune_index]
        train_X = train_data.loc[:, "Output"].values
        train_Y = train_data.loc[:, "LinkTypeId"].values
        tune_X = tune_data.loc[:, "Output"].values
        tune_Y = tune_data.loc[:, "LinkTypeId"].values
        test_X = test_pd.loc[:, "Output"].values
        test_Y = test_pd.loc[:, "LinkTypeId"].values
        params, evaluation = experiment.tune_learner(learner, train_X, train_Y, tune_X,tune_Y, goal) if tuning else ({}, 0)
#       clf = learner(train_X, train_Y, test_X, test_Y, goal)
#       F = clf.learn(F, **params)
#       clfs.append(clf)
#   print_results(clfs)

run_tuning_SVM(myword2vecs[0])