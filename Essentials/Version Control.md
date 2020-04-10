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

**Create A Repo From Scratch**

- Running the `git init` command sets up all of the necessary files and directories that Git will use to keep track of everything. All of these files are stored in a directory called `.git`. This is where git records all of the commits and keeps track of:

  - **config file :** Git looks for configuration values in the configuration file in the Git directory (.git/config) of whatever repository you’re currently using. These values are specific to that single repository.
  - **description file**  used by the GitWeb program
  - **hooks directory** client-side or server-side scripts to use to hook into Git's different lifecycle events
  - **info directory** the global excludes file
  - **objects directory** this directory will store all of the commits we make
  - **refs directory** this directory holds pointers to commits (basically the "branches" and "tags")

- Cloning a sample repository `git clone <path-to-repository-to-clone> target_folder_name `

- `git status` provides the state of our repository as Git sees it.It tells about new files that have been created in the Working Directory that Git hasn't started tracking yet, files that Git is tracking that have been modified

**Review a Repo's History**

- `git log` command is used to display all of the commits of a repository. By default, this command displays:
  - the SHA (Each SHA is unique, so we don't really need to see the entire SHA) 
  - the author
  - the date
  - and the message
  
- `--oneline` The git log command uses this flag to alter how it displays the repository's information.

- `--stat` The git log command uses this flag to display the files that have been changed in the commit, as well as the number of lines that have been added or deleted. ("stat" is short for "statistics")

- `-p`  The git log command uses this flag to display the actual changes made to a file. ("p" is short for "patch")

- `git log --stat -p fdf5493` By supplying a SHA, the git log -p command will start at that commit! 

- `git show`  will show only one commit (output is the same as the git log -p ). It can be combined with `--stat` and `w` flags where `-patch` is the default


**Add Commits to A Repo**

 - `git add <filename> ` command is used to move files from the Working Directory to the Staging Index
 -  the period `.` can be used in place of a list of files to tell Git to add the current
   - we have some new files that we want Git to start tracking
   - for Git to track a file, it needs to be committed to the repository
   - for a file to be committed, it needs to be in the Staging Index
   - ![Working Directory - Staging Index](https://video.udacity-data.com/topher/2017/February/58ade4ac_ud123-l4-git-add-to-staging-recap/ud123-l4-git-add-to-staging-recap.gif)
 
 - use `git rm --cached <file>...` to unstage
 
 - `git config --global core.editor <your-editor's-config-went-here>`  ( default is VIM , [link to update](https://help.github.com/en/github/using-git/associating-text-editors-with-git) 
 
 - `git commit` or `git commit -m "Initial commit"` to bypass The Editor 
 
 - [Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/)
 
 - `git diff` command can be used to see changes that have been made but haven't been committed, yet
   -  `git log -p` uses `git diff` under the hood

 - `.gitignore file` prevents files from being tracked and committed. This file should be placed in the same directory that the .git directory is in.
 
 - Globbing lets you use special characters to match patterns/characters : 
   - blank lines can be used for spacing
   - `#` - marks line as a comment
   - `*` - matches 0 or more characters
   - `?` - matches 1 character
   - `[abc]` - matches a, b, _or_ c
   - `**` - matches nested directories - a/**/z matches
    - to ignore 50 images are JPEG images in the "samples" folder `samples/*.jpg`
    - a/z
    - a/b/z
    - a/b/c/z
    
    
 
 
 
