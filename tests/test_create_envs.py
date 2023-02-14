# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

import gymnasium as gym
import gym_dart
import pytest


env_names = [
    'DartCartPole-v0',
    # 'DartParticle-v0',
    # 'DartReacher-v0'
]


def test_create_envs():
    for env_name in env_names:
        env = gym.make(env_name)
