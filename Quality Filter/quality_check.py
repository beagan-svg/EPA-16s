import os 
import sys
import itertools
import glob

class FastAreader :
	def __init__ (self, fname=''):
		self.fname = fname
			
	def doOpen (self):
		if self.fname == '':
			return sys.stdin
		else:
			return open(self.fname)
 
	def readFastq (self):
		header = ''
		sequence = ''
		
		with self.doOpen() as fileH:
			header = ''
			sequence = ''
			quality_score = ''

			line = fileH.readline()
			header = line[1:].rstrip()
			for line in fileH:
				if line.startswith('@'):
					yield header, sequence, quality_score
					header = line[1:].rstrip()
					sequence = ''
					quality_score = ''
				elif line.startswith('+'):
					quality_score = fileH.readline()
				else:
					sequence += ''.join(line.rstrip().split()).upper()
						
		yield header, sequence, quality_score

# Convert ascii score to phred score
def convert_phred(letter):
    phred_score = ord(letter) - 33
    return phred_score
	
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

# If there is a phred score below 30 for any nucleotide return false, otherwise
# the read is good and return true.
def qualityCheck(quality_list):
	bad_call_count = 0
	for letter in quality_list:
		if convert_phred(letter) < 30:
			bad_call_count += 1
	
	if bad_call_count < 10:
		return True
	else:
		return False

def main():
	# Parent Directories
	parent_dir = "/Volumes/DJI FPV"

	# Leaf directory
	directory = "Cohort1"

	# Path
	path = os.path.join(parent_dir, directory)

	# Get the list of all files and directories
	dir_list = glob.glob(path + "/*")

	# Make a new directory containing the filtered r1 an r2
	new_dir_path = parent_dir + '/' + 'Filtered_Cohort'
	
	# If directory exist pass, else create new diretory
	try:
		os.mkdir(new_dir_path)
	except:
		# Clear all files in new directory
		try:
			for f in os.listdir(new_dir_path):
				os.remove(os.path.join(new_dir_path, f))
		except:
			pass

	file_count = 0

	readQualty1 = True
	readQualty2 = True
	for r1, r2 in pairwise(dir_list):
		r1_split_list = r1.split("/")
		filter_r1_path = new_dir_path + '/' + r1_split_list[4]

		r2_split_list = r2.split("/")
		filter_r2_path = new_dir_path + '/' + r2_split_list[4]

		f_r1 = open(filter_r1_path, 'w')
		f_r2 = open(filter_r2_path, 'w')
		
		for read_1_content, read_2_content in itertools.zip_longest(FastAreader(r1).readFastq(), FastAreader(r2).readFastq()):
			readQualty1 = qualityCheck(read_1_content[2])
			readQualty2 = qualityCheck(read_2_content[2])

			if readQualty1 == False and readQualty2 == False:
				continue
			else:
				f_r1.write('@' + read_1_content[0] + '\n')
				f_r1.write(read_1_content[1] + '\n')
				f_r1.write('+' + '\n')
				f_r1.write(read_1_content[2])

				f_r2.write('@' + read_2_content[0] + '\n')
				f_r2.write(read_2_content[1] + '\n')
				f_r2.write('+' + '\n')
				f_r2.write(read_2_content[2])

		f_r1.close() 
		f_r2.close()

		if os.stat(filter_r1_path).st_size == 0:
			os.remove(filter_r1_path)

		if os.stat(filter_r2_path).st_size == 0:
			os.remove(filter_r2_path)

	
if __name__ == "__main__":
	main()



