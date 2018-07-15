#!/usr/bin/env python3
# Author: Kaushal Thaker

import sys

# represent each roll as number of pins knocked down to make processing easier
def convert(arr):
	roll_vals = []
	for i in range(len(arr)):
		if (arr[i] == "X"):
			roll_vals.append(10)
		elif (arr[i] == "-"):
			roll_vals.append(0)
		elif (arr[i] == "/"):
			roll_vals.append(10 - roll_vals[i-1])
		else:
			roll_vals.append(int(arr[i]))
	return roll_vals


def score(rolls, i, frame):
	# rolls after the 10th frame have already been counted in the score for the 10th frame
	if (frame > 10):
		return 0
	# strike
	if (rolls[i] == 10):
		frame_score = 10 + rolls[i+1] + rolls[i+2]
		return frame_score + score(rolls, i+1, frame+1)
	# spare
	elif (rolls[i] + rolls[i+1] == 10):
		frame_score = 10 + rolls[i+2]
		return frame_score + score(rolls, i+2, frame+1)
	# nothing
	else:
		frame_score = rolls[i] + rolls[i+1]
		return frame_score + score(rolls, i+2, frame+1)

def main():
	# Scores a game of American Ten Pin Bowling
	game = sys.argv[1]
	rolls = convert(game)
	total_score = score(rolls, 0, 1)
	print("Score: " + str(total_score))


if __name__ == "__main__":
    main()