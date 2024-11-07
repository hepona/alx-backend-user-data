import re
message = "15/09/2005"
# print(re.sub("\d\d+/+\d\d+/+\d\d\d\d", "x", message))
# # message = "toto@gmail.com"
# # print(re.sub("\w+@\w+\.com", "x", message))

"""returns the log message obfuscated"""
reg = [
    "\d",
    "\w+@\w+\.com",
]
sensitive = ["\d\d+/+\d\d+/+\d\d\d\d", "/w"]
for e in sensitive:
    censored = [re.sub(e, "xxx", message)]
print(censored)
