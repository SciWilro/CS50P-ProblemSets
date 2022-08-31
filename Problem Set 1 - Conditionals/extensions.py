import mimetypes

# Extensions
# https://cs50.harvard.edu/python/2022/psets/1/extensions/
__author__ = "Wilro - https://github.com/SciWilro"

usr_input = input("Filename?: ").strip()
if "." in usr_input:
    mtype = mimetypes.guess_type(usr_input)[0]
else:
    mtype = "application/octet-stream"

print(mtype)

# guess_type() returns tuple (mimetype, encoding)
#  so point to first element [0]
