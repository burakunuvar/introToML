
  - [**Terminal Mac Cheatsheet**](https://github.com/0nn0/terminal-mac-cheatsheet#english-version )

  - **When to use quotes `'` or ``''`` **

      - Single quotes used to escape special characters ( space, * , ... )
      - It indicate that a special character should be treated as non-special

```bash
#move all files
mv source/* target
#move all pdf files
mv source/*.pdf target
#move file with name *
mv "source/*" target
```

```bash
touch 'Good Name Bad Face.txt'
rm *'Bad F'*
touch 'Good Name *Bad* Face.txt'
rm '*Bad*'
rm *'*Bad*'*
```
  - **Downloading**

    - `curl -o google.html  -L 'http:/google.com'`
    - `-o` tag is for saving as object whereas
    - `-L` tag is for web redirects
    - a lot of URLs have special characters like `%` or `&` in them, so prefer using quotes

  - **Viewing**

    - what's inside a file
    - `cat` : View file content - concatenate
    - `less`: View file content screen by screen.
         - then use `b` to go below, `/` to search for a keyword

  - **Searching**

    - `grep`: "global regular expression print,” processes text line by line and prints any lines which match a specified pattern
    - `wc`: "short for word count" reads either standard input or a list of files and generates one or more of the following
     statistics: newline count, word count, and byte count

    - Regular expressions are patterns that `grep` lets use - also known as regexps or regexes.


```bash
 grep keyword dictionary.txt | less
 grep keyword dictionary.txt | wc -l
 grep -c keyword dictionary.txt
 curl -L 'http:/google.com' | grep keyword
 curl -L 'http:/google.com' | grep keyword | wc -l    

 ```

  - **Shell and Environment variables**

```bash
 username='buraku'
 echo $username
 echo $LINES X $COLUMNS
 #to list where program files are
 echo $PATH
 #to add a directory, for => temporary
 PATH=$PATH:/new/dir/here
```

```bash
nano intro.sh
    echo " your logname is: "
    echo $LOGNAME
    echo "*********"
    echo "you are user: "
    echo $USER
    echo "*********"
    echo "you current working directory "
    echo $PWD
    echo "*********"
chmod 755 intro.sh
./intro.sh
```
   - [**BashProfile**](https://friendly-101.readthedocs.io/en/latest/bashprofile.html)

```bash
man bash
/prompting to search for PS1 primary prompt
nano .bash_profile
    echo -e "\n Hey, welcome back BURAK ! "
    date
    export PS1="buraku-aws \W $ "
    alias ll='ls-la'
```

   - [Bash PS1 Generator](http://bashrcgenerator.com/)

   - Useful links
       - https://regexr.com/
       - http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
       - http://www.tldp.org/LDP/Bash-Beginners-Guide/html/
       - https://www.bash.academy/
