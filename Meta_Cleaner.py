#!/usr/bin/env python
import argparse
import os

class Meta_Cleaner():
	def __init__(self):
		self.raw_reads = []

	def remove_CpG_sites(self,input_fasta):


	def remove_introns(self,input_dir):


def main():
	parser = argparse.ArgumentParser(description='Takes in a fasta/fastq file directory and filters unique characteristics of human DNA.')
	parser.add_argument('--input_fasta', '-i', help='Name of fasta/fastq file containing metagenome to process.')

	parser.add_argument('--output_fasta', '-o', help='If one input file is specified,')
	args = parser.parse_args()
	instance = CpG()

	# Single file specified
	if :
		instance.remove_CpG_sites()

	# Else process all fasta and fastq files in input directory
	else:

if __name__ == "__main__":
	main()
