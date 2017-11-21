'''
Created on 11-Nov-2017

@author: advai
'''
counter = 0
import random
class Particle():
    def __init__(self,kernel,position,velocity,bestPosition,fitness = -1, bestFitness = -1):
        self.kernel = kernel
        self.position = position
        self.velocity = velocity
        self.bestPosition = bestPosition
        self.fitness = fitness['Macro_F']
        self.bestFitness = bestFitness['Macro_F']

class PSO(object):
    def __init__(self,learner, params_distribution, goal, target_class,hi_lo,
               num_population=10, iterations=100, w=0.75, c1=1.2, c2=0.8,bestGlobal=-1):
        self.learner = learner
        self.np = num_population
        self.iterations = iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.params_distribution = params_distribution
        self.goal = goal
        self.target_class = target_class
        self.evaluation = 0
        self.scope =hi_lo
        self.scores = {}
        self.frontier = [self.generate_kernel(kernel,self.scope) for kernel in ['linear','rbf','sigmoid','poly']for _ in xrange(self.np)]
        self.swarm = []
        self.particleInitialization(self.swarm, self.scope)
        self.minC = self.scope['lo']['C']
        self.maxC = self.scope['hi']['C']
        self.minCoef = self.scope['lo']['coef0'] 
        self.maxCoef = self.scope['hi']['coef0'] 
        self.minGamma =  self.scope['lo']['gamma']
        self.maxGamma =  self.scope['hi']['gamma']
        self.minX = [self.minC,self.minCoef,self.minGamma]
        self.maxX = [self.maxC,self.maxCoef,self.maxGamma]
#         for i in self.swarm:
#             print i.kernel
#             print i.position
#             print i.velocity
#             print i.bestPosition
#             print i.fitness
#             print i.bestFitness
        self.bestGlobal = self.swarm[0].bestFitness
        self.bestParameters = {'kernel':self.swarm[0].kernel,'C':self.swarm[0].position[0],'coef0':self.swarm[0].position[1],'gamma':self.swarm[0].position[2], 'random_state':1}
        self.bestGlobalPosition = [self.swarm[0].position[0],self.swarm[0].position[1],self.swarm[0].position[2]]

    def generate_kernel(self,kernel,scope):
        candidate = {}
        def generate_1(scope):
            
            global counter
#         print self.params_distribution
            for key, val in self.params_distribution.iteritems():
                if isinstance(val[0], float):
                    candidate[key] = round(random.uniform(val[0], val[1]), 3)
                elif isinstance(val[0], bool):
                    candidate[key] = random.random() <= 0.5
                elif isinstance(val[0], str):
                    candidate[key] = kernel
                    counter += 1
                elif isinstance(val[0], int):
                    candidate[key] = int(random.uniform(val[0], val[1]))
                elif isinstance(val[0], list) and isinstance(val[0][0], int):
                    candidate[key] = [int(random.uniform(each[0], each[1])) for each in val]
                else:
                    raise ValueError("type of params distribution is wrong!")  
#         print candidate
            if "random_state" in self.params_distribution.keys():
                candidate["random_state"] = 1  ## set random seed here
            
            return candidate
        return (generate_1(scope))
      
    def generate(self,scope):
        candidate = {}
        global counter
#         print self.params_distribution
        for key, val in self.params_distribution.iteritems():
          if isinstance(val[0], float):
            candidate[key] = round(random.uniform(val[0], val[1]), 3)
          elif isinstance(val[0], bool):
            candidate[key] = random.random() <= 0.5
          elif isinstance(val[0], str):
            candidate[key] = val[counter%len(val)]
            counter += 1
          elif isinstance(val[0], int):
            candidate[key] = int(random.uniform(val[0], val[1]))
          elif isinstance(val[0], list) and isinstance(val[0][0], int):
            candidate[key] = [int(random.uniform(each[0], each[1])) for each in
                              val]
          else:
            raise ValueError("type of params distribution is wrong!")  
#         print candidate
        if "random_state" in self.params_distribution.keys():
          candidate["random_state"] = 1  ## set random seed here
            
        return candidate
    
    def initialVelocity(self,scope):
        hi_c = scope['hi']['C']
        lo_c = scope['lo']['C']
        hi_gamma = scope['hi']['gamma']
        lo_gamma = scope['lo']['gamma']
        hi_coef = scope['hi']['coef0']
        lo_coef = scope['lo']['coef0']
        random_vel_c = (abs(hi_c - lo_c) - (-1.0 *abs(hi_c - lo_c)))*random.random() + (-1.0 *abs(hi_c - lo_c))
        random_vel_gamma = (abs(hi_gamma - lo_gamma) - (-1.0 *abs(hi_gamma - lo_gamma)))*random.random() + (-1.0 *abs(hi_gamma - lo_gamma))
        random_vel_coef = (abs(hi_coef - lo_coef) - (-1.0 *abs(hi_coef - lo_coef)))*random.random() + (-1.0 *abs(hi_coef - lo_coef))
        return [random_vel_c,random_vel_coef,random_vel_gamma] 
   
    
    def particleInitialization(self,swarm,scope):
        for n, kwargs in enumerate(self.frontier):
            score_dict = self.learner.learn({}, **kwargs)
            self.scores[n] = self.get_target_score(score_dict)
            bestKernel = kwargs['kernel']
#             candidate['bestRandomState'] = kwargs['random_state']
            vel = self.initialVelocity(scope)
    #         print candidate
            initial = [kwargs['C'],kwargs['coef0'],kwargs['gamma']]
            fitness = self.scores[n]
            bestFitness  = fitness
            swarm.append(Particle(bestKernel,initial,vel,initial,fitness,bestFitness))
    
    def get_target_score(self, score_dict):
        temp = {}
        for key, val in score_dict.iteritems():
            if key == self.target_class:
                temp[key] = val[0]  # value, not list
        return temp
    
    
    def computeScore(self,kwargs):
            score_dict = self.learner.learn({}, **kwargs)
            self.scores[0] = self.get_target_score(score_dict)
            return self.scores[0]

    
    def Tune(self):
        for iteration in range(self.iterations):
            for currP in self.swarm:
                new_velocity = []
                new_position = []
                for j in range(len(currP.velocity)):
                    r1 = random.random()
                    r2 = random.random()
                    temp = (self.w*currP.velocity[j]) + (self.c1*r1*(currP.bestPosition[j] - currP.position[j])) + (self.c2 * r2 * (self.bestGlobalPosition[j] - currP.position[j]))
                    if temp < self.minX[j]:
                        temp = self.minX[j]
                    elif temp > self.maxX[j]:
                        temp =  self.maxX[j]
                    new_velocity.append(temp)
                currP.velocity = new_velocity
                for j in range(len(currP.position)):
                    temp = currP.position[j] + currP.velocity[j]
                    if temp < self.minX[j]:
                        temp = self.minX[j]
                    elif temp > self.maxX[j]:
                        temp =  self.maxX[j]
                    new_position.append(temp)
                    
                    temp_D = {'kernel':currP.kernel}
                    if j ==0:
                        temp_D['C'] = currP.position[j]
                    elif j == 1:
                        temp_D['coef0'] = currP.position[j]
                    elif j == 2:
                        temp_D['gamma'] = currP.position[j]
                currP.position = new_position
                temp_D['random_state'] = 1
                fitness = self.computeScore(temp_D)
                self.evaluation += 1
                if  fitness['Macro_F'] >  currP.bestFitness:
                    currP.bestFitness = fitness['Macro_F']
                    currP.bestPosition = currP.position
          
                if fitness['Macro_F'] >  self.bestGlobal:
                    self.bestGlobal = fitness['Macro_F']
                    self.bestParameters = {'kernel':currP.kernel,'C':currP.position[0],'coef0':currP.position[1],'gamma':currP.position[2],'random_state':1}
            
            return (self.bestParameters,self.evaluation)
            
        

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




class DE_Tune_ML(PSO):
  def __init__(self, learner,params_distribution, goal, target_class,hi_lo,
               num_population=10, iterations=100, w=0.75, c1=1.2, c2=0.8):
    self.learner = learner
    
    super(DE_Tune_ML, self).__init__(learner,params_distribution,goal, target_class,hi_lo,
               num_population=10, iterations=100, w=0.75, c1=1.2, c2=0.8)
    
    


tunelst = {"kernel": ["linear", "poly", "rbf", "sigmoid"],
               "C": [1, 50],
               "coef0": [0.0, 1],
               "gamma": [0.0, 1],
               "random_state": [1, 1]}   
    
