# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

from gymnasium.envs.registration import (
    register,
)

register(
    id="DartCartPole-v0",
    entry_point="gym_dart.envs:DartCartPoleEnv",
    # vector_entry_point="gym_dart.envs:DartCartPoleVectorEnv",
    max_episode_steps=200,
    reward_threshold=195.0,
)

# register(
#     id='DartParticle-v0',
#     entry_point='gym_dart.envs:DartParticleEnv',
# )

# register(
#     id='DartReacher-v0',
#     entry_point='gym_dart.envs:DartReacherEnv',
# )
