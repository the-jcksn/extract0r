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



print("███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝")
print("██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗")
print("███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║")
print("╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("                    \"Keeping only the good bits\"")
print("                         github.com/the_jcksn\n")
selection = ""
while selection != "q":
        print("[+] Please choose from the following:\n")
        print("[1]      - Extract IP addresses from standard nmap output file")
        print("[2]      - Extract the LM hashes from standard windows sam file")
        print("[3]      - Extract username list from standard windows sam file (duplicates removed)")
        print("[q]      - Quit extract0r")
        selection = input("Please choose option (1 - 3) or 'q' to quit: ")

        while selection != "1" and selection != "2" and selection != "3" and selection != "q":
                print("[!] Invalid selection: Please try again")
                selection = input("Please choose option (1 - 2) or 'q' to quit : ")


        if selection == "1":
                print("\n[+]Extracting the IP addresses from nmap -oN output file")
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                string = "Nmap scan report for "
                ips = []
                for line in input_file:
                        if string in line:
                                newline = line.replace(string,"")
                                ips.append(newline)
                for i in ips:
                        with open(output_file, "a") as output:
                                output.write(i)

                print("\n[+] Results saved in",output_file)
                input_file.close()
                output.close()
                selection = more_extractions()

        elif selection == "2":
                print("\n[+] Extracting the LM hashes from a sam file")
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                for line in input_file:
                        count = 0
                        position_start = 0
                        position_end = 0
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
                        newline = line[position_start:position_end - 1]
                        with open(output_file, "a") as output:
                                output.write(newline)
                                output.write("\n")
                print("\n[+] Results saved in",output_file)
                input_file.close()
                output.close()
                selection = more_extractions()

        elif selection == "3":
                print("\n[+] Extracting the Usernames from a sam file")
                filename = input("\n[?] Please enter filename to extract from: ")
                input_file = open(filename, "r")
                output_file = input("[?] Please choose a filename for the output: ")
                dupes = []
                no_dupes = []
                for line in input_file:
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
                        if i not in no_dupes:
                                no_dupes.append(i)
                for d in no_dupes:
                        with open(output_file, "a") as output:
                                output.write(d)
                                output.write("\n")

                print("\n[+] Results saved in",output_file)
                input_file.close()
                output.close()
                selection = more_extractions()


print("\n[!] Quitting extract0r")
