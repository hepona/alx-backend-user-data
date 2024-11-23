#!/bin/bash

curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'

session_id=$(curl -XPOST localhost:5000/sessions \
    -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v 2>&1 | \
    grep -oP 'Set-Cookie: session_id=\K[^;]+')

if [[ -z "$session_id" ]]; then
    echo "Failed to retrieve session_id. Exiting."
    exit 1
fi

echo "Extracted session_id: $session_id\n"

curl -XDELETE localhost:5000/session -b "session_id=$session_id" -v
