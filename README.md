Getting started with the SimpleMDM API and Python
----

I wrote a [blog post]() about some baby steps in querying the [SimpleMDM API](https://simplemdm.com/docs/api/) using python and the python `requests` library.

This is my example code. It's not the prettiest, nor is it the cleverest, but it's worked for me.

Modify the `key` and `serial` variables with your SimpleMDM API key and a test device serial number respectively.

The code will return a device ID - as well as a group ID - and then belt and braces will return a list of *ALL* the groups in your SimpleMDM instance as unformatted json.
