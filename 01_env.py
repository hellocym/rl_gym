import gymnasium as gym

env_name = 'CartPole-v1'
env = gym.make(env_name, render_mode="human")

done = False
score = 0
state = env.reset()

while not done:
    # env.render()
    action = env.action_space.sample()
    observation, reward, done, _, info = env.step(action)
    score += reward

print('score:', score)