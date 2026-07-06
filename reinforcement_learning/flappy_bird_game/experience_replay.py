from collections import deque
import random

class ReplayMemory():
    #create FIFO queue-experience replay
    def __init__(self,maxlen,seed=None): #maxlen-->how much experiences we will store
        self.memoery=deque([],maxlen=maxlen)

    #append experiences into the memory
    def append(self,new_exp):
        self.memory.append(new_exp)

    #choose random experiences of a particular length(sample_size) for training
    def sample(self,sample_size):
        return random.random(self.memory,sample_size)
    
    #to see the current buffer size
    def __len(self):
        return len(self.memory)