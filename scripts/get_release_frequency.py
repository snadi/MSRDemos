# Description:
# This script is adapted from https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/ReleaseFrequency/releasefrequency.py
# Original Authors: Rehab El-Hajj and Fernando Lopez de la Mora
# Adapted by Sarah Nadi
# - Obtains the Release Frequency (in days) of a library based on its Github repository. Additionally, this script the date and name of
# all releases of a library (see class ReleaseData)
#
#Requirements: 
# - You will need to install PyGithub
# - You will need to input your Github credentials to make use of the Github API (ideally, you should use a token so you don't need user input but just taking user input for demo purposes)
#Input:
# - A file with the library repository names (LibraryData.json)
#Output:
# - lists each library and its avg release frequency
#How to run: 
# - Just run the script.

import os
import pickle
from github import Github, Repository, GitTag
import getpass
import json

class ReleaseData:
	def __init__(self, repository):
		self.repository = repository
		self.release_dates = []
		self.release_names = []
		self.release_frequency_average = 0.0

	def addReleaseName(self, name):
		self.release_names.append(name)

	def addReleaseDate(self, date):
		self.release_dates.append(date)

	def calculateReleaseFrequency(self):
		self.release_dates.sort()
		number_of_differences = len(self.release_dates)-1
		total_seconds = 0
		for i in range(1, len(self.release_dates)):
			total_seconds += int((self.release_dates[i] - self.release_dates[i-1]).total_seconds())
		#divide the average by the number of seconds per day
		self.release_frequency_average = float((total_seconds/number_of_differences)/86400)

def printData(data):
	for repo, relFreq in data.items():
		print(relFreq.repository, relFreq.release_frequency_average)

def getReleaseDates(username, password):

	data = {}

	repositories = []
	LibraryData = read_json_file('LibraryData.json')
	for line in LibraryData:
		repositories.append(line['FullRepoName'])

	github = Github(username, password)

	for repository in repositories:
		repo = github.get_repo(repository)
		release_data = ReleaseData(repository)

		#Obtain the date of the git tag
		for tag in repo.get_tags():
			release_data.addReleaseDate(tag.commit.commit.author.date)
			release_data.addReleaseName(tag.name)

		release_data.calculateReleaseFrequency()

		data[repository] = release_data

	printData(data)

def read_json_file(file_path):
    main_array = []
    with open(file_path, 'r') as myfile:
        main_array = json.loads(myfile.read())
    return main_array

def main():
    username = input("Enter your Github username: ")
    password = getpass.getpass("Enter your password: ")
    getReleaseDates(username, password)

if __name__ == "__main__":
	main()