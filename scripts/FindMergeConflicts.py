import os
import time
from datetime import datetime, timedelta
from git import Repo

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
		for commit in self.repo.iter_commits('master'):
			parents = commit.parents
			if len(parents) > 1 and "conflict" in commit.message.lower() and ".java" in commit.message.lower():
				#uncomment if you want to get only recent merge conflicts (e.g., in the last 5 days)
				#if datetime.fromtimestamp(commit.committed_date) >= current_date - timedelta(5):
				conflict_commits.append(commit)

		return conflict_commits

#run script in cloned repo
commit_analyzer = CommitAnalyzer(os.getcwd())
for commit in commit_analyzer.get_conflict_commits():
	print (commit, time.asctime(time.gmtime(commit.committed_date)))