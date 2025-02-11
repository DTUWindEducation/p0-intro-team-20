# Git Answers

### 1. What is the difference between git and GitLab?
- **Git** is a distributed version control system used to track changes in code, allowing multiple people to work on a project simultaneously.
- **GitLab** is a web-based Git repository manager that provides features for hosting Git repositories, code reviews, continuous integration/continuous delivery (CI/CD), issue tracking, and more. It enhances Git's functionalities by providing a UI, additional collaboration tools, and security features.

### 2. What is the difference between GitLab, GitHub, and BitBucket?
- **GitHub**: A cloud-based platform primarily for hosting Git repositories. It offers collaborative features like pull requests, issue tracking, and project management tools. It is widely used in open-source development.
- **GitLab**: Similar to GitHub but with a focus on DevOps and CI/CD tools. GitLab provides more extensive features like continuous integration, deployment pipelines, and issue tracking built-in, with an option to host your own instance.
- **BitBucket**: Another Git-based platform for version control that also integrates with CI/CD tools. BitBucket is popular with private repositories and has strong integration with other Atlassian products like Jira and Trello.

### 3. Why would I ever want to use Git, but not GitLab?
- You might want to use **Git** without GitLab if you don’t need a central server or collaborative features that GitLab provides. Git can be used locally on your computer for small projects or personal use, without the need for a remote server. If you don’t need to manage team workflows or CI/CD pipelines, Git alone may suffice.

### 4. What are the steps to update the GitLab server with some changes I made on my computer?
1. **Stage** your changes:
   ```bash
   git add .
