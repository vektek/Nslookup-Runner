# Nslookup-Runner
Pyhton script to run nslookup on list of targets and output to txt file for OSINT research

This script:

Takes a text file (domains.txt) containing a list of domains (one per line)
Runs nslookup on each domain
Writes the results to an output file (nslookup_results.txt)
Includes error handling for:

File not found
Timeout errors
General exceptions


Provides console feedback on progress

To use this script:

Create a text file named domains.txt with one domain per line, for example:

textgoogle.com
yahoo.com
example.com

Save the script as something like nslookup_script.py
Run the script:

bash python nslookup_script.py
The output file nslookup_results.txt will contain the nslookup results for each domain, separated by headers and divider lines.
Features:

Strips whitespace from input lines
Handles empty lines in input file
Includes both stdout and stderr from nslookup
Uses a 10-second timeout for each lookup
Formats output for easy reading
Provides console feedback during processing

Requirements:

Python 3.x
nslookup command available on your system
Write permissions in the directory for creating the output file

Note: Make sure the nslookup command is available on your system. It's typically included with most operating systems, but on some Linux distributions, you might need to install it (e.g., dnsutils package on Debian/Ubuntu).
