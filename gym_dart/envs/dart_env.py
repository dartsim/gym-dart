from os import path

import dartpy as dart
import gym
from OpenGL.GLUT import *
from dartpy.gui import SimWindow


def get_asset_full_path(model_path):
    if model_path.startswith("/"):
        full_path = model_path
    else:
        full_path = os.path.join(os.path.dirname(__file__), "assets", model_path)

    if not path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    return full_path


def load_world(full_path):
    if not path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    if full_path[-5:] == '.urdf':
        urdf_loader = dart.utils.DartLoader()
        world = urdf_loader.parseWorld(full_path)
        return world
    elif full_path[-5:] == '.skel':
        world = dart.utils.skel.readWorld(full_path)
        return world
    else:
        raise NotImplementedError


def load_skeleton(full_path):
    if not path.exists(full_path):
        raise IOError("File %s does not exist" % full_path)

    if full_path[-5:] == '.urdf':
        urdf_loader = dart.utils.DartLoader()
        world = urdf_loader.parseSkeleton(full_path)
        return world
    elif full_path[-5:] == '.skel':
        world = dart.utils.skel.readSkeleton(full_path)
        return world
    else:
        raise NotImplementedError


class DartEnv(gym.Env):
    """Superclass for all DART environments.
    """

    def __init__(self, name='Noname', world_path=None, skeleton_paths=[]):
        gym.Env.__init__(self)

        self.name = name
        if world_path is None:
            self.world = dart.simulation.World.create()
        else:
            world_path = get_asset_full_path(world_path)
            self.world = load_world(world_path)
        assert self.world is not None

        if skeleton_paths:
            for skeleton_path in skeleton_paths:
                skeleton_path = get_asset_full_path(skeleton_path)
                skeleton = load_skeleton(skeleton_path)
                if skeleton is None:
                    raise ValueError("Failed to load skeleton from file '{}'".format(skeleton_path))
                self.world.addSkeleton(skeleton)

    def visualize(self):
        window = SimWindow()
        window.setWorld(self.world)

        glutInit(sys.argv)
        window.initWindow(640, 480, self.name)
        glutMainLoop()
