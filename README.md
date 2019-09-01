# Python-Object-Oriented-Programming-Concepts

## Table of content: 
 1. Class and object  
 2. __init__ method 
 3. Constructor, self and comparing objects 
 4. Types of variables 
 5. Types of methods  
 6. Inner class  
 7. Constructor in inheritance  
 8. Introduction to polymorphism  
 9. Duck typing  
 10. Operator overloading 
 11. Method overloading
 12. Method overriding

## Some useful commands for version control via git bash

+ Link to download git 
https://git-scm.com/downloads
+ Configuring user name = git config --global user.name "Your user name of github" 
+ Configuring user email = git config --global user.email "Your user email of github" 
+ To view git config file = git config --global -e
+ To list git config = git config --global --list


## Configuring p4merge for visual comprison and merging 
 + website: perforce.com
 + Install visual merge tool from download section 
 + To set p4merge as graphical compare tool 
   1. git config --global diff.tool p4merge
   2. git config --global difftool.p4merge.path "C:/Program Files/.../p4merge.exe" (user forward slashes)
   3. git config --global difftool.prompt false
   

## Setting up repo (local)
+ To change the directory = cd "folder name where you you have the repo or you want to create a repo"
+ Create git project folder = git init PROJECTNAME_HERE
+ Go into project folder and create README file = code (editor you are using) README.md

## Git add, status and commit procedure 
+ To add a file into stagging area = git add  file_name
+ To commit that file = git commit -m 'commit message'
+ To see any kind of changes in current branch = git status
+ To add all the untracked files into staging area = git add .
## Git express commit
+ To add modified file to staging area and then directly into commit = git commit -am "Commit massage"

## Push file into github
+ To push that file into github repo = git push 

## Adding git version control to existing project 
+ Navigate to the project folder 
+ To create a repo in that folder = git init .

## Commit history and log 
+ To show log of all commit = git log
+ To show all changes made in the last commit = git show

## Undo Staging of file
+ Undo staging of file = git reset HEAD file_name
+ To change your code to an earlier commit = git checkout -- file_name

## File Handling 
+ Renaming an already commited file = git mv original_file_name new_file_name
+ Deletation of file = git rm file_name
+ Updating git with modification made externally to the file = git add -A (all changes) and git add -u (update)

## Ingnoring file that don't need to be commited/ not needed in repo 
+ Create a '.gitignore' file and add files name you don't want 

## Comparing differences 
+ To find difference between two different commits = git diff old_commit_id commit_id_you_want_to_comapre
+ To find recent changes = git diff.

## Branching 
+ Listing branches = git branch 
+ Creating new branch = git branch branch_name
+ Making branch active = git checkout branch_name_you_want_to_make_active
+ To push new branch into github = git push -- set-upstream origin branch_name
+ To checkout any panding changes in the branch = git checkout -b branch_name
+ To delete unnecessory branches = git branch -d branch_name

## Merging 
+ Activate the parent branch which whom you want to merge other child branch 
+ Then merge the other branch = git merge child_branch

## Conflict resolution 
+ When automatic merge is unable to handle the merge due to some clashes or overlap, we need to manually sort out the error. 
+ When merge command return an automatic merge failure. Pan the command 'cat file_name_with_conflict'
+ The conflicts are now displayed. 
+ To sort it out, we launch the mergetool 'git merge'
+ We select the version, save and exit the merge tool and then commit
+ After this action a copy of the original file is created 'file_name.orig'
+ To ignore this add the file name in the .gitignore file

## Tags
+ It is a concept in git that allows us to save a milestone 
+ It saves a particular state of the repo (git tag tagname)
+ On checking the status you will see (tag: tagname)
+ Proper method = Ex. git tag -a V1.0 -m "Release 1.0"

## Reset and Reflog
+ Used to go back to a different commit point
+ Soft reset: Change where HEAD is pointing = git reset commit_id --soft
+ Hard reset: Destractive but efficient = git reset commit_id --hard
+ Mixed reset: Reset staging area = git reset commit_id --mixed
+ To show all the action tacken into repo = git reflog

## Add repo to github
+ git remote add origin 'URL for Repo'
+ Sync changes between local and remote repo = git push -u origin master --tags















