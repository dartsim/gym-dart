from gym.envs.registration import register

register(
    id='DartReacher-v0',
    entry_point='gym_dart.envs:DartReacherEnv',
)
