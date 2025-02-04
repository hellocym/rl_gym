import gymnasium as gym

env_name = 'CartPole-v1'
env = gym.make(env_name, render_mode="rgb_array")

score = 0

while score < 90:
    done = False
    score = 0
    state = env.reset()
    frames = []
    while not done:
        frames.append(env.render())
        action = env.action_space.sample()
        observation, reward, done, _, info = env.step(action)
        score += reward

    print('score:', score)
    # print('frames:', frames)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams


def display_frames_as_gif(frames):
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi = 72)
    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    anim.save('movie_cartpole.gif', writer='imagemagick', fps=60)

display_frames_as_gif(frames)