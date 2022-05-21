+++
title = "Remote Pair Programming"
author = "Logan Connolly"
date = "2022-05-20"
keywords = ["tmux", "ngrok", "pair-programming", "neovim"]
tags = ["tmux", "ngrok", "linux", "neovim"]
description = "Improve remote pair programming with ngrok + tmux + neovim"
+++

# The problem

Remote pair programming on a pixelated screen gets old fast. Not only is the picture quality lacking, but also the interactivity and collaboration that is needed for good pairing. So when I found out that there was an alternative to the status quo, I jumped right in.

# A solution

The source of inspiration was this excellent [article](https://cbctl.dev/blog/remote-pair-programming) from [@callisto13](https://github.com/callisto13). In her article, she details the main points that I will talk about today: 

> ngrok + tmux + neovim => more productive remote pair-programming

# Why another article

The goal of this article is to go into a bit more detail, particularly how to set up your system to make sure that the person you are pairing with has _limited access_ to your system - ideally they should only have access to the project you are working on.

# Birds eye view

Here is a high-level overview of what we will cover:

1. Prerequisites
2. User creation
3. Get project code
4. Clone dotfiles
5. Setup and start ssh server
6. Setup and start ngrok
7. Wrap up

# Prerequisites

Here is what you need to get setup:

- [tmux](https://github.com/tmux/tmux): terminal multiplexer for handling terminal sessions
- [ngrok](https://ngrok.com/): service for exposing what is running on your local machine to a public URL
- [neovim](https://neovim.io/): terminal text editor (you could swap this out for vim, emacs, nano, etc.)

> **NOTE**: You need to be signed up with ngrok before you can proceed! Also, I highly recommend setting up a dotfiles (config) repository, so that you can quickly sync your editor and tmux settings.

# Add user with reduced privileges

Now that everything is installed, it is time to add a user named _pair_:

`$ sudo useradd --create-home --shell /usr/bin/fish pair`

Then add a password for this user with:

`$ sudo passwd pair`

> **NOTE**: this does not mean that the user will not have any privileges! It all depends on how you have your system setup up, but generally this user should not have write/execute permissions on your files, but may have read... Since the user is not of the same group, you could restrict read access by setting your files to `640`. Here is a snippet for changing the permissions for all files in a specific file path: `find <path> -type f -exec chmod 640 {} +
`

# Get project code

Now that we have a limited user named _pair_, we can sync our project to its home directory. You can do this by either syncing the directory from your other user, like so:

`$ sudo rsync -av --chown=pair:pair --delete /path/to/cool-project/ /home/pair/cool-project`

Or just by cloning it from a remote repository:

`$ git clone https://github.com/team/cool-project`

# Clone dotfiles

So now that we have access to the project's source code, let's first login as the newly created _pair_ user:

`$ su pair`

Once we are logged in, we should clone your configuration files (or sync them from other user). For my dotfiles it looks like this:

{{< code language="bash" title="Clone dotfiles" id="1" expand="Show" collapse="Hide" isCollapsed="false" >}}
git clone https://github.com/logan-connolly/dotfiles
cd dotfiles
make symlink      # create symbolic links to user's home directory
make paq-install  # install neovim plugins
{{< /code >}}

After this, you should be able to log out (`$ exit`) and back in (`$ su pair`) after which you will be greeted with your configured terminal.

> **NOTE**: What's great about making use of system user management as opposed to creating a new virtual environment, is that you still have access to your system dependencies like git, python, etc. So when you clone your dependencies, you only need to run your configuration sync.

# Setup ssh server

It is now time to give your colleague access to your machine and login as the _pair_ user. To accomplish this we first need to install [openssh](https://www.openssh.com/) package.

Once it is installed, you should configure the server settings to prevent users from logging in with password. You can do this by adding `PasswordAuthentication no` to the bottom of the `/etc/ssh/sshd_config` file.

Once your ssh server is configured, start it with `$ sudo systemctl start sshd`. The openssh server should be running on your system and will accept only users with public keys that are stored in `/home/pair/.ssh/authorized_keys`. Have your colleague send over there preferred public key and store it in that file.

> **NOTE**: the server will continue running for the remainder of the time you are logged in. To manually disable it, run `$ sudo systemctl stop sshd`.

# Initialize ngrok ssh tunnel

Your ssh server is running, but what link do you share? This is where Ngrok comes in. Ngrok basically allows you to publish your ssh server to the internet using their proxy. 

In the source article, `callisto13` uses a nice little script to create this connection; I have adapted it slightly here, but the results should be the same:

{{< code language="bash" title="Start ngrok session" id="2" expand="Show" collapse="Hide" isCollapsed="false" >}}
#!/bin/bash

init_ngrok_session() {
  echo "Starting ngrok tmux session ..."
  tmux new-session -s ngrok -d
  tmux send -t ngrok "ngrok tcp --region=eu 22" ENTER
}

ngrok_status() {
  echo "Checking to see if ngrok session is running ..."
  ngrok_url=http://localhost:4040/api/tunnels

  while [ "$url" == "" ] || [ "$url" == "null" ]
  do
    echo "Could not detect running ngrok instance"
    echo "Sleeping for 5 seconds and then retrying..."
    echo
    sleep 5
    url=$(curl $ngrok_url 2>/dev/null | jq -r .tunnels[0].public_url)
  done

  host=$(echo "$url" | cut -d / -f 3 | cut -d : -f 1)
  port=$(echo "$url" | cut -d / -f 3 | cut -d : -f 2)

  echo "Send your pair the following ssh command:"
  echo "ssh -p ${port} $(whoami)@${host}"
}

init_ngrok_session
ngrok_status
{{< /code >}}

We want to add this script to a path that _pair_ will have access to:

```shell
# copy contents into this script and save
sudo vim /usr/local/bin/start-rpp 

# make it executable
sudo chmod +x /usr/local/bin/start-rpp
```

Now log into _pair_ (`$ su pair`) and run script `$ start-rpp`. You should get some feed back saying which command to send your friend.

> **NOTE**: You may get a permission denied error if you are running a tmux session with your normal system user.

# Wrap up

After this, you should be ready to go! All you need to do is create a tmux session to work on and both attach to it: `$ tmux new-session -s cool-project` Then you can tell your pair to attach to the same session with `$ tmux attach-session -s cool-project`.

Happy pairing!
