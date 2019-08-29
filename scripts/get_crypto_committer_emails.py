'''
Author: Sarah Nadi
Adapted from scripts used in ICSE '16 paper http://www.st.informatik.tu-darmstadt.de/artifacts/crypto-api-misuse/
Changed to use different python wrapper lib
This assumes you already have the list of repos to search in. If you don't, you need a different step first to get the list of repos
IMPORTANT: spamming developers with survey emails is highly discouraged. If you do need to contact developers for your work, think about whether this is the only way for you to get
this information. Also, if this is your only reasonable option, come up with extremely specific criteria that increase the chance of that developer being interested
in your work. With the ease of having email addresses available and easy to obtain, tons of researchers all over the world end up emailing these developers and they
really get frustrated. See https://speakerdeck.com/gousiosg/the-number-issue32-incident to see what kind of problems you may run to if you are not careful. 
Also, see https://empirical-software.engineering/assets/pdf/esem16-sampling.pdf about different ethical considerations and sampling strategies
Finally, involving any humans in your research requires (At least in Canada) ethics approval.
'''

import json
from github import Github, Repository
import getpass
import csv
import argparse

class CodeSearch:

	def __init__(self, repo_file, output_file, username):
		self.github = Github(username, getpass.getpass("Enter your password:"))
		self.base_query = '"javax.crypto" language:java'
		self.repositories = []
		self.writer = None
		self.repo_file = repo_file
		self.output_file = output_file
		self.hundred_repos = set()

	def read_repositories(self):
		'''
		Read list of repositories whose code will be queried
		'''
		repositories = set()
		with open(self.repo_file, 'r') as input_file:
			for repo_name in input_file:
				repositories.add(repo_name.rstrip('\n'))
			input_file.close()

		self.repositories = list(repositories)

	def get_committers(self, code_results):
		'''
		Given the results of the code search, find committers of the files
		in the search results and write them out
		'''
		users = set()
		result_repos = set()
		for code_result in code_results:
			repository = code_result.repository
			file_path = code_result.path
			result_repos.add(repository.full_name)

			#fixing until date here for reproducibility
			commits = repository.get_commits(path=file_path, until=datetime.date(2019, 8, 29))
			for commit in commits:
				if commit.committer is not None:
					users.add((commit.commit.committer.name,commit.commit.committer.email))

		print ('repos from results', len(result_repos))
		print ('found ' , len(users))
		self.write_committers(users)

	def write_committers(self, users):
		'''
		Writes the list of committers to the output file
		'''
		users_file = open(self.output_file, 'w')
		for user in users:
			users_file.write(user[0].__str__() + "," + user[1].__str__() + "\n")

		users_file.close()

	def search_code_in_repos(self):
		'''
		Appends a list of given repos to the base_query
		and uses the Github search API to search those repos 
		'''
		query = self.base_query

		for repo in self.repositories:
			query += " repo:" + repo

		return self.github.search_code(query)

	def get_repositories(self):
		'''
		returns the available list of repos
		'''
		return self.repositories

	def get_github_obj(self):
		'''
		returns the github3 wrapper object
		'''
		return self.github

def run(repoFile, outputFile, username):
	code_search = CodeSearch(repoFile, outputFile, username)
	code_search.read_repositories()

	num_of_repos =  len(code_search.get_repositories())
	print ('num of repos',num_of_repos)
	code_results = code_search.search_code_in_repos()
	code_search.get_committers(code_results)


parser = argparse.ArgumentParser(description='Process repositories in repoFile and output matching code files in codeFile')
parser.add_argument('--repoFile', help='name of file containing repository list', required=True)
parser.add_argument('--outputFile', help='name of output file', required=True)
parser.add_argument('--username', help='github username', required=True)

args = parser.parse_args()
print ('repofile', args.repoFile)
print ('outputfile', args.outputFile)
run(args.repoFile, args.outputFile, args.username)
