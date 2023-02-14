import numpy as np
import math

from gym_dart.envs import DartEnv
from gymnasium.spaces import Space
from gymnasium import error, logger, spaces
from gymnasium.spaces import Box


class DartCartPoleEnv(DartEnv):
    def __init__(self):
        # Angle at which to fail the episode
        self.theta_threshold_radians = 12 * 2 * math.pi / 360
        self.x_threshold = 2.4

        # Angle limit set to 2 * theta_threshold_radians so failing observation
        # is still within bounds.
        high = np.array(
            [
                self.x_threshold * 2,
                np.finfo(np.float32).max,
                self.theta_threshold_radians * 2,
                np.finfo(np.float32).max,
            ],
            dtype=np.float32,
        )

        DartEnv.__init__(
            self,
            observation_space=Box(-high, high, dtype=np.float32),
            world_path="cartpole.skel",
            name="Cartpole",
        )

        self.world.setGravity([0, 0, -9.8])
        self.world.setTimeStep(0.01)

        self.cartpole = self.world.getSkeleton("cartpole")

        self.max_time_steps = 10000
        self.current_step = 0

        self.theta_threshold = 0.1

        # State
        self.state_dim = 4
        self.state_max = np.ones(self.state_dim) * 10
        self.state_min = -self.state_max
        self.initial_state_upper_limits = np.ones(self.state_dim) * 0.1
        self.initial_state_lower_limits = -self.initial_state_upper_limits

        # Goal
        self.goal_dim = 2
        self.goal_max = np.ones(self.goal_dim) * 5.0
        self.goal_min = -self.goal_max
        self.goal = np.zeros(self.goal_dim)

        # Action
        self._action_dim = 1
        self.cart_velocity_upper_limits = np.ones(self._action_dim) * 5.0
        self.cart_velocity_lower_limits = -self.cart_velocity_upper_limits
        self.action_space = spaces.Box(
            low=self.cart_velocity_lower_limits,
            high=self.cart_velocity_upper_limits,
            dtype=np.float32,
        )

        self.reset()

    def reset(self):
        self._simulation_reset()
        return self._get_obs()

    def step(self, action):
        """Returns reward"""
        reward = self._simulation_step(action)
        obs = self._get_obs()
        done = self._is_done()

        return obs, reward, done

    def get_state_dim(self):
        return self.state_dim

    def get_state_max(self):
        return self.state_max

    def get_state_min(self):
        return self.state_min

    def get_state(self):
        pos = self.cartpole.getPositions()
        vel = self.cartpole.getVelocities()
        return np.array([pos[1], vel[1], pos[0], vel[0]])

    def get_obs_max(self):
        # Assumed fully observable
        return self.get_state_max()

    def get_obs_min(self):
        # Assumed fully observable
        return self.get_state_min()

    def _get_obs(self):
        # Assumed fully observable
        return self.get_state()

    def get_goal_dim(self):
        return self.goal_dim

    def get_goal_max(self):
        return self.goal_max

    def get_goal_min(self):
        return self.goal_min

    def get_goal(self):
        return self.goal

    def get_action_dim(self):
        return self._action_dim

    def get_action_max(self):
        return self.cart_velocity_upper_limits

    def get_action_min(self):
        return self.cart_velocity_lower_limits

    def _simulation_reset(self):
        self.world.reset()
        self.current_step = 0

        pos = np.random.uniform(
            self.initial_state_lower_limits, self.initial_state_upper_limits
        )
        self.cartpole.setPosition(0, pos[2])
        self.cartpole.setVelocity(0, pos[3])
        self.cartpole.setPosition(1, pos[0])
        self.cartpole.setVelocity(1, pos[1])
        self.cartpole.resetAccelerations()

        return self.get_state()

    def _get_reward(self, _):
        state = self.get_state()
        pole_theta = state[0]
        cart_pos = state[2]

        if np.abs(pole_theta) < self.theta_threshold:
            reward = (
                self.theta_threshold - np.abs(pole_theta)
            ) / self.theta_threshold + np.exp(-cart_pos)
        else:
            reward = 0.0

        return reward

    def _simulation_step(self, action, take_step=True):
        if self._is_done():
            return 0

        action = np.clip(action, self.get_action_min(), self.get_action_max())
        self.cartpole.setVelocity(0, action[0])

        if take_step:
            reward = self._get_reward(action)
            self.world.step()
            self.current_step += 1
            return reward
        else:
            # self.world.step()
            self.current_step += 1
            return 0

    def _is_done(self):
        state = self.get_state()
        pole_theta = state[0]
        cart_pos = state[2]

        has_step_reached_max = self.current_step >= self.max_time_steps
        is_pole_theta_out_of_bound = np.abs(pole_theta) > self.theta_threshold
        is_cart_out_of_bound = np.abs(cart_pos) > 1.0

        return (
            is_pole_theta_out_of_bound or is_cart_out_of_bound or has_step_reached_max
        )
