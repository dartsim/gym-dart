import dartpy

import numpy as np
import numpy.linalg as la

from gym_dart.envs import DartEnv
import gym.spaces as spaces

from gym_dart.envs.dart_env import get_asset_full_path


class DartWamArmReacherEnv(DartEnv):

    def __init__(self):
        DartEnv.__init__(self, skeleton_paths=['wam/target.skel'])

        self.world.setGravity(np.array([0, 0, -9.8]))
        self.world.setTimeStep(0.01)

        wam_path = get_asset_full_path('wam/wam.urdf')
        urdf_loader = dartpy.utils.DartLoader()
        urdf_loader.addPackageDirectory('herb_description', get_asset_full_path('wam'))
        self.wam_arm = urdf_loader.parseSkeleton(wam_path)
        self.world.addSkeleton(self.wam_arm)

        self.leaf_body = self.wam_arm.getBodyNode('/wam7')
        self.end_effector = self.leaf_body.createEndEffector('ee')

        self.target_skeleton = self.world.getSkeleton('target')
        assert self.target_skeleton is not None
        self.target = self.target_skeleton.getRootBodyNode()
        assert self.target is not None

        self.max_time_steps = 1000
        self.current_step = 0

        # Observations
        wam_arm_dof = self.wam_arm.getNumDofs()
        wam_arm_position_min = self.wam_arm.getPositionLowerLimits()
        wam_arm_position_max = self.wam_arm.getPositionUpperLimits()

        # Goal

        # Action

        self.reset()

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self, mode='human'):
        pass
