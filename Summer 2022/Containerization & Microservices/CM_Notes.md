# Containerization and Micro Services Notes

## Module 1: Introduction

### Containers

- Operative System virtual technology
- Allows you to package (CONTAINERIZE!):
  - applications
  - services
  - dependencies
  - configurations in isolated environments
- Benefits:
  - **Portability**: Standardize environments across different infrastructures allowing developers to deploy applications with little to no modification
  - **Isolation**: Isolate applications from each other on a shared OS providing more security and avoiding dependency problems
  - **Agility**: has a smaller footprint by using the host OS resources, allowing start/stop services faster
  - **Scalability**: allows you to increase the number of replicas of a container
- Containers are created from *container images* that act like templates that hold all the required information for a container to run
- Images are created in layers in which one image can be used to run multiple containers or to create another more complex image that can be used to run multiple containers
- Containers:
  - can be built on your laptop and deployed on the cloud
  - interchangeable
  - stackable
  - portable
  - generic

![Container Architecture Overview](/SchoolNotes/MarkdownPics/container_architecture_overview.png)
