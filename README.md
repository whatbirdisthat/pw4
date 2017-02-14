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

        git clone https://github.com/whatbirdisthat/pw4.git

2. Use pip into install the prerequisites
    
        sudo pip -H install python-gnupg
        sudo pip -H install pyperclip

3. Put a symbolic link to pw4.py in your $HOME/bin folder (or /usr/bin)

        ln -s $PROJECT/pw4.py $HOME/bin/pw4
        
4. Create a `.ini` file containing your passwords
        
        vim pw.ini
        
5. GPG encrypt it
        
        gpg -e -r 'your-id' pw.ini

6. Move the encrypted .gpg file to ~/secure

        mv pw.ini ~/secure

7. Get your password:

        pw4 nasa

## When you forget where your password is
Use the `all` argument to get a list of all the passwords.

    pw4 all

