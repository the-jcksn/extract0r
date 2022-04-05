print("███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝")
print("██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗")
print("███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║")
print("╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("                    \"Keeping only the good bits\"")
print("                         github.com/the-jcksn\n")
selection = ""
while selection != "q":
	print("[+] Please choose from the following:\n")
	print("[1]	- Extract IP addresses from standard nmap output file")
	print("[2]	- Extract the LM hashes from standard windows sam file")
	print("[q] 	- Quit extract0r")
	selection = (input("Please choose option (1 - 2) or 'q' to quit: "))

	while selection != "1" and selection != "2" and selection != "q":
		print("[!] Invalid selection: Please try again")
		selection = (input("Please choose option (1 - 2) or 'q' to quit : "))


	if selection == "1":
		print("\n[+]Extracting the IP addresses from nmap -oN output file")
		filename = input("\n[?] Please enter filename to extract from: ")
		input_file = open(filename, "r")
		output_file = input("[?] Please choose a filename for the output: ")
		string = "Nmap scan report for "

		for line in input_file:
			if string in line:
				newline = line.replace(string, "")
				with open(output_file, "a") as output:
					output.write(newline)

		print("\n[+] Results saved in",output_file)
		input_file.close()
		output.close()
		print("\n[?] Would you like to perform further extractions?")

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
		print("\n[?] Would you like to perform further extractions?")

print("\n[!] Quitting extract0r")
