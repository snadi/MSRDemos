# About

This repo contains a bunch of demos related to mining various kinds of information from different data sources (e.g., git repos, GitHub repos, Stack Overflow). These are simple use cases just to demonstrate available options and how to get started.

The demos are prepared by [Sarah Nadi](https://sarahnadi.org) and are mainly used in CMPUT 663 at the University of Alberta.

# Running the Demos

The repo comes with a Dockerfile that takes care of using the correct version of python and setting up dependencies. 

To build the Docker image (this will take a bit of time):

```
docker build --tag=msrdemo:f19 .
```

To run the docker image:

```
docker run --name MSRDemo -it --rm msrdemo:f19 /bin/sh
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
* Check out this [sample simple script](https://github.com/snadi/MSRDemos/blob/master/scripts/FindMergeConflicts.py) for finding merge conflicts in a repo's history. The criteria here is finding commits with two parents with the word "conflict" in their commit message. Note that this is a simplified crtieria and might miss cases with edited commit messages.
* Running this:

```
/msrdemo# cd repos/elasticsearch/
/msrdemo/repos/elasticsearch# python ../../scripts/FindMergeConflicts.py 
```

You should see this output:

```
3245e78b780c2b7ee00a2a031582824a79c2ea0a Sat May 19 11:38:17 2018
a5be4149a3ca867f8bb239a8e2a62751b904a392 Thu May 10 17:04:08 2018
db14717098e9e50751654f0f45a0c5cc5441a346 Fri May  4 13:40:57 2018
42e8d4b76109980d1974f1739263e6792981cc20 Mon May 15 10:25:07 2017
744b1afcb244601210778ed69ce250f8f72ac28b Fri May 12 08:55:05 2017
bf718a686fa9ba51a8292178740c15670d0f0ec5 Wed May 10 11:40:39 2017
35946a13d0218909941edf4a0ea479229286ae88 Thu Apr 20 11:35:21 2017
5717ac3cc67fbda09cf54828e14e463c3fe07566 Wed Apr 19 08:12:11 2017
fd509d015cf8b2a181e788adbf3a4f0000020d1f Fri Feb 24 10:52:56 2017
b680e62831574b3d2620cdacae6664830af98f32 Fri Feb 24 07:58:22 2017
0bbcd948275bd3d710e732e6c1db80fc6b9ddb8e Wed Feb 15 15:08:29 2017
4cb8d9d08cb6ebd1f63a5addd974649c6b1a31f5 Fri Feb  3 16:27:20 2017
d6738fa650a94a791971d3abf004045917667dfe Tue Nov 15 13:56:36 2016
1c02e48a8fe25700ca56f47dff400da87ccb3832 Thu Sep  1 11:06:21 2016
4d272cc9b26cd77d06e03d0ebb35974d63206c90 Tue Aug  9 09:53:29 2016
bdebaba8f5ceb015e28b8a3699640c9bd7991241 Mon Jul 11 21:17:38 2016
a9e93a0da4c982e8f40bdddbe25e8f05d8c1af26 Thu Jun 30 09:53:09 2016
bf7a6f550933b9944a4b2629ddf716e14711b007 Fri Jun 17 15:23:12 2016
b27b0483d597dfb3d3318cdde18a3dd272b62f00 Tue May 17 16:47:33 2016
d7eb375d2433a328b9715ae141e93e21b3aca277 Fri Apr 29 13:21:16 2016
407e2cdcf93475e2b326228eaf169fa2572d7d8b Tue Mar 29 09:04:02 2016
08d989d9b61a5c4a526b64e9b3d80ad4c4a3cb8d Thu Mar 24 11:06:10 2016
41ddc6fa3f202c082ade41dafa6c6f45f178664f Wed Mar 23 13:30:53 2016
1f1f6861b777cff0deb925ba88b623d2b3c249ed Tue Mar 15 10:03:28 2016
9acb0bb28ce4f6affe3de86943acb393d9c665ec Sun Mar 13 13:52:10 2016
69c83b3459f100055c316f364cea3cd58d713b52 Thu Mar 10 10:44:36 2016
c11cf3bf1fec128946f2517b944e3feed27f1f0a Fri Mar  4 11:23:10 2016
5fbf1b95dc4e0e0c71f393eeeeefa171fda11a6f Wed Mar  2 08:43:53 2016
aecf51cb42ea1abf1399989a23cae296542bfe6c Tue Mar  1 16:20:15 2016
1a46628daaea0a0a55649bb557976e2c9ef63733 Mon Feb 15 10:37:16 2016
4a9c84d86d508f68722eeb8686277a22545cbcff Thu Feb 11 14:04:04 2016
e000808836b384388c3a5350656693c0c6c9d4ad Thu Feb 11 10:09:28 2016
421ed1228b545a07db4710f0ee56959d70e64d45 Wed Feb 10 10:37:51 2016
80bbb4a385cb88800837fbe2d9a5367dcbfaaaf9 Tue Feb  9 10:37:20 2016
fab3b5568f0e238fbefbb1352789f8a61fc8ef0e Tue Feb  9 10:35:13 2016
f06f17f328574aeb8178156e407952ec47d58713 Fri Feb  5 09:22:14 2016
a241983c9d7def1927406cf7db9a9b5c7c23442a Mon Feb  1 13:38:33 2016
859f9e69b7927d06fa866b6fd3016366ddff52ba Fri Jan 29 11:58:19 2016
641aaab8967d9b2765daba06bbdff1c2d77f40c5 Tue Jan 26 16:07:17 2016
3b35754f5900286acdeb9ada7d2a988a9d177ecd Tue Jan 26 13:17:53 2016
cd8320b1716642ae4b0daec6ebc7623d041df674 Mon Jan 25 10:42:20 2016
e6f9cbce8f76096ea7366922e731cc9e93fb83b9 Thu Jan 14 15:00:26 2016
3b7d1b47f71879a463d5b22530304d9b0a9c9fe0 Thu Jan  7 12:42:02 2016
2c33f781929be230c7b7c5ee5d59334d45bfa5ce Wed Jan  6 09:35:53 2016
c618f75b7640365387ad790bb6e485e16990da9f Thu Oct 15 10:02:34 2015
6819224d2c541f7482050679250c7d98c005dfeb Mon Oct 12 11:54:14 2015
4557d1b560fdd3d7ec0f2aeea6f82a2031ce423e Thu Oct  8 10:39:34 2015
23f97c30a094e8557d7ea4b28c2daba5c0ed9bdf Wed Oct  7 16:20:27 2015
a0821355384ec6881bade28dd3d29e1a64bea550 Tue Oct  6 08:19:56 2015
a21238beda0f60e74387f1ba0274bb1a5c3ab615 Tue Sep 29 12:40:27 2015
44722700b0ab7b2abf40b36fb9ef5d635e9da6d0 Fri Sep 25 12:04:50 2015
9f08d48d340783fc8096b52d3c8f3631c2e21312 Fri Sep 25 09:14:53 2015
34de79370f2b7e220d254484ebb2e01cb94b74f2 Fri Sep 25 07:38:24 2015
a9c6e4c051ca5d682a40a956c67949ee47b69f44 Thu Sep 24 13:33:35 2015
08ae68c19544a3bcf4e517d78093bac8ef60949f Wed Sep 23 17:07:30 2015
1aae68d2e8b0ad8e7524ccd0119bd56375bfcca6 Tue Sep 22 10:43:55 2015
bab9523c5688f254a75b3e975f0f5ae934dc0190 Fri Sep 18 10:05:03 2015
ff74e94260f482ed6a32ad33db6dba7de52e452f Wed Sep 16 11:04:18 2015
2cc873b2d6991fd899c980aba3998a8e53772179 Tue Sep 15 15:34:49 2015
90f24c1a79705cdf63e232517b87905744ae5b3d Mon Sep 14 12:31:01 2015
73f7df510e45d36e9892dfbbf219a66df2d7322e Fri Sep 11 12:15:12 2015
56b3db6ba3463d244ea777b527b7a786caa5042c Thu Sep 10 13:52:28 2015
db705ab4609c48961333d984d21d4a26f8b86781 Wed Sep  9 15:08:22 2015
f2605b34d6c93d4c1a7cedcbb1d748a66c52afa3 Tue Sep  8 14:11:22 2015
be3409f1dbd38de5b61c5a29160828048501ef84 Fri Sep  4 17:21:38 2015
8bd7cdbdad05348aac409e64088cd29415e9c4ef Thu Sep  3 18:56:06 2015
fa93cc7b89e4a55e89d1e16fdcba7153a6dcceb5 Thu Sep  3 11:02:49 2015
52be313c69de9358944943ef2df4b7e3cdd77b15 Wed Sep  2 14:00:35 2015
78d097de39906fae207accf413bf6a6878aa5d80 Fri Aug 28 08:49:28 2015
96b5cebfb1fcecb4bf3533e38a138cc47017774a Tue Aug 25 11:16:46 2015
59cb67c7bd0ab6311115b20954e013412b676b29 Tue Aug 25 09:59:40 2015
2d42839eefa506e568fdb2b7045fa260ef2354c5 Fri Aug 21 13:58:36 2015
4a3faf1126800a4e4be736e11fae64269e7a4e55 Tue Aug 18 13:20:16 2015
de54671173003750b5df2671c1ab64d1903fe8fb Tue Aug 18 08:35:17 2015
32dfd249e95feede1732b3df7479059c30d5c3a6 Mon Aug 17 08:16:55 2015
f3d63095dbcc985e24162fbac4ee0d6914dc757d Fri Aug 14 10:34:26 2015
f8a90edab28fe6039b2d418519393f34d2f8da80 Fri Aug 14 09:40:49 2015
e2181990c439138f5fce28c7ba3e8cd5e07d2b2c Tue Aug 11 11:24:17 2015
5edb287d3a5e9e774698f3e8f610b0fcef9fb23b Fri Aug  7 09:13:24 2015
20f944bf9459c5dd0b8326641c43782ddc0880b4 Thu Aug  6 13:09:14 2015
b763265f677132fe3772d51135734f542540e6bb Thu Aug  6 09:14:04 2015
4cceb08a0b786788c8fba7c1c2a80ed1d8f1d441 Tue Aug  4 08:53:19 2015
e472cbed09cb6a4020a2ff4114e546abe8476252 Mon Aug  3 17:20:34 2015
c0490215c7dcc48a042e712aaaa851754bc03df2 Mon Jul 20 10:20:57 2015
fc1b178dc4b844070f29074ce27f8bc348a9499f Wed Jul  8 11:11:25 2015
63530631f9fe1f63b9677af61019639bd8cb78cf Thu Jul  2 13:29:48 2015
d7187238a21cdf5aaee75e2820855893a36a7e16 Thu Jul  2 09:46:47 2015
654dc20897b0e4eb479c5dea64b3a87dc496ba4e Tue Jun 30 15:38:31 2015
4406d236de9483a35d4e3b08be8a2558e8f99274 Tue Jun 30 08:52:34 2015
6678acfe23bf9a10bcfaa9028a3f18c25970e0f1 Fri Jun 26 12:48:20 2015
99147228d721acfad158a6b0166783e3ab930ebb Tue Jun 23 08:16:21 2015
cccc71f1e4adbb25c2563e1afb971fac95337777 Thu Jun 18 14:19:27 2015
de39879558cae701b5266797258d42fc914cf2c2 Wed Jun 17 13:56:45 2015
c5bf86554319e84e10677240abcc524c0059cba3 Tue Jun 16 18:12:05 2015
10c5ac635326ef82f723342309765f689c45a06f Tue Jun 16 15:48:06 2015
5d3bedfe9680c002b2b2eca578669ba06d92df70 Tue Jun 16 09:12:00 2015
5f66f681358f6376eb000eaecae72bc34de45ddf Wed Jun 10 07:09:43 2015
42acee358705868f099edd3e6c6c92e7c18cf80e Tue Jun  9 08:48:32 2015
7f673fbdfd92a204b06a4ec307909a338d4721fe Mon Jun  8 13:14:13 2015
e1197dfea98712b085083639f74901d1c6a7e0f2 Thu Jun  4 17:59:10 2015
313e9c67697a8c6f0b332e2005a39cf69f68c3df Thu Jun  4 12:44:52 2015
b1f6d1abd65735f6abee642212bb4b4569fe1aca Wed Jun  3 08:44:02 2015
b964004a6a3751f6260069475e6ade56bed32b30 Thu May 21 09:04:01 2015
242a452142c1f821cffb1d8843570eb0f3b92fb8 Tue May 19 12:55:45 2015
9d2852f0ab76f42f267feed3328c215e51b6c088 Tue May 19 10:16:22 2015
f9f0e99eae0792b4eb3040803745e7a46ccfd8a7 Sun May 17 18:11:19 2015
9f81ae48459ede10f3de1e71ab9ef9b3801eb404 Fri May 15 15:01:23 2015
020ad5a72366838e38369b4668447d66f4c5ea4a Wed May 13 16:20:22 2015
c98f290d927b15d5840f92ac4e68562e60cd901f Fri May  8 08:33:39 2015
1a8ab9a33dd9a0276b107d2a890b6b0138a9c7f1 Tue May  5 10:54:52 2015
fe5a35b68efa9128ef524de6a215f6fccae2cc9d Tue May  5 09:46:02 2015
01d6f0dc1d569f4d7e947a322129e492092724ee Mon May  4 13:55:29 2015
7e5f9d5628fda74e73af48048594a4369fd39099 Mon May  4 09:37:54 2015
0589adb8b4d2f6f8d73f7293c9ba585b6c002c84 Wed Apr 29 15:32:05 2015
57a88859643477db5ae62a3a64d936a8ef5679b7 Wed Apr 29 14:49:41 2015
0fd7ed4bcddc833aac32f5a403a00f1a1c22d970 Wed Apr 29 09:54:19 2015
ffd8db6828da2f1f94eb6aa4bcde02ff17005143 Thu Apr 23 19:09:34 2015
6c32279cdd9265453df050ac5edeb5fc04c5dd36 Wed Apr 22 09:36:36 2015
fb481bc145778d5aba996b01af4b82e2f8e84952 Wed Apr 15 22:34:24 2015
56a37620ed2cffd57b8b3fa6b5dcbf4ee4718df9 Thu Apr  9 14:33:34 2015
2ac93098b28ce61bad24e40c478ea04ce9e1c980 Wed Mar 18 21:13:44 2015
dc0391273197ef0060d8d1da58d87f51dd9d9a93 Wed Mar  4 10:49:46 2015
2203f439e211be5510cfb0d6e1d2483dba15c6fe Fri Nov 21 10:00:01 2014
3fcae916334410dd2516e898035e6011c07e629c Thu Nov 20 15:44:25 2014
9f3f23698f18466de292c3706eda6afbc5225923 Tue Nov  4 17:09:40 2014
```

Take any commit SHA and check it out on GitHub to verify that it is a merge conflict. e.g., [https://github.com/elastic/elasticsearch/commit/9f3f23698f18466de292c3706eda6afbc5225923](https://github.com/elastic/elasticsearch/commit/9f3f23698f18466de292c3706eda6afbc5225923)

## Using PyDriller to Mine git Repos

* Use case: finding commits with messages containing certain keywords related to non-functional requirements
* Check [https://github.com/snadi/MSRDemos/blob/master/scripts/find_NFR_commits.py](https://github.com/snadi/MSRDemos/blob/master/scripts/find_NFR_commits.py)
* To run:

```
/msrdemo# cd scripts/
/msrdemo/scripts# python find_NFR_commits.py ../data/elasticsearch/
```

# Mining GitHub

## Using Python Github APIs

* Example of a simple script thaat retrieves emails of developers who committed to java files using the `javax.crypto.*` APIs: [https://github.com/snadi/MSRDemos/blob/master/scripts/get_crypto_committer_emails.py](https://github.com/snadi/MSRDemos/blob/master/scripts/get_crypto_committer_emails.py) -- **PLEASE DO NOT EMAIL DEVELOPERS TO FILL SURVEYS ETC. AS PART OF THIS COURSE. SUCH CONTACT REQUIRES ETHICS APPROVAL. Also, please check the notes at the beginning of the script for further consideration**
* To run:

```
/msrdemo# cd scripts/
/msrdemo/scripts# python get_crypto_committer_emails.py --repoFile=../resources
/repositories.txt --outputFile=contactemails.csv --username=<your github username>
```

Output:

```
num of repos 57
repos from results 3
found  13
/msrdemo# cat contactemails.csv 
```

Note that the script now uses a username and password for authentication. It is better to use a github autherization token, but such tokens cannot be pushed to any public GitHub repo. 

Another example is looking at the average release times of various GitHub repos, as shown in [https://github.com/snadi/MSRDemos/blob/master/scripts/get_release_frequency.py](https://github.com/snadi/MSRDemos/blob/master/scripts/get_release_frequency.py).

```
/msrdemo# cd scripts/
/msrdemo# python get_release_frequency.py 
``` 

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

