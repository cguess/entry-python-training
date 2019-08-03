# The Command Line (Basic Intro)

Welcome to the wonderful world of modern computer programming! Most of the time you'll spend it in a system that, in all honesty, hasn't changed a whole lot since the early 1980's.

That system is called the "command line" (or CLI, command-line-interface in more arcane circles). This is a text based screen that, if you went to an elemtary/primary school in the 90's you'll think of as DOS, otherwise you'll recognize a bastardized version from very bad "hacking" scenes on medicore TV shows.

Rest assurd, it's not as hard as it seems, and once you understand a few patterns it becomes extremely powerful and often much faster than using a mouse.

## Reasoning

Before we continue let's just understand why we have to learn this at all. A lot of IDE's and other programming tools include the ability to run any code you write inside it, so who cares? Well, eventually you need to run the software you write in situations where they do more than just novelty tricks. Since most of what we'll write either a.) outputs a website or b.) runs through a lot of data and spits out a spreadsheet file or something similar, it makes more sense to have text/file based input instead of wasting time creating buttons and the like.

There's a lot more reasons, but they're beyond the scope of what we need to think about now.

## To start

The command line allows us to type in commands, and get the output. These commands can be very simple or exceedingly complex. For now, we'll start easy.

---

First, to open the command line it depends on your system. For now I'm going to assume MacOS since it's the most straight forward, but if you're on Linux, once it's open, everything should be, more or less, the same. Windows, that's another story, which I'll ignore for now.

---

Open the "Terminal" app by going to Finder, then to the Applications folder, then the Utlities folder, and then double clicking "Terminal"

### Navigation

1. Welcome to the terminal! The first thing to learn is to how to navigate around. Command lines work like the folders you're already used to in Finder. The structure is the same, just expressed differently.

1. When opening a terminal the folder you'll be automatically put in is your "Home" folder. This is the equivolent of the folder in Finder that has your "Documents" and "Pictures" etc. folder in it (on the left of Finder there's actually a little house, get it?). A quick note, when you're looking at the terminal the "Home" folder/directory is often abbreviated by a `~` which is just a substitute because you end up back in it a lot.

### Running Programs

1. The next thing to know is to how to see what's in your folder. To do that we type `ls` and press "Enter" From here you'll see something like this

```
AC_RunActiveContent.js               Documents                            Push-Test-US-East-1.pem              anaconda3
```

which runs the `ls` program, outputs everything in the folder, and then quits.

1. So that's cool, but what if want more information? In a graphic interface you may click another button or check boxes or something like that. Well, we can do something similar in the command line by passing in "flags" or "arguments". Flags are enable/disable commands, and arguments let us pass in additional info, like words or filenames for the program to use. So next type `ls -l` and get something like:

```
-rw-r--r--@    1 christopher  staff      8029 Dec 29  2017 AC_RunActiveContent.js
-rw-r--r--@    1 christopher  staff     33724 Dec 29  2017 ACatheader.jpg
-rw-r--r--     1 christopher  staff       261 Dec 29  2017 Accessible_Design.css
drwxrwxrwx     3 christopher  staff        96 Dec 31  2016 Adobe
drwxr-xr-x     3 christopher  staff        96 Sep 20  2017 AnypointStudio
drwx------     6 christopher  staff       192 May 22  2018 Applications
drwx------@    4 christopher  staff       128 Jul 10  2018 Applications (Parallels)
```

1. This last command gives you *a lot* more information about your files. Most of which doesn't matter to you for quite awhile, but there's still useful stuff. For instance: the fifth column is the size of the file (in bytes, so divide by 1000 to get the number of megabytes). The sixth column is when the file was created.

### Why we need this

This may seem dull and unnecessary over clicking a button to run your program, but trust me when I say that being able to be comfortable in the command line is a very important step to programming. Most programmers prefer to be in the command line if at all possible, some to the extent that they edit and write all of their code in it, never leaving it at all except to (sometimes) open a web browser.

A big, practical reason, is that the command line is often where error messages are shown when something goes wrong (which it will, all the time). So being able to read them and not be intimidated by a large wall of text is super important.

## A couple of other notes

- When you read books or look for answers online command line example will often start with a `$` character followed by a space. This is solely to indicate that it's a command line statement, only copy and paste everything after the `$ ` For example, if a StackOverflow answer says `$ cat sample.txt | grep 'oh the humanity'` only copy the `cat sample.txt | grep 'oh the humanity'` portion.

- There are actually a *bunch* of different command lines out there. The most popular is BASH which is default on MacOS and most Linux machines. Though it is being phased out for ZSH in the next version of MacOS. Either way, the lessons here won't change, just know that if you see "Bash" or "Zsh" they mean, usually, the command line.

- You can actually write entire programs just in the command line using its own specific programming langauge. We won't, because it's still like something from the 70's, but you can.

- To rerun the previous command, press the up-arrow key on your keyboard and it will automatically fill in the last command you typed. If you keep pressing up you can see the whole history of your commands.
