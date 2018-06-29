# core modules
import logging.config
import math
import os

# 3rd party modules
import numpy as np
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

class SudokuEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.__version__ = "0.1.0"
        logging.info("SudokuEnv - Version {}".format(self.__version__))
        
        # General variables defining the environment
        self.TOTAL_TIME_STEPS = 90

        self.current_step = -1
        self.is_false = False

        # Define what the agent can do
        #self.action_space = spaces.Discrete(21)

        # Observation is the remaining time
        low = np.array([0.0, # remaining time
                        ])
        high = np.array([self.TOTAL_TIME_STEPS, # remaining_tries
                        ])
        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        # Store what the agent tried
        self.current_episode = -1
        self.action_episode_memory = []

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

    if self.is_false:
        raise RuntimeError("Episode is done")
    self.current_step += 1
    self._take_action(action)
    reward = self._get_reward()
    ob = self._get_state()
    return ob, reward, self.is_false, {}

    def _reset(self):
    """
    Reset the state of the environment and returns an initial observation.

    Returns
    -------
    observation (object) : the initial observation of the space.
    """
    self.current_episode +=1
    self.action_episode_memory.append([])
    self.is_false = False
    # line missing !!!
    #self.grid...
    return self._get_state()

    def _render(self, mode='human', close=False):
        return

    def _get_state(self):
        """Get the observation."""
        ob = [self.TOTAL_TIME_STEPS - self.current_step]
        return ob

    def _take_action(self, action):
        pass

    def _get_reward(self):
        pass




