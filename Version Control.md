### What is Version Control

- Main point of a version control system is to help you maintain a detailed history of the project as well as the ability to work on different versions of it. Having a detailed history of a project is important because it lets you see the progress of the project over time. If needed, you can also jump back to any point in the project to recover data or files.

- There are two main types of version control system models:
    - the centralized model - all users connect to a central, master repository
    - the distributed model - each user has the entire repository on their computer
    
**First Time Git Configuration** 

```bash 

mv /Users/buraku/Desktop/3-DataScience/udacity-terminal-config .udacity-terminal-config


# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3

git config --list
```

**Git & Code Editor**

```bash

git config --global core.editor "atom --wait"
git config --global core.editor "'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' -n -w"
git config --global core.editor "code --wait"

```

