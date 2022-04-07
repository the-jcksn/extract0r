# extract0r

Python script for extracting information from files.

Currently has 5 options:

1) Extract unique email addresses from any file.
2) Extracting IP addresses from nmap output files created with the -oN switch during scan. Saves the list of IP addresses in newly created file for further use. Can exclude certain IP addresses from the output on request.
3)  Extracts LM hashes from windows sam files. Saves the list of LM hashes in a newly created file for further use.
4)  Extracts usernames from windows sam files. Removes the duplicates and saves the list in a newly created file for further use.
5)  Extracts unique lines from any file, thereby removing the duplicates in the file. Saves the unique lines to a newly created file for further use.


The testfiles are not necessary for the script to function, they are there purely for testing out parts of the script and learning how it maniplulates the data in input files. 
