# About

This repo contains a bunch of demos related to mining various kinds of information from different data sources (e.g., git repos, GitHub repos, Stack Overflow). These are simple use cases just to demonstrate available options and how to get started.

The demos are prepared by [Sarah Nadi](https://sarahnadi.org) and are mainly used in CMPUT 663 at the University of Alberta.

# Running the Demos

The repo comes with a Dockerfile that takes care of using the correct version of python and setting up dependencies. 

First, clone this repo recursively to also clone the submodule:

```
git clone git@github.com:snadi/MSRDemos.git --recurse-submodules
```

To build the Docker image (this will take a bit of time):

```
docker build --tag=msrdemo:f21 .
```

To run the docker image:

```
docker run --name MSRDemo -it --rm msrdemo:f21 /bin/sh
```

All instructions below are based on running from within the Docker image.

# Mining git Repositories

## Creating your own scripts for mining git

git provides many commands for exploring the history. You can simply write custom scripts that execute these commands and parse the output.

* For example, go to the `elasticsearch` repo in `repos/` and explore the history using the following `git log` commands:

```
git log -10 -p --format=fuller --no-merges
git log -10 -p --format=fuller --no-merges -- '*.gradle'
git log -10 -p --format=fuller --no-merges -- '*.java'
```

The first one lists the last 10 commits that are not merge commits. The second one lists the last 10 commits that have modified gradle files, while the last one lists the last 10 commits that have modified java files. You can see a structure for how each commit is displayed and you can process that text yourself.

You probably never have to go that route unless you have something very specific to do that current git processing libraries can't support.


## Using GitPython

* See [http://gitpython.readthedocs.io/en/stable/index.html](http://gitpython.readthedocs.io/en/stable/index.html) for complete documentation
* Check out this [sample simple script](https://github.com/snadi/MSRDemos/blob/master/scripts/FindMergeConflicts.py) for finding merge conflicts in a repo's history. The criteria here is finding commits with two parents with the word "conflict" in their commit message. Note that this is a simplified crtieria and might miss cases with edited commit messages. The script prints the 5 most recent merge conflicts.

* Running this:

```
/msrdemo# cd repos/elasticsearch/
/msrdemo/repos/elasticsearch# python ../../scripts/FindMergeConflicts.py 
```

You should see this output:

```
09056ed3229ccf42ec006eae65b5941c75452ec4 Thu May 27 06:16:19 2021
4528e780c48ada91fd452b9c51dc1a37772c5f07 Wed May 12 12:50:26 2021
3245e78b780c2b7ee00a2a031582824a79c2ea0a Sat May 19 11:38:17 2018
a5be4149a3ca867f8bb239a8e2a62751b904a392 Thu May 10 17:04:08 2018
db14717098e9e50751654f0f45a0c5cc5441a346 Fri May  4 13:40:57 2018
```

Take any commit SHA and check it out on GitHub to verify that it is a merge conflict. e.g., [https://github.com/elastic/elasticsearch/commit/09056ed3229ccf42ec006eae65b5941c75452ec4](https://github.com/elastic/elasticsearch/commit/09056ed3229ccf42ec006eae65b5941c75452ec4)

If we want a bit more insights like "Which files are typically involved in the conflicts", then uncomment out the bottom part of the script and re-run. You should see this as the output:

```
This repo had 127 merge conflicts; The top 5 files with the most merge conflicts are:
core/src/main/java/org/elasticsearch/common/io/stream/StreamInput.java appears in 6 conflicts
core/src/test/java/org/elasticsearch/index/query/SimpleIndexQueryParserTests.java appears in 6 conflicts
core/src/main/java/org/elasticsearch/common/io/stream/StreamOutput.java appears in 4 conflicts
core/src/main/java/org/elasticsearch/index/query/QueryParseContext.java appears in 4 conflicts
core/src/main/java/org/elasticsearch/index/query/HasChildQueryParser.java appears in 4 conflicts
```

## Using PyDriller to Mine git Repos

* Use case: finding the most frequently modified funciton in the repo's commits
* Check [https://github.com/snadi/MSRDemos/blob/master/scripts/get_most_freq_chgd_method.py]https://github.com/snadi/MSRDemos/blob/master/scripts/get_most_freq_chgd_method.py)
* To run:

```
/msrdemo# python scripts/get_most_freq_chgd_method.py --path=repos/pydriller/
```

It will display tuples containing the methods (including the file path) and their frequency in commits (shows 10 most modified functions)

# Mining GitHub

## Using Python Github APIs

* Example of a simple script thaat retrieves emails of developers who committed to java files using the `javax.crypto.*` APIs: [https://github.com/snadi/MSRDemos/blob/master/scripts/get_crypto_committer_emails.py](https://github.com/snadi/MSRDemos/blob/master/scripts/get_crypto_committer_emails.py) -- **PLEASE DO NOT EMAIL DEVELOPERS TO FILL SURVEYS ETC. AS PART OF THIS COURSE. SUCH CONTACT REQUIRES ETHICS APPROVAL. Also, please check the notes at the beginning of the script for further consideration**
* To run:

```
/msrdemo# cd scripts/
/msrdemo/scripts# python get_crypto_committer_emails.py --repoFile=../resources
/repositories.txt --outputFile=contactemails.csv --token=<tokenfile>
```

Output:

```
num of repos 57
repos from results 3
found  13
/msrdemo# cat contactemails.csv 
```

You need to [create your own token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) and save it in a token file that you pass to the script. 

Another example is looking at the average release times of various GitHub repos, as shown in [https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/ReleaseFrequency/releasefrequency.py](https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/ReleaseFrequency/releasefrequency.py).

## Using GHTorrent

* The website provides all the details on how to download a data dump to use [http://ghtorrent.org/downloads.html](http://ghtorrent.org/downloads.html)
* Alternatively, they now also offer a VM through vagrant that removes the burden of doing a lot of the setup needed
* You can follow the instructions [here](https://github.com/ghtorrent/ghtorrent-vagrant) to use this

# Mining Stack Overflow Data

## Using StackExchange APIs in Python

* The script [https://github.com/snadi/MSRDemos/blob/master/scripts/get_so_answer_stats.py](https://github.com/snadi/MSRDemos/blob/master/scripts/get_so_answer_stats.py) shows how you can use the StackExchange API to get the number of answer for a list of questions.

* To run:


```
/msrdemo# cd scripts/
/msrdemo# python get_so_answer_stats.py  
``` 

As another example for using Stack Exchange APIs, check out the code we used in our SANER '20 paper on navigating Stack Overflow answers [https://github.com/ualberta-smr/StackOverflowNavCues](https://github.com/ualberta-smr/StackOverflowNavCues). 

