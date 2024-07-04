#!/usr/bin/env bash

# Define variables
KEY_NAME="school"
BITS=4096
PASSPHRASE="betty"

# Generate SSH key pair with passphrase
ssh-keygen -t rsa -b $BITS -f ~/.ssh/$KEY_NAME -N "$PASSPHRASE"

# Display success message
echo "Generating public/private rsa key pair."
echo "Your identification has been saved in $KEY_NAME."
echo "Your public key has been saved in $KEY_NAME.pub."
echo "The key fingerprint is:"
ssh-keygen -lf ~/.ssh/$KEY_NAME
echo "The key's randomart image is:"
ssh-keygen -lvf ~/.ssh/$KEY_NAME.pub

# Move generated files to current directory
mv ~/.ssh/$KEY_NAME* .

# List current directory contents
ls -l
