<html>
  <head>
    <style>
      .watermark {
        position: fixed;
        bottom: 10%;
        right: 10%;
        font-size: 3em;
        color: rgba(0, 0, 0, 0.1);
        transform: rotate(-45deg);
        z-index: 9999;
        pointer-events: none;
        opacity: 0.5;
        user-select: none;
      }
    </style>
  </head>
  <body>
    <div class="watermark">https://github.com/shreyuu</div>
  </body>
</html>


# Cyber Security and Digital Forensics

### Experiment 1: Tracking Emails and Investigating Email Crimes

**1.	Why Analyze Email Header?**

ans:- Analyzing email headers is crucial for tracing the origin and path of an email, understanding the servers it passed through, and verifying the authenticity of the sender. It helps in detecting email spoofing and investigating email-based crimes.

**2.	What Fields are Analyzed During Email Header Analysis?**

ans:- Fields like From, To, Received, Subject, Date, and Message-ID are essential. These fields help in tracking the sender’s IP address, the servers involved in transmitting the email, and identifying tampering or malicious content.

**3.	Which Readymade Tools are Available for Analyzing Email Headers?**

ans:- Tools like MXToolbox, WhatIsMyIP Email Header Analyzer, and Email Tracker Pro are popular for analyzing headers. These tools provide detailed insights into the path an email has taken and help in identifying potential red flags.

**4.	Explain Email Architecture in Detail.**

ans:- Email architecture consists of Mail User Agents (MUA), Mail Transfer Agents (MTA), and protocols like SMTP for sending and IMAP/POP3 for receiving. The MTA is responsible for transferring emails between servers, while MUAs allow users to compose, send, and read emails.

**5.	What is POP3, IMAP, SMTP, and MIME?**

ans:- 	•	POP3: A protocol that downloads emails from the server and deletes them after retrieval, making emails accessible offline.
	•	IMAP: Syncs emails with the server, allowing access from multiple devices and maintaining server copies.
	•	SMTP: A protocol for sending emails, handling mail transfer between servers.
	•	MIME: Extends email capabilities, enabling the transmission of attachments like images, audio, and video.




### Experiment 2: CAPTCHA Image Generation and Verification

**1.	Full Form of CAPTCHA**

ans:- CAPTCHA stands for “Completely Automated Public Turing test to tell Computers and Humans Apart”. It is a security measure used to distinguish between human and automated bot interactions.

**2.	Different Forms of CAPTCHA**

ans:- Common types include text-based CAPTCHA, image-based CAPTCHA, audio CAPTCHA for visually impaired users, and reCAPTCHA, which often involves selecting images or solving simple puzzles to verify humanity.

**3.	Why CAPTCHA is Needed?**

ans:- CAPTCHA is essential for preventing automated bots from abusing services like account creation, login attempts, and data scraping. It helps protect websites from spam and cyberattacks by requiring human verification.

**4.	Uses of Different CAPTCHAs as per Requirement**

ans:- 	
	•	**Text-based CAPTCHAs** are used in login and sign-up forms for basic security.
	•	**Image-based CAPTCHAs** are effective for complex spam prevention on comment forms.
	•	**Audio CAPTCHAs** help users who are visually impaired access secure areas.

## Program
### 1. **Captcha Number.py**
This script is a simple text-based CAPTCHA system. It generates a 4-digit random number and asks the user to input that number as part of the login verification.

#### **Explanation:**
```python
import random

# Asking for the username and password
username = input("Enter Username: ")
pwd = input("Enter Password: ")

# Check if the username and password are correct
if username == 'test' and pwd == '1234':
    # Generate a 4-digit random number
    num = random.randint(1000, 9999)
    print("Enter this 4 digit number:", num)
    
    # Ask the user to input the 4-digit number
    user_num = int(input())
    
    # Check if the entered number matches the generated number
    if num == user_num:
        print("Login Successfully")
    else:
        print("Login Failed")
else:
    print("Login Failed")
```

#### **What it does:**
- **Username & Password Input:** It prompts the user to enter a username and password.
- **Login Authentication:** It checks if the username is `'test'` and the password is `'1234'`. If both are correct, it proceeds to the next step.
- **Captcha Generation:** If the credentials are correct, it generates a random 4-digit number.
- **User Input for Captcha:** The user is prompted to input the exact number that was generated.
- **Login Success or Failure:** If the user's input matches the generated number, the login is successful. If not, or if the username/password are incorrect, the login fails.

### 2. **Captcha.py**
This script generates an image-based CAPTCHA using the `captcha` Python library. It creates an image with a predefined CAPTCHA text (`'snjb'`), and saves that image as `abc.png`.

#### **Explanation:**
```python
from captcha.image import ImageCaptcha

# Initialize the ImageCaptcha generator with specific width and height for the CAPTCHA image
image_info = ImageCaptcha(width=250, height=100)

# Set the text that will be used in the CAPTCHA
captcha_text = 'snjb'

# Generate the CAPTCHA image
source = image_info.generate(captcha_text)

# Save the generated image as 'abc.png'
image_info.write(captcha_text, 'abc.png')
```

#### **What it does:**
- **Captcha Image Generation:** It uses the `ImageCaptcha` class from the `captcha` library to generate an image of the CAPTCHA text ('snjb').
- **Saving the Image:** The generated image is saved as `abc.png` in the current directory.

This file doesn't take any user input or handle authentication. It just creates the CAPTCHA image for later use.

### 3. **Generate_verify_image_captcha.py**
This program creates a graphical user interface (GUI) using the `tkinter` library to simulate a login form that includes both a **username/password** and **image CAPTCHA** verification. The program checks if the user enters the correct credentials and matches the CAPTCHA text ('snjb').

#### **Explanation:**
```python
from tkinter import *
from captcha.image import ImageCaptcha
from tkinter import messagebox

# Function to handle the login process
def addNumbers():
    # Get user input for username, password, and CAPTCHA text
    a = u.get()  # Username
    b = p.get()  # Password
    ca = c.get()  # Captcha input
    
    # Generate CAPTCHA image and save it
    image_info = ImageCaptcha(width=250, height=100)
    captcha_text = 'snjb'
    source = image_info.generate(captcha_text)
    image_info.write(captcha_text, 'abc.png')
    
    # Check if the username and password are correct
    if a == 'test' and b == '1234':
        # Check if the CAPTCHA entered by the user matches the generated text
        if ca == captcha_text:
            messagebox.showinfo("showinfo", "Login successfully")  # Successful login
        else:
            messagebox.showinfo("showinfo", "Login Failed")  # Incorrect CAPTCHA
    else:
        messagebox.showinfo("showinfo", "Login Failed")  # Incorrect username/password

# Create the main window for the GUI
root = Tk()

# Create a canvas to display the CAPTCHA image
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# Load and display the generated CAPTCHA image
img = PhotoImage(file="abc.png")
canvas.create_image(20, 20, anchor=NW, image=img)

# Create Labels and Entry widgets for username, password, and CAPTCHA input
l1 = Label(root, text="Username")
l1.config(font=("Courier", 14))
u = Entry(root)

l2 = Label(root, text="Password")
l2.config(font=("Courier", 14))
p = Entry(root)

l3 = Label(root, text="Captcha")
l3.config(font=("Courier", 14))
c = Entry(root)

# Create a button to trigger the login process
b2 = Button(root, text="Login", command=addNumbers)

# Pack all widgets into the window
l1.pack()
u.pack()
l2.pack()
p.pack()
l3.pack()
c.pack()
b2.pack()

# Start the main loop to display the window
mainloop()
```

#### **What it does:**
- **Tkinter GUI:** It creates a simple GUI window where the user can input a username, password, and CAPTCHA text.
  - The **Canvas widget** is used to display the CAPTCHA image (`abc.png`).
  - There are **Labels** for `username`, `password`, and `captcha`.
  - The **Entry widgets** are used to take user input for each field.
  - A **Button** is used to trigger the login process when clicked.
  
- **Captcha Image Display:** The CAPTCHA image (`abc.png`) generated by `Captcha.py` is displayed on the GUI window.
  
- **Login Validation:**
  - If the username is `'test'` and the password is `'1234'`, it checks if the entered CAPTCHA text matches the pre-defined text (`'snjb'`).
  - If the username/password are correct and the CAPTCHA is correct, a success message is displayed.
  - If either the username/password or CAPTCHA is incorrect, a failure message is displayed.

#### **How It Works Together:**
- **Captcha Number.py** handles a simple 4-digit number-based CAPTCHA login.
- **Captcha.py** generates an image-based CAPTCHA with the text `'snjb'` and saves it as `abc.png`.
- **Generate_verify_image_captcha.py** creates a GUI where the user can enter the CAPTCHA (image), username, and password to verify if the login is successful or not.

### Flow of the System:
1. **Captcha.py** creates a CAPTCHA image.
2. **Generate_verify_image_captcha.py** displays the CAPTCHA image and asks the user to input the CAPTCHA text, username, and password.
3. **Captcha Number.py** could be an alternative approach (but isn't directly connected in this flow).

### Summary:
- This system simulates a basic login mechanism with two methods of CAPTCHA verification:
  1. A **numeric CAPTCHA** in `Captcha Number.py` that asks the user to input a randomly generated number.
  2. A **graphical CAPTCHA** in `Generate_verify_image_captcha.py` that asks the user to type a CAPTCHA string displayed as an image.
  
- Both methods ensure that the user is human by requiring additional verification beyond just the username and password.

## Experiment 3: Recovering Deleted Files and Partitions

**1.	Path of Trash Folder in Ubuntu**

ans:- The path is /home/user/.local/share/Trash/files for storing deleted files and /home/user/.local/share/Trash/info for the metadata. These directories are critical for data recovery operations in Linux.

**2.	How to See Hidden Files in Ubuntu?**

ans:- Use the command ls -a in the terminal to list all files, including hidden ones. Alternatively, pressing Ctrl + H in the file manager displays hidden files and folders.

**3.	Different File Systems in Ubuntu and Main Directories**

ans:- Common file systems include ext4, xfs, and btrfs. Key directories are /home for user data, /var for logs and variable data, /etc for configuration files, and /usr for installed software and libraries.

**4.	Options of ls Command for File Listing**

ans:- The ls command offers several options: -l for a detailed listing with permissions, -a to show hidden files, and -h to display sizes in a human-readable format. These options are useful for managing files effectively.

## Program
```python
import os
import re

# Define the paths for the trash files and info directory
path = "/home/lenovo/.local/share/Trash/files"
infopath = "/home/lenovo/.local/share/Trash/info"

# List of files in the Trash folder
dirlist = os.listdir(path)
directory = []  # List to hold the filenames
popis = ""

# Iterate through the files in the Trash
for fname in dirlist:
    directory.append(fname)
    popis = popis + " " + fname  # Build a string of file names for display

# Print the list of files
print(popis)

# Ask the user to enter the file name to recover
fname = raw_input("\nEnter the file name which you want to recover: ")

# Open the corresponding .trashinfo file for the selected file
a = open(infopath + "/" + fname + ".trashinfo", "r")
print(a)

# Read the trashinfo file to get the original path of the file
for line in a:
    if "Path=" in line:  # Look for the line containing the original path of the file
        ab = re.findall(r'/.*', line)  # Extract the path using regex
        print(ab)

# Clean up the extracted path (remove extra characters)
destipath = str(ab)
destipath = destipath.lstrip('[')  # Remove the starting '[' character
destipath = destipath.rstrip(']')  # Remove the ending ']' character
destipath = destipath[:-1]  # Remove the last character (newline or other)
destipath = destipath[1:]  # Remove the first character (extra space)

print("Destination path is: " + destipath)

# Open the file in the Trash folder
file1 = open(path + "/" + fname, "r")
print(file1)

# Open the destination file where the recovered file will be stored
file2 = open(destipath, "w")
print(file2)

# Write the contents of the file from Trash to the destination
file2.write(file1.read())
file1.close()
file2.close()

print("File is recovered to destination")

# Remove the file from the Trash folder
os.remove(path + "/" + fname)
print("Removed from Trash: " + path + "/" + fname)

# Remove the corresponding .trashinfo file from the Trash info folder
os.remove(infopath + "/" + fname + ".trashinfo")
print("Removed from Trash info: " + infopath + "/" + fname + ".trashinfo")
```

---

### **Explanation of the Code:**

This program is used to recover a file from the **Trash** on a Linux system, specifically the files and associated metadata stored in `~/.local/share/Trash/`. It takes the file name from the user, retrieves its original path, copies it to the original location, and then deletes the file from the Trash.

Let's break it down step by step:

#### **1. Importing Modules:**
```python
import os
import re
```
- **os**: This module provides functions to interact with the operating system. It's used to navigate directories, remove files, etc.
- **re**: This module is used for regular expression (regex) matching. In this case, it extracts the original file path from the `.trashinfo` file.

#### **2. Defining Paths:**
```python
path = "/home/lenovo/.local/share/Trash/files"
infopath = "/home/lenovo/.local/share/Trash/info"
```
- **path**: This is the directory where the files in the Trash are stored (`~/.local/share/Trash/files`).
- **infopath**: This is the directory where the metadata (in `.trashinfo` files) for each trashed file is stored (`~/.local/share/Trash/info`).

#### **3. Listing Files in the Trash:**
```python
dirlist = os.listdir(path)
directory = []  # List to hold the filenames
popis = ""

for fname in dirlist:
    directory.append(fname)
    popis = popis + " " + fname  # Build a string of file names for display
```
- **os.listdir(path)** lists all the files in the Trash (`~/.local/share/Trash/files`).
- The program appends each file name to the `directory` list and builds a string `popis` to display all the file names.

#### **4. Asking the User for Input:**
```python
print(popis)
fname = raw_input("\nEnter the file name which you want to recover: ")
```
- The program prints the list of files in the Trash (`popis`) and prompts the user to enter the name of the file they want to recover.

#### **5. Opening the `.trashinfo` File:**
```python
a = open(infopath + "/" + fname + ".trashinfo", "r")
print(a)
```
- The program opens the `.trashinfo` file corresponding to the selected file from the Trash. This file contains metadata about the file, such as its original location before it was moved to Trash.

#### **6. Extracting the Original Path:**
```python
for line in a:
    if "Path=" in line:
        ab = re.findall(r'/.*', line)
        print(ab)
```
- The program loops through the `.trashinfo` file and looks for a line containing `Path=`.
- It uses **regex** (`re.findall(r'/.*', line)`) to extract the original path of the file. The regex `r'/.*'` matches anything starting with `/`, which should be the full path of the file.

#### **7. Cleaning Up the Extracted Path:**
```python
destipath = str(ab)
destipath = destipath.lstrip('[')
destipath = destipath.rstrip(']')
destipath = destipath[:-1]
destipath = destipath[1:]
```
- The regex returns a list, and the program converts it to a string and removes any extra characters like `[` and `]` that might appear due to the list format.
- The `[:-1]` and `[1:]` operations are used to clean up the first and last unwanted characters.

#### **8. Opening Files for Recovery:**
```python
file1 = open(path + "/" + fname, "r")
file2 = open(destipath, "w")
```
- **file1**: The program opens the trashed file from `path` (the Trash directory).
- **file2**: The program opens the destination file (`destipath`), where the file will be recovered (restored).

#### **9. Writing the File Back:**
```python
file2.write(file1.read())
file1.close()
file2.close()
```
- It reads the content from the trashed file (`file1.read()`) and writes it to the destination file (`file2.write()`).
- Both files are then closed using `file1.close()` and `file2.close()`.

#### **10. Removing the File from the Trash:**
```python
os.remove(path + "/" + fname)
print("Removed from Trash: " + path + "/" + fname)

os.remove(infopath + "/" + fname + ".trashinfo")
print("Removed from Trash info: " + infopath + "/" + fname + ".trashinfo")
```
- After the file is successfully recovered, it removes the file from the Trash directory (`path`) and deletes the corresponding `.trashinfo` file (`infopath`).
- The program prints messages indicating that the files have been removed from both the Trash and the Trash info folder.

---

### **Summary of the Program:**
1. The program lists all the files in the Trash.
2. It prompts the user to select a file to recover by entering its name.
3. It retrieves the original location of the file (before it was deleted) by reading the `.trashinfo` file associated with it.
4. It copies the file back to its original location.
5. It then deletes the file from the Trash and the associated `.trashinfo` file.

The program effectively helps restore files from the Linux Trash and places them back in their original locations.

## Experiment 4: Log Capturing and Event Correlation

**1.	Why Configure Proxy Server?**

ans:- Configuring a proxy server helps control and monitor internet usage, enhance network security, and improve bandwidth utilization. It acts as a barrier between internal networks and external threats from the internet.

**2.	What is SARG?**

ans:- SARG (Squid Analysis Report Generator) is a tool that creates detailed reports from Squid proxy logs. It helps administrators analyze web usage, monitor employee activity, and manage bandwidth consumption effectively.

**3.	Parameters in SARG Report**

ans:- The SARG report includes information such as IP addresses, top visited sites, data transferred, time spent on each site, and access patterns. These parameters help in understanding user behavior and managing network resources.

**4.	Log and Event Correlation Meaning**

ans:- Log and event correlation refers to linking and analyzing logs from multiple sources to detect security incidents or suspicious activities. It provides a comprehensive view of network events, helping to identify patterns and anomalies.

## Program
 SquidGuard installation and configuration steps

```bash
# Update the package list
sudo apt update

# Install Squid proxy server
sudo apt -y install squid

# Start the Squid service
sudo systemctl start squid

# Enable Squid to start on boot
sudo systemctl enable squid

# Check the status of Squid
sudo systemctl status squid

# Install Apache utilities (needed for htpasswd to create a password file)
sudo apt install apache2-utils

# Create an empty password file for Squid authentication
sudo touch /etc/squid/passwd

# Change ownership of the password file to the 'proxy' user
sudo chown proxy: /etc/squid/passwd

# List the details of the password file
ls -l /etc/squid/passwd

# Create a password for a user (e.g., 'tecmint') in the password file
sudo htpasswd /etc/squid/passwd tecmint

# Open the Squid configuration file in vim
sudo vim /etc/squid/squid.conf

# Search for the 'auth_param' lines and replace them with the following:
# (These settings enable basic authentication for the Squid proxy)
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Squid Basic Authentication
auth_param basic credentialsttl 2 hours

# Define an ACL (Access Control List) for authenticated users
acl auth_users proxy_auth REQUIRED

# Allow authenticated users access to the proxy
http_access allow auth_users

# Search for the 'localnet' line and replace it with the following:
# (This sets up the proxy to allow access from specific local IPs)
acl localnet src 10.1.100.222

# Restart Squid to apply the changes
sudo systemctl restart squid

# Set browser proxy settings to the Squid server (10.1.100.222, port 3128)

# View Squid's access logs to monitor traffic
sudo cat /var/log/squid/access.log

# Squid configuration file location
# Squid configuration file: /etc/squid/squid.conf

# Squid access log location
# Squid Access log: /var/log/squid/access.log

# Squid cache log location
# Squid Cache log: /var/log/squid/cache.log
```

### Explanation of the Steps:

1. **Update the Package List**:  
   - `sudo apt update`: This command updates the local package list to ensure you're installing the latest versions of the software.

2. **Install Squid**:  
   - `sudo apt -y install squid`: Installs the Squid proxy server. The `-y` flag automatically answers "yes" to any prompts, making the installation non-interactive.

3. **Start and Enable Squid**:  
   - `sudo systemctl start squid`: Starts the Squid service immediately.
   - `sudo systemctl enable squid`: Ensures Squid starts automatically on boot.
   - `sudo systemctl status squid`: Checks and displays the status of the Squid service.

4. **Install Apache Utilities**:  
   - `sudo apt install apache2-utils`: Installs Apache utilities like `htpasswd` that are used to manage authentication files.

5. **Create the Password File**:  
   - `sudo touch /etc/squid/passwd`: Creates an empty file where Squid will store user credentials.
   - `sudo chown proxy: /etc/squid/passwd`: Changes the ownership of the password file to the `proxy` user, ensuring Squid has the appropriate permissions to access it.

6. **Create a User and Set Password**:  
   - `sudo htpasswd /etc/squid/passwd tecmint`: Creates a user (`tecmint`) and prompts for a password. This command adds the username and hashed password to the `/etc/squid/passwd` file.

7. **Configure Squid for Authentication**:  
   - `sudo vim /etc/squid/squid.conf`: Opens the Squid configuration file (`squid.conf`) for editing.
   - `auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd`: Specifies that Squid should use basic authentication and the location of the password file.
   - `auth_param basic children 5`: Configures the number of authentication processes Squid should spawn (set to 5).
   - `auth_param basic realm Squid Basic Authentication`: Defines the realm, which is used when displaying the login prompt.
   - `auth_param basic credentialsttl 2 hours`: Sets the time period for which credentials are cached (2 hours in this case).

8. **Set Access Rules**:
   - `acl auth_users proxy_auth REQUIRED`: Defines an Access Control List (ACL) for users who must authenticate.
   - `http_access allow auth_users`: Allows access to Squid for users who authenticate.

9. **Configure Local Network Access**:  
   - `acl localnet src 10.1.100.222`: Allows access from a specific IP address (`10.1.100.222`). You can add more IPs or subnets as needed.

10. **Restart Squid**:  
    - `sudo systemctl restart squid`: Restarts Squid to apply the new configuration.

11. **Browser Settings**:  
    - Set the browser’s proxy settings to `10.1.100.222` (the Squid server IP) and port `3128` (the default Squid proxy port).

12. **Monitor Logs**:  
    - `sudo cat /var/log/squid/access.log`: Displays the Squid access log, where you can see the incoming requests and other details about Squid's activity.
    - The other log paths are for additional Squid logs, including cache and error logs.

This setup configures Squid to require basic HTTP authentication for users, allows access from a specific local network, and logs all access attempts for monitoring.

## Experiment 5: Honeypot Implementation

**1.	What is a Honeypot?**

ans:- A honeypot is a decoy system designed to lure cyber attackers and log their activities. It appears as a legitimate system but is used to study attack methods and improve security measures.

**2.	Types of Honeypots**

ans:- 	•	Production Honeypots: Simple to deploy, capture limited data, and are used by companies to enhance security.
	•	Research Honeypots: Complex systems that gather extensive data, used by researchers to study cyber threats and attacker behavior.

**3.	What is Malware Honeypot?**

ans:- A malware honeypot is set up to attract and analyze malware attacks. It helps researchers understand how malware operates and develop defensive strategies.

**4.	What is Database Honeypot?**

ans:- A database honeypot simulates a database system to lure attackers who exploit database vulnerabilities. It captures attack details for analysis and helps in strengthening database security.

**5.	What is Honey Nets?**

ans:- Honey nets are networks of multiple honeypots used to monitor extensive attack patterns and gather comprehensive data. They simulate a complete network environment to attract sophisticated attackers.

**6.	Goals Behind Setting Up a Honeypot**

ans:- The two main goals are to detect unauthorized access attempts and learn about new attack methods. Honeypots also help in assessing the effectiveness of existing security measures.

## Program
```python
import socket
import atexit

# Local IP/Port for the honeypot to listen on (TCP)
LHOST = '0.0.0.0'
LPORT = 23

# Remote IP/Port to send the log data to (TCP)
RHOST = '192.168.1.210'
RPORT = 9000

# Banner displayed when connecting to the honeypot
BANNER = b'Ubuntu 14.04 LTS\nlogin:\n username: '

# Socket timeout in seconds
TIMEOUT = 10

def main():
    print(f'[*] Honeypot starting on {LHOST}:{LPORT}')
    atexit.register(exit_handler)
    
    # Create and configure the listener socket
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((LHOST, LPORT))
    listener.listen(5)

    while True:
        insock, address = listener.accept()
        insock.settimeout(TIMEOUT)
        
        print(f'[*] Honeypot connection from {address[0]}:{address[1]} on port {LPORT}')
        
        try:
            # Send banner to the connecting client
            insock.send(BANNER)

            data = []
            user = ""
            password = ""
            
            # Receive username
            while True:
                user1 = insock.recv(1024)
                user += str(user1, "utf8")
                if str(user1, "utf8") == "\\":
                    break

            # Ask for password
            insock.send(b'\npassword: ')
            
            # Receive password
            while True:
                password1 = insock.recv(1024)
                password += str(password1, "utf8")
                if str(password1, "utf8") == "\\":
                    break

            # Alert and send the log data to the client
            string = f'\nAlert!!! Your action has been reported {user} | {password}'
            msg = bytes(string, 'utf-8')
            insock.send(msg)

            # Print captured username and password
            print(f"Username: {user} \nPassword: {password}")

        except socket.error as e:
            sendLog(address[0], f'Error: {str(e)}')
        else:
            sendLog(address[0], data)
        finally:
            insock.close()

def sendLog(fromip, message):
    """Send log data to a remote server."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    s.send(f'IP:{fromip} Port:{LPORT} | {message.replace("\r\n", " ")}')
    s.close()

def exit_handler():
    """Handles exit events (clean-up)."""
    print('\n[*] Honeypot is shutting down!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
```

### Explanation of the Code:

1. **Imports and Constants**:
   - The script imports `socket` for network communication and `atexit` to handle clean-up when the script exits.
   - `LHOST` is set to `'0.0.0.0'`, meaning it will listen on all available network interfaces on the machine. `LPORT` is set to `23`, the default port for Telnet.
   - `RHOST` and `RPORT` represent the IP and port where the log data will be sent. This is typically another machine or server you want to log the honeypot activity to.

2. **Main Function**:
   - The `main` function starts by printing a message indicating that the honeypot is starting and binds a TCP socket (`listener`) to the local host and port (`LHOST` and `LPORT`).
   - The honeypot listens for incoming connections (`listener.listen(5)`).
   - When a connection is received, it prints details about the incoming connection and sends the `BANNER` to the client. The client is expected to provide a username and password.

3. **Receiving User Input**:
   - The honeypot simulates a login prompt by sending a banner message to the client and asking for a username.
   - It then waits for the user to input a username and password. The input is collected by repeatedly calling `recv()` on the socket.
   - The username and password are stored in `user` and `password` variables respectively.

4. **Sending Logs**:
   - Once the username and password are collected, an alert message is sent back to the client. The alert indicates that the action has been reported (simulating that the attacker’s activity is logged).
   - The username and password are printed to the console and also logged via the `sendLog` function.

5. **Error Handling**:
   - If there’s an error while receiving data from the client, the error is logged to the remote server using `sendLog`.
   - If everything goes smoothly, the collected data (username and password) is sent to the remote server.

6. **Logging Data**:
   - `sendLog` establishes a connection to the remote host (`RHOST`) and sends the log message containing the attacker's IP, port, and the captured data (username/password).

7. **Graceful Shutdown**:
   - `atexit.register(exit_handler)` ensures that when the script exits (e.g., via keyboard interrupt), the honeypot socket is properly closed, and a shutdown message is printed.

### Example of Output:

- When the honeypot is running and a client connects, it will output:
  ```
  [*] Honeypot starting on 0.0.0.0:23
  [*] Honeypot connection from 127.0.0.1:50677 on port 23
  Username: rajnor\
  Password: snjbcomp\
  ```

  In the example above:
  - A client connected from `127.0.0.1` (localhost) on port `50677`.
  - The user entered the username `rajnor\` and the password `snjbcomp\`.

### Steps for Execution (as per the `steps_program_output.txt`):

1. Run the script in your environment, for example, through Anaconda's Spider or any Python IDE.
2. Open a command prompt on a Windows machine and connect to the honeypot using the Telnet client:
   ```bash
   C:\Users\lenovo> telnet localhost
   ```
3. Once connected, the banner will appear, and the user will be prompted to enter a username and password:
   - Username: `rajnor\`
   - Password: `snjbcomp\`
4. After entering the username and password, the honeypot will capture and log the input, and print it on the server side.

### Notes:
- **Security**: This honeypot script is a very basic one and is for educational purposes. In a real-world deployment, honeypots would need better error handling, logging, and security considerations.
- **Python Version**: Ensure that you are using a compatible version of Python (3.x) for this script, as it uses `str` and `bytes` operations that may behave differently in Python 2.x.

This honeypot captures basic login attempts and records the data for further analysis. It's a simple yet effective way to observe attack attempts on your network or system.

# Software Testing and Quality Assurance

### Experiment 1: Test Scenario for Gmail Login Page

**1.	What are Test Scenario Examples?**

ans:- Examples include checking if users can log in with valid credentials, if incorrect passwords are rejected, and if the “Forgot Password” feature works as expected. These scenarios cover core functionalities.

**2.	Scenario-Based Questions in Manual Testing**

ans:- These questions test the understanding of how a feature should work under specific conditions. For example, testing how an application handles multiple failed login attempts.

**3.	Test Scenarios for Test Cases**

ans:- Test scenarios outline high-level actions, such as testing the response of a login button. Each scenario can have multiple test cases covering different input conditions and expected outcomes.

**4.	How Many Test Scenarios Are There?**

ans:- The number depends on the complexity of the feature. A simple feature may have 5-10 scenarios, while a complex one could have over 50, ensuring comprehensive coverage.

**5.	What Do You Understand by Software Testing?**

ans:- Software testing ensures that a software product is free from defects and meets the user’s requirements. It involves verification (checking if it works as expected) and validation (ensuring it fulfills user needs).

**6.	When Should You Stop the Testing Process?**

ans:- Testing should be stopped when all critical test cases are executed, major defects are fixed, or project timelines and budgets are exhausted. The decision also depends on meeting the quality benchmarks.

**7.	Verification vs. Validation**

ans:- 	•	Verification: Ensures the product is built according to specifications, typically through reviews and inspections.
	•	Validation: Ensures the product meets user needs through actual testing.

**8.	Test Scenarios for Gmail Functionality**

ans:- These include testing email composition, sending and receiving messages, handling attachments, and verifying that spam filters work correctly. It also covers testing performance under heavy email loads.

### Experiment 2: Test Scenario for Inbox Functionality

**1.	Test Scenarios for Inbox Functionality**

ans:- Scenarios include verifying the display of unread/read emails, search functionality, organizing emails into folders, and performance when handling thousands of messages. It covers both functional and performance aspects.

**2.	What are Test Scenario Examples?**

ans:- Examples involve checking if unread emails are highlighted, if searching by sender works correctly, and if emails can be moved between folders without errors. These scenarios ensure that the inbox is fully functional.

**3.	Scenario-Based Questions in Manual Testing**

ans:- Focus on testing the application’s behavior in realistic situations. For instance, how does the inbox handle emails with large attachments or emails marked as spam?

**4.	Test Scenarios for Test Cases**

ans:- They provide a framework for creating detailed test cases, such as verifying email sorting by date or testing the behavior of the “Mark as Read” feature.

**5.	What is Static Testing?**

ans:- Static testing involves reviewing code, documents, or requirements without executing the program. It helps identify errors early and improve code quality through techniques like code inspections and walkthroughs.

**6.	Define Black-Box Testing**

ans:- Black-box testing examines the functionality of an application without knowledge of its internal workings. Testers focus on input and output, ensuring the software performs as expected based on user requirements.

### Experiment 3: Test Cases for Social Media Applications

**1.	Examples of Test Cases**

ans:- Test cases could include verifying user registration, checking if the profile picture can be uploaded, ensuring posts are visible to friends, and testing privacy settings. Each case ensures the app works as expected.

**2.	How Many Test Cases Can Execute Per Day?**

ans:- The number varies based on complexity and testing resources. Typically, a QA tester can execute 5-50 test cases per day, depending on how detailed and complex the scenarios are.

**3.	What is a Good Test Case in QA?**

ans:- A good test case is simple, clear, and covers a specific requirement. It should include the test steps, expected results, and any preconditions necessary for testing.

**4.	Who Writes Test Cases in Agile?**

ans:- QA engineers are primarily responsible, but developers and product owners may also contribute. Collaboration is key in Agile environments to ensure comprehensive coverage.

**5.	Test Case Quality Factors**

ans:- Quality factors include clarity, completeness, reusability, and maintainability. Well-written test cases should be easily understandable and provide detailed expected outcomes.

**6.	What Makes a Test Case a Good Test Case?**

ans:- It should be easy to understand, execute, and should have a clear expected outcome. A good test case also covers both positive and negative scenarios to ensure robustness.

**7.	Can We Write Test Cases Without Test Scenarios?**

ans:- While possible, it is not recommended. Test scenarios provide context and ensure that test cases are comprehensive and aligned with user requirements.

**8.	How Many Test Cases Are Possible?**

ans:- The number of possible test cases depends on the complexity of the feature. A well-defined application can have hundreds of test cases to cover all functional and edge cases.

**9.	What Makes Good Test Cases?**

ans:- Test cases should be detailed, cover both common and edge cases, and be easily maintainable. They should provide a clear path from input to expected output.

### Experiment 4: Selenium Grid and WebDriver Installation

**1.	What is Automation Testing?**

ans:- Automation testing involves using tools and scripts to perform tests on software. It reduces manual effort, speeds up testing, and is ideal for regression and performance testing.

**2.	Types of Automation Testing**

ans:- Includes unit testing, integration testing, functional testing, performance testing, and regression testing. Each type addresses specific aspects of software quality.

**3.	Manual vs. Automated Testing**

ans:- Manual testing is performed by humans and is suitable for exploratory testing. Automated testing uses scripts, is faster, and more reliable for repetitive tasks.

**4.	When to Automate a Test?**

ans:- Automate tests that are repetitive, stable, and time-consuming. Regression tests and scenarios with a large number of input combinations are ideal for automation.

**5.	When to Avoid Automated Testing?**

ans:- Avoid automation for tests requiring human judgment, exploratory testing, or one-off tests. Automation may not be cost-effective in these cases.

**6.	Choosing a Tool/Framework**

ans:- Consider the application type, team expertise, and budget. For example, Selenium is suitable for web apps, while Appium is used for mobile applications.

**7.	Popular Automation Tool**

ans:- Selenium is widely used for web testing because of its open-source nature and cross-browser support. It allows testing across different platforms and browsers.

**8.	Types of Automation Tools**

ans:- Functional testing tools like Selenium, performance testing tools like JMeter, and load testing tools like LoadRunner are some examples. Each serves a different purpose.

**9.	Crucial Requirements for Automation Tools**

ans:- Ease of use, support for various technologies, detailed documentation, and good reporting features. The tool should also integrate well with the development and CI/CD processes.

**10.	When Not to Use Automation Tools for Testing?**

ans:- Avoid automation when tests are exploratory, infrequent, or highly dynamic. Also, if setting up automation takes more effort than the testing itself, manual testing is preferable.

**11.	What Cannot be Automated Using Selenium?**

ans:- Selenium cannot automate tasks like CAPTCHA, visual testing, or tests requiring interaction with non-browser-based elements like desktop applications.

**12.	What Makes Selenium Unique from Other Tools?**

ans:- It is open-source, supports multiple languages like Python, Java, and C#, and allows cross-browser testing. Selenium’s flexibility and large community make it a preferred choice.

**13.	Tools Required for Selenium Automation**

ans:- Selenium WebDriver for browser automation, Selenium IDE for recording tests, and Selenium Grid for running tests across multiple environments. Integration tools like TestNG or JUnit are also useful.

**14.	Limitations of Selenium Automation**

ans:- It lacks built-in reporting features, struggles with dynamic web elements, and requires extensions to automate tasks like file uploads or downloads. It also does not support desktop application testing.

### Experiment 5: Software Requirement Specification (SRS)

**1.	Which Part of SRS is More Important?**

ans:- Functional requirements are crucial as they detail the software’s features and behavior. They define what the system should do and serve as a basis for development and testing.

**2.	Role of SRS in Software Lifecycle**

ans:- SRS serves as a foundation for the entire project. It guides the development, testing, and maintenance of the software, ensuring that all stakeholders have a clear understanding of the project.

**3.	Why SRS is Called Black Box?**

ans:- SRS describes the functionality of the system without specifying how the system will be implemented. It focuses on what the system should do, rather than how it does it.

**4.	Need for SRS & Significant Components**

ans:- SRS is needed for clear communication among stakeholders. Key components include functional requirements, performance requirements, interface specifications, and constraints.

**5.	Questions for Requirements Gathering**

ans:- Questions like “What is the primary goal of the software?”, “Who are the end users?”, and “What are the security requirements?” help gather comprehensive requirements.

**6.	Phase for SRS Preparation**

ans:- SRS is prepared during the requirements analysis phase. This phase involves understanding and documenting what the software needs to achieve.

**7.	Qualities of a Good SRS**

ans:- A good SRS is clear, complete, consistent, and verifiable. It should be easy to understand, cover all requirements, and be flexible to accommodate changes.

**8.	Major Components of SRS**

ans:- Components include functional and non-functional requirements, use cases, and system models. Each component addresses a different aspect of the software’s behavior.

**9.	Functional Requirements in SRS**

ans:- These are detailed descriptions of what the system should do. Examples include user authentication, data processing, and response to user inputs.