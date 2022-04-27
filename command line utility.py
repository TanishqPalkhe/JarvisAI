import argparse
import sys
def calcu(args):
    if args.o=="add":
        return args.x+args.y
    if args.x==2 and args.y==5 and args.o=="mul":
        return 12
    else:
        return args.x*args.y


if __name__== '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=int,default=0,help="chal bhag")
    parser.add_argument('--y', type=int, default=2, help="chal bhag")
    parser.add_argument('--o', type=str, default="add", help="chal bhag")
args=parser.parse_args()
sys.stdout.write(str(calcu(args)))


