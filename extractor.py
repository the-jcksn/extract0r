#defining the functions

#function to continue after one extraction or quit
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


#fancy banner shit
print("███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝")
print("██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗")
print("███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║")
print("╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("                    \"Keeping only the good bits\"")
print("                         github.com/the_jcksn\n")
#initial menu, takin user input and assigning to selection
selection = ""
while selection != "q":
        print("[+] Please choose from the following:\n")
        print("[1]      - Extract IP addresses from standard nmap output file")
        print("[2]      - Extract the LM hashes from standard windows sam file")
        print("[3]      - Extract username list from standard windows sam file (duplicates removed)")
        print("[q]      - Quit extract0r")
        selection = input("Please choose option (1 - 3) or 'q' to quit: ")
        # checking that selection has been made appropriately
        while selection != "1" and selection != "2" and selection != "3" and selection != "q":
                print("[!] Invalid selection: Please try again")
                selection = input("Please choose option (1 - 2) or 'q' to quit : ")

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
                #iterate the input file and check for the string
                for line in input_file:
                        if string in line:
                                #remove the string and add remaining to ip list
                                newline = line.replace(string,"")
                                ips.append(newline)
                #add ips in list to output file
                for i in ips:
                        with open(output_file, "a") as output:
                                output.write(i)
                print("\n[+] Results saved in",output_file)
                #close files and call more_extractions
                input_file.close()
                output.close()
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
                print("\n[+] Results saved in",output_file)
                input_file.close()
                output.close()
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

                print("\n[+] Results saved in",output_file)
                input_file.close()
                output.close()
                selection = more_extractions()


print("\n[!] Quitting extract0r")
