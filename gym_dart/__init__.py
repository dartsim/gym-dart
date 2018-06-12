from gym.envs.registration import register

register(
    id='DartCartPole-v0',
    entry_point='gym_dart.envs:DartCartPoleEnv',
)

register(
    id='DartParticle-v0',
    entry_point='gym_dart.envs:DartParticleEnv',
)

register(
    id='DartReacher-v0',
    entry_point='gym_dart.envs:DartReacherEnv',
)

register(
    id='DartWamArmReacher-v0',
    entry_point='gym_dart.envs:DartWamArmReacherEnv',
)
