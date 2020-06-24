from sys import argv 
from src.currconvert.conversion import convert 

if __name__ == "__main__":
	input_fn = argv[1]
	 try:
	 	output_fn = argv[2]
	 except Exception:
	 	output_fn = "output.txt"

	 with open(input_fn, "r") as fh, open(output_fn, "w") as fw:
	 	for line in fh:
	 		line = line.strip('\n')
	 		val, base, curr = line.split(' ')
	 		val = float(val)
	 		fw.write(f"{convert(val,curr,base)} {curr}\n")