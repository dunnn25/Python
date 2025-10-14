import argparse

# create parser
parser = argparse.ArgumentParser()
# positional arguments
# pass args
parser.add_argument("--x",type=int, required=True)
parser.add_argument("--y",type=int, default=100)

# get info
args = parser.parse_args()

print("x = ",args.x)
print("y = ",args.y)
print("sum = ",args.x + args.y)