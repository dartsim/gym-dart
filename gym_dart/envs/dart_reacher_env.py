# import numpy as np
# import numpy.linalg as la

# from gym_dart.envs import DartEnv
# import gymnasium as gym.spaces as spaces

# class DartReacherEnv(DartEnv):

#     def __init__(self):
#         DartEnv.__init__(self, world_path='reacher.skel')

#         self.world.setGravity(np.array([0, 0, -9.8]))
#         self.world.setTimeStep(0.01)

#         self.reacher = self.world.getSkeleton('reacher')
#         assert self.reacher is not None
#         self.finger_tip = self.reacher.getBodyNode('fingertip')

#         self.target_skeleton = self.world.getSkeleton('target')
#         assert self.target_skeleton is not None
#         self.target = self.target_skeleton.getRootBodyNode()
#         assert self.target is not None

#         self.max_time_steps = 1000
#         self.current_step = 0

#         # Observations
#         self.obs_dim = 10
#         self.obs_max = np.array([
#             1.0, 1.0,  # cos(joint_angles_of_reacher)
#             1.0, 1.0,  # sin(joint_angles_of_reacher)
#             0.2, 0.2,  # XY_position_of_target
#             5, 5,      # joint_velocities_of_reacher
#             0.4, 0.4,  # com_of_fingertip - com_of_target
#         ])
#         self.obs_min = -self.obs_max
#         self.initial_reacher_pos_lower_limits = np.ones(2) * -0.1
#         self.initial_reacher_pos_upper_limits = np.ones(2) * 0.1
#         # self.initial_target_pos_lower_limits = np.ones(2) * -0.2
#         self.initial_target_pos_lower_limits = np.array([-0.2, -0.001])
#         # self.initial_target_pos_upper_limits = np.ones(2) * 0.2
#         self.initial_target_pos_upper_limits = np.array([-0.199, 0.])
#         self.observation_space = spaces.Box(low=self.obs_min, high=self.obs_max)

#         # Goal
#         self.goal_dim = 2
#         self.goal_max = np.ones(self.goal_dim) * 0.2
#         self.goal_min = -self.goal_max
#         self.goal = np.zeros(self.goal_dim)

#         # Action
#         self.action_dim = 2
#         self.actuator_upper_limits = np.ones(self.action_dim) * 1000.
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

#         reacher_pos \
#             = np.random.uniform(self.initial_reacher_pos_lower_limits, self.initial_reacher_pos_upper_limits)
#         self.reacher.setPositions(reacher_pos)
#         self.reacher.resetVelocities()
#         self.reacher.resetAccelerations()

#         target_pos \
#             = np.random.uniform(self.initial_target_pos_lower_limits, self.initial_target_pos_upper_limits)
#         while True:
#             target_pos \
#                 = np.random.uniform(self.initial_target_pos_lower_limits, self.initial_target_pos_upper_limits)
#             if la.norm(target_pos)<0.2 and la.norm(target_pos)>0.01:
#                 break
#         self.target_skeleton.setPosition(0, target_pos[0])
#         self.target_skeleton.setPosition(1, target_pos[1])

#         return self._get_obs()

#     def render(self, mode='human'):
#         pass

#     def _get_obs(self):
#         # References: https://github.com/openai/gym/blob/v0.10.5/gym/envs/mujoco/reacher.py#L35-L43
#         reacher_pos = self.reacher.getPositions()
#         reacher_vel = self.reacher.getVelocities()
#         target_pose = self.target.getTransform()
#         target_xy = target_pose.translation()[:2]
#         target_com = self.target.getCOM()
#         finger_tip_com = self.finger_tip.getCOM()

#         return np.concatenate([
#             np.cos(reacher_pos).flatten(),
#             np.sin(reacher_pos).flatten(),
#             target_xy.flatten(),
#             reacher_vel.flatten(),
#             (finger_tip_com - target_com).flatten()[:2]
#         ])

#     def _step_world(self, action):
#         if self._is_done():
#             return 0
#         action = np.array(action).astype(float)
#         self.reacher.setCommands(action)
#         self.world.step()

#     def _is_done(self):
#         return self.current_step >= self.max_time_steps

#     def _get_reward(self, action):
#         fingertip_com = self.finger_tip.getCOM()
#         target_com = self.target.getCOM()
#         diff = (fingertip_com - target_com).flatten()[:2]

#         reward_distance = -la.norm(diff)
#         reward_control = -la.norm(action)

#         return reward_distance + 0.00001*reward_control
