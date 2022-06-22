# Linux Installation & Configuration Lecture Notes

## Module 3: Working in Linux

### Navigating the Linux Desktop

- To be a Linux sysadmin, it is necessary to be comfortable with Linux as a desktop OS and have proficiency with basic information and communication technology (ICT) skills
- Sysadmins use Linux to:
  - manage servers
  - assist users with configuration issues
  - recommend new software
  - update documentation among other tasks
- After familiarizing oneself with the Linux *Graphical User Interface* (GUI) the next step is learning how to perform tasks from the command line

### Getting to the Command Line

- The *command line interface (CLI)* is a simple text input system for entering anything from single word commands to complicated scripts
- On systems that boot to a GUI, there are two common ways of accessing the command line: a GUI-based terminal and a virtual terminal
  - browse to the **Terminal** application from the applications' menu
  - a virtual terminal can be run at the same time as a GUI but may require the user to log in via the virtual terminal before they can execute commands

### Applications

- The *kernel*:
  - decides which programs get which blocks of memory
  - starts and kills *applications*
  - handles displaying text and graphics on a monitor
- Applications make requests to the kernel and in turn receive resources such as memory, CPU, and disk space
- The kernel also handles the switching of applications, a process known as *multitasking*
- There are a large variety of application types such as:
  - word processors
  - web browsers
  - email clients and more
- A process is just one task that is loaded and tracked by the kernel
- An application may even need multiple processes to function, so the kernel takes care of running the processes, starting and stopping them as requested, and handing out system resources

#### Major Applications

- Linux software generally falls into one of three categories:
  - **Server Applications**: the purpose of this software is to serve information to other computers, called *clients*
  - **Desktop Applications**: web browsers, text editors, music players, or other applications with which uers interact directly
  - **Tools**: a loose category of software that exists to make it easier to manage computer systems

##### Server Applications

- Linux excels at running server applications because of its reliability and efficiency
- One of the early uses of Linux was for *web servers*
  - a web server hosts content for web pages, which are viewed by a web browser using the **HyperText Transfer Protocol (HTTP)** or its encrypted flavor **HTTPS**
- There is a growing demand for *private cloud* server software to store, sync, and share data from private cloud servers
  - the **Owncloud** project provides software to store, sync, and share data from private cloud servers
  - the **Nextcloud** project also provides private cloud software

##### Desktop Applications

- The Linux ecosystem has a wide variety of desktop applications
- Email
  - the **Mozilla Foundation** came out with **Thunderbird**, a full-featured desktop email client that connects to a POP or IMAP server
  - other notable email clients are **Evolution** and **KMail** which are the GNOME and KDE project's email clients
- Creative
  - **Blender**
    - 3D movie creation
  - **GIMP (GNU Image Manipulation Program)**
    - 2D image manipulation
  - **Audacity** 
    - audio editing
- Productivity
  - **LibreOffice** is a fork of the OpenOffice application suite

##### Console Tools

- UNIX has considerable overlap between the skills of software development and systems administration
- The tools for managing systems have features of computer languages, such as loops, and are used extensively in **automating systems administration tasks**
- Therefore, basic familiarity with programming is required for competent sysadmins
- Shells:
  - users interact with a Linux system through a *shell*, which accepts commands to execute
  - Linux offers a variety of shells to choose from such as:
    - Bourne shell
    - C shell
    - Bourne Again (BASH) shell
    - tcsh
    - Korn shell (Ksh)
    - zsh
- Text editors
  - most Linux systems provide a choice of text editors which are commonly used at the console to edit configuration files
  - the two main editors are **Vi** (or the more modern **VIM**) and **Emacs**
  - **Pico** and **Nano** are available on most systems and provide very basic, yet user friendly text editing

### Package Management

- Every Linux system needs to add, remove, and update software
- Modern distributions use *packages*
- Packages are compressed files that bundle up an application and it's *dependencies* (required files), greatly simplifying the installation
- A *package manager* takes care of keeping track of which files belong to which package and even downloading updates from repositories
- In Linux, there are many different software package management systems, but the two most popular are those from Debian and Red Hat
- Debian Package Management:
  - Has software packages that are distributed as files ending in the `.deb` extension
  - Tools for managing these files include:
    - `dpkg`
    - `apt-get`
    - `aptitude`
    - Synaptic
    - Software Center
- RPM (Red Hat Package Manager) Package Management:
  - according to the Linux Standards Base, the standard package management system is RPM
  - RPM makes use of an `.rpm` file for each software package
  - distros derived from Red Hat, including CentOS and Fedora, use RPM
  - the backend tool most commonly used for RPM package management is the `rpm` command
  - tools for managing these files include `yum` and `up2date`

### Development Languages

- Languages fall into one of two camps: *interpreted* or *compiled*
  - an *interpreted language* translates the written code into computer code as the program runs
  - a *compiled language* is translated all at once
- Linux was written in a compiled language called **C**
- C has been extended over the years to **C++** and **Objective C** and other variants
- the **Java** language uses hypothetical CPU called the **Java Virtual Machine (JVM)** and then compiles all the code to that
- **JavaScript** is a high-level interpreted programming language that is one of the core technologies on the World Wide Web
- **Perl** is an interpreted language originally developed to perform text manipulation but has gained favor with sysadmins and is used in everything from automation to building web applications
- **PHP** was initially built to create dynamic web pages
- **Ruby** was influenced by Perl and Shell that powers many of the leading automation tools
- **Python** a scripting language in general use
  - has excellent statistical processing abilities and is a favorite in academia
- **OpenSSL** a cryptographic library that is used in everything from web servers to the command line
- **C library** provides a basic set of functions for reading and writing to files and displays, which is used by applications and other languages alike

### Security

- *Cookies* are the primary mechanism that websites use to track you
  - as you browse the web, a web server can send back the cookie, which is a small piece of text, along with the web page
  - browsers typically offer cookie-related settings, users can opt to have the browser tell the site not to track

#### Password Issues

- Good password management is essential to security in any computing environment
- The most privileged user on any Linux system is *root*; this account is the primary *administrator* which is created when the OS is installed
- There are many levels of access and various means of password management on a Linux system
  - when *users* are created, they are given different login permissions depending on what *groups* they are assigned to
  - *services* that run on systems such as databases can also have login permissions with their own passwords and privileges
  - there are specific passwords for *accessing systems remotely* through SSH, FTP, or other management programs

### The Cloud

- *Cloud computing* allows computing resources to be moved to remote locations where content can be accessed, manipulated and shared around the globe
- *Cloud adoption* is the migration of an organization's IT applications and processes to cloud services
- A cloud can be described as computing resources from one or many off-site data centers which can be accessed over the internet
- The data and resources that organizations store in the cloud can include:
  - data
  - servers
  - storage
  - application hosting
  - analytics
  - and a myriad of other services
- A cloud deployment model provides a basis for how cloud infrastructure is built, managed, and accessed
- 4 primary cloud deployment models:
  - **Public Cloud**: deployed by a provider to offer cloud services to the general public and organizations over the internet
  - **Private Cloud**: set up for the sole use of an organization
  - **Community Cloud**: set up for the sole use by a group of organizations with common goals or requirements
  - **Hybrid Cloud**: composed of two or more individual clouds, each of which can be private, community, or public clouds

#### Linux in the Cloud

- **Flexibility**: provides the capability to provision IT resources quickly and at any time
- **Accessibility**: applications and data reside centrally and are accessed from anywhere over a network from any device
- **Community Cloud**: consumers can scale IT resources to meet workload demand, thereby eliminating overhead from underutilized resources
- **Hybrid Cloud**: a significant portion of Linux servers operating in the cloud are created and managed by automated management programs rather than human operators
  - this process frees up admins to monitor computing operations rather than manually configuring and updating systems
- **Security**: Linux can help offset security issues because it is one of the most secure and reliable OSs available
  - Linux is open source meaning its source code can be inspected for vulnerabilities and compatibility issues

## Module 4: Open Source Software and Licensing

### Open Source Philosophy

- Philosophy that users have the right to obtain the software source code and modify it for their own use
- Software projects use source code; a human-readable set of computer instructions
- **UNIX** source code language preceded Linux
  - UNIX was created at AT&T Bell Labs in 1969
- Standards organizations like **IEEE** and **POSIX** ensure that code has the ability to be compatible with other programs and operating systems for collaboration
- **GNU Project** built tools that are compatible with UNIX, which were used to create Linux and now make Linux a more complete package

### Open Source Licensing

- Purchasing software:
  - **Ownership**: who owns the intellectual property
  - **Money transfer**: does it cost anything/how do you pay?
  - **Licensing**: What do you get? What can you do with the software? How many computers? Can you share it?
- **End User License Agreement (EULA)** is a legal document you must accept before installing software
- **GNU General Public License version 2 (GPLv2)** is a license that states the source code must be made available to anyone and that anyone can make changes
  - changes must be made under the same license
- **Free and Open Source Software (FOSS)** is software where anyone can view source code, modify it, and redistribute it

### The Free Software Foundation

- The Free Software Foundation and the Open Source Initiative are considered to be the most influential forces in the world of open source
- Founded in 1985 with the goal of promoting free software
- Advocates for freedom to share, study, and modify the underlying source code
- Enforces *copyleft*, the philosophy that if someone modifies free software, they are required to share those changes when they share the modified software
- Developed their own licenses which are free and are based on GNU General Public License (GPL)
  - also GPLv2, GPLv3, LGPLv2, and LGPLv3

### The Open Source Initiative

- Licenses without copyleft are called *permissive*
- **Free and Open Source Software (FOSS)** is a term used to refer to the open source community, which consists of the Free Software and Open Source as a collective (a catch-all term)
- **Free/Libre/Open Source Software (FLOSS)** uses the term *libre* to define the difference between free from *restrictions* (Libre) and free from *cost* (free)

### Creative Commons

- **Attribution**: must acknowledge the author
- **ShareAlike**: copyleft
- **No-Derivs**: you may not change content
- **NonCommercial**: no commercial use
- Combinations are allowed, such as Attribution-No-Derivs-NonCommercial

|Name|Description|
|:--|:--|
|Attribution (CC-BY)| You can use CC BY content for any use but must credit the copyright holder|
|Attribution ShareAlike (CC-BY-SA)|Copyleft version of the Attribution license|
|Attribution No-Derivs (CC-BY-SA)|You may redistribute the content under the same conditions as CC-BY but may not change it|
|Attribution-NonCommercial (CC-BY-NC)|Like CC BY, but you may not use it for commercial purposes|
|Attribution-NonCommercial-ShareAlike (CC-BY-NC-SA)|Requires that your changes be shared under the same license|
|Attribution-NonCommercial-No-Derivs (CC-BY-NC-ND)|Allows sharing the content to be used for non-commercial purposes, but people may not change the content|
|No Rights Reserved (CC0)|Public domain|

### Open Source Business Models

- Offer products and services; Red Hat and Ubuntu
- Create tools; Wireshark
- Package hardware and open source software; Tivo, appliances
