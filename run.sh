#!/bin/bash

file_dir="/Volumes/DJI_FPV/Cohort1"
r1=''
r2=''
file2_dir="/Volumes/DJI_FPV/Meep"
count=0
for file in "$file_dir"/*.fastq
	do
		if [[ $count -eq 2 ]]; then
			echo "Round"
			echo $r1
			echo $r2
			IFS='/'
			read -ra ADDR <<< "$file"
			echo ${ADDR[4]}
			IFS=''
			output_dir="$file2_dir"/"${ADDR[4]}"
			echo $output_dir
			command="-i $r1 -o $output_dir -m 1.5"
			echo "./meeptools $command"
			count=$(echo "scale=2; 0" | bc)
		fi

		if [[ "$file" == *"R1"* ]]; then
			r1=$file
		elif [[ "$file" == *'R2'* ]]; then
			r2=$file
		fi
		count=$(echo "scale=2; $count + 1" | bc)
done