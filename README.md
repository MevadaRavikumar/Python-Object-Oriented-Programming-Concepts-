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
   
   
+ To change the directory = cd "folder name where you you have the repo or you want to create a repo"
+ Create git project folder = git init PROJECTNAME_HERE


+ To see any kind of changes in current branch = git status
+ To add a file into stagging area = git add  file_name
+ To add all the untracked files into staging area = git add .
+ To commit that file = git commit -m 'commit message'
+ To add modified file to staging area and then directly into commit = git commit -am "Commit massage"
+ To push that file into github repo = git push 


## Adding git version control to existing project 
+ Navigate to the project folder 
+ To create a repo in that folder = git init .

+ To show log of all commit = git log
+ To show all changes made in the last commit = git show
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













