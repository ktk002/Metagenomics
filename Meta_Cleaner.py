#!/usr/bin/env python
import argparse
import os
from collections import OrderedDict

class Meta_Cleaner():
	def __init__(self):
		self.raw_reads = OrderedDict() # {header: read sequence}
		self.file_type = None

	# Default option to remove CpG islands from reads
	def remove_CpG_sites_window(self,input_file):
		# Add all headers and sequences to raw_reads
		if self.file_type == ".fastq":
			pass
		# fasta file
		else:
			pass
	def remove_CpG_sites_HMM(self,input_file):
		pass

	def remove_introns(self,input_file):
		pass

def main():
	parser = argparse.ArgumentParser(description='Takes in a fasta/fastq file directory and filters unique characteristics of human DNA.')
	parser.add_argument('-i', '--input_file', help='Name of fasta/fastq file containing metagenome to process.')

	parser.add_argument('-o', '--output_file', help='If one input file is specified, ouput one fasta/fastq file.')
	args = parser.parse_args()
	instance = Meta_Cleaner()

	# Set file type
	filename, file_extension = os.path.splitext(args.input_file)
	fasta_extensions = [".fasta",".fas",".fa",".seq",".fsa",".fna"]
	#self.file_type = "fasta" if file_extension in fasta_extensions else self.file_type = "fastq"
	if file_extension in fasta_extensions:
		instance.file_type = file_extension
	elif file_extension == ".fastq":
		instance.file_type = file_extension
	else:
		raise AssertionError("Invalid file type. Please use either fasta or fastq.")
	

	# Single input file specified, update read dictionary
	instance.remove_CpG_sites_window(args.input_file)

	# Else process all fasta and fastq files in input directory

	# Write raw_reads file
	with open(args.output_file,"wb") as file_handler_out:
		for key,value in instance.raw_reads:
			file_handler_out.write(key)
			file_handler_out.write(value)

		
if __name__ == "__main__":
	main()
