from accountlinks_generator import main
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", help="path to config file - MUST BE .yaml FILE", required=True)
parser.add_argument("--output", help="desired output path - MUST be .md FILE", required=True)
parser.add_argument(
    "--intro", help="path to introductory text (optional)", required=False
)
parser.add_argument("--outro", help="path to outro text (optional)", required=False)

args = parser.parse_args()

config = str(args.config)
output = str(args.output)
intro = str(args.intro)
outro = str(args.outro)

if __name__ == "__main__":
    main(config, output, intro, outro)
