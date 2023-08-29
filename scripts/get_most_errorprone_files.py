from github import Github, Repository
import argparse

# this is a simplistic script that looks only at the commits mentioned in the issues
# and counts the number of times each file was changed in the commits
# it is missing out on changes in PRs linked to these issues

def is_bug(issue):
    bug_keywords = ['bug', 'defect', 'error', 'problem']
    title = issue.title.lower() if issue.title else ''
    body = issue.body.lower() if issue.body else ''

    all_content = title + body

    if any(keyword in all_content.lower() for keyword in bug_keywords) :
        return True
    
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True, help="File containing your Github token")
    parser.add_argument("--repo", required=True, help="username/reponame of the repository")
    args = parser.parse_args()

    token = open(args.token, "r").read()
    github = Github(token)

    repo = github.get_repo(args.repo)

    bug_fixing_commits = set()
    issues = repo.get_issues(state="closed")

    for issue in issues:
        if not is_bug(issue):
           continue
        for event in issue.get_events():
            if event.event == 'referenced':
                bug_fixing_commits.add(event.commit_id)
    

    bug_fixing_files = {}
    for commit in bug_fixing_commits:
        try:
            commit = repo.get_commit(commit)
            for file in commit.files:
                if file.filename not in bug_fixing_files:
                    bug_fixing_files[file.filename] = 0
                bug_fixing_files[file.filename] += 1
        except:
            #print("Commit not found: " + commit)
            continue

    bug_fixing_files = sorted(bug_fixing_files.items(), key=lambda x: x[1], reverse=True)

    for file in bug_fixing_files:
        print(f"{file[0]}: {file[1]} bug fixes")

if __name__ == "__main__":
    main()





