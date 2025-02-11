7. #Git will detect a merge conflict when both branch1 and branch 2 have modified the same line in file.txt.
#example
git add file.txt
git commit -m "Initial commit"
git checkout -b branch1
git add file.txt
git commit -m "Change on branch1"
git checkout main
git checkout -b branch2
git add file.txt
git commit -m "Changes on branch2"
git checkout main
git merge branch1
git merge branch2

#8. Yes. Git allows you to track changes over time, and Git’s branching system is very useful for LaTeX documents.

#9. Not recommend. Word (.docx) and PowerPoint (.pptx) files are binary formats. Git works best with text-based files (like .txt, .md, .tex, etc.) and for binary files, resolving merge conflicts becomes extremely difficult since you cannot see the textual differences directly. 

#10. Merge conflicts may occur. If someone else has made changes and pushed them to the remote branch after you last pulled, then your local branch is behind the remote branch. When you try to push your changes, you will likely encounter an error, such as:
! [rejected]        your-branch -> your-branch (non-fast-forward)
error: failed to push some refs to 'https://github.com/your-repo'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.

#11. It depends on whether the local changes conflict with remote changes or not. If so, Git will stop and mark the file as conflicted. We'll have to manually resolve the conflicts before proceeding. If not, Git will successfully merge the local changes with the changes from the remote branch, and the pull will create a new merge commit if necessary.

#12. Branching is a way to create a parallel version of your code within the same repository. Tipically used in teams. Forking is a way to create a personal copy of someone else's entire repository. Common in open-source projects.