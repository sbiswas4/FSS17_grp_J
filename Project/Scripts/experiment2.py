'''
Created on 12-Nov-2017

@author: advai
'''
from __future__ import division, print_function
import pickle
import pdb
import os
import time
from sklearn.cross_validation import StratifiedKFold
from sklearn import svm
from sklearn import metrics
import gensim
import random
from learners import SK_SVM
from tuner_2 import DE_Tune_ML
from model import PaperData
from utility import study
from results import results_process
import numpy as np
import wget
import zipfile
import time


def tune_learner(learner, train_X, train_Y, tune_X, tune_Y, goal,
                 target_class=None):
  """
  :param learner:
  :param train_X:
  :param train_Y:
  :param tune_X:
  :param tune_Y:
  :param goal:
  :param target_class:
  :return:
  """
  if not target_class:
    target_class = goal
  clf = learner(train_X, train_Y, tune_X, tune_Y, goal)
  tuner = DE_Tune_ML(clf, clf.get_param(), goal, target_class,hi_lo(clf.get_param()))
  return tuner.Tune()

def hi_lo(params):
        hi = {}
        lo = {}
        for value in params:
            
            if value == 'C':
                hi['C'] = params[value][1]
                lo['C'] = params[value][0]
            elif value == 'coef0':
                hi['coef0'] = params[value][1]
                lo['coef0'] = params[value][0]
            elif value == 'gamma':
                hi['gamma'] = params[value][1]
                lo['gamma'] = params[value][0]
        return {'hi':hi,'lo':lo}

@study
def run_tuning_SVM(word2vec_src, repeats=1,
                   fold=5,
                   tuning=True):
  
  print(time.time())
  print("# word2vec:", word2vec_src)
  word2vec_model = gensim.models.Word2Vec.load(word2vec_src)
  print(time.time())
  data = PaperData(word2vec=word2vec_model)
  train_pd = load_vec(data, data.train_data, file_name=False)
  test_pd = load_vec(data, data.test_data, file_name=False)
  print(time.time())
  learner = [SK_SVM][0]
  goal = {0: "PD", 1: "PF", 2: "PREC", 3: "ACC", 4: "F", 5: "G", 6: "Macro_F",
          7: "Micro_F"}[6]
  F = {}
  clfs = []
  for i in xrange(repeats):  # repeat n times here
    kf = StratifiedKFold(train_pd.loc[:, "LinkTypeId"].values, fold,
                         shuffle=True)
    print("Stratified")
    print(time.time())
    for train_index, tune_index in kf:
      train_data = train_pd.ix[train_index]
      tune_data = train_pd.ix[tune_index]
      train_X = train_data.loc[:, "Output"].values
      train_Y = train_data.loc[:, "LinkTypeId"].values
      tune_X = tune_data.loc[:, "Output"].values
      tune_Y = tune_data.loc[:, "LinkTypeId"].values
      test_X = test_pd.loc[:, "Output"].values
      test_Y = test_pd.loc[:, "LinkTypeId"].values
      params, evaluation = tune_learner(learner, train_X, train_Y, tune_X,
                                            tune_Y, goal) if tuning else ({}, 0)
#       params = {'kernel':'rbf','C':1,'gamma':'auto'}
      print("Tuning Done...now running")
      print("********************")
      print(params)
      print("********************")
      clf = learner(train_X, train_Y, test_X, test_Y, goal)
      F = clf.learn(F, **params)
      clfs.append(clf)
    print_results(clfs)

def print_results(clfs):
#   file_name = time.strftime(os.path.sep.join([".", "results",
#                                               "%Y%m%d_%H:%M:%S.txt"]))
  file_name = "output_see_new_pso_wdamp_5x5.txt"
  content = ""
  for each in clfs:
    content += each.confusion
  with open(file_name, "w") as f:
    f.write(content)
  results_process.reports(file_name)



def load_vec(d, data, use_pkl=False, file_name=None):
  if use_pkl:
    if os.path.isfile(file_name):
      with open(file_name, "rb") as my_pickle:
        return pickle.load(my_pickle)
  else:
    # print("call get_document_vec")
    return d.get_document_vec(data, file_name)

if __name__ == "__main__":
  word_src = "word2vecs_models"
  for x in xrange(5):
    random.seed(x)
    np.random.seed(x)
    myword2vecs = [os.path.join(word_src, i) for i in os.listdir(word_src)
                   if "syn" not in i]
    run_tuning_SVM(myword2vecs[x])