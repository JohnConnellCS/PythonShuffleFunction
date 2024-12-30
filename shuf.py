#!/usr/local/cs/bin/python3
import random, sys, argparse

parser = argparse.ArgumentParser("shuf.py","Outputs lines of input in a random order.")
group = parser.add_mutually_exclusive_group(required=False)

group.add_argument("filename", nargs='?')
group.add_argument("-i", "--input-ranges", type=str)
group.add_argument("-e", "--echo", type=str, nargs='*')

parser.add_argument("-r", "--repeat", action="store_true", help='Outputted lines can repeat. Loops infinitely unless -n is specified')
parser.add_argument("-n", "--head-count", type=int, help='Specifies the number of lines of output')



class Shufflable:
    def __init__(self, filepath, repeatability, maxReps, lowVal, hiVal, echoVal, stdInputList):
        if(filepath != None):
            f = open(filepath, 'r')
            self.lineList = f.readlines()
            f.close()
        if(lowVal != None and hiVal != None):
            self.lineList = [str(num) + '\n' for num in range(lowVal, hiVal+1)]
        if(echoVal != None):
            self.lineList = echoVal
            for i in range(len(self.lineList)):
                self.lineList[i] = self.lineList[i] +  "\n"
        if(stdInputList != None):
            self.lineList = stdInputList
        self.isRepeated = repeatability
        self.repCount = maxReps
    def chooseline(self):
        return random.choice(self.lineList)
    def outputshuf(self):
        if(self.isRepeated == True):
            i = 0
            while(i != self.repCount):
                sys.stdout.write(self.chooseline())
                i += 1
        else:
            j = 0
            k = len(self.lineList)
            if(self.repCount != None and self.repCount < len(self.lineList)):
                k = self.repCount
            shufList = random.sample(self.lineList, len(self.lineList))
            for l in range(k):
                sys.stdout.write(shufList[l])
            
        
def main():
    args = parser.parse_args()
    if(args.filename != None and args.filename != '-'):
        generator = Shufflable(args.filename, args.repeat, args.head_count, None, None, None, None)
    elif(args.echo != None):
        generator = Shufflable(None, args.repeat, args.head_count, None, None, args.echo, None)
    elif(args.input_ranges != None):
        vals = args.input_ranges.split("-",1)
        lo = int(vals[0])
        high = int(vals[1])
        generator = Shufflable(None, args.repeat, args.head_count, lo, high, None, None)
    else:
        passedInput = sys.stdin.readlines()
        generator = Shufflable(None, args.repeat, args.head_count, None, None, None, passedInput)
    generator.outputshuf()

if __name__ == "__main__":
    main()
