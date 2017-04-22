#   34. SYS

import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
sys.stdout.flush()

def main(args):
    for arg in args:
        print(arg)

if __name__ == '__main__':
    main(sys.argv)

#command in script dir : python s34_sys.py '1st' '2nd' '3rd'
