#!/bin/bash

curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v

session_id=$(curl -XPOST localhost:5000/sessions \
    -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v 2>&1 | \
    grep -oP 'Set-Cookie: session_id=\K[^;]+')

if [[ -z "$session_id" ]]; then
    echo "Failed to retrieve session_id. Exiting."
    exit 1
fi

echo "Extracted session_id: $session_id\n"

curl -XGET localhost:5000/profile -b "session_id=$session_id"
curl -XGET localhost:5000/profile -b "session_id=nope" -v