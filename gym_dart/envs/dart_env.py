# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

import os

import dartpy as dart
import gymnasium as gym
from gymnasium.spaces import Space
from gymnasium import error, logger, spaces


def get_asset_full_path(model_path):
    if model_path.startswith("/"):
        full_path = model_path
    else:
        full_path = os.path.join(os.path.dirname(__file__), "assets", model_path)

    if not os.path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    return full_path


def load_world(full_path):
    if not os.path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    if full_path[-5:] == ".urdf":
        urdf_loader = dart.io.DartLoader()
        world = urdf_loader.parseWorld(full_path)
        return world
    elif full_path[-5:] == ".skel":
        world = dart.io.SkelParser.readWorld(full_path)
        return world
    else:
        raise NotImplementedError


def load_skeleton(full_path):
    if not os.path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    if full_path[-5:] == ".urdf":
        urdf_loader = dart.io.DartLoader()
        world = urdf_loader.parseSkeleton(full_path)
        return world
    elif full_path[-5:] == ".skel":
        world = dart.io.SkelParser.readSkeleton(full_path)
        return world
    else:
        raise NotImplementedError


class DartEnv(gym.Env):
    """Superclass for all DART environments."""

    def __init__(
        self, observation_space: Space, name="Noname", world_path=None, model_paths=[]
    ):
        gym.Env.__init__(self)

        self.name = name
        if world_path is None:
            self.world = dart.simulation.World()
        else:
            world_path = get_asset_full_path(world_path)
            self.world = load_world(world_path)
        assert self.world is not None

        if model_paths:
            for skeleton_path in model_paths:
                skeleton_path = get_asset_full_path(skeleton_path)
                skeleton = load_skeleton(skeleton_path)
                self.world.addSkeleton(skeleton)

        if self.world.getNumSkeletons() < 1:
            raise ValueError("At least one model is needed.")

        # Assume that the skeleton of interest is always the last one
        self.robot_skeleton = self.world.getSkeleton(self.world.getNumSkeletons() - 1)

        # Observation space
        self.observation_space = observation_space

    def visualize(self):
        node = dart.gui.osg.RealTimeWorldNode(self.world)

        # Create world node and add it to viewer
        viewer = dart.gui.osg.Viewer()
        viewer.addWorldNode(node)

        # Create world node and add it to viewer
        viewer = dart.gui.osg.Viewer()
        viewer.addWorldNode(node)

        # Grid settings
        grid = dart.gui.osg.GridVisual()
        grid.setPlaneType(dart.gui.osg.GridVisual.PlaneType.ZX)
        grid.setOffset([0, -0.55, 0])
        viewer.addAttachment(grid)

        viewer.setUpViewInWindow(0, 0, 640, 480)
        viewer.setCameraHomePosition(
            [2.0, 1.0, 2.0], [0.00, 0.00, 0.00], [-0.24, 0.94, -0.25]
        )
        viewer.run()
