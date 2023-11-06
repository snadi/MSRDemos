from pydriller import Repository
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--path', help='path to the repository')
args = parser.parse_args()

modified_functions = {}

commits = Repository(args.path, only_in_branch='main',only_modifications_with_file_types=['.py']).traverse_commits()
for commit in commits:
    for modified_file in commit.modified_files:
        changed_methods = modified_file.changed_methods
        for changed_method in changed_methods:
            method_path = f"{modified_file.new_path}#{changed_method.name}"
            if method_path not in modified_functions.keys():
                modified_functions[method_path] = 1
            else:
                modified_functions[method_path] += 1        

sorted_modified_functions = sorted(modified_functions.items(), key=lambda x: x[1], reverse=True)
print (sorted_modified_functions[:10])