import flappy_bird_gymnasium
import gymnasium as gym
import torch 
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml
import torch.nn as nn
import torch.optim as optim

if torch.backends.mps.is_available():
    device="mps"
elif torch.cuda.is_available():
    device="cuda"
else:
    device="cpu"

class Agent:
    def __init__(self,params_set):
        self.params_set=params_set

        with open("parameters.yaml","r") as f:
            all_params_set=yaml.safe_load(f)
            params=all_params_set[params_set]

        #saare paramets save krenge
        self.alpha=params["alpha"]
        self.gamma=params["gamma"]
        self.reward_threshold=params["reward_threshold"]
        self.network_sync_rate=params["network_sync_rate"]
        self.mini_batch_size=params["mini_batch_size"]
        self.replay_memory_size=params["replay_memory_size"]
        self.epsilon_decay=params["epsilon_decay"]
        self.epsilon_min=params["epsilon_min"]
        self.epsilon_init=params["epsilon_init"]

        self.loss_fn=nn.MSELoss()
        self.optimizer=None
        
    def run(self,is_training=True,render=False):
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states=env.observation_space.shape[0]  #input dim #instead of shape[0] we can also write .n
        num_actions=env.action_space.n  #output dim
        policy_dqn=DQN(num_states,num_actions).to(device) #no.of states and actions are passed

        

        if is_training:
            memory=ReplayMemory(self.replay_memory_size) #maxlen pass kiya h

        for episode in itertools.count():

            state, _ = env.reset()
            episode_reward=0
            terminated=False

            while not terminated:
                # Next action:
                # (feed the observation to your agent here)
                action = env.action_space.sample()

                # Processing: terminated-->done
                next_state, reward, terminated, _, _ = env.step(action)

                if is_training:
                    memory.append((state,action,next_state,reward,terminated)) #joh sikha h voh memory mei daal do
                
                state=next_state
                episode_reward+=reward
                
            print(f"for episode{episode} total rewards={episode_reward}")
            #env.close()-->manually stop krenge