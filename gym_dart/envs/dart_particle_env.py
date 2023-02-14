# import numpy as np
# import numpy.linalg as la

# from gym_dart.envs import DartEnv
# import gymnasium as gym.spaces as spaces

# class DartParticleEnv(DartEnv):

#     def __init__(self):
#         DartEnv.__init__(self, world_path='particle.skel')

#         self.world.setGravity(np.array([0, 0, -9.8]))
#         self.world.setTimeStep(0.01) # FUTURE: make this an input parameter
#         self.max_time_steps = 1000  # FUTURE: make this an input parameter

#         self.particle_skeleton = self.world.getSkeleton('particle')
#         assert self.particle_skeleton is not None
#         self.particle = self.particle_skeleton.getRootBodyNode()
#         assert self.particle is not None

#         self.target_skeleton = self.world.getSkeleton('target')
#         assert self.target_skeleton is not None
#         self.target = self.target_skeleton.getRootBodyNode()
#         assert self.target is not None

#         self.current_step = 0

#         # Observations
#         self.obs_dim = 8
#         self.obs_max = np.array([
#             0.2, 0.2,  # XY_position_of_particle
#             5.0, 5.0,  # XY_velocity_of_particle
#             0.2, 0.2,  # XY_position_of_target
#             1.0, 1.0,  # diff_positions
#         ])
#         self.obs_min = -self.obs_max
#         self.initial_particle_pos_lower_limits = np.ones(2) * -0.2
#         self.initial_particle_pos_upper_limits = np.ones(2) * 0.2
#         self.initial_target_pos_lower_limits = np.ones(2) * -0.2
#         self.initial_target_pos_upper_limits = np.ones(2) * 0.2
#         self.observation_space = spaces.Box(low=self.obs_min, high=self.obs_max)

#         # Goal
#         self.goal_dim = 2
#         self.goal_max = np.ones(self.goal_dim) * 0.2
#         self.goal_min = -self.goal_max
#         self.goal = np.zeros(self.goal_dim)

#         # Action
#         self.action_dim = 2
#         self.actuator_upper_limits = np.ones(self.action_dim) * 1
#         self.actuator_lower_limits = -self.actuator_upper_limits
#         self.action_space = spaces.Box(low=self.actuator_lower_limits, high=self.actuator_upper_limits)

#         self.reset()

#     def step(self, action):
#         reward = self._get_reward(action)
#         self._step_world(action)
#         obs = self._get_obs()
#         done = self._is_done()
#         self.current_step += 1
#         info = None
#         return obs, reward, done, info

#     def reset(self):
#         self.world.reset()
#         self.current_step = 0

#         particle_pos \
#             = np.random.uniform(self.initial_particle_pos_lower_limits, self.initial_particle_pos_upper_limits)
#         self.particle_skeleton.setPosition(0, particle_pos[0])
#         self.particle_skeleton.setPosition(1, particle_pos[1])
#         self.particle_skeleton.resetVelocities()
#         self.particle_skeleton.resetAccelerations()

#         target_pos \
#             = np.random.uniform(self.initial_target_pos_lower_limits, self.initial_target_pos_upper_limits)
#         self.target_skeleton.setPosition(0, target_pos[0])
#         self.target_skeleton.setPosition(1, target_pos[1])

#         return self._get_obs()

#     def render(self, mode='human'):
#         pass

#     def _get_obs(self):
#         particle_xy_pos = self.particle_skeleton.getPositions()[:2]
#         particle_xy_vel = self.particle_skeleton.getVelocities()[:2]
#         target_xy_pos = self.target_skeleton.getPositions()[:2]
#         target_com = self.target.getCOM()
#         particle_com = self.particle.getCOM()
#         diff_com = (target_com - particle_com).flatten()[:2]
#         self.diff_norm = la.norm(diff_com)
#         return np.concatenate([
#             particle_xy_pos.flatten(),
#             particle_xy_vel.flatten(),
#             target_xy_pos.flatten(),
#             diff_com.flatten(),
#         ])

#     def _step_world(self, action):
#         if self._is_done():
#             return 0
#         action = np.clip(action, self.actuator_lower_limits, self.actuator_upper_limits)
#         action = np.array(action).astype(float)
#         action = np.concatenate([action, np.array([0.0])])
#         self.particle_skeleton.setCommands(action)
#         self.world.step()

#     def _is_done(self):
#         if self.current_step >= self.max_time_steps:
#             return True
#         elif self.diff_norm > 1.0:
#             # incase particle flies away
#             return True
#         else:
#             return False

#     def _get_reward(self, action):
#         particle_com = self.particle.getCOM()
#         target_com = self.target.getCOM()
#         diff = (particle_com - target_com).flatten()[:2]

#         reward_distance = -la.norm(diff)
#         reward_control = -la.norm(action)

#         return reward_distance + 0.01 * reward_control
