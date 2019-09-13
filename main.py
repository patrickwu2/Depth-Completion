import argparse

import depth_completion.agent as agent
from depth_completion import config

if __name__ == "__main__":
    # agent = agent.GCSC(config.GCSC) -> w/o unet model example
    agent = agent.BCU(config.BCU)   # -> w/  unet model example
    agent.run()

