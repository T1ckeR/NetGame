import os
import time
import random
import sys
import shutil
import urllib.request
from datetime import datetime
import webbrowser

newest_version = 1100

with open('configurations//ver.txt', 'r') as f:
	cur_ver = (int(f.read()))
f.close()
if cur_ver != newest_version:
	newest_version = (str(newest_version))
	with open('configurations//ver.txt', 'w') as f:
		f.write(newest_version)
	f.close()
	print('\nYour program has been successfully updated from version ' + str(cur_ver) + ' to version ' + str(newest_version) + '.\n')
	time.sleep(5)

sys.setrecursionlimit(2000)

with open('configurations//routers', 'r') as f:
	router_config = f.read().splitlines()
f.close()

files = os.listdir('saves')
if (str(files)) == '[]':
	print('No device configurations detected. Creating a new one...')
	with open('saves//my_first_save.txt', 'w') as f:
		pass
	f.close()
	time.sleep(0.5)
	save_file = False
	devices = False
else:
	if (len(files)) > 1:
		count = 0
		for line in files:
			print("(" + str(count) + ") " + files[count])
			count += 1
		try:
			save_file = (int(input("Please enter a choice: ")))
			save_file = (files[save_file])
		except:
			print('Wrong choice.')
			exit()
	else:
		save_file = (files[0])
	print('Loading ' + save_file + "...")
	time.sleep(0.4)
	with open(('saves//' + save_file), 'r') as f:
		save = f.read().splitlines()
	f.close()
	print('Importing devices...')
	time.sleep(0.2)
	devices = []
	count = 0
	for line in save: 
		line_ = save[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			devices.append(line_)
			if '_' in line_:
				line_ = (line_.replace('_', ''))
		elif line_[0] == ' ':
			line_ = (line_.replace(' ', ''))
			devices.append(line_)
		count += 1

files = os.listdir('network_saves')
if (str(files)) == '[]':
	print('No network configurations detected.')
	saved_file = False
	network = False
	networks = False
else:
	if (len(files)) > 1:
		count = 0
		for line in files:
			print("(" + str(count) + ") " + files[count])
			count += 1
		try:
			saved_file = (int(input("Please enter a choice: ")))
			saved_file = (files[saved_file])
		except:
			print('Wrong choice.')
			exit()
		print('Devices imported successfully.')
	else:
		saved_file = (files[0])
	with open(('network_saves//' + saved_file), 'r') as f:
		networks = f.read().splitlines()
	f.close()
	print('Loading ' + saved_file + "...")
	time.sleep(0.4)
	print('Importing networks...')
	time.sleep(0.2)
	network = []
	count = 0
	for line in networks: 
		line_ = networks[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			if '_' in line_:
				line_ = (line_.replace('_', ''))
			network.append(line_)
		elif line_[0] == ' ':
			line_ = (line_.replace(' ', ''))
			network.append(line_)
		count += 1
	print('Networks imported successfully.')
main_directory = (os.getcwd())


def menu(save_file, devices):
	ftp_host = False
	first_opened = True
	os.chdir(main_directory)
	with open('servers//main.txt', 'r') as f:
		server_config = f.read().splitlines()
	f.close()
	print('\n\n\n\n')
	print('(1) Create Device\n(2) Command Line\n(3) Delete Device\n(99) Quit')
	try:
		choice = input('\n\nPlease enter your choice: ')
		print('\n\n\n\n')
	except:
		menu(save_file, devices)
	with open(('saves//' + save_file), 'r') as f:
		save = f.read().splitlines()
	f.close()
	devices = []
	count = 0
	for line in save: 
		line_ = save[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			devices.append(line_)
			if '_' in line_:
				line_ = (line_.replace('_', ''))
		elif line_[0] == ' ':
			line_ = (line_.replace(' ', ''))
			devices.append(line_)
		count += 1
	if choice == '1':
		print('(1) Network\n(2) Desktop\n(3) Server\n(99) Back')
		device_to_create = input("\n\nPlease enter your choice: ")
		if device_to_create == '99':
			menu(save_file, devices)
		else:
			create_device(device_to_create, save_file)
	elif choice == '2':
		if str(devices) == '[]':
			input('You do not have any existing devices. Press ENTER to go back.')
			menu(save_file, devices)
		else:
			counted = 0
			count = 0
			print('Computers: \n')
			for _ in range((len(devices)) // 6):
				print("(" + str(counted) + ") " + (devices[count].replace('_', ' ', 1000)))
				count += 6
				counted += 1
			if not server_config == '[]':
				print('\nServers: \n')
				counted = 0
				count = 0
				for _ in range((len(server_config)) // 10):
					line_ = (server_config[counted])
					line_ = line_.replace('_', ' ', 1000)
					print('(S' + str(count) + ') ' + line_)
					count += 1
					counted += 10
			print("(99) Back")
			try:
				cmd = (input('\n\nPlease select a device: '))
			except:
				menu(save_file, devices)
			try:
				cmd = int(cmd.replace("S", ""))
				cmd = int(cmd.replace("s", ""))
				number = True
			except:
				try:
					cmd = int(cmd.replace("S", ""))
					cmd = int(cmd.replace("s", ""))
					number = True
				except:
					number = False
			if number == True:
				if cmd == 99:
					menu(save_file, devices)
			print('\n\n\n\n')
			selected_index = (cmd)
			server = False
			ftp = False
			if 'S' in str(selected_index) or 's' in str(selected_index):
				server = True
				selected_index = selected_index.replace("S", "")
				selected_index = selected_index.replace("s", "")
				selected_index = int(selected_index)
				selected_index = (selected_index * 10)
				saved_dir = (main_directory + '\\servers\\' + (server_config[selected_index]))
				selected_device = [(server_config[(selected_index)]), (server_config[(selected_index + 1)]), (server_config[(selected_index + 2)]), (server_config[(selected_index + 3)]), (server_config[(selected_index + 4)]), (server_config[(selected_index + 5)]), (server_config[(selected_index + 6)]), (server_config[(selected_index + 7)]), (server_config[(selected_index + 8)]), (server_config[(selected_index + 9)]), (server_config[(selected_index + 10)])]
			else:
				selected_index = int(selected_index)
				selected_index = (selected_index * 6)
				saved_dir = (main_directory + '\\computers\\' + (devices[selected_index]))
				selected_device = [(devices[(selected_index)]), (devices[(selected_index + 1)]), (devices[(selected_index + 2)]), (devices[(selected_index + 3)]), (devices[(selected_index + 4)]), (devices[(selected_index + 5)])]
			command_line(devices, save_file, selected_index, network, saved_file, main_directory, saved_dir, server, selected_device, ftp, ftp_host)
	elif choice == '3':
		if str(devices) == '[]':
			input('You do not have any existing devices. Press ENTER to go back.')
			menu(save_file, devices)
		else:
			counted = 0
			count = 0
			print('Computers: \n')
			for _ in range((len(devices)) // 6):
				print("(" + str(counted) + ") " + devices[count])
				count += 6
				counted += 1
			print("(99) Back")
			try:
				cmd = (int(input('\n\nPlease select a device: ')))
			except:
				menu(save_file, devices)
			if cmd == 99:
				menu(save_file, devices)
			selected_index = int(cmd)
			selected_index = (selected_index * 6)
			saved_dir = (main_directory + '\\computers\\' + (devices[selected_index]))
			del devices[selected_index]
			del devices[selected_index]
			del devices[selected_index]
			del devices[selected_index]
			del devices[selected_index]
			del devices[selected_index]
			with open(('saves//' + save_file), 'w') as f:
				count = 0
				first = True
				for line in devices:
					line_ = str(devices[count])
					if '=' in line_:
						line_ = (' ' + line_)
					else:
						line_ = (line_ + ':')
					if first == True:
						f.write(line_)
					elif first == False:
						f.write('\n' + line_)
					first = False
					count += 1
			f.close()
			menu(save_file, devices)
	elif choice == '99':
		exit()
	else:
		menu(save_file, devices)


def command_line(devices, save_file, selected_index, network, saved_file, main_directory, saved_dir, server, selected_device, ftp, ftp_host):
	with open('servers//main.txt', 'r') as f:
		server_config = f.read().splitlines()
	f.close()
	try:
		with open(('network_saves//' + saved_file), 'r') as f:
			networks = f.read().splitlines()
		f.close()
	except:
		print('Please configure a network first.')
		menu(save_file, devices)
	network = []
	count = 0
	for line in networks: 
		line_ = networks[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			network.append(line_)
		else:
			network.append(line_)
		count += 1
	with open(('saves//' + save_file), 'r') as f:
		save = f.read().splitlines()
	f.close()
	devices = []
	count = 0
	for line in save: 
		line_ = save[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			devices.append(line_)
			if '_' in line_:
				line_ = (line_.replace('_', ''))
		elif line_[0] == ' ':
			line_ = (line_.replace(' ', ''))
			devices.append(line_)
		count += 1
	if server == True:
		selected_device = [(server_config[(selected_index)]), (server_config[(selected_index + 1)]), (server_config[(selected_index + 2)]), (server_config[(selected_index + 3)]), (server_config[(selected_index + 4)]), (server_config[(selected_index + 5)]), (server_config[(selected_index + 6)]), (server_config[(selected_index + 7)]), (server_config[(selected_index + 8)]), (server_config[(selected_index + 9)]), (server_config[(selected_index + 10)])]
		ftp_enabled = (selected_device[6])
		ftp_enabled = ftp_enabled.replace(' ', '')
		ftp_enabled = ftp_enabled.replace('ftp_enabled=', '')
		samba_enabled = (selected_device[7])
		samba_enabled = samba_enabled.replace(' ', '')
		samba_enabled = samba_enabled.replace('samba_enabled=', '')
		dtb_enabled = (selected_device[8])
		dtb_enabled = dtb_enabled.replace(' ', '')
		dtb_enabled = dtb_enabled.replace('dtb_enabled=', '')
		ftp_home = (selected_device[9])
		ftp_home = ftp_home.replace(' ', '')
		ftp_home = ftp_home.replace("'", '', 2)
		ftp_home = ftp_home.replace('ftp_home=', '')
		web_home = (selected_device[10])
		web_home = web_home.replace(' ', '', 2)
		web_home = web_home.replace('web_home=', '')
		web_home = web_home.replace("'", '', 2)
	elif server == False:
		selected_device = [(devices[(selected_index)]), (devices[(selected_index + 1)]), (devices[(selected_index + 2)]), (devices[(selected_index + 3)]), (devices[(selected_index + 4)]), (devices[(selected_index + 5)])]
	host_name = (selected_device[0])
	host_ip = (selected_device[1])
	host_ip = host_ip.replace(' ', '', 2)
	host_ip = host_ip.replace('ip=', '')
	host_ip = host_ip.replace("'", '', 2)
	host_dhcp = (selected_device[2])
	host_dhcp = host_dhcp.replace(' ', '', 2)
	host_dhcp = host_dhcp.replace("dhcp=", '')
	host_os = (selected_device[3])
	host_os = host_os.replace(' ', '', 2)
	host_os = host_os.replace("'", '', 2)
	host_os = host_os.replace("os=", '')
	host_subnet_mask = (selected_device[4])
	host_subnet_mask = host_subnet_mask.replace(' ', '')
	host_subnet_mask = host_subnet_mask.replace("'", '', 2)
	host_subnet_mask = host_subnet_mask.replace('subnet_mask=', '')
	host_network_id = (selected_device[5])
	host_network_id = host_network_id.replace(' ', '')
	host_network_id = host_network_id.replace("'", '', 2)
	host_network_id = host_network_id.replace('network_id=', '')

	# Finding DNS records
	try:
		previous_dir = os.getcwd()
		os.chdir(main_directory + '\\servers')
		with open('dns.txt', 'r') as f:
			dns_records = f.read().splitlines()
		f.close()

		index_count = 0
		dns_completed = {}

		for _ in range(len(dns_records)):
			record = dns_records[index_count]
			record = record.split(":")
			dns_completed.update( {(record[0]) : (record[1])} )
			index_count += 1
	except:
		dns_completed = 'None'
	os.chdir(previous_dir)
	network_id = (network[1])
	network_id = network_id.replace(' ', '', 100)
	network_id = network_id.replace("'", '', 2)
	network_id = network_id.replace("id=", '')

	network_internal_ip = (network[2])
	network_internal_ip = network_internal_ip.replace(' ', '', 100)
	network_internal_ip = network_internal_ip.replace("'", '', 2)
	network_internal_ip = network_internal_ip.replace("ip_internal=", '')

	network_public_ip = (network[3])
	network_public_ip = network_public_ip.replace(' ', '', 100)
	network_public_ip = network_public_ip.replace("'", '', 2)
	network_public_ip = network_public_ip.replace("ip_public=", '')

	network_range = (network[4])
	network_range = network_range.replace(' ', '', 100)
	network_range = network_range.replace("'", '', 2)
	network_range = network_range.replace("ip_range=", '')

	network_subnet_mask = (network[5])
	network_subnet_mask = network_subnet_mask.replace(' ', '', 100)
	network_subnet_mask = network_subnet_mask.replace("'", '', 2)
	network_subnet_mask = network_subnet_mask.replace("subnet_mask=", '')

	network_dhcp_ip_start = (network[6])
	network_dhcp_ip_start = network_dhcp_ip_start.replace(' ', '', 100)
	network_dhcp_ip_start = network_dhcp_ip_start.replace("'", '', 2)
	network_dhcp_ip_start = network_dhcp_ip_start.replace("dhcp_start=", '')

	network_dhcp_ip_stop = (network[7])
	network_dhcp_ip_stop = network_dhcp_ip_stop.replace(' ', '', 100)
	network_dhcp_ip_stop = network_dhcp_ip_stop.replace("'", '', 2)
	network_dhcp_ip_stop = network_dhcp_ip_stop.replace("dhcp_stop=", '')

	network_dhcp = (network[8])
	network_dhcp = network_dhcp.replace(' ', '', 100)
	network_dhcp = network_dhcp.replace("'", '', 2)
	network_dhcp = network_dhcp.replace("dhcp=", '')

	network_ignore = network
	for _ in range(10):
		del network_ignore[0]
	network_devices = {}
	count = 0
	for line in network_ignore:
		line_ = network_ignore[(count)]
		try:
			second_line_ = (network_ignore[(count + 1)])
		except:
			pass
		if line_[0] == ' ':
			line_ = line_.replace(' ', '')
			network_devices.update({(second_line_) : (line_)})
		count += 1
	network_devices.update({(network_internal_ip) : (network_id)})
	network_ips = {}
	count = 0
	for line in network_ignore:
		try:
			line_ = network_ignore[(count)]
			second_line_ = (network_ignore[(count + 1)])
		except:
			pass
		if line_[0] == ' ':
			line_ = line_.replace(' ', '')
			network_ips.update({(line_) : (second_line_)})
		count += 1

	try:
		with open(('network_saves//' + saved_file), 'r') as f:
			networks = f.read().splitlines()
		f.close()
	except:
		print('Please configure a network first.')
		menu(save_file, devices)
	completed_network = []
	count = 0
	for line in networks: 
		line_ = networks[count]
		if ':' in line_:
			line_ = (line_.replace(':', ''))
			completed_network.append(line_)
		else:
			completed_network.append(line_)
		count += 1
	if host_os == 'Linux':
		if ftp == False:
			if server == False:
				if (saved_dir.replace((main_directory + '\\computers\\' + host_name), '')) == '' or (saved_dir.replace((main_directory + '\\computers\\' + host_name), '')) == ' ':
					command_dir = ('/')
				else:
					command_dir = (saved_dir.replace((main_directory + '\\computers\\' + host_name), ''))
					command_dir = command_dir.replace('\\', '/', 2000)
			elif server == True:
				if (saved_dir.replace((main_directory + '\\servers\\' + host_name), '')) == '' or (saved_dir.replace((main_directory + '\\computers\\' + host_name), '')) == ' ':
					command_dir = ('/')
				else:
					command_dir = (saved_dir.replace((main_directory + '\\servers\\' + host_name), ''))
					command_dir = command_dir.replace('\\', '/', 2000)
			command = input('[root@' + host_ip + ' ' + command_dir + ']# ')
		else:
			if saved_dir == ftp:
				command_dir = ('/')
			else:
				command_dir = (saved_dir.replace((ftp), ''))
				command_dir = command_dir.replace('\\', '/', 2000)
			command = input('[root@' + ftp_host + ' ' + command_dir + ']# ')
		if command == "ifconfig":
			print('IP................: ' + host_ip + '\nSubnet Mask.......: ' + host_subnet_mask + '\nNetwork ID........: ' + host_network_id + '\nDHCP Enabled......: ' + host_dhcp)
		elif command == "help":
			print(
				'help:\n'
				'    Will show all commands.\n'
				'ifconfig:\n'
				'    This command shows the IP configuration including:\n'
				'        ip\n'
				'        subnet mask\n'
				'        network id\n'
				'        dhcp status\n'
				'stop:\n'
				'    This command wil stop the command line.\n'
				'set static ip:\n'
				'    This command requires a ip for example:\n'
				'    set static ip 192.168.1.50\n'
				'    This value depends on the ip range of the network you would like to connect the device to. It also automaticly disables dhcp.\n'
				'set static subnet_mask:\n'
				'    This command requires a subnet mask for example:\n'
				'    set static subnet_mask 255.255.255.0\n'
				'    This value depends on the ip range of the network you would like to connect the device to.\n'
				'set dynamic:\n'
				'    This command enables dhcp and if dhcp is already enabled it will re-request an ip and subnet mask.\n'
				'connect eth0:\n'
				'    This command requires a network id for example:\n'
				'    connect eth0 my_network\n'
				'    It will connect ethernet adapter 0 to the network and if dhcp is enabled request an ip.\n'
				'connect wlan0:\n'
				'    This command is coming soon!\n'
				'connect status:\n'
				'    This command will show if the ethernet or wlan adapter is disconnected or connected.\n'
				'ping:\n'
				'    This command requires a ip for example:\n'
				'    ping 192.168.1.4\n'
				'    It will ping the ip 4 times.and display the response time.\n'
				'ping -t:\n'
				'    This command requires a ip for example:\n'
				'    ping 192.168.1.4\n'
				'    It will ping the ip forever sand display the response time.\n'
				'netdiscover:\n'
				'    This command will show all avaidable networks. It takes a random amount of time to discover them.\n'
				'ls:\n'
				'    This command shows all files and directories in the current directory.\n'
				'mkdir:\n'
				'    This command requires a directory name for example:\n'
				'    mkdir mydirectory\n'
				'    It will create a directory with the name you specified at the end.\n'
				'cd:\n'
				'    This command requires a directory name for example:\n'
				'    cd mydirectory\n'
				'    It will open the directory with the name you specified at the end.\n'
				'cd \\:\n'
				'    This command will bring you back to the root directory.\n'
				'cd..:\n'
				'    This command will bring you back one directory.\n'
				'rmdir -f:\n'
				'    This command requires a directory name for example:\n'
				'    rmdir -f mydirectory\n'
				'    This command will forcefully remove the directory with the name you specified at the end.\n'
				'wd:\n'
				'    This command will show the full working directory.\n'
				'service enable:\n'
				'    This command requires a service name for example:\n'
				'    service enable ftp\n'
				'service disable:\n'
				'    This command requires a service name for example:\n'
				'    service disable ftp\n'
				'    It will disable the service you specified at the end.\n'
				'service status:\n'
				'    This command requires a service name for example:\n'
				'    service status ftp\n'
				'    It will show the status of the service you specified at the end.\n'
				'clear:\n'
				'    It will clear the command line.\n'
				)
		elif command == 'stop':
			if ftp == False:
				print('Connection closed on ' + host_ip)
				menu(save_file, devices)
			else:
				os.chdir(ftp)
				with open('ftp.log', 'a') as f:
					log = ('\n' + host_ip + ' disconnected at ' + (time.strftime("%G-%m-%d %H:%M:%S")))
					f.write(log)
				f.close()
				print('Connection closed on ' + host_ip)
				menu(save_file, devices)
		elif command[0:3] == "set":
			if command[4:10] == "static":
				if command[11:13] == "ip":
					if server == True:
						command_stripped = command
						command_stripped = command_stripped.replace(' ', '', 3)
						command_stripped = command_stripped.replace('setstaticip', '')
						try:
							command_stripped = command_stripped.replace('.', '', 3)
							static_ip_value = int(command_stripped)
							validation = True
						except:
							validation = False
							print('Invalid value.')
						if validation == True:
							command = command.replace(' ', '', 3)
							command = command.replace('setstaticip', '')
							index = server_config.index(host_name)
							index = (index + 1)
							del server_config[index]
							server_config.insert((index), (" ip='" + command + "'"))
						if not host_network_id == 'none':
							if server == True:
								index = completed_network.index(' ' + host_name + '_server')
							elif server == False:
								index = completed_network.index(' ' + host_name)
							index = (index + 1)
							del completed_network[index]
							completed_network.insert((index), (command))
					else:
						if host_dhcp == 'true':
							index = devices.index(host_name)
							index = (index + 2)
							del devices[index]
							devices.insert((index), ("dhcp=false"))
						command_stripped = command
						command_stripped = command_stripped.replace(' ', '', 3)
						command_stripped = command_stripped.replace('setstaticip', '')
						try:
							command_stripped = command_stripped.replace('.', '', 3)
							static_ip_value = int(command_stripped)
							validation = True
						except:
							validation = False
							print('Invalid value.')
						if validation == True:
							command = command.replace(' ', '', 3)
							command = command.replace('setstaticip', '')
							index = devices.index(host_name)
							index = (index + 1)
							del devices[index]
							devices.insert((index), ("ip='" + command + "'"))
						if not host_network_id == 'none':
							index = completed_network.index(' ' + host_name)
							index = (index + 1)
							del completed_network[index]
							completed_network.insert((index), (command))
				elif command[11:22] == "subnet_mask":
					if server == False:
						command_stripped = command
						command_stripped = command_stripped.replace(' ', '', 4)
						command_stripped = command_stripped.replace('setstaticsubnet_mask', '')
						try:
							command_stripped = command_stripped.replace('.', '', 3)
							static_subnet_value = int(command_stripped)
							validation = True
						except:
							validation = False
							print('Invalid value.')
						if validation == True:
							command = command.replace(' ', '', 3)
							command = command.replace('setstaticsubnet_mask', '')
							index = devices.index(host_name)
							index = (index + 4)
							del devices[index]
							devices.insert((index), ("subnet_mask='" + command + "'"))
					elif server == True:
						command_stripped = command
						command_stripped = command_stripped.replace(' ', '', 4)
						command_stripped = command_stripped.replace('setstaticsubnet_mask', '')
						try:
							command_stripped = command_stripped.replace('.', '', 3)
							static_subnet_value = int(command_stripped)
							validation = True
						except:
							validation = False
							print('Invalid value.')
						if validation == True:
							command = command.replace(' ', '', 3)
							command = command.replace('setstaticsubnet_mask', '')
							index = server_config.index(host_name)
							index = (index + 4)
							del server_config[index]
							server_config.insert((index), (" subnet_mask='" + command + "'"))
			elif command[4:12] == "dynamic":
				if server == True:
					print('Dynamic IP is not avaidable on servers.')
				else:
					validation = False
					index = devices.index(host_name)
					index = (index + 2)
					del devices[index]
					devices.insert((index), ("dhcp=true"))
					host_dhcp = 'true'
					if host_network_id == 'none':
						pass
					else:
						network_dhcp_ip_start = network_dhcp_ip_start.replace('.', '', 2)
						network_dhcp_ip_stop = network_dhcp_ip_stop.replace('.', '', 2)
						network_dhcp_ip_start = network_dhcp_ip_start.split('.')
						network_dhcp_ip_stop = network_dhcp_ip_stop.split('.')
						network_dhcp_ip_start = network_dhcp_ip_start[1]
						network_dhcp_ip_stop = network_dhcp_ip_stop[1]
						new_ip = (network_range + (str(random.randint(int(network_dhcp_ip_start), int(network_dhcp_ip_stop)))))
						try:
							already_in_list = (network_devices[new_ip])
						except:
							validation = True
						if validation == True:
							index = devices.index(host_name)
							index = (index + 1)
							del devices[index]
							devices.insert((index), ("ip='" + new_ip + "'"))
							index = (index + 3)
							del devices[index]
							devices.insert((index), ("subnet_mask='" + network_subnet_mask + "'"))

							index = completed_network.index(" " + host_name)
							index = (index + 1)
							del completed_network[index]
							completed_network.insert((index), (new_ip))
						elif validation == False:
							print('Unable to complete DHCP request. Please try again or check configurations.')
			else:
				print('Missing arguments. [static] or [dynamic]')
		elif command[0:7] == 'connect':
			if command[8:12] == 'eth0':
				if server == False:
					command = command.replace(' ', '', 3)
					command = command.replace('connecteth0', '')
					# Checking if the network ID is right
					if command == network_id:
						try:
							already_in_list_check = (network_ips[host_name])
						except:
							validation = True
							host_network_id = (command)
					else:
						warning = False
						print('Please specifiy a valid network ID.')
					if host_dhcp == 'true':
						validation = False
						index = devices.index(host_name)
						index = (index + 2)
						del devices[index]
						devices.insert((index), ("dhcp=true"))
						if host_network_id == 'none':
							pass
						else:
							network_dhcp_ip_start = network_dhcp_ip_start.replace('.', '', 2)
							network_dhcp_ip_stop = network_dhcp_ip_stop.replace('.', '', 2)
							network_dhcp_ip_start = network_dhcp_ip_start.split('.')
							network_dhcp_ip_stop = network_dhcp_ip_stop.split('.')
							network_dhcp_ip_start = network_dhcp_ip_start[1]
							network_dhcp_ip_stop = network_dhcp_ip_stop[1]
							new_ip = (network_range + (str(random.randint(int(network_dhcp_ip_start), int(network_dhcp_ip_stop)))))
							try:
								already_in_list = (network_devices[new_ip])
							except:
								validation = True
							if validation == True:
								index = devices.index(host_name)
								index = (index + 1)
								del devices[index]
								devices.insert((index), ("ip='" + new_ip + "'"))

								index = (index + 3)
								del devices[index]
								devices.insert((index), ("subnet_mask='" + network_subnet_mask + "'"))
								host_ip = new_ip
							elif validation == False:
								print('Unable to complete DHCP request. Please try again or check configurations.')
					validation = False
					warning = True
					try:
						already_in_list_check = (network_ips[host_name])
					except:
						validation = True
					if validation == True:
						completed_network.append(' ' + host_name)
						completed_network.append(host_ip)

						# Editing client file
						index = devices.index(host_name)
						index = (index + 5)
						del devices[index]
						devices.insert((index), ("network_id='" + command + "'"))
					else:
						if warning == True:
							print('Please remove the device from the network before re-adding it.')
				elif server == True:
					command = command.replace(' ', '', 3)
					command = command.replace('connecteth0', '')
					if command == network_id:
						try:
							already_in_list_check = (network_ips[host_name])
						except:
							validation = True
							host_network_id = (command)
					else:
						warning = False
						print('Please specifiy a valid network ID.')
					validation = False
					warning = True
					# Checking if the host already exists on the network
					try:
						already_in_list_check = (network_ips[host_name])
					except:
						validation = True
					if validation == True:
						completed_network.append(' ' + host_name + '_server')
						completed_network.append((host_ip.replace(" ", "")))

						# Editing server file
						index = server_config.index(host_name)
						index = (index + 5)
						del server_config[index]
						server_config.insert((index), (" network_id='" + command + "'"))
					else:
						if warning == True:
							print('Please remove the device from the network before re-adding it.')
			elif command[8:13] == 'wlan0':
				if server == True:
					print('This feature is not avaidable for servers.')
				elif server == False:
					print('This feature is coming soon.')
			elif command[8:14] == 'status':
				if host_network_id == 'none':
					print('Network ID: disconnected')
				else:
					print('Network ID: connected')
		elif command[0:4] == 'ping':
			if command[5:7] == '-t':
				ping_count = 0
				command = command.replace(' ', '', 2)
				command = command.replace('ping-t', '')
				destination_ip = (command)
				error = False
				print('PING ' + destination_ip + ' (' + destination_ip + ') 56(84) bytes of data.')
				for _ in range(4000000):
					# Re-reading configuration files
					with open(('network_saves//' + saved_file), 'r') as f:
						networks = f.read().splitlines()
					f.close()
					network = []
					count = 0
					for line in networks: 
						line_ = networks[count]
						if ':' in line_:
							line_ = (line_.replace(':', ''))
							network.append(line_)
						else:
							network.append(line_)
						count += 1
					with open(('saves//' + save_file), 'r') as f:
						save = f.read().splitlines()
					f.close()
					devices = []
					count = 0
					for line in save: 
						line_ = save[count]
						if ':' in line_:
							line_ = (line_.replace(':', ''))
							devices.append(line_)
							if '_' in line_:
								line_ = (line_.replace('_', ''))
						elif line_[0] == ' ':
							line_ = (line_.replace(' ', ''))
							devices.append(line_)
						count += 1
					try:
						destination_host = (network_devices[destination_ip])
					except:
						time.sleep(2)
						print('ping: ' + destination_ip + ': Name or service not known')
						command_line(devices, save_file, selected_index, network, saved_file, main_directory, saved_dir, server, selected_device, ftp, ftp_host)
					devices.append(network_id)
					devices.append("ip='" + network_internal_ip + "'")
					devices.append('dhcp=true')
					devices.append('os=Router OS 1.2.5')
					devices.append("subnet_mask='" + network_subnet_mask + "'")
					devices.append("network_id='" + network_id + "'")
					index = devices.index(destination_host)
					destination_subnet_mask = (devices[(index + 4)])
					destination_subnet_mask = destination_subnet_mask.replace("'", '', 2)
					destination_subnet_mask = destination_subnet_mask.replace("subnet_mask=", '')
					with open(('saves//' + save_file), 'r') as f:
						save = f.read().splitlines()
					f.close()
					devices = []
					count = 0
					for line in save: 
						line_ = save[count]
						if ':' in line_:
							line_ = (line_.replace(':', ''))
							devices.append(line_)
							if '_' in line_:
								line_ = (line_.replace('_', ''))
						elif line_[0] == ' ':
							line_ = (line_.replace(' ', ''))
							devices.append(line_)
						count += 1
					if destination_subnet_mask == host_subnet_mask:
						time.sleep(0.8)
						print("64 bytes from " + destination_ip + ": icmp_seq=" + str(ping_count) + " ttl=64 time=0." + str(random.randint(100,950)) + " ms")
						ping_count += 1
					else:
						error = True
				if error == True:
					print("Please make sure the subnet mask's of both machines are matching.")
			else:
				ping_count = 0
				command = command.replace('ping', '')
				command = command.replace(' ', '', 1)
				destination_ip = (command)
				error = False
				print('PING ' + destination_ip + ' (' + destination_ip + ') 56(84) bytes of data.')
				if host_network_id == 'none':
					print('ping: ' + destination_ip + ': Name or service not known')
				else:
					for _ in range(4):
						# Re-reading configuration files
						with open(('network_saves//' + saved_file), 'r') as f:
							networks = f.read().splitlines()
						f.close()
						network = []
						count = 0
						for line in networks: 
							line_ = networks[count]
							if ':' in line_:
								line_ = (line_.replace(':', ''))
								network.append(line_)
							else:
								network.append(line_)
							count += 1
						with open(('saves//' + save_file), 'r') as f:
							save = f.read().splitlines()
						f.close()
						devices = []
						count = 0
						for line in save: 
							line_ = save[count]
							if ':' in line_:
								line_ = (line_.replace(':', ''))
								devices.append(line_)
								if '_' in line_:
									line_ = (line_.replace('_', ''))
							elif line_[0] == ' ':
								line_ = (line_.replace(' ', ''))
								devices.append(line_)
							count += 1
						try:
							destination_host = (network_devices[destination_ip])
						except:
							print('ping: ' + destination_ip + ': Name or service not known')
							command_line(devices, save_file, selected_index, network, saved_file, main_directory, saved_dir, server, selected_device, ftp, ftp_host)
						if '_server' in destination_host:
							# Adding the router to the visible list
							server_config.append(network_id)
							server_config.append("ip='" + network_internal_ip + "'")
							server_config.append('dhcp=true')
							server_config.append('os=Router OS 1.2.5')
							server_config.append("subnet_mask='" + network_subnet_mask + "'")
							server_config.append("network_id='" + network_id + "'")

							destination_host = destination_host.replace('_server', '')
							index = server_config.index(destination_host)
							destination_subnet_mask = (server_config[(index + 4)])
							destination_subnet_mask = destination_subnet_mask.replace(" ", '')
							destination_subnet_mask = destination_subnet_mask.replace("'", '', 2)
							destination_subnet_mask = destination_subnet_mask.replace("subnet_mask=", '')
						else:
							# Adding the router to the visible list
							devices.append(network_id)
							devices.append("ip='" + network_internal_ip + "'")
							devices.append('dhcp=true')
							devices.append('os=Router OS 1.2.5')
							devices.append("subnet_mask='" + network_subnet_mask + "'")
							devices.append("network_id='" + network_id + "'")

							index = devices.index(destination_host)
							destination_subnet_mask = (devices[(index + 4)])
							destination_subnet_mask = destination_subnet_mask.replace("'", '', 2)
							destination_subnet_mask = destination_subnet_mask.replace("subnet_mask=", '')
							with open(('saves//' + save_file), 'r') as f:
								save = f.read().splitlines()
							f.close()
							devices = []
							count = 0
							for line in save: 
								line_ = save[count]
								if ':' in line_:
									line_ = (line_.replace(':', ''))
									devices.append(line_)
									if '_' in line_:
										line_ = (line_.replace('_', ''))
								elif line_[0] == ' ':
									line_ = (line_.replace(' ', ''))
									devices.append(line_)
								count += 1
						if destination_subnet_mask == host_subnet_mask:
							time.sleep(0.8)
							print("64 bytes from " + destination_ip + ": icmp_seq=" + str(ping_count) + " ttl=64 time=0." + str(random.randint(100,950)) + " ms")
							ping_count += 1
						else:
							error = True
					if error == True:
						print("Please make sure the subnet mask's of both machines are matching.")
		elif command[0:5] == 'clear':
			print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		elif command[0:11] == 'netdiscover':
			print('Discovering networks...')
			discovery_time = random.randint(1, 5)
			time.sleep(discovery_time)
			#discovery_time = random.randint(1, 10)
			#pbar = tqdm(total=100)
			#for i in range(int(int(100) / int(discovery_time))):
				#pbar.update((discovery_time))
				#time.sleep(0.1)
			print('Discovered Networks:\n' + network_id)
		# Directory commands
		elif command[0:2] == 'ls':
			os.chdir(saved_dir)
			cur_dir = os.listdir()
			count = 0
			for line in cur_dir:
				print(cur_dir[count])
				count += 1
		elif command[0:5] == 'mkdir':
			os.chdir(saved_dir)
			command = command.replace(' ', '')
			command = command.replace('mkdir', '')
			try:
				os.mkdir(command)
			except:
				print('Unable to create directory.')
		elif command[0:4] == 'cd /':
			if ftp == False:
				if server == False:
					os.chdir((main_directory + '\\computers\\' + host_name))
				elif server == True:
					os.chdir((main_directory + '\\servers\\' + host_name))
			else:
				os.chdir(ftp)
		elif command[0:2] == 'cd':
			os.chdir(saved_dir)
			command = command.replace(' ', '')
			command = command.replace('cd', '')
			try:
				os.chdir(saved_dir + '\\' + command)
			except FileNotFoundError:
				print('Directory not found.')
		elif command[0:5] == 'rmdir':
			os.chdir(saved_dir)
			if command[6:8] == '-f':
				command = command.replace(' ', '', 2)
				command = command.replace('rmdir', '')
				command = command.replace('-f', '')
				shutil.rmtree((saved_dir + '\\' + command), ignore_errors=True)
		elif command[0:2] == 'rm':
			os.chdir(saved_dir)
			file_name = command.replace(' ', '')
			file_name = file_name.replace('rm', '')
			try:
				os.remove(file_name)
			except:
				print('Unknown error occurred while removing the file.')
		elif command[0:2] == 'wd':
			wd = (saved_dir)
			wd = wd.replace((main_directory + '\\computers\\' + host_name), '')
			wd = wd.replace((main_directory + '\\servers\\' + host_name), '')
			wd = wd.replace('\\', '/', 1000)
			if wd == '' or wd == ' ':
				pass
			else:
				print(wd)
		elif command[0:4] == 'nano':
			os.chdir(saved_dir)
			print("You can start typing the contect of the file. To start a new line please use 'new_'. When you are done press ENTER.\n")
			content = input()
			content = content.replace('new_', '\n', 1000)
			file_name = input('\n\nPlease enter a file name: ')
			try:
				with open((file_name), 'w') as f:
					f.write(content)
				f.close()
			except:
				print('Unknown error occurred while opening the file.')
		elif command[0:3] == 'cat':
			os.chdir(saved_dir)
			file_name = command.replace(" ", "")
			file_name = file_name.replace("cat", "")
			try:
				with open((file_name), 'r') as f:
					content = f.read().splitlines()
				f.close()
				for line in content:
					print(line)
			except:
				print('Unknown error occurred while opening the file.')
		# Server commands
		elif command[0:7] == 'service':
			if server == True:
				if command[8:14] == 'enable':
					command = command.replace('service', '')
					command = command.replace(' ', '', 3)
					command = command.replace('enable', '')
					service = command

					index = int(server_config.index(host_name))
					if service == 'ftp':
						index += 6
						del server_config[index]
						server_config.insert((index), " ftp_enabled=true")
					elif service == 'samba':
						index += 7
						del server_config[index]
						server_config.insert((index), " samba_enabled=true")
					elif service == 'dtb':
						index += 8
						del server_config[index]
						server_config.insert((index), " dtb_enabled=true")
					else:
						print('Service ' + service + '.service not found.')
				elif command[8:15] == 'disable':
					command = command.replace('service', '')
					command = command.replace(' ', '', 3)
					command = command.replace('disable', '')
					service = command

					index = int(server_config.index(host_name))
					if service == 'ftp':
						index += 6
						del server_config[index]
						server_config.insert((index), " ftp_enabled=false")
					elif service == 'samba':
						index += 7
						del server_config[index]
						server_config.insert((index), " samba_enabled=false")
					elif service == 'dtb':
						index += 8
						del server_config[index]
						server_config.insert((index), " dtb_enabled=false")
					else:
						print('Service ' + service + '.service not found.')
				elif command[8:14] == 'status':
					command = command.replace('service', '')
					command = command.replace(' ', '', 3)
					command = command.replace('status', '')
					service = command
					if service == 'samba':
						if samba_enabled == 'true':
							print(service + '.service running.')
						else:
							print(service + '.service stopped.')
					elif service == 'ftp':
						if ftp_enabled == 'true':
							print(service + '.service running.')
						else:
							print(service + '.service stopped.')
					elif service == 'dtb':
						if dtb_enabled == 'true':
							print(service + '.service running.')
						else:
							print(service + '.service stopped.')
					else:
						print('Service ' + service + '.service not found.')
				else:
					print('Missing arguments. [enable], [disable] or [status]')
			elif server == False:
				print('Please connect to a server to use this command.')
		elif command[0:3] == 'ftp':
			if server == True:
				if command[4:7] == 'set':
					if ftp_enabled == 'true':
						if command[8:14] == 'home':
							command = command.replace(' ', '', 10)
							command = command.replace('sethome', '')
							os.chdir(saved_dir)
							ftp_home = (os.getcwd())
							with open('ftp.log', 'w') as f:
								f.write('FTP LOG:\n')
							f.close()
							ftp_home = ftp_home.replace((main_directory), '')
							index = server_config.index(host_name)
							index = (index + 9)
							del server_config[(index)]
							server_config.insert((index), (" ftp_home='" + ftp_home + "'"))
					elif ftp_enabled == 'false':
						print("Please enable the FTP service first by: 'service enable ftp'.")
			elif server == False:
				if command[4:11] == 'connect':
					validation = False
					command = command.replace(' ', '', 10)
					command = command.replace('ftpconnect', '')
					ftp_ip = command
					wait_time = random.randint(1, 2)
					print('Connecting to ' + command + '...')
					time.sleep(wait_time)
					try:
						index = completed_network.index(ftp_ip)
						validation = True
					except:
						validation = False
					if validation == True:
						validation = False
						destination_host = (completed_network[(index - 1)])
						destination_host = destination_host.replace(' ', '')
						destination_host = destination_host.replace('_server', '')
						index = (server_config.index(destination_host))
						index = (index + 6)
						destination_ftp = (server_config[index])
						destination_ftp = destination_ftp.replace(' ', '')
						destination_ftp = destination_ftp.replace('ftp_enabled=', '')
						if destination_ftp == 'true':
							validation = True
							index = (index + 3)
							destination_path = (server_config[index])
							destination_path = destination_path.replace("'", '', 2)
							destination_path = destination_path.replace(' ftp_home=', '')
							if destination_path == 'none':
								validation = False
						elif destination_ftp == 'false':
							validation = False
						if validation == True:
							ftp = (main_directory + destination_path)
							ftp_host = (destination_host)
							os.chdir(ftp)
							# Writing log
							with open('ftp.log', 'a') as f:
								log = ('\n' + host_ip + ' connected at ' + (time.strftime("%G-%m-%d %H:%M:%S")))
								f.write(log)
							f.close()
							wait_time = random.randint(1, 2)
							print('Fetching files...')
							time.sleep(wait_time)
							print('Connection established successfully.')
						elif validation == False:
							time.sleep(5)
							print('Unable to connect to server.')
					elif validation == False:
						time.sleep(5)
						print('Unable to connect to server.')
				elif command[4:14] == 'disconnect':
					if ftp == False:
						print('Cannot disconnect from an FTP server without connecting.')
					else:
						os.chdir(ftp)
						with open('ftp.log', 'a') as f:
							log = ('\n' + host_ip + ' disconnected at ' + (time.strftime("%G-%m-%d %H:%M:%S")))
							f.write(log)
						f.close()
						print('Connection closed on ' + ftp_host + '.')
						ftp = False
						os.chdir((main_directory + '\\computers\\' + host_name))
				elif command[4:7] == 'get':
					if ftp == False:
						print('Please connect to a FTP server to use this command.')
					else:
						file_name = command.replace(' ', '', 3)
						file_name = file_name.replace('ftpget', '')
						try:
							os.chdir(saved_dir)
							with open((file_name), 'r') as f:
								content = f.read().splitlines()
							f.close()
							previous_dir = os.getcwd()
							os.chdir(main_directory + '\\computers\\' + host_name)
							with open((file_name), 'w') as f:
								first = True
								for line in content:
									if first == True:
										f.write(line)
									elif first == False:
										f.write('\n' + line)
									first = False
							f.close()
							os.chdir(previous_dir)
						except:
							print('File not found.')
				else:
					print('Please connect to a server to use this command.')
		elif command[0:3] == 'dns':
			if command[4:10] == 'lookup':
				dns_website = command.replace(' ', '', 20)
				dns_website = dns_website.replace('dnslookup', '')
				try:
					dns_results = dns_completed.get(dns_website)
					print(dns_results)
				except:
					print('None')
			else:
				if server == True:
					if command[4:9] == 'setup':
						if dns_completed == 'None':
							print('Creating database...')
							wait_time = random.randint(2, 4)
							time.sleep(wait_time)
							dns_website = input('Please enter a website address in the following format: google.com: ')
							dns_ip = input('Please enter a IP linked to the website address: ')
							dns_record = (dns_website + ':' + dns_ip)
							os.chdir(main_directory + '\\servers')
							with open('dns.txt', 'w') as f:
								f.write(dns_record)
							f.close()
						else:
							print('DNS already configured.')
					elif command[4:7] == 'add':
						dns_website = input('Please enter a website address in the following format: google.com: ')
						dns_ip = input('Please enter a IP linked to the website address: ')
						dns_record = ('\n' + dns_website + ':' + dns_ip)
						try:
							previous_dir = os.getcwd()
							os.chdir(main_directory + '\\servers')
							with open('dns.txt', 'a') as f:
								f.write(dns_record)
							f.close()
						except:
							print('Unable to add record.')
						os.chdir(previous_dir)
				elif server == False:
					print('Please connect to a server to use this command.')
		elif command[0:3] == 'web':
			if command[4:9] == 'setup':
				if server == True:
					index = server_config.index(host_name)
					index = (index + 10)
					del server_config[index]
					server_config.insert((index), (" web_home='" + (saved_dir.replace((main_directory), '')) + "'"))
			elif command[0:7] == 'website':
				if command[8:14] == 'create':
					if server == True:
						website_name = command.replace(' ', '', 3)
						website_name = website_name.replace('websitecreate', '', 3)
						if website_name == '' or website_name == ' ':
							print('Please specify a domain.')
						else:
							previous_dir = os.getcwd()
							os.chdir(main_directory + web_home)
							os.mkdir(website_name)
							os.chdir(main_directory + web_home + '\\' + website_name)
							website_content = (
									'<!DOCTYPE html>'
									'<html>\n'
									'<head>\n'
									'<title>' + website_name + '</title>\n'
									'<style>\n'
									'h1 { cursor: pointer; opacity: 1; margin-right: 0px; text-align: center; font-family: "Roboto"; margin-top: 25%; font-size: 300%; animation-name: header; animation-duration: 1.5s; }\n'
									'@keyframes header { from {opacity: 0.1; margin-right: 500px; font-size: 250%;} to {opacity: 1; margin-right: 0px; font-size: 300%;} }\n'
									'</style>\n'
									'</head>\n'
									'<body>\n'
									'<h1>Welcome to ' + website_name + '!</h1>\n'
									'</body>\n'
									'</html>\n'
									)
							with open('index.html', 'w') as f:
								f.write(website_content)
							f.close()
							with open('web.log', 'w') as f:
								f.write('WEB LOG:\n')
							f.close()
							os.chdir(previous_dir)
					elif server == False:
						print('Please connect to a server to use this command.')
				else:
					dns_website = command.replace(' ', '', 1000)
					dns_website = dns_website.replace('website', '')
					try:
						dns_results = dns_completed.get(dns_website)
						index = completed_network.index(dns_results)
						index = (index - 1)
						destination_host = (completed_network[index])
						destination_host = destination_host.replace(' ', '', 1)
						destination_host = destination_host.replace('_server', '', 1)
						index = server_config.index(destination_host)
						index = (index + 10)
						website_home = (server_config[index])
						website_home = website_home.replace(' ', '', 1)
						website_home = website_home.replace("web_home=", '')
						website_home = website_home.replace("'", '', 2)
						previous_dir = os.getcwd()
						os.chdir(main_directory + website_home + '\\' + dns_website)
						with open('web.log', 'a') as f:
							log = ('\n' + host_ip + ' connected at ' + (time.strftime("%G-%m-%d %H:%M:%S")))
							f.write(log)
						os.chdir(previous_dir)
						os.startfile(main_directory + website_home + '\\' + dns_website + '\\index.html')
					except:
						print('Website address not found.')
		elif command[0:3] == 'dtb':
			if server == True:
				if command[4:9] == 'setup':
					validation = True
					if dtb_enabled == 'true':
						previous_dir = os.getcwd()
						os.chdir(main_directory + '\\servers')
						dtb_list = os.listdir()
						for line in dtb_list:
							line = line.split(".")
							if line[1] == 'dtb':
								validation = False
						os.chdir(previous_dir)
						if validation == True:
							dtb_name = input('Please enter a name for the database: ')
							dtb_name = dtb_name.replace('.', '', 2000)
							print("Databases have keys and values for example: 'Brand' : 'Ford'. You need the key to get the value.")
							time.sleep(3)
							dtb_key = input("Please specify a key: ")
							dtb_value = input("Please specify a value: ")
							print('Creating databse...')
							wait_time = random.randint(1, 2)
							dtb_entry = (dtb_key + ':' + dtb_value)
							os.chdir(main_directory + '\\servers')
							with open((dtb_name + '.dtb'), 'w') as f:
								f.write(dtb_entry)
							f.close()
							os.chdir(saved_dir)
						elif validation == False:
							print("Database already exists.")
					elif dtb_enabled == 'false':
						print("Please enable the DTB service first by: 'service enable dtb'.")
			elif server == False:
				if command[4:11] == 'connect':
					previous_dir = os.getcwd()
					os.chdir(main_directory + '\\servers')
					validation = False
					dtb_list = os.listdir()
					for line in dtb_list:
						line = line.split(".")
						try:
							if line[1] == 'dtb':
								dtb_name = (line[0])
								validation = True
						except:
							pass
					if validation == True:
						with open((dtb_name + '.dtb'), 'r') as f:
							dtb_readed = f.read().splitlines()
						f.close()
						index_count = 0
						dtb_completed = {}
						for _ in range(len(dtb_readed)):
							dtb_entry = dtb_readed[index_count]
							dtb_entry = dtb_entry.split(":")
							dtb_completed.update( {(dtb_entry[0]) : (dtb_entry[1])} )
							print('key:' + dtb_entry[0])
							print('value:' + dtb_entry[1])
							index_count += 1
						search = input('Enter a key: ')
						try:
							results = dtb_completed.get(search)
							print('Value: ' + results)
						except:
							print('Key not found.')
						os.chdir(previous_dir)
					elif validation == False:
						print('No database found.')
						os.chdir(previous_dir)
		elif command[0:2] == '99':
			exit()
		elif command[0:6] == 'python':
			print('Python scripts are coming soon!')
		else:
			print("bash: " + command + ": command not found... Use the command help for help.")
	elif host_os == 'Windows':
		command = input('C:\\')
	else:
		print('Unknown host OS. Please check configuration.')
		menu(save_file, devices)
	if (os.getcwd()) == main_directory:
		pass
	else:
		saved_dir = (os.getcwd())
	if ftp == False:
		if server == False:
			if (os.getcwd()) == (main_directory + '\\computers'):
				saved_dir = (main_directory + '\\computers\\' + host_name)
		elif server == True:
			if (os.getcwd()) == (main_directory + '\\servers'):
				saved_dir = (main_directory + '\\servers\\' + host_name)
	else:
		if (os.getcwd()) == ftp:
			saved_dir = (ftp)
	os.chdir(main_directory)
	if server == False:
		with open(('saves//' + save_file), 'w') as f:
			count = 0
			first = True
			for line in devices:
				line_ = str(devices[count])
				if '=' in line_:
					line_ = (' ' + line_)
				else:
					line_ = (line_ + ':')
				if first == True:
					f.write(line_)
				elif first == False:
					f.write('\n' + line_)
				first = False
				count += 1
		f.close()
	elif server == True:
		with open(('servers//main.txt'), 'w') as f:
			count = 0
			first = True
			for line in server_config:
				line_ = str(server_config[count])
				if first == True:
					f.write(line_)
				elif first == False:
					f.write('\n' + line_)
				first = False
				count += 1
		f.close()
	# Saving the network configuration
	with open(('network_saves//' + saved_file), 'w') as f:
		count = 0
		first = True
		for line in completed_network:
			line_ = str(completed_network[count])
			if first == True:
				f.write(line_)
			elif first == False:
				f.write('\n' + line_)
			first = False
			count += 1
	f.close()
	command_line(devices, save_file, selected_index, network, saved_file, main_directory, saved_dir, server, selected_device, ftp, ftp_host)


def create_device(device_to_create, save_file):
	print('\n\n\n\n')
	if device_to_create == '1':
		network_name = input('Please enter a name for the network: ')
		network_id = input('\n\nPlease enter a non-existing network id: ')
		network_internal_ip = input('\n\nPlease enter a internal IP for the host: ')
		network_public_ip = input('\n\nPlease enter a external IP for the host: ')
		network_range = input('\n\nPlease enter a network range (example: 192.168.1.): ')
		network_subnet_mask = input('\n\nPlease enter a subnet_mask: ')

		network_dhcp_ip_start = input('\n\nPlease enter a starting IP for the DHCP server: ')
		network_dhcp_ip_stop = input('\n\nPlease enter a ending IP for the DHCP server: ')
		network_dhcp = input('\n\nPlease enter a DHCP state (false or true): ')

		network_name = network_name.replace(' ', '_', 100)
		network_id = (" id='" + network_id + "'")
		network_internal_ip = (" ip_internal='" + network_internal_ip + "'")
		network_public_ip = (" ip_public='" + network_public_ip + "'")
		network_range = (" ip_range='" + network_range + "'")
		if (len(network_range.split('.'))) < 4:
			network_range = (network_range + '.')
		network_subnet_mask = (" subnet_mask='" + network_subnet_mask + "'")

		network_dhcp_ip_start = (" dhcp_start='" + network_dhcp_ip_start + "'")
		network_dhcp_ip_stop = (" dhcp_stop='" + network_dhcp_ip_stop + "'")
		network_dhcp = (" dhcp=" + network_dhcp)
		print('Configuration in progress...')
		time.sleep(0.8)
		with open(('network_saves//' + network_name + '.txt'), 'w') as f:
			f.write((network_name + ':\n' + network_id + '\n' + network_internal_ip + '\n' + network_public_ip + '\n' + network_range + '\n' + network_subnet_mask + '\n' + network_dhcp_ip_start + '\n' + network_dhcp_ip_stop + '\n' + network_dhcp + '\n connected_devices:'))
		f.close()
		input('Network configuration completed. As this is your first network your program has to be restarted. Press ENTER to continue.')
		exit()
		if saved_file == False:
			exit()
	elif device_to_create == '2':
		with open(('saves//' + save_file), 'r') as f:
			save = f.read().splitlines()
		f.close()
		device_name = input('Please enter a device name: ')
		for line in save:
			line = line.replace(" ", "")
			if line == device_name:
				print('There already is a device with this name. Please try again.')
				menu(save_file, devices)
		print('\n\n(1) Windows (Coming Soon!)\n(2) Linux\n\n')
		device_os = input('Please choose a OS: ')
		if device_os == '1':
			device_os = 'Windows'
		elif device_os == '2':
			device_os = 'Linux'
		else:
			menu(save_file, devices)
		print('Configuration in progress...')
		time.sleep(0.3)
		device_name = device_name.replace(' ', '_', 100)
		devices.append(device_name)
		devices.append("ip='0.0.0.0'")
		devices.append("dhcp=false")
		devices.append('os=' + device_os)
		devices.append("subnet_mask='0.0.0.0'")
		devices.append("network_id='none'")
		with open(('saves//' + save_file), 'w') as f:
			count = 0
			first = True
			for line in devices:
				line_ = str(devices[count])
				if '=' in line_:
					line_ = (' ' + line_)
				else:
					line_ = (line_ + ':')
				if first == True:
					f.write(line_)
				elif first == False:
					f.write('\n' + line_)
				first = False
				count += 1
		f.close()
		os.chdir(main_directory + '\\computers')
		os.mkdir(device_name)
		input('Device configuration completed. Press ENTER to continue.')
	elif device_to_create == '3':
		with open('servers//main.txt', 'r') as f:
			server_config = f.read().splitlines()
		f.close()
		device_name = input('Please enter a device name: ')
		if device_name == 'server':
			input("The server name cannot include 'server'. Please re-create the server. Press ENTER to continue.")
			menu(save_file, devices)
		device_name = device_name.replace('server', '')
		print('\n\n(1) Windows (Coming Soon!)\n(2) Linux\n\n')
		device_os = input('Please choose a OS: ')
		if device_os == '1':
			device_os = 'Windows'
		elif device_os == '2':
			device_os = 'Linux'
		else:
			menu(save_file, devices)
		#device_ip = (input("\n\nPlease enter a static IP: "))
		#device_subnet_mask = (input("\n\nPlease enter a static subnet mask: "))
		#device_network_id = (input("\n\nPlease enter a network id: "))
		print('Configuration in progress...')
		time.sleep(0.3)
		device_name = device_name.replace(' ', '_', 100)
		server_config.append(device_name)
		#server_config.append(" ip='" + device_ip + "'")
		#server_config.append(" subnet_mask='" + device_subnet_mask + "'")
		#server_config.append(" network_id='" + device_network_id + "'")
		server_config.append(" ip='0.0.0.0'")
		server_config.append(" dhcp=false")
		server_config.append(' os=' + device_os)
		server_config.append(" subnet_mask='0.0.0.0'")
		server_config.append(" network_id='none'")
		server_config.append(" ftp_enabled=false")
		server_config.append(" samba_enabled=false")
		server_config.append(" dtb_enabled=false")
		server_config.append(" ftp_home='none'")
		server_config.append(" web_home='none'")
		with open(('servers//main.txt'), 'w') as f:
			count = 0
			first = True
			for line in server_config:
				line_ = str(server_config[count])
				if first == True:
					f.write(line_)
				elif first == False:
					f.write('\n' + line_)
				first = False
				count += 1
		f.close()
		os.chdir(main_directory + '\\servers')
		os.mkdir(device_name)
		input('Server configuration completed. Press ENTER to continue.')
	print('WARNING! After creating a new device it is always recommended to restart your program.')
	time.sleep(3)
	menu(save_file, devices)


def update_checker():
	print('Checking for updates...')
	with open('configurations//ver.txt', 'r') as f:
		cur_ver = (int(f.read()))
	f.close()
	files = os.listdir()
	amount_of_netgames = 0
	for line in files:
		if 'NetGame ' in line:
			line = line.replace("NetGame ", "")
			amount_of_netgames += 1
	if amount_of_netgames > 1:
		print('We detected multiple installations. Please remove the oldest one.')
		time.sleep(60)
		exit()
	data = urllib.request.urlopen('https://yoursystem.be/updates/version_checker.txt')
	for line in data:
		version = (str(line))
	version = version.replace("'", "", 2)
	version = version.replace("b", "", 1)
	version = version.replace("\\n", "")
	version = version.replace(",", "\n", 1000)
	version = version.splitlines()
	server_version = (int(version[0]))
	new_url = (version[1])
	#print(version)
	#print('Current version: ' + str(cur_ver))
	#print('Server version: ' + str(server_version))
	#print('New version link: ' + str(new_url))
	if server_version > cur_ver:
		print('Installing new update...')
		file_name = new_url
		urllib.request.urlretrieve (str(new_url), (file_name.replace("https://yoursystem.be/downloads/", "")))
		print("The program has been updated. This file will be unusable please delete this file and use the newest version.")
		time.sleep(60)
		exit()
	elif server_version == cur_ver:
		print('You have the latest version. (V ' + str(cur_ver) + ')')
	else:
		print('Unexpected error while checking for updates.')


update_checker()
menu(save_file, devices)