



def load_dataset():
	"""
	Load the data in dataset.csv file into a dataframe
	"""
	
	## importation
	import pandas as pd

	## parameters
	input_data_file = "dataset.csv"

	## load dataset
	df = pd.read_csv(input_data_file, sep="\t")

	## return the dataframe
	return df



stuff = load_dataset()
print(stuff)
