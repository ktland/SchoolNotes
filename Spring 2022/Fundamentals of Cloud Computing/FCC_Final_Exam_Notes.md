# Final Exam Study Guide

## AWS Regions

* **AWS Region** is a geographical area
  * Data replication across Regions is controlled by you
  * Communication between Regions uses AWS backbone network infrastructure
* Each Region provides full redundancy and connectivity to the network
* A Region typically consists of two or more Availability Zones

## Selecting A Region

Determine the right Region for your services, applications, and data based on:

* Data governance & legal requirements
* Proximity to customers (latency)
* Services available within the Region
* Costs (vary by Region)

## Availability Zones

### Each Availability Zone is a fully isolated partition of the AWS infrastructure

* Availability Zones consist of one or more discrete data centers and are designed for fault isolation
* They are interconnected with other Availability Zones by using high-speed private networking
  * accomplishes synchronous replication
* AWS recommends replication data and resources across Availability Zones for resiliency

**A single AZ can span multiple data centers, but no two zones *share* a data center**

![AWS Availability Zones](aws_availability_zones.png)

## Access to AWS Services

* AWS Management Console
  * Web application that allows access to services
* AWS Command Line Interface (AWS CLI)
  * With just one tool to download and configure, you can control multiple AWS services from the CLI and automate them through scripts
* Software Development Kits (SDK)
  * Access via an Application Programming Interface (API) tailored to your programming language or platform

## AWS Pricing Model

### Three Fundamental Drivers of Cost with AWS

* Compute
  * Charged per hour/second\*
    * \*Available for Linux and Ubuntu only
  * Varies by instance type
* Storage
  * Charged typically per GB
* Data Transfer
  * No charge for inbound data transfer or transfer between AWS services within the same region
  * Outbound is aggregated and charged
  * Charged typically per GB

## AWS Free Tier

### AWS Free Tier helps customers get started in the cloud

### Limitations:

* Free, hands-on experience for new customers
* Valid up to one year
* Applicable to only certain services and options
* Provides customers the ability to explore and try out AWS services free of charge up to specified limits for each service
* If your application use exceeds the free tier limits, you simply pay standard, pay-as-you-go service rates

## No Charge AWS Services

* Amazon VPC
* AWS Identity and Access Management (IAM)
* Consolidated Billing
* AWS Elastic Beanstalk\*\*
* AWS CloudFormation\*\*
* Automatic Scaling\*\*
* AWS OpsWorks\*\*

\*\* **Note:** there may be charges associated with other AWS services used in conjunction with these services

## Total Cost of Ownership (TCO)

*Total Cost of Ownership (TCO)* is the financial estimate to help identify direct and indirect costs of a system

### Why use TCO?

* to compare the costs of running an entire infrastructure environment or specific workload on-premises vs. on AWS
* To budget and build the business case for moving to the cloud

## AWS Pricing Calculator

* Estimate monthly costs of AWS services
* Identify opportunities to reduce monthly costs
* Model your solutions before building them
* Explore price points and calculations behind your estimate
* Find the available instance types and contract terms that meet your needs

## Intro to AWS Organizations

AWS Organizations is an **account management service** that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage

* You can create Service Control Policies (SCPs) to control access to AWS services across multiple AWS accounts
* With Consolidated billing, you can see a combined view of charges incurred by all your AWS accounts as well as take advantage of pricing benefits from aggregate usage
* Consolidated billing provides a central location to manage billing from volume discounts

## AWS Billing and Cost Management Tools

* **AWS Bills**
  * lists the costs you incurred over the past month for each AWS service with a further breakdown by AWS Region and linked account
* **AWS Cost Explorer**
  * view charts of your data
  * *historical* cost data for past 13 months
  * forecasts for the next three months
  * discover patterns in spending
  * identify cost problem areas
* **AWS Budgets**
  * Create budgets
  * set Amazon Simple Notification Service (SNS) if you go over budget for the month or when your estimated costs exceed your budget
* **AWS Cost and Usage Reports**
  * single location for accessing comprehensive information about your AWS costs and usage
  * you can choose to have AWS publish billing reports to an Amazon S3 bucket (can be updated once per day)

## AWS Support

### Proactive Guidance

#### Technical Account Manager (TAM)

* Designated primary Point of Contact (PoC) for users
* TAM can provide guidance, architectural review, and continuous ongoing communication to keep the user informed and prepared as they plan, deploy, and optimize their AWS solutions

### Best Practices:

#### Trusted Advisor

* Online resource that checks for opportunities to:
  * reduce costs
  * increase performance
  * improve security
* Core Checks and Recommendations come with all accounts
* Full Trusted Advisor benefits *only for* **Business** and **Enterprise** support plans

### Account Assistance

#### AWS Support Concierge

* A billing and account expert who will provide quick and efficient analysis on an issue
  * Addresses all *non-technical* billing and account level inquiries

## Support Plans

- **Basic Support**
- **Developer Support:** Support for early development on AWS
- **Business Support:** Customers that run production workloads
- **Enterprise Support:** Customers that run business and mission-critical workloads

## Support Plan Prices

*Insert screenshot*

## Case Severity & Response Times

*Insert Screenshot*

## Security

- **Customer** is responsible for the security *in* the cloud
- **AWS** is responsible for the security *of* the cloud

### AWS Responsibility: Security *of* the Cloud

- Physical security of data centers
- Hardware & Software
	- Servers
	- storage devices
	- appliances
	- Host OS
	- virtualization software
- Virtualization Infrastructure
	- Instance Isolation
- Network Infrastructure
	- Routers
	- switches
	- load balancers
	- firewalls
	- cabling
	- continuous network monitoring
	- secure access points
	- intrusion protection
	
### Customer Responsibility: Security *in* the Cloud

- Data and Encryption
- Application Access
- Account Management (IAM)
	- Login and permission settings for each user
- Configuration of:
	- VPC
	- Subnets
	- Security Groups
- Amazon EC2 instance OS
	- Includes upgrades, patching, maintenance

## AWS Identity and Access Management (IAM)

- AWS IAM allows you to control access to:
	- compute
	- storage
	- database
	- application services
- With IAM, you can manage *which* resources can be accessed by *who*, and *how* these resources can be accessed
- IAM is a global service and offered at no additional charge

### IAM: Essential Components

- **IAM User**
	- A person, application, or service that is defined in an AWS account and must make API calls to AWS resources
- **IAM Group**
	- A collection of IAM users that are granted identical permissions
- **IAM Policy**
	- IAM Policies are constructed with JavaScript Object Notation (JSON) and define permissions to determine what users can do with resources
- **IAM Role**
	- Tool to grant temporary access to specific AWS resources in an AWS account

### Authenticate as an IAM User to Gan Access

When you define an **IAM user**, you select what ***types of access*** the user is permitted to use

- **Programmatic Access (via AWS CLI & AWS SDKs)**
	- Authenticate using:
		- Access key ID
		- Secret access key
- **AWS Management Console Access**
  - Authenticate using:
    - 12-digit Account ID *or* alias
    - IAM username and password
  - Multi-factor authentication (MFA) offers improved security

### IAM Policies

- An IAM policy is a document that defines permissions
- 2 Types of Policies:
  - **Identity-based** policies
    - attached to any IAM entity such as:
      - IAM user
      - IAM group
      - IAM role
    - Policies specify: actions that ***may*** or ***may not*** be performed by the entity
	- A single *policy* can be attached to multiple *entities*
	- A single *entity* can have multiple *policies* attached to it
  - **Resource-based** policies
    - attached to a resource such as an S3 bucket
    - control what actions can be performed on the resource and under what conditions
	
### Example Use of an IAM Role

An **IAM role** can have permissions policies attached to it and can be used to delegate temporary access to users or applications

- **Scenario**
	- An application that runs on an EC2 instance needs access to an S3 bucket
	- Attach the policy to a role
	- Allow the EC2 instance to assume the role

## Best Practices

- **DO NOT** use the AWS account root user for day-to-day interactions with AWS
	- access to the **account root user** requires logging in with the *email address* and password that you used to create the account
- Secure logins with multi-factor authentication (MFA)
- Delete the account root user access keys
- Create individual IAM users and grant permissions according to the principal of least privilege
- Use groups to assign permissions to IAM users
- Configure a strong password policy
- Delegate using roles instead of sharing credentials
- Monitor account activity using AWS CloudTrail

| Account root user | IAM |
|:--|:--|
| Privileges cannot be controlled | Secure access for applications |
| Full access to all resources | Granular permissions |
|  | Identity federation |
|  | Integrates with other AWS services |

## Working to Ensure Compliance

- **AWS CloudTrail**
	- Tracks user activity on your account
		- Logs all API requests in all supported services of your account
	- Basic AWS CloudTrail event history is enabled by default and is free
		- Contains all management event data on latest 90 days of account activity
- **AWS Artifact**
	- Resource for compliance-related information
	- Provides access to AWS security and compliance documents
	- You can download:
		- AWS ISO certifications
		- Payment Card Industry (PCI) and Service Organization Control (SOC) reports
- **AWS Config**
	- Enables you to assess, audit, and evaluate the configurations of your AWS resources
	- Evaluates recorded configurations vs. desired configurations; non-compliant resources are flagged
	- Simplifies compliance auditing

## Additional Security Services

- **AWS Shield**
	- a managed and distributed denial of service (DDoS) protection service that safeguard applications that run on AWS
- **AWS Macie**
	- Discovers and proactively protects sensitive data in AWS such as Personally Identifiable Information (PII)
- **Amazon Inspector**
	- Automatically assesses applications for exposure, vulnerabilities, and deviations from best practices
- **Amazon GuardDuty**
	- Intelligent threat detection service that monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads

## Amazon VPC

- Enables you to provision a **logically isolated** section of the AWS cloud where you can launch AWS resources in a virtual network that you define
- Gives you control over your virtual networking resources including:
	- selection of IP address range
	- creation of subnets
	- configuration of route tables and network gateways
- Enables you to customize the network configuration for your VPC
- Enables you to use multiple layers of security
- Each Amazon VPC lives in a single region and can span multiple AZs
- Each Amazon VPC must specify the IPv4 address range by choosing a CIDR block
	- The largest IPv4 CIDR block size is /16
	- The smallest IPv4 CIDR block size is /28
	- Address range *cannot* be changed after the Amazon VPC is created

### Subnets

- further divide a VPC
- belong to a single Availability Zone
- classified as **public** or **private**
- CIDR blocks of subnets cannot overlap
- AWS reserves 5 IP addresses within every subnet
	- the *first 4* IP addresses and the *last* IP address in the block
	- these addresses aren’t available for use

### VPC Networking Options

- **Internet Gateway (IGW)**
	- scalable, redundant, and highly available component that connects your VPC to the internet
- **NAT Gateway**
	- enables instances in a private subnet to connect to the internet
- **VPC Sharing**
	- enables customers to share subnets with other AWS accounts in the same organization
- **VPC Peering**
	- networking connection between two VPCs that enables you to route traffic between them privately
- **VPC Endpoint**
	- connects your VPC to supported AWS services such as:
		- Amazon S3
		- DynamoDB table
- **AWS Site-to-Site VPN**
	- connects your VPC to remote networks such as the corporate data center via internet
- **AWS Direct Connect**
	- connects your VPC to a remote network by using a dedicated private network connection that bypasses the internet
- **AWS Transit Gateway**
	- a hub-and-spoke connection alternative to VPC peering to simplify management and reduce costs

### VPC Example - Two-tier Architecture

*insert screenshot*

### VPC Peering

*insert screenshot*

### AWS Site-to-Site VPN

*insert screenshot*

### AWS Direct Connect

*insert screenshot*

### Security Groups

*insert screenshot*

### Network Access Control Lists

*insert screenshot*

### Security Groups vs. Network ACLs

| Attribute | Security Groups | Network ACLs (NACLs) |
|:--|:--|:--|
| **Scope** | Control inbound and outbound traffic to and from your instance | Control traffic in and out of subnets |
| **Supported Rules** | Allow rules only | Allow and Deny rules |
| **State** | **stateful**: return traffic in response to an inside request is automatically allowed, regardless of inbound rules | **stateless**: return traffic must be explicitly allowed by rules |
| **Order of Rules** | All rules are evaluated before decision to allow traffic | Rules are evaluated in number order before decision to allow traffic |

## Amazon CloudFront

- Content Delivery Network (CDN) service delivers content to users with low latency and high transfer speeds
- **Edge Locations:**
	- worldwide network of data centers that CloudFront uses to server popular content quickly to customers
- **Regional Edge Caches**
	- CloudFront locations that cache content not popular enough to stay at the edge locations; caches are located between the origin server and the global edge locations

## Amazon EC2 

### Overview

- **Amazon Elastic Compute Cloud (Amazon EC2)**
	- provides virtual machines—referred to as EC2 instances— in the cloud
	- Gives you *full control* over the guest OS (Windows or Linux) on each instance
	- You can launch instances from **Amazon Machines (AMIs)** is minutes

### Storage Options

- **Amazon EC2 Instance Store**
	- ephemeral storage located on disks that are attached to the host computer where the EC2 instance is running
	- if the instance stops, data stored here is deleted
- **Amazon Elastic Block Store (Amazon EBS)**
	- durable, block-level storage volumes
	- You can stop the instance and start it again and data will be preserved
- Other storage options:
	- Amazon Elastic File System (Amazon EFS)
	- Amazon Simple Storage Service (S3)

### EC2 Pricing Models

#### On-demand Instances

- pay by the hour
- no long-term commitments

#### Reserved Instances

- Full, partial, or no upfront payment for the instance you reserve
- Discount on hourly charge for that instance
- 1-year or 3-year term

#### Spot Instances

- Instances run as long as they are available and your bid is above the Spot Instance price
- They can be interrupted by AWS with a 2-minute notification
- Prices can be significantly less expensive compared to On-Demand Instances
- Good choice when you have flexibility in when your applications can run

#### Dedicated Hosts

- A physical server with EC2 instance capacity fully dedicated to your use

#### Dedicated Instances

- Instances that run in a VPC on hardware that’s is dedicated to a single customer

##### *Per second billing* available for

- On-Demand Instances
- Reserved Instances
- Spot Instances
- **Must run Amazon Linux or Ubuntu**

### EC2 Pricing Models: Use Cases

#### On-Demand Instances

- short-term, spiky, or unpredictable workloads
- application development or testing

#### Spot Instances

- applications with flexible start and end times
- applications with only feasible at very low compute prices
- users with urgent computing needs for large amounts of additional capacity

#### Reserved Instances

- Steady-state workloads or predictable usage workloads
- applications that require reserved capacity, including disaster recovery
- users able to make upfront payments to reduce total computing costs even further

#### Dedicated Hosts

- Highly sensitive workloads
- Good choice for bring your own license (BYOL)
- help meet compliance and regulatory restrictions

### Amazon CloudWatch for Monitoring

- use **Amazon CloudWatch** to monitor EC2 instances
	- provides near real-time metrics
	- provides charts in the Amazon EC2 console **Monitoring** tab
	- maintains 15 months of historical data
- **Basic monitoring**
	- default, no additional cost
	- metric data sent to CloudWatch every 5 minutes
- **Detailed monitoring**
	- fixed monthly rate for 7 pre-selected metrics
	- metric data delivered every 1 minute

### Other Compute and Container Services

#### AWS Lambda

- an event-driven, serverless compute service
- enables you to run code without provisioning or managing servers
- 15 minute execution time

#### AWS Elastic Beanstalk

- AWS compute service option
- PaaS service that facilitates quick deployment, scaling, and management of your web applications and services

#### Docker

- software platform that packages software or applications into containers

#### Amazon ECS (Elastic Container Service)

- container orchestration service that supports Docker containers
- ECS enables you to easily run applications on a managed cluster of Amazon EC2 instances

#### AWS Fargate

- allows you to run containers without managing clusters of EC2 instances
- EC2 instances are managed for you by AWS

#### Kubernetes

- open-source software for container orchestration

#### Amazon EKS (Elastic Kubernetes Service)

- enables you to deploy, manage, and scale containerized applications using Kubernetes on AWS

#### Amazon ECR (Elastic Container Registry)

- enables you to store, manage, and deploy your Docker container images

## Amazon ECS Cluster Options

- **Key Question:** do you want to manage the Amazon ECS cluster that runs the containers?
	- If yes, create an Amazon ECS cluster backed by Amazon EC2
		- provides more granular control over infrastructure
	- If no, create an Amazon ECS cluster backed by AWS Fargate
		- easier to maintain, focus on your applications
	- *insert screenshot*

## Amazon EBS

- offeres persistent, block-level storage
- provides extremely low latency because the volume is directly attached to the instance
- each EBS volume is automatically replicated within its Availability Zone to protect from failures
- you can change the capacity or type of EBS volumes without needing to stop the instances
- you can encrypt Amazon EBS volumes at no additional cost
- an EBS volume cannot be shared between multiple instances

## Amazon EFS Features

- file storage in the AWS cloud
- works well for:
	- big data
	- analytics
	- media processing workflows
	- content management
	- web serving
	- home directories
- petabyte-scale, low-latency file system
- shared storage
- elastic capacity
- supports Network File System (NFS) versions 4.0 & 4.1 (NFSv4)
- compatible with all Linux-based AMIs for Amazon EC2

### Amazon EFS Architecture

*insert screenshot*

## Amazon S3

- fully managed, object storage solution for:
	- images
	- videos
	- logs
	- etc
- can store as many objects as you want
- single object limited to 5TB
- objects are stored in *buckets*
	- bucket names are universal and must be unique across all existing bucket names in Amazon S3
- by default, none of your data is shared publicly
- data is redundantly stored across multiple Availability Zones in the Region by default

### Amazon S3 Storage Classes

#### Amazon S3 Standard

- object storage for frequently accessed data

#### Amazon S3 Standard-IA

- for data accessed less frequently, but requires rapid access when needed
- low per GB storage price and per GB retrieval fee
- examples:
	- long-term storage
	- backups
	- disaster recovery

#### Amazon S3 One Zone-IA

- stores long-lived, less frequently accessed data in a single AZ, costs less than Standard-IA
- examples:
	- non-critical data
	- secondary backup copies of on-premise data
	- easily re-creatable data

#### Amazon Glacier

- extremely low cost storage for data archival, archives are stored in logical containers known as *vaults*

#### Amazon S3 Intelligent Tiering

- suitable for data with access patterns that are unknown or unpredictable
- data is monitored and moved between two tiers:
	- frequent access
	- infrequent access
- small monthly monitoring and automation fee per object
- no additional fees when objects are moved between access tiers and no retrieval fees

### Amazon S3: Storage Pricing

- Consider:
	- type of storage class
	- amount of storage
		- number and size of objects
		- GB per month
	- number and type of requests
		- PUT, GET, COPY, etc.
	- Data transfer
		- pricing is based on the amount of data that is transferred *out* of the Amazon S3 Region
- You DO NOT pay for:
	- transfers **INTO** Amazon S3
	- Transfers **OUT** from S3 to Amazon CloudFront or EC2 in the same Region

## Storage Comparison

|  | Amazon S3 | Amazon Glacier |
|:--|:--|:--|
| **Data Volume** | No limit | No limit |
| **Average Latency** | ms | minutes/hours |
| **Item Size** | 5TB max | 40TB max |
| **Storage Cost/GB per Month** | Higher Cost | Lower cost |
| **Billed Requests** | PUT, COPY, POST, LIST, and GET | UPLOAD and retrieval |
| **Retrieval Pricing** | Cent per request | Double cent per request and per GB |
| **Encryption** | Optional | Data stored is encrypted by default |

## Amazon RDS

- managed service that sets up, operates, and scales a relational database in the cloud without ongoing administration

### From On-Premises to Amazon RDS

*insert screenshot*

### Amazon RDS DB instances

*insert screenshot*

### High Availability Multi-AZ Deployment

*insert screenshot*

### Amazon RDS Read Replicas

#### Functionality

- you can reduce load on your master database instance by routing *read queries* from the application to the read replica