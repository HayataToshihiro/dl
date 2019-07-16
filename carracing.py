import numpy as np 
import gym

# env = gym.make("Pendulum-v0")
# env = gym.make("CartPole-v0")
env = gym.make("CarRacing-v0")

obs = env.reset()
ob_space = env.observation_space
ac_space = env.action_space
print('obs:',ob_space)
print('act:',ac_space)


done = False
while not done:
    env.render()
    a = np.random.uniform(env.action_space.low,env.action_space.high,env.action_space.shape)
    obs, r, done, info = env.step(a)
    print(a,r)
