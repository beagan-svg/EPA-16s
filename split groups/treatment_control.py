import csv
import os
import glob
import sys
import pprint
import shutil

def main():
	# Parent Directories
	parent_dir = "/Volumes/DJI_FPV"

	# Leaf 
	directory = "Meep"

	# Path
	path = os.path.join(parent_dir, directory)

	# Get the list of all files and directories
	dir_list = glob.glob(path + "/*")

	# Make a new directory for every treatment group
	treatment_dir_path = parent_dir + '/' + 'Meep_Treatment_Seperate_Cohort'
	print(treatment_dir_path)

	control_t1_path = treatment_dir_path + '/' + 'control_t1'
	control_t2_path = treatment_dir_path + '/' + 'control_t2'
	control_t3_path = treatment_dir_path + '/' + 'control_t3'

	treatment_t0_path = treatment_dir_path + '/' + 'treatment_t0'
	treatment_t1_path = treatment_dir_path + '/' + 'treatment_t1'
	treatment_t2_path = treatment_dir_path + '/' + 'treatment_t2'

	try:
		os.mkdir(control_t1_path)
		os.mkdir(control_t2_path)
		os.mkdir(control_t3_path)

		os.mkdir(treatment_t0_path)
		os.mkdir(treatment_t1_path)
		os.mkdir(treatment_t2_path)
	except:
		pass

	# Read metadata
	f = open('metadata_EPA_all_16S.csv')
	csv_reader = csv.DictReader(f)

	control_t1 = list()
	control_t2 = list()
	control_t3 = list()

	treatment_t0 = list()
	treatment_t1 = list()
	treatment_t2 = list()

	for dict_row in csv_reader:
		if dict_row["Treatment"] == "C" and dict_row["Time"] == "T1":
			control_t1.append(dict_row["ID#"])
		if dict_row["Treatment"] == "C" and dict_row["Time"] == "T2":
			control_t2.append(dict_row["ID#"])
		if dict_row["Treatment"] == "C" and dict_row["Time"] == "T3":
			control_t3.append(dict_row["ID#"])

		if dict_row["Treatment"] == "T" and dict_row["Time"] == "T0":
			treatment_t0.append(dict_row["ID#"])
		if dict_row["Treatment"] == "T" and dict_row["Time"] == "T1":
			treatment_t1.append(dict_row["ID#"])
		if dict_row["Treatment"] == "T" and dict_row["Time"] == "T2":
			treatment_t2.append(dict_row["ID#"])

	count = 0
	for file in dir_list[:-1]:
		print(file)
		split_files = file.split("-")
		sample_id = split_files[1]
		print(sample_id)
		
		if sample_id in treatment_t0:
			split_files = file.split("/")
			shutil.copyfile(file, treatment_t0_path + "/" + split_files[4])

		elif sample_id in treatment_t1:
			print("11111")
			split_files = file.split("/")
			shutil.copyfile(file, treatment_t1_path + "/" + split_files[4])

		elif sample_id in treatment_t2:
			print("22222")
			split_files = file.split("/")
			shutil.copyfile(file, treatment_t2_path + "/" + split_files[4])

		elif sample_id in control_t1:
			split_files = file.split("/")
			shutil.copyfile(file, control_t1_path + "/" + split_files[4])

		elif sample_id in control_t2:
			split_files = file.split("/")
			shutil.copyfile(file, control_t2_path + "/" + split_files[4])

		elif sample_id in control_t3:
			split_files = file.split("/")
			shutil.copyfile(file, control_t3_path + "/" + split_files[4])


if __name__ == "__main__":
	main()

'''
	temp = dict()
	count = 0
	for list_row in csv_reader:
		index = 0
		if count == 0:
			for value in list_row:
				temp[value] = []
		else:
			for key in temp:
				temp[key].append(list_row[key])
				index += 0
		count += 1
	pprint.pprint(temp)
	'''



