+++
title = "Remote Pair Programming with TMUX"
author = "Logan Connolly"
date = "2022-05-20"
keywords = ["tmux", "ngrok", "pair-programming", "neovim"]
tags = ["tmux", "ngrok", "linux", "neovim"]
description = "Improve remote pair programming with ngrok + tmux + neovim"
+++

# The problem

Remote pair programming on a pixelated screen gets old fast. Not only is the picture quality lacking, but also the interactivity and collaboration that is needed for good pairing.

So when I found out that there was an alternative to the status quo, I jumped right in.

# A solution

> ngrok + tmux + neovim => more productive remote pair-programming

The source of inspiration was this excellent [article](https://cbctl.dev/blog/remote-pair-programming) from [@callisto13](https://github.com/callisto13). In her article, she details the main points that I will talk about today: 

# Why another article

The goal of this article is to go into a bit more detail, particularly how to set up your system to make sure that the person you are pairing with has _limited access_ to your system - ideally they should only have access to the project you are working on.

# Birds eye view

Here is a high-level overview of what we will cover:

1. Prerequisites
2. User creation
3. Sync project files
4. Clone dotfiles
5. Setup and start ssh server
6. Setup and start ngrok
7. Pair program

# Prerequisites

Here is what you need to get setup:

**Software**

- [tmux](https://github.com/tmux/tmux): terminal multiplexer for handling terminal sessions
- [ngrok](https://ngrok.com/): service for exposing what is running on your local machine to a public URL
- [neovim](https://neovim.io/): terminal text editor (you could swap this out for vim, emacs, nano, etc.)

> I highly recommend setting up a dotfiles (config) repository, so that you can quickly sync your editor and tmux settings.

# Add user with reduced privileges

Now that everything is installed, it is time to add a user named _pair_:

`$ sudo useradd --create-home --shell /usr/bin/fish pair`

Then add a password for this user with:

`$ sudo passwd pair`

# Rsync project to home directory 

Now that we have an unpriveledged user named _pair_, we can sync our project to its home directory via:

`$ sudo rsync -av --chown=pair:pair --delete /path/to/cool-project/ /home/pair/cool-project`

# Clone dotfiles

So now that we have access to the project's source code, let's login as the newly created _pair_ user:

`$ su pair`

> NOTE: What's great about making use of system user management as opposed to creating a new virtual environment, is that you still have access to your system dependencies like git, python, etc. So when you clone your dependencies, you only need to run your configuration sync.

For my dotfiles it looks like this:

```shell
git clone https://github.com/logan-connolly/dotfiles
cd dotfiles
make symlink      # create symbolic links to user's home directory
make paq-install  # install neovim plugins
```
After this, you should be able to log out (`$ exit`) and back in (`$ su pair`) after which you will be greeted with your configured terminal.

# Setup ssh server

We are getting close now. Everything should be said up locally so now it is time to allow your colleague to connect to your machine and login as _pair_. To accomplish this we first need to install [openssh](https://www.openssh.com/).

Once it is installed, you make want to configure the server settings to prevent users from having the ability to login to your computer with a password. You can do this by adding `PasswordAuthentication no` to the bottom of `/etc/ssh/sshd_config`.

Once your ssh server is configured, start it with `$ sudo systemctl start sshd`. The openssh server should be running on your system and will accept only users with public keys that are stored in `/home/pair/.ssh/authorized_keys`. Have your colleague send over there preferred publich key and store it in that file.

# Initialize ngrok ssh tunnel

So the openssh server is running, you have your friend's key, now what? Here is where ngrok comes in. Ngrok basically allows you to publish your ssh server to the internet using their proxy. `callisto13` uses a nice little script to create this connection; I have adapted it slightly here:

```shell
#!/bin/bash

init_ngrok_session() {
  echo "Starting ngrok tmux session ..."
  tmux new-session -s ngrok -d
  tmux send -t ngrok "ngrok tcp --region=eu 22" ENTER
}

ngrok_status() {
  url = ""
  while [ "$url" == "" ] || [ "$url" == "null" ]
  do
    echo "Could not detect running ngrok instance"
    echo "Sleeping for 5 seconds and then retrying..."
    echo
    sleep 2
    url=$(curl http://localhost:4040/api/tunnels 2>/dev/null | jq -r .tunnels[0].public_url)
  done

  host=$(echo "$url" | cut -d / -f 3 | cut -d : -f 1)
  port=$(echo "$url" | cut -d / -f 3 | cut -d : -f 2)

  echo "Send your pair the following ssh command:"
  echo "ssh -p ${port} $(whoami)@${host}"
}

init_ngrok_session
ngrok_status
```
We want to add this script to a path that _pair_ will have access to:

```shell
# copy contents into this script and save
sudo vim /usr/local/bin/start_rpp 

# make it executable
sudo chmod +x /usr/local/bin/start_rpp
```
