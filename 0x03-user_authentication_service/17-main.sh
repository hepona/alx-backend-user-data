#!/bin/bash

curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
curl -X POST http://127.0.0.1:5000/reset_password -d "email=bob@me.com"