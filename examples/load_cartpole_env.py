import sys
import gymnasium as gym
import gym_dart


if __name__ == '__main__':
    if len(sys.argv) > 1:
        env = gym.make(sys.argv[1])
    else:
        env = gym.make('DartCartPole-v0')

    env.reset()

    for i in range(1000):
        print('i:', i, ', ', env.step([0, 0]))
