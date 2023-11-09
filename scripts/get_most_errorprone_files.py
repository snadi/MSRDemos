from github import Github, Repository, RateLimitExceededException, UnknownObjectException, GithubException
import argparse
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

# this is a simplistic script that looks only at the commits mentioned in the issues
# and counts the number of times each file was changed in the commits
# it is missing out on changes in PRs linked to these issues

def is_bug(issue):
    bug_keywords = ['bug', 'defect', 'error', 'problem']
    title = issue.title.lower() if issue.title else ''


    for label in issue.get_labels():
        if label.name.lower() == "bug":
            return True

    if any(keyword in title.lower() for keyword in bug_keywords) :
        return True
    
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True, help="File containing your Github token")
    parser.add_argument("--repo", required=True, help="username/reponame of the repository")
    parser.add_argument('--lastyearonly', help='only analyze commits from the last year', default=False, action='store_true')
    args = parser.parse_args()
        
    token = open(args.token, "r").read()
    github = Github(token)

    repo = github.get_repo(args.repo)

    bug_fixing_commits = set()
    issue_count = 0
    bug_fixing_files = {}
    
    try:
        issues = repo.get_issues(state="closed", sort="created", direction="desc")

        if args.lastyearonly:
            date_limit = datetime.now() - relativedelta(year=1)

        for issue in issues:
            if date_limit:
                if issue.created_at < date_limit:
                    break
            issue_count += 1
            print(f"Processing issue {issue_count}, with ID {issue.number}")
            if not is_bug(issue):
                continue
            print(f"Found bug issue {issue.id}")
            for event in issue.get_events():
                if event.event == 'referenced':
                    bug_fixing_commits.add(event.commit_id)
    except RateLimitExceededException as error:
        # we will sleep to be able to use API again, but will just skip remaining issues
        print(f"Rate limit exceeded. Managed to process {issue_count} issues")
        print(f"Exact exception: ", error)

        print("Sleeping for an hour...")
        time.sleep(3600) # sleep for an hour to avoid rate limit before processing commits

    print(f"Processed {issue_count} issues..")
    commits_processed = 0

    try:
        for commit_id in bug_fixing_commits:
            try:
                commit = repo.get_commit(commit_id)
                commits_processed += 1
                for changed_file in commit.files:
                    if 'doc' in changed_file.filename : # skip doc changes
                        continue
                    if changed_file.filename not in bug_fixing_files:
                        bug_fixing_files[changed_file.filename] = 0
                    bug_fixing_files[changed_file.filename] += 1
            except RateLimitExceededException as error:
                print(f"Rate limit exceeded. Managed to process {commits_processed} commits from {len(bug_fixing_commits)} commits")
                print(f"Exact exception: ", error)
                break
            except (UnknownObjectException, GithubException) as error:
                print(f"Commit {commit_id} not found. Skipping...")
                continue
            
    except RateLimitExceededException as error:
        print(f"Rate limit exceeded. Managed to process {commits_processed} commits from {len(bug_fixing_commits)} commits")
        print(f"Exact exception: ", error)

    bug_fixing_files = sorted(bug_fixing_files.items(), key=lambda x: x[1], reverse=True)

    for changed_file in bug_fixing_files:
        print(f"{changed_file[0]}: {changed_file[1]} bug fixes")

if __name__ == "__main__":
    main()





