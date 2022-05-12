#file: main.py
# author: Senjuti Dutta
# This is the main file that instantiates the SlitherAgent class and calls its start()
#function.
#The class should be instantiated with a mode parameter (i.e., “autonomous” or “suggestion”) and a num_games parameter (e.g., 5).
#Both parameter should be provided as command line arguments (e.g. “‘python main.py autonomous 10” would execute in autonomous mode for 10 games.)

import sys
import agent

input = sys.argv
slither = agent.SlitherAgent(mode = input[1], no_of_games = int(input[2]))
slither.start()
