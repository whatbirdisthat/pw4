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

2. Use pip into install the prerequisites
    
```bash
sudo pip -H install python-gnupg
sudo pip -H install pyperclip
```

3. Put a symbolic link to pw4.py in your $HOME/bin folder (or /usr/bin)

```bash
ln -s $PROJECT/pw4.py $HOME/bin/pw4
```
        
4. Create a `.ini` file containing your passwords
        
```bash
vim pw.ini
```
        
There's an [example-pw.ini](example-pw.ini) file to show the simplicity.
        
5. GPG encrypt it
        
```bash
gpg -e -r 'your-id' pw.ini
```

6. Move the encrypted .gpg file to ~/secure

```bash
mv pw.ini.gpg ~/secure
# make sure you can decrypt and view it before you delete it!
rm pw.ini
```

7. Get your password:

```bash
pw4 nasa
```

## When you forget where your password is
Use the `all` argument to get a list of all the passwords.

```bash
pw4 all
```
