import gym
import sinergym
import numpy as np

from sinergym.utils.wrappers import MultiObsWrapper, NormalizeObservation, LoggerWrapper

default_env = gym.make('Eplus-demo-v1')

# apply wrappers
env = MultiObsWrapper(LoggerWrapper(NormalizeObservation(default_env)))

for i in range(1):
    obs = env.reset()
    rewards = []
    done = False
    current_month = 0
    while not done:
        a = env.action_space.sample()
        obs, reward, done, info = env.step(a)
        rewards.append(reward)
        if info['month'] != current_month:  # display results every month
            current_month = info['month']
            print('Reward: ', sum(rewards), info)
    print('Episode ', i, 'Mean reward: ', np.mean(
        rewards), 'Cumulative reward: ', sum(rewards))
env.close()
