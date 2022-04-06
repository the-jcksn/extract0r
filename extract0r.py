#extract0r - a tool for automating the boring daily copy and paste text extractions. Written by the-jcksn, to save me time when colleagues give me the tasks they don't want to do.

#defining the functions

#continue after extraction or quit
def more_extractions():
        more = input("\n[?] Would you like to perform further extractions? (y/n): ")
        while more != "y" and more != "n":
                print("[!] Invalid selection: Please try again")
                more = input("\n[?] Would you like to perform further extractions? (y/n): ")
        if more == "y":
                answer = "y"
        else:
                answer = "q"
        return(answer)

#end of extraction
def extraction_end(output_file):
        print("\n[+] Results saved in",output_file)
        input_file.close()
        output.close()


#fancy banner shit
print("███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝")
print("██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗")
print("███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║")
print("╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("                    \"Keeping only the good bits\"")
print("                         github.com/the-jcksn\n")
#initial menu, taking user input and assigning to selection
selection = ""
while selection != "q":
        print("[+] Please choose from the following:\n")
        print("[1]      - Extract IP addresses from standard nmap output file")
        print("[2]      - Extract the LM hashes from standard windows sam file")
        print("[3]      - Extract username list from standard windows sam file (duplicates removed)")
        print("[4]      - Extract all unique lines from any file (remove duplicate lines)")
        print("[q]      - Quit extract0r")
        selection = input("Please choose option (1 - 4) or 'q' to quit: ")
        # checking that selection has been made appropriately
        while selection != "1" and selection != "2" and selection != "3" and selection != "4" and selection != "q":
                print("[!] Invalid selection: Please try again")
                selection = input("Please choose option (1 - 4) or 'q' to quit : ")

        #if ip extract has been selected
        if selection == "1":
                print("\n[+]Extracting the IP addresses from nmap -oN output file")
                #gathering filename inputs
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                #initialise the string to remove and the empty ip list
                string = "Nmap scan report for "
                ips = []
                ip_exclude = []
                results = []
                #iterate the input file and check for the string
                for line in input_file:
                        if string in line:
                                #remove the string and add remaining to ip list
                                newline = line.replace(string,"")
                                newline = newline.replace("\n","")
                                ips.append(newline)
                #removing any excluded ip addresses from the results
                exclusion = input("[?] Would you like to exclude any specific IP addresses from the results? (y/n): ")
                #requesting if any IPs want excluding, checking input is y or n
                while exclusion != "y" and exclusion != "n":
                        print("[!] Invalid selection: Please try again")
                        exclusion = input("[?] Would you like to exclude any specific IP addresses from the output? (y/n): ")
                #gather IP addresses to exclude and add to ip_exclude list
                if exclusion == "y":
                        excluded = input("[?] Please enter the first IP address to exclude: ")
                        ip_exclude.append(excluded)
                        while excluded != "f":
                                excluded = input("[?] Please enter the next IP address to exclude, or type 'f' to finish: ")
                                if excluded != "f":
                                        ip_exclude.append(excluded)
                        #printing the IPs to exclude and aligning data format with other list
                        print("[+] Excluding the following IP addresses from the output:")
                        for i in ip_exclude:
                                print(i)
                        for i in ip_exclude:
                                i = i.replace("\n","")
                #checking ip list for any in the exclude list
                for i in ips:
                        if i not in ip_exclude:
                                results.append(i)
                #save results to file and run end of section commands
                for i in results:
                        with open(output_file, "a") as output:
                                output.write(i)
                                output.write("\n")
                extraction_end(output_file)
                selection = more_extractions()

        #if selection is lm hashes
        elif selection == "2":
                print("\n[+] Extracting the LM hashes from a sam file")
                #gather inputs
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                for line in input_file:
                        #set variables
                        count = 0
                        position_start = 0
                        position_end = 0
                        #find where the 3rd and 4th colon is
                        for char in line:
                                if count < 3:
                                        if char == ":":
                                                count += 1
                                        position_start += 1
                                        position_end += 1
                                elif count < 4:
                                        if char == ":":
                                                count += 1
                                        position_end += 1
                        #set newline to the characters between 3rd and 4th colon and add to output file
                        newline = line[position_start:position_end - 1]
                        with open(output_file, "a") as output:
                                output.write(newline)
                                output.write("\n")
                extraction_end(output_file)
                selection = more_extractions()
                
        #if selection is username from sam file
        elif selection == "3":
                print("\n[+] Extracting the Usernames from a sam file")
                #collect the inputs
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                #initialise empty lists
                dupes = []
                no_dupes = []
                for line in input_file:
                        #find everything before the first colon and add to list of dupes
                        count = 0
                        position_start = 0
                        position_end = 0
                        for char in line:
                                if count < 1:
                                        if char == ":":
                                                count += 1
                                        position_end +=1
                        newline = line[position_start:position_end - 1]
                        dupes.append(newline)
                for i in dupes:
                        #check dupes list for duplicates, add unique values to no_dupes
                        if i not in no_dupes:
                                no_dupes.append(i)
                for d in no_dupes:
                        #write no_dupes to output file
                        with open(output_file, "a") as output:
                                output.write(d)
                                output.write("\n")
                extraction_end(output_file)
                selection = more_extractions()

        #if selection is unique lines
        elif selection == "4":
                print("\n[+] Extracting unique lines from file (removing duplicate lines)")
                #collect the inputs
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                #initialise empty lists
                dupes = []
                no_dupes = []
                for line in input_file:
                        dupes.append(line)
                #check for duplicates and add unique lines to no_dupes
                for i in dupes:
                        if i not in no_dupes:
                                no_dupes.append(i)
                #write no_dupes to output  file
                for d in no_dupes:
                        with open(output_file, "a") as output:
                                output.write(d)
                #end of extraction functions
                extraction_end(output_file)
                selection = more_extractions()

print("\n[!] Quitting extract0r")
