# Fundamentals of Cloud Computing Midterm Review

## NIST Characteristics of Cloud Computing

* On-demand Self Service
  * A user can provision computing abilities as needed without needing any human interaction with the service provider
* Broad Network Access
  * Access to resources available over the network through the various client platforms (phones, tablets, laptops, and workstations)
* Resource Pooling
  * The service provider creates resources (i.e. servers, storage, etc.) that are pooled together to serve multiple consumers (multitenancy)
* Rapid Elasticity
  * Resources can be elastically provisioned or released
  * From client standpoint, the resources must look limitless and can be purchased at any time and in any quantity
* Measured Service
  * Resource usage is monitored, controlled, and reported, providing transparency to both the provider and the consumer
  * Billing is based on the actual consumption of services (pay-as-you-go)

## NIST Cloud Deployment Models

***A deployment model defines the purpose of a cloud and the nature of how the cloud is located***

* **Public Cloud**
* **Private Cloud**
* **Community Cloud**
* **Hybrid Cloud**

### Public Cloud

* Open to the public to use
* Exists on the premises of the cloud service provider (CSP)
* Most cost-effective through multitenancy; enormous scalability
* Enterprises do not control the location of data or equipment
  * Can be a concern for organizations with regulatory or legislative mandates
* Examples:
  * AWS
  * Salesforce
  * Google

### Private Cloud

* Provided for the exclusive use of a single organization
* Organization is responsible for:
  * Purchase
  * Maintenance
  * Management of hardware
* Pros:
  * Security
  * Privacy
  * Reliability
* Cons
  * Limited scalability
  * Cost-intensive
* Preferred choice for:
  * Companies that already own a data center and developed IT infrastructure
  * Need to maintain control of the environment due to regulatory or business reasons
* Can also be managed by a 3rd party on or off-premise

### Hybrid Cloud

* Usually a combination of private and public clouds
* The models remain unique entities but are bridged together by standardized or proprietary technology that enables data and application portability
* Pros:
  * Better alignment to business needs
* Cons:
  * Harder management
* Example:
  * Allows an organization to deploy less critical applications and data to the public cloud by leveraging the scalability and cost-effectiveness of the public cloud
  * The organizations mission-critical applications and data remain on the private cloud that provides greater security

#### Cloud Bursting Using Hybrid Clouds

* Private cloud is used to support applications
* When a spike in demand exceeds private cloud limits, *bursts* or *surges* are handled by the public cloud
* Example:
  * A tax prep company may experience a surge in demand during tax season

## NIST Service Models

***Service models define the type of service that the cloud provider is offering***

* **SaaS** - Software as a Service
* **PaaS** - Platform as a Service
* **IaaS** - Infrastructure as a Service

|**Type**|**Consumer**| |--------|------------| |Apps|Users| Platform|Application Developers| |Infrastructure|System Administrators|

### Characteristics of IaaS

* Provisioning of:
  * Servers
  * Storage
  * Networks
  * Other computing resources to the client
* Cloud provider provisions and manages infrastructure
* Client is responsible for other aspects such as
  * OS
  * Deployed Applications
  * Data
* IaaS reduces/eliminates high, upfront capital expenses as organizations do not need to buy hardware; they can consume hardware assets as needed and pay for what is used
* Example:
  * Amazon EC2 is an example of on-demand, scalable, compute capacity (servers) in AWS cloud

### Characteristics of PaaS

* Provisioning of a software development platform to the client
  * programming languages
  * libraries
  * tools
* Most applications are accessed through an Application Programming Interface (API)
* Facilitates low-cost, easy, and rapid development of new applications
* Client does not manage the underlying cloud infrastructure or the OS but has complete control over deployed applications
* High risk of *vendor lock-in*
  * the condition in which an organization finds itself relying on a proprietary technology base that restricts future migration to alternative solutions without significant costs
* Examples:
  * Google App Engine
  * Microsoft Windows Azure

### Characteristics of SaaS

* Provisioning of ready-to-use software (applications) to the client
* SaaS applications are multitenant
* Applications are prebuilt and consumed without customization beyond personalization and some configuration settings
* Users just use the software; they don't control the underlying infrastructure
* Device and location independence
* Example: Office 365

## Shared Responsibility Model

![Alt text](sharedresponsibilitymodel.png)

## Identifying Business Drivers for Cloud Computing

### Some Business Terms

* **Economies of Scale**
  * Refers to the relationship between per-unit cost and production volume
  * Increase in production leads to a decrease in per-unit cost by spreading out fixed costs over more units
* **CAPEX vs. OPEX**
  * **CAPEX (Capital Expenses)**
    * related to fixed assets, including both original purchase and later improvements
    * life of these purchases extends beyond the current accounting period in which they were purchased
    * Example: costs of purchasing computing equipment and software
  * **OPEX (Operational Expenses)**
    * associated with running ordinary business operations
    * short-term costs and are used up in the same accounting period
    * Examples:
      * internet costs
      * subscription-based services
      * payroll
* **Total Cost of Ownership (TCO)**
  * Refers to the complete cost of an object or service throughout its lifetime, from purchase to disposal, including direct and indirect costs

***Hosting IT services in-house can be costly and distract businesses from focusing on their core competencies***

Major business drivers for cloud are:

* Cost
* Organizational agility and efficiency

### Reducing Costs

* **Lower costs from economies of scale**
  * cloud providers support thousands of customers
  * able to offer reasonable rates for their services due to economies of scale
* **Cloud computing reduces CAPEX**
  * no upfront costs of purchasing:
    * computing hardware
    * licensing
    * maintenance (except when cloud is built on-premise)
  * only pay for resources or services used (pay-per-use)
  * facilitates shift from *CAPEX* to *OPEX* (variable)
* **Reducing IT administrative overhead**
  * cloud transfers routine administrative duties from internal IT staff to the service provider
  * time spent on these duties can be reallocated to other work such as:
    * innovation
    * system analysis
    * IT process improvement
  * allows organization to reduce IT staffing levels, reducing HR-related operational expenses

### Increasing Organizational Agility and Efficiency

* **Organizational agility** is the ability to rapidly adapt to changes in the market or industry through identification and realization of opportunities
* Organization agility can be improved by:
  * **Scalability**
    * access to computing resources when needed
    * eliminates the need for guessing, planning, or provisioning capacity
    * scaling can be either vertical (scaling up) or horizontal (scaling out)
      * *vertical scaling* involves adding resources such as memory, processing power, etc. to the same node
      * *horizontal scaling* involves adding more nodes to a distributed system
      * if both are used → *diagonal scaling* ![scaling](scaling.png)
  * **Shortened time to market**
    * self-service provisioning and pay-as-you-go billing with cloud enable organizations to rapidly develop and release new projects
  * **Rapid development and testing**
    * ability to create and deploy large scale development and testing environments on demand
    * provides organizations with greater opportunities to experiment and innovate
  * **Global access (Mobility)**
    * cloud-based applications can be easily accessed from any location using various types of devices
    * data collaboration is easily achieved

## Types of Disks and Configurations

* Magnetic Tapes
  * data storage and retrieval are performed sequentially; data access is slow
  * data cannot be accessed by multiple applications simultaneously
  * mainly used for off-site storage and data archiving
* Hard Disk Drives
  * Electromechanical devices
  * use rapidly rotating disks called platters to store and retrieve digital information
  * high risk of mechanical failures
  * data can be stored or retrieved in any order
  * used when storage is more important than speed
  * common configurations are 500 GB and 1 TB
* Solid State Drives (SSD)
  * no moving parts
  * use semiconductor-based solid-state memory to store and retrieve data
  * more expensive than HDDs, but less risk of failure or data loss
  * SSDs produce the highest possible I/O rates

### RAID Techniques

* HDDs are inherently susceptible to failures due to mechanical wear and tear and environmental factors, which could result in data loss
* RAID is a technique that combines multiple drives into a logical unit for data across multiple drives for data protection against drive failures or improved performance
* Key RAID techniques:
  * **Striping**
    * spreading data across multiple drives in order to use drives in parallel
  * **Mirroring**
    * same data is stored on two different disk drives, yielding two copies of the data
  * **Parity**
    * redundancy that ensures protection of data without maintaining a full set of duplicate data

#### RAID Levels

![RAID](raid.png)

* **RAID 0**
  * 2 disks with data striped across them
  * the highest speed
  * failure of *any* disks results in data loss
* **RAID 1**
  * identical copies of data stored on two drives
  * limited speed
  * requires twice as much storage
* **RAID 5**
  * stripes data across disks in the set
  * uses single and distributed parity to reconstruct data if a drive fails
  * fast read speed
  * computation of parity reduces write speed
* **RAID 6**
  * similar to RAID 5 but uses double parity
  * can recover from loss of two drives
  * higher write penalty
* **RAID 1+0**
  * takes mirrored sets and stripes data across them
  * high read and write performance
  * requires double the amount of drives for storage

### Storage Types

* **Block Storage**
  * files are split into raw chunks of data called *blocks*
  * each block has its own address but no metadata
  * Best solution for:
    * performance sensitive applications
    * transactional applications
    * database applications
  * Example: AWS EBS
* **File Storage**
  * files are organized under directories or subdirectories (hierarchical storage system)
  * files are tagged with metadata and retrieved based on their location and name
  * ideal for simple file sharing
  * Example: AWS EFS
* **Object Storage**
  * files are stored in a flat address space as *objects* each with a unique identifier calculated based on a hash function
  * based on its content and attributes rather than name and location
  * Scalable
  * uses detailed metadata
  * ideal for unstructured big data, analytics, and archiving
  * 90% of data used today is unstructured
  * often used for media files in cloud storage such as:
    * music
    * pictures
    * movies
    * video
    * graphics
  * Example: AWS S3

![Object Storage](objectstorage.png)

### Storage Area Network (SAN)

* A dedicated network of servers and shared storage devices
* Provides block-level storage
* Enables *storage to be shared* across multiple devices or access to the same data at the same time by multiple computers which is critical for high availability
* High-performing, but requires specialized skill sets and knowledge of proprietary technology
* High price tag
* Computers require a special adapter called a Host Bus Adapter (HBA) to connect to a SAN

### Network Attached Storage (NAS)

* File-level storage
* Can be connected to and accessed from an existing TCP/IP network
* Low-cost solution with good performance, no additional training or specialized skill sets necessary
* Uses file sharing protocols such as:
  * FTP (File Transfer Protocol)
  * SMB (Server Message Block)
  * NFS (Network File System)

![NAS](nas.png)

### Storage Tiering

* Permits an organization to adjust where its data is being stored based on the following requirements of an application
  * **Performance**
  * **Availability**
  * **Cost**
  * **Recovery**
* An organization can implement policies that define what data fits into each tier and manage how data migrates between tiers
  * **Tier 1**: mission-critical data that must bee stored on expensive and highly available disks
  * **Tier 2**: important business applications that require reasonably fast recovery time:
    * CRM (Customer Relationship Management)
    * ERP (Enterprise Resource Planning)
    * corporate email
  * **Tier 3**: older emails/data on completed transactions, infrequent access
  * **Tier 4**: data that must be kept to comply with regulatory or legal requirements (data archival)

![Storage Tiering](storage_tiering.png)

### Storage Replication

* **Synchronous Replication**
  * writes data to the local store and then immediately replicates it to the replica set
    * application is not informed that the data has been written until all replica sets have acknowledged receipt and storage of data
    * synchronous replication requires high-speed, low-latency connection between sites and ensure greater consistency
    * Example: data replication between multiple Availability Zones of an AWS Region
* **Asynchronous Replication**
  * stores data locally and then reports back to the application that the data has been stored; it sends data to the other replication partners at the next opportunity
    * not all members of the replica set may be fully consistent in a timely manner if latency is high or bandwidth is low
    * Example: data replication between multiple regions of AWS

## Server Virtualization

![Server Virtualization](server_virtualization.png)

* Before virtualization → server limited to run only one application
* Virtualization enables a single server to run multiple VMs concurrently, thus more applications
* VMs can be powered on, off, or rebooted independently of each other
* Different OSes and applications can be installed into each separate VM

### Benefits of Virtualization

* enables server consolidation by using fewer physical servers which reduces:
  * footprint of data centers
  * power and cooling costs
  * costs of IT operations (lower TCO)
* virtualization improves hardware utilization rates up to 70-80% (10-15% w/o virtualization)
* creating of VMs takes less time than a physical server
  * ability to dynamically increase capacity based on need (rapid elasticity)
* High availability - can reduce planned and unplanned downtime
* maintenance and upgrades are significantly easier and less expensive

### What is a Hypervisor?

* Hypervisor or Virtual Machine Monitor (VMM) is a **low-level program** that creates and manages the virtual infrastructure
* allows multiple VMs to run on a single physical machine
* the computer that runs the hypervisor is called the "host" and the VMs running on the host are called "guests"
* the host provides the underlying hardware and compute resources to the guest machines including:
  * CPU
  * memory
  * hard disk drives
* two distinct types of hypervisors:
  * **Type 1**
  * **Type 2**

#### Type 1 Hypervisor

![Type 1 Hypervisor](type1hv.png)

* runs directly on the system hardware
* best choice for:
  * high performance
  * scalability
  * reliability
* Examples:
  * VMware ESX/ESXi
  * Microsoft Hyper-V, Xen releases

#### Type 2 Hypervisor

![Type 2 Hypervisor](type2hv.png)

* runs on top of a preexisting host OS
* type 2 relies on the host OS and cannot boot until the OS has loaded and is operational (less efficient than type 1)
* less scalable (can support fewer VMs)
* great for testing, not production
* Examples:
  * VMware Workstation/Fusion/Player
  * Oracle VirtualBox

### Virtual Host

* The virtualization host provides all underlying hardware and compute resources for the guest virtual machines
* the first step in configuring a virtualization host is to confirm that it meets the following hardware requirements:
  * BIOS configurations
    * Hardware Assisted Virtualization must be enabled in BIOS (or UEFI)
  * CPU and cores
  * Memory capacity
  * NIC

### CPU and Cores

* **Multicore**
  * A **multicore** processor has two or more independent processing units called 'cores' enabling multitasking
  * having more cores is better than higher speed processors since VM load can be spread across more CPU units
* **Hyperthreading**
  * creates two **logical** CPUs for each physical CPU
  * proprietary technology for Intel CPUs
  * logical cores can handle different software threads, improved CPU throughput
  * not the same as having multiple cores in a CPU (hyperthreading shares the CPU's pipeline, cache, and interface)
  * **Overcommitment: assigning more vCPUs to VMs than available physical CPU cores**
    * allows the hypervisor to host more VMs than possible and make better use of available processors
    * overcommitment is possible because VMs often need more CPU only when starting up or when loading processes for the first time
      * CPU utilization then decreases significantly with occasional increases due to utilization
    * Safe to maintain overcommitment ratio of 3:1
      * i.e. 3 vCPUs for each physical CPU
    * when using overcommitment, one should evaluate the workload of all the VMs on a server and whether the workload is *processor-intensive*

### Memory Capacity

* more RAM and faster RAM speed is better for a virtualization host
* VMs often require more memory when starting up or loading processes for the first time
  * safe to maintain overcommitment ratio of 1.25:1
* Use the following measures when there aren't enough resources available to handle new memory requests:
  * **Memory Ballooning**
    * hypervisor borrows memory resources from other VMs
    * places loaned memory pages into a balloon that is temporarily allocated to the virtual machine that urgently needs memory (released back after)
  * **Transparent Page Sharing**
    * deduplicates hypervisor memory allocated to VMs, i.e. maintains only one copy of data
  * **Memory Compression**
    * Hypervisors can be configured to compress memory pages when available memory is low, consumes CPU resources
  * **Swapping (Paging) to Disk**
    * when memory is insufficient, the OS will dump data from memory into a page file
    * page file is located on the disk and much slower to access
    * causes performance degradation

### Virtual Machine Cloning

* installing a guest OS and loading applications is a time-consuming process
* cloning is used to create one or multiple *replicas* of an existing VM
* the clone can share virtual disks with the parent (linked clone) or create its own (full clone)
* the clone's MAC address is different from the parent
* cloning allows faster deployment of identical VMs to a group

### Virtual Machine Snapshots

* captures the state of a VM at a specific time when the snapshot is taken
* Contents of a snapshot:
  * state of a VM's disks
  * contents of the VM's memory
  * VM settings
* can be taken when a VM is running, powered off, or suspended
* very useful before a major software installation or maintenance task; if the work fails or causes issues, the machine can be restored back to its "before" state in a short time

### Virtual Machines vs. Containers

![Virtual Machines vs. Containers](vm_vs_container.png)

* **A container is a self-contained package of software that includes everything it needs to run i.e. code, runtime, libraries, etc.**
* Containers are very portable and offer consistent performance in different environments such as testing, development, staging, and production. They are extensively used in microservices-based architectures

## Security

### Data Security

* **Symmetric Encryption**
  * Single key that encrypts and decrypts data, not a scalable method
* Asymmetric Encryption
  * Use two different keys - pair of public and private key that are mathematically related
  * public keys can be freely shared with others and the private key must be accessible to the owner
  * data is encrypted using the public key and decrypted using the owner's private key
* **Digital Signatures**
  * test the integrity of the data
  * a mathematic hashing function is applied to the data in the message which results in a hash or message digest. The signer's private key is used to encrypt the hash and create the digital signature
  * other parties use the public key of the signer to validate the hash; the signature is invalidated if the message is tampered with

![CIA Triad](cia-triad.png)

![Encryption](encryption.png)

### Network Security

#### Virtual Private Clouds (VPC)
  
* created for deployment of resources such as VMs
* VPCs are divided into separate segments based on trust
* **Public subnet (DMZ)**
  * least-trusted traffic, used to deploy web servers that are accessible from the internet
* **Private subnet**
  * hosts backend databases that are not publicly accessible

#### Three Cloud Firewall Implementations

* Virtual Firewall Appliance (VFA)
  * analyzes traffic and performs port or service filtering
  * additional functions include:
    * Web Application Firewall (WAF)
      * screens traffic for web applications (layer 7 of the OSI model)
      * prevents common exploits such as cross-site scripting (XSS) and SQL injection
    * Intrusion Detection System (IDS)/Intrusion Prevention System (IPS)
      * identify malicious traffic and take action
      * an *IDS* sends alerts and logs suspicious traffic
      * an *IPS* can also block or quarantine traffic
* Network ACLs (NACLs)
  * rules for what traffic is allowed in and out of subnets within the VPC
* Security Groups
  * control traffic to and from the deployed virtual machines (e.g. web servers, database servers) within the VPC

### Access Control

* **Process of who or what should be able to view, modify, or delete information**
* **Authentication:** Users must validate their identity, some environments use a combination of multiple authentication mechanisms (MFA)
  * something you know
  * something you have
  * something you are
* **Authorization:** determines what resources do authenticated users have access to
* **Identity Federation:** enables cloud customers to retain their own on-premise user accounts and credentials to access cloud services
* **SSO:** requires users to authenticate only once; they are authorized to use multiple cloud systems without having to log in each time

#### Access Control Methodologies

* **Mandatory Access Control (MAC)**
  * permissions to resources are mandated by OS or application (not the data owner)
  * requires resource classification or data labeling
  * example: only HR can access files that are classified as "Confidential"
* **Discretionary Access Control (DAC)**
  * power to grant or deny access relies on the data owner
  * small networks
  * example: use of ACLs to access a resource
* **Non-discretionary Access Control (NDAC)**
  * based on organizational rules
  * scales well as access is not resource specific
  * Two types:
    * Role-based Access Control (RBAC)
    * Task-based Access Control (TBAC)

### Vulnerability Management

* security testing helps companies stay *aware of the security gaps* in the cloud environments
* security testing can be:
  * **black-box**: no information about targets is provided
    * companies perform black-box first and then use gray and white-box testing
  * **gray-box**: some information is provided
    * faster and cheaper than black-box
    * somewhat more expensive than white-box
  * **white-box**: significant information about targets is provided
* **Vulnerability scanning:** process of *discovering flaws or weaknesses* in systems and applications; occurs in three phases:
  * intelligence gathering
  * vulnerability assessment
  * vulnerability validation
* **Penetration testing:** an extension of vulnerability scanning that evaluates system security at a point in time by attacking target systems as an outside attacker would and documenting:
  * which attacks were successful
  * how the systems were exploited
  * which vulnerabilities were utilized
* Pen testing is organized into seven phases:
  * intelligence gathering
  * vulnerability assessment/validation
  * attack planning/simulation
  * exploitation
  * post-exploitation
  * reporting
* A pen test tests the network and host security by simulating malicious attacks and analyzing the results

## Contingency Planning

Contingency planning involves establishing alternate practices, site, and resources in an emergency situation, or to establish high availability

* acceptable recovery time objective (RTO) for an organization helps an administrator choose between three types of backup sites
* **Cold Site**
  * least expensive
  * availability of physical space and network connectivity
  * no hardware or backed up data, takes longer to get up and running after a disaster
  * RTO of a day or more
* **Hot Site**
  * replica of the original site
  * readily available hardware with the latest data backups
  * quickly available if disaster strikes, minimal impact on normal operations
  * most expensive
  * RTO of a few hours
* **Warm Site**
  * readily available hardware on a smaller scale, backed up data may be a few days old

### Metrics for Critical Resources

* **CPU Utilization**
  * Collect CPU metrics once systems have been moved to production and track the metrics according to system load
* Metrics to monitor:
  * **CPU time**
    * shows amount of time a process or thread spends executing on a processor core; if an application runs multiple processes
    * CPU time is additive
  * **Wait Time**
    * amount of time a thread (process) waits to be processed
* **Memory Utilization**
  * **Paged Pool**
    * shows the amount of data that has been paged to disk
    * paging from disk is performed when insufficient memory or RAM is available and results in lower performance for each page fault
  * **Page Faults**
    * number of times data was fetched from disk that memory since process was launched
    * a high number indicates that memory needs to be increased
  * **Peak Memory Usage**
    * peak memory used by a process since it was launched

### RTO and RPO

![RPO and RTO](rto_rpo.png)

* **Recovery Time Objective (RTO)**: maximum tolerable amount of time between an outage and restoration of the service before an organization suffers unacceptable losses
* **Recovery Point Objective (RPO)**: maximum amount of time in which data can be lost for a service due to a major incident (measured in number of hours or days of work)
  * RPO decides the frequency of backups
  * Example: if RPO is 24 hours, backups would need to occur once daily
  * different data may need different RPO

### Types of Data Backup

* **Full:**
  * copy of all data and files on the drive in a single process
  * requires most space
  * fastest to restore
* **Differential:**
  * only backs up the changes since the last full backup
  * restore faster than incremental but slower than full
* **Incremental:**
  * only backs up files that have been changed since the last backup
  * last backup can be full or incremental
  * backups happen faster and requires less space
  * restoration takes longer

![Types of Backups](types_of_backups.png)

## Automation and Orchestration

* **Automation:** uses scripts or tools to execute a single task
* **Orchestration:** manages workflows to optimize efficiency and ensures effective execution
  * workflow automations are called as *runbooks* and each step in a runbook is called an *activity*
* **Scripting:** most orchestration tools support many scripting languages:
  * JavaScript
  * Python
  * Ruby
  * PowerShell
  * PHP
  * SQL
  * R
  * and others
* **Custom Programming**
  * use of full-fledged programming languages to create runbooks or with APIs
  * more capabilities and enable a more powerful testing environment
  * useful when runbooks are complex (programs can be organized as modules)
  * Examples:
    * C
    * C++
    * Java
    * Python

## Change Management

* involves a *set of policies and procedures* that allow companies do the following in a controlled fashion:
  * prioritize
  * plan
  * test
  * implement
  * document
  * review
* needs to be applied equally to big and small changes
* must maximize business value through modification of the cloud environment while reducing disruptions and unnecessary cloud expenses due to rework
* optimizes risks
* involves a process to evaluate both the **risks and benefits** of the proposed change in the change procedure and organizational culture
* identified risks contribute to the decision to approve or reject the proposed change

### Change Management Breakdown

#### Change Requests

* request for change (RFC) is a formal request to make a modification
* submitted by anyone who is involved or has a stake in a particular item or a service

#### Change Request Types

* normal
* standard
* emergency

#### Change Proposals

* reserved for **changes with major organizational impact or financial implications**
* decision-making is handled by the right level of leadership (managed by CIO or higher position)

#### Change Approval or Rejection

* Change manager: individual responsible for all the activities in the change management process
* ensures all RFCs follow the defined policies and procedures
* evaluates the change to decide to approve or reject
* cannot have full knowledge of the scope or impact of the change (systems are complex and integrated) so they assemble the right collection of stakeholders for input and advice

#### Change Advisory Board (CAB)

* group of stakeholders that provides input to the change manager about the RFCs
* should be composed of members from all areas of business and customers who may be affected by the change

#### Change Scheduling

* approved changes must be scheduled
* some can be implemented immediately, and others must be planned after notifying the stakeholders

#### Change Documentation

* keep detailed logs of changes made
* review process evaluates whether:
  * objectives were accomplished
  * whether users and customers were satisfied
  * if and whether new side effects were produced
* review and closure process is also intended to evaluate:
  * resources used
  * time it took
  * overall cost for improving efficiency
  * effectiveness of the process

## Configuration Management

* purpose is to ensure that CIs (Configuration Item) required to deliver IT services are adequately controlled, and accurate and reliable information is available where and when needed
* Objectives:
  * identifying CIs
  * controlling CIs
  * protecting the integrity of CIs
  * maintaining an accurate and complete Configuration Management System (CMS)
  * maintaining information about the state of all CIs
  * providing accurate configuration information

### Configuration Management Database (CMDB)

* database used to store CIs throughout their lifecycle
* CMS maintains one or more CMDBs and each database stores attributes of CIs and the relationships with other CIs
* one of the key attributes that all CIs must contain is **ownership**
  * this accountability imposes responsibility for:
    * keeping all attributes current
    * inventorying
    * financial reporting
    * safeguarding
    * other controls necessary for the optimal use, maintenance, and disposal of the CI

![Configuration Items](ci.png)
