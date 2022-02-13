import os, sys



class cipher_project:

	def __init__(self):
		self.current_path = os.getcwd()
		self.current_directory  = os.listdir(self.current_path)		
		self.run_encrytion = False
		self.run_decryption = False
		self.view_files = False
		self.shift_flag = False

	def run_program(self):
		"""Run the main program loop"""
		
		while True:
			os.system('cls')
			self._main_menu()
			if self.run_encryption == True:				
				self._run_encryption()
				
	def _main_menu(self):
		"""Presents the main menu of the program"""

		self.run_encryption = False
		self.run_decryption = False
		self.view_files = False
		print("Please select from the following options:\n0) Quit\n1) Encrypt File\n2) Decrypt File\n3) View File List")		
		while True:
			try:
				self.menu_choice = int(input("> "))
			except:
				print("Please enter a number.")
			if self.menu_choice == 0:
				quit()				
			elif self.menu_choice > 3:
				continue
			else:
				if self.menu_choice == 1:
					self.run_encryption = True
				elif self.menu_choice == 2:
					self.run_decryption = True
				else:
					self.view_files = True
				break

	def _get_file(self):
		"""User selects file for encryption"""

		print("Enter filename to encrypt:\n ")
		menu_index = 0
		print(str(menu_index) + ") Quit")
		for file in self.current_directory:
			menu_index += 1
			print(str(menu_index) + ") " + str(file))						
		
		while True:
			try:
				self.file_choice = int(input("\n> "))				
			except:
				print("\nPlease enter a valid number.")
				continue
			
			if self.file_choice == 0:
					quit()
			else:
				try:
					self.file_selection = self.current_directory[self.file_choice -1]
				except:
					print("\nPlease enter a valid number. exception: 1")
					continue
				else:
					break

		self.file = open(self.file_selection, 'r')		
		self.unencrypted_content = self.file.read()			
		print("\n" + self.unencrypted_content + "\n")			

		self.pause_loop = input("<Enter> to continue...\n")

	def _choose_cipher(self):
		"""User selects encryption method"""

		print("Select cipher to apply to plaintext \n 1 - Alphabet Shift")
		cipher_selection = int(input("> "))
		if cipher_selection == 1:
			self.cipher = ciphers.alphabet
			self.shift_flag = True

	def _choose_shift(self):
		"""User selects direction and amount of shift"""
		
		while True:			
			print("Shift which direction? [(l)eft or (r)ight]")
			self.shift_direction = input("> ")
			self.shift_direction = self.shift_direction.lower()			
			if self.shift_direction == "l" or self.shift_direction == "r":
				break
			else:
				print("\nInvalid option.")

		while True:
			print("Shift how many spaces?")
			try:
				self.shift_amount = int(input("> "))*2
			except:
				print("\nInvalid option.")
				continue
			else:				
				break
			

	def _run_encryption(self):
		"""Encrypts selected text file"""
		self._get_file()
		self._choose_cipher()
		if self.shift_flag == True:
			self._choose_shift()
		self.encrypted_content = ""
		for character in self.unencrypted_content:
			if character in self.cipher:
				cipher_index = 0
				for i in self.cipher:
					if character == i:						
						if self.shift_direction == 'l':
							self.new_character_index = cipher_index - self.shift_amount
							if self.new_character_index < 0:
								self.negative_index = True
								while self.negative_index == True:
									self.new_character_index = len(self.cipher) + self.new_character_index
									if self.new_character_index >= 0:
										self.negative_index = False	
						elif self.shift_direction == 'r':
							self.new_character_index = cipher_index + self.shift_amount
							if self.new_character_index > len(self.cipher)-1:
								self.over_index = True
								while self.over_index == True:
									self.new_character_index = self.new_character_index - len(self.cipher)
									if self.new_character_index < len(self.cipher):
										self.over_index = False					
						self.encrypted_content = self.encrypted_content + self.cipher[self.new_character_index]
					cipher_index += 1
			else:
				self.encrypted_content = self.encrypted_content + character

					
		

		input(self.encrypted_content)



class ciphers:

	def __init__(self):
		
		self.alphabet = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r","R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
		


ciphers = ciphers()
initialize = cipher_project()
initialize.run_program()