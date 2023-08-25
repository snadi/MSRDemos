import os
import time
from datetime import datetime, timedelta
from git import Repo
import re

class CommitAnalyzer():

	"""
	Takes path of the repo
	"""
	def __init__(self, repo_path):
		self.repo_path = repo_path
		self.repo = Repo(self.repo_path)
		assert not self.repo.bare

	def get_conflict_commits(self):
		conflict_commits = []
		current_date = datetime.now()
		for commit in self.repo.iter_commits('main'):
			parents = commit.parents
			if len(parents) > 1 and "conflict" in commit.message.lower() and ".java" in commit.message.lower():
				#uncomment if you want to get only recent merge conflicts (e.g., in the last 5 days)
				#if datetime.fromtimestamp(commit.committed_date) >= current_date - timedelta(5):
				conflict_commits.append(commit)

		return conflict_commits

	def get_conflict_files(self, commits):
		# we are going to rely on the commit message to find the conflicting files
		# this assumes that the developer did not change git's default behavior of listing the conflicting files in the message
		# a more precise way to do this would be to "replay" the merge and check for conflicts
		conflicting_file_count = {}
		for commit in commits:
			# get the conflicting files from the commit message which is in the format:
			# Conflicts:
			#  foo/bar/baz.java
			#  foo/bar/baz.java
			commit_lines = commit.message.splitlines()
			
			for line in commit_lines:
				if re.match(r".*\/+.*\.java", line):
					conflict_file = line.strip("#").strip()
					if conflict_file not in conflicting_file_count.keys():
						conflicting_file_count[conflict_file] = 1
					else:
						conflicting_file_count[conflict_file] += 1

		return conflicting_file_count

#run script in cloned repo
commit_analyzer = CommitAnalyzer(os.getcwd())
merge_conflicts = commit_analyzer.get_conflict_commits()
for commit in merge_conflicts[:5]:
	print (commit, time.asctime(time.gmtime(commit.committed_date)))

# conflicting_files = commit_analyzer.get_conflict_files(commit_analyzer.get_conflict_commits())

# sorted_conflicting_files = sorted(conflicting_files.items(), key=lambda x: x[1], reverse=True)

# print(f"This repo had {len(merge_conflicts)} merge conflicts; The top 5 files with the most merge conflicts are:")

# for file in sorted_conflicting_files[:5]:
# 	print (f"{file[0]} appears in {file[1]} conflicts")