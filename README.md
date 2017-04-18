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

```bash
git clone https://github.com/whatbirdisthat/pw4.git
```

2. Use pip to install the prerequisites
    
```bash
sudo -H pip install python-gnupg pyperclip
```

3. Put a symbolic link to pw4.py in your `$HOME/bin` folder (or `/usr/local/bin` for example)

```bash
ln -s $PWD/pw4.py $HOME/bin/pw4
```
        
4. Create a `.ini` file containing your passwords
        
```bash
vim pw4.ini
```
        
There's an [example-pw.ini](example-pw.ini) file to show the simplicity.
        
5. GPG encrypt it
        
```bash
gpg -e -r 'your-id' pw4.ini
```

6. Move the encrypted .gpg file to ~/.gnupg/

```bash
mv pw4.ini.gpg ~/.gnupg/
# make sure you can decrypt and view it before you delete it!
rm pw4.ini
```

7. Get your password:

```bash
pw4 nasa
```

## Add a new password

```bash
pw4 --new
```

You will be prompted to name the new section,
then asked for a number of new key-value pairs.

```bash
$ pw4 --new
Decryption Passphrase: (hidden)
New account name: a-new-account
New password: (hidden)
New key: newkey
New value: newvalue
New key: (enter)
AVAILABLE ENCRYPTION KEYS:
PW4 User (pw4-key) <pw4@localhost>
Enter recipient(s): pw4-key
newkey: newvalue
```

The excerpt above shows a new password section being added,
with a new account name, new password and extra field (key/value).

PW4 then shows the user a list of available encryption keys,
which gives the user to change the key used to encrypt the pw4.ini file.

Then the newly added password is put onto the clipboard and the
other key(s) are printed to the console.

>To exit the `new key/value` loop, press enter when prompted for a
>key name.

>`AVAILABLE ENCRYPTION KEYS` is a list of keys for which
>gnupg has both a private and a public.

## When you forget where your password is
Use the `all` argument to get a list of all the passwords.

```bash
pw4 --all
```

Or, if you have _bash completion_ set up, type `pw4` and press `<TAB>`.

# Bash Completion

If you have bash completion installed, you can perform some magic here.

First, create the completion file in the `/secure` folder using the following command:

```bash
pw4 --all > ~/.gnupg/pw4-all.txt
```

You'll need to create a symlink to the completion script too:
```bash
# mac with homebrew bash-completion
sudo ln -s $PWD/pw4-complete.sh /usr/local/etc/bash_completion.d/pw4-complete
# linux
sudo ln -s $PWD/pw4-complete.sh /etc/bash_completion.d/pw4-complete
```

Now you can tab-complete your PWs - which is awesome because that
gives you a way of showing all the keys (the equivalent of using `pw4 all`)

```bash
pw4 na[tab]
```

## A note on generating a secured .ini
You will need to install GPG before any of this will work.
```bash
# mac
brew install gpg
# linux
sudo apt install gpg
```
You will also need to create a key (if you need one).
```bash
gpg --full-gen-key
```
Answer the questions and your key is generated.

I find it is helpful to use the "comment" field as a quick identifier
for the key during encryption. That way you can use the "short name"
of the comment field as the recipient when encrypting:
```bash
gpg -er "comment" file.txt
```

### Bonus Extra points!
If you have `help2man` installed you can create a man page for pw4.
```bash
cd $PROJECT
# assuming you haven't given yourself permission to write to the man folders
sudo bash -c 'help2man -N ./pw4.py | gzip > /usr/share/man/man1/pw4.1.gz'
```
