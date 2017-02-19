# PW4
### Tiny Password Manager Thingy

A command line password manager to copy your password to the clipboard
without all the steps usually involved in keeping a GPG encrypted file
on your HDD etc.

Just get the _"pw for"_ your account.

*pw4* is just a wrapper around some other tools and it makes the
task of retrieving a password less clunky.

## How to install
1. Clone the repo.

```commandline
git clone https://github.com/whatbirdisthat/pw4.git
```

2. Use pip into install the prerequisites
    
```commandline
sudo -H pip install python-gnupg
sudo -H pip install pyperclip
```

3. Put a symbolic link to pw4.py in your $HOME/bin folder (or /usr/bin)

```commandline
ln -s $PROJECT/pw4.py $HOME/bin/pw4
```
        
4. Create a `.ini` file containing your passwords
        
```commandline
vim pw4.ini
```
        
There's an [example-pw.ini](example-pw.ini) file to show the simplicity.
        
5. GPG encrypt it
        
```commandline
gpg -e -r 'your-id' pw4.ini
```

6. Move the encrypted .gpg file to ~/secure

```commandline
mv pw4.ini.gpg ~/secure
# make sure you can decrypt and view it before you delete it!
rm pw.ini
```

7. Get your password:

```commandline
pw4 nasa
```

## When you forget where your password is
Use the `all` argument to get a list of all the passwords.

```commandline
pw4 all
```

Or, if you have _bash completion_ set up, type `pw4` and press `<TAB>`.

# Bash Completion

If you have bash completion installed, you can perform some magic here.

First, create the completion file in the `/secure` folder using the following command:

```commandline
pw4 all > ~/secure/pw-all.txt
```

You'll need to create a symlink to the completion script too:
```commandline
sudo ln -s $PROJECT/pw4-completion.sh /usr/local/bash_completion.d/pw4-completion
```

Now you can tab-complete your PWs - which is awesome because that
gives you a way of showing all the keys (the equivalent of using `pw4 all`)

```commandline
pw4 na[tab]
```


## A note on generating a secured .ini
You will need to install GPG before any of this will work.
 ```commandline
 brew install gpg
```
You will also need to create a key (if you need one).
```commandline
gpg --full-gen-key
```
Answer the questions and your key is generated.

I find it is helpful to use the "comment" field as a quick identifier
for the key during encryption. That way you can use the "short name"
of the comment field as the recipient when encrypting:
```commandline
gpg -er "comment" file.txt
```


