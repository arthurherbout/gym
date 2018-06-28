import numpy as np
import os
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

class SudokuEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def step(self, action):
       """
        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environmment-specific object representing your observation of the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale varies between environments, but the goal is always to increase your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and done being True indicates the episode has terminated.
            info (dict) :
                diagnostic information useful for debugging. It can sometimes be useful for learning. However, official evaluations of your agent are not allowed to use this for learning.
       """
       self._take_action(action)
       self._status = self.env.step()
       ob = self.env.getState()
       episode_over = self.status !=hfo_py.IN_GAME
       return ob, reward, episode_over, {}

    def _reset(self):
        pass

    def _render(self, mode='human', close= False):
        pass

    def _take_action(self, action):
        pass

    def _get_reward(self):
        pass




