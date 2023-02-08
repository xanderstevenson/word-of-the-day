#!/Users/alexstev/Documents/CiscoDevNet/code/wod/venv/bin/python3
import random

# database connection
from tinydb import TinyDB, Query

db = TinyDB("db.json")
User = Query()

##                        ATTENTION DEVELOPERS!!

##     Hi, please add new definitions to the end of the list.
##     A Wikipedia entry is the default url unless it is lacking, absent or clearly outdone.

##     Use SINGLE QUOTES inside the "definition" if quotes are needed. Double quotes nested inside double quotes will throw an error when run.


def return_word():

    word_list = [

        {
            "name": "Wireframe",
            "definition": "A basic sketch or outline of the key information of a planned website. This 'skeleton' is used by developers and designers when laying out a webpage.",
            "url": "https://en.wikipedia.org/wiki/Website_wireframe",
            "id": 0
        },
        {
            "name": "Kerning",
            "definition": "The space between characters (numbers, letters, puncuation) and the process of adjusting this space to improve the readabilty.",
            "url": "https://en.wikipedia.org/wiki/Kerning",
            "id": 1
        },
        {
            "name": "Leading",
            "definition": "(pronounced 'led-ing') The vertical distance between lines on a website.",
            "url": "https://en.wikipedia.org/wiki/Leading",
            "id": 2
        },
        {
            "name": "Scalability",
            "definition": "The ability of a system to efficiently handle a growing or shrinking workload by providing it with more or less resources. Scaling horizontally (out/in) means adding more nodes to (or removing nodes from) a system while scaling vertically (up/down) means adding resources to (or removing resources from) a single node.\n\nScalability is the ability of the system to accommodate larger loads just by adding resources either making hardware stronger (scale up) or adding additional nodes (scale out). Elasticity is the ability to fit the resources needed to cope with loads dynamically usually in relation to scale out.",
            "url": "https://en.wikipedia.org/wiki/Scalability",
            "id": 3
        },
        {
            "name": "DevOps",
            "definition": "DevOps combines software development (Dev) and IT Operations (Ops). It's primary goals include shortening the software and systems develoment lifecycles while increasing the quality of products. DevOps practices involve continuous development, continuous testing, continuous integration, continuous deployment and continuous monitoring of software applications throughout its development life cycle.",
            "url": "https://en.wikipedia.org/wiki/DevOps",
            "id": 4
        },
        {
            "name": "CI/CD",
            "definition": "The combined practices of Continuous Integration (CI) and either Continuous delivery or Continuous deployment (CD) with the aim towards increasing efficiency and productivity. CI/CD compiles incremental changes to software code made by developers. Automated testing is performed and then automated delivery to customers is generated.",
            "url": "https://en.wikipedia.org/wiki/CI/CD",
            "id": 5
        },
        {
            "name": "Circuit breaking",
            "definition": "Circuit breaking creates resilient microservices applications by stopping the request and response process if a service is not working. Protected functions are wrapped in circuit breakers, which, when tripped, stop receiving calls. This makes sure threads ar enot waiting on calls, which can render a system unresponsive.",
            "url": "https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern",
            "id": 6
        },
        {
            "name": "Fault injection",
            "definition": "Fault injection is a system testing method which involves the deliberate introduction of network faults and errors into a system. It can be used to identify design or configuration weaknesses, and to ensure that the system can handle faults and recover from error conditions.",
            "url": "https://en.wikipedia.org/wiki/Fault_injection",
            "id": 7  
        },  
        {
            "name": "Sidecar",
            "definition": "Just as a sidecar can attach to a motorcycle, in software architecture a sidecar attaches to a parent application and enhances/extends its functionality.",
            "url": "https://en.wikipedia.org/wiki/Microservices#Service_mesh",
            "id": 8
        },
        {
            "name": "Canary deployment",
            "definition": "A strategy of delayed deployment where an application is releases incrementally to a subset of users (e.g. 1%, 5%, 15%, 50%, 75%, 100%).",
            "url": "https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html",
            "id": 9  
        },  
        {
            "name": "Zero trust",
            "definition": "Zero trust is a security framework which requires all users, both internal and external to the network or organization, to be continuously validated for security posture and configuration before being granted or keeping any access to data and applications.",
            "url": "https://en.wikipedia.org/wiki/Zero_trust_security_model",
            "id": 10
        },
        {
            "name": "Hardening",
            "definition": "The process of securing a system by reducing its vulnerability to attack. Hardening typically includes keeping software updated, changing default passwords, removing unnecessary software and accounts, and the disabling or removal of unnecessary services and software.",
            "url": "https://en.wikipedia.org/wiki/Hardening_(computing)",
            "id": 11       
        },       
        {
            "name": "Enumeration",
            "definition": "An enumeration is a complete, ordered listing of all the items in a collection. The term is commonly used in mathematics and computer science to refer to a listing of all of the elements of a set. In cybersecurity, enumeration is defined as a process which establishes an active connection to the target hosts to discover potential attack vectors in the system.",
            "url": "https://en.wikipedia.org/wiki/Enumeration",
            "id": 12       
        },       
        {
            "name": "Runtime",
            "definition": "Runtime is the period of time when a program is running. It begins when a program is opened (or executed) and ends with the program is quit or closed. Runtime is a technical term, used most often in software development. It is commonly seen in the context of a 'runtime error',  which is an error that occurs while a program is running.\n\nThe term 'runtime error' is used to distinguish from other types of errors, such as syntax errors and compilation errors, which occur before a program is run.",
            "url": "https://techterms.com/definition/runtime",
            "id": 13       
        },       
        {
            "name": "Abstraction",
            "definition": "Abstraction the process of hiding specifics, details or attributes from a user's view, making a system more generic and, therefore, easily understood. A good example is your laptop’s OS; It abstracts away all the details of how your computer actually works.",
            "url": "https://en.wikipedia.org/wiki/Abstraction_(computer_science)",
            "id": 14       
        },       
        {
            "name": "Chaos engineering",
            "definition": "The discipline of experimenting on a software system in production in order to build confidence in the system's capability to withstand turbulent and unexpected conditions.",
            "url": "https://en.wikipedia.org/wiki/Chaos_engineering",
            "id": 15       
        },       
        {
            "name": "Cloud native",
            "definition": "An approach to software engineering which takes advantage of innovations in cloud computing to build and run scalable apps via the cloud’s resources and technologies such as containers, microservices, serverless functions and immutable infrastructure.\n\nThe result is loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers the granular control to make major changes frequently with relative safety and ease. Cloud native systems are container packaged, dynamically merged and microservices oriented.",
            "url": "https://en.wikipedia.org/wiki/Cloud_native_computing",
            "id": 16       
        },       
        {
            "name": "Containerization",
            "definition": "Containerization, or OS-level virtualization, is an operating system (OS) paradigm in which the kernel allows the existence of multiple isolated user space instances, called containers (LXC, Solaris containers, Docker, Podman), zones (Solaris containers), virtual private servers (OpenVZ), partitions, virtual environments (VEs), virtual kernels (DragonFly BSD), or jails (FreeBSD jail or chroot jail) Such instances may look like real computers from the point of view of programs running in them.\n\nA computer program running on an ordinary operating system can see all resources (connected devices, files and folders, network shares, CPU power, quantifiable hardware capabilities) of that computer. However, programs running inside of a container can only see the container's contents and devices assigned to the container.",
            "url": "https://en.wikipedia.org/wiki/OS-level_virtualization",
            "id": 17       
        },       
        {
            "name": "DevSecOps",
            "definition": "DevSecOps is the augmentation of DevOps to allow for security practices to be integrated into the DevOps approach, resulting in the merger of development, operational and security responsibilities. Security practices and testing are performed earlier in the development lifecycle, hence the term ‘shift left’ can be used.\n\nDevSecOps empowers the developer by breaking down team silos and promoting the creation of secure, automated workflows and policy enforcement which provide the developer with timely and accurate information on how to move the project forward.",
            "url": "https://www.ibm.com/cloud/learn/devsecops",
            "id": 18       
        },       
        {
            "name": "Distributed apps",
            "definition": "A distributed application is an application whose functionality is delegated to smaller, independent components. In a cloud native environment, the individual parts typically run as containers on a cluster. In contrast with monolithic applications, if a node which is running on a distributed application goes down, another node can resume the task, thus eliminating a single point of failure.",
            "url": "https://en.wikipedia.org/wiki/Distributed_computing",
            "id": 19       
        },       
        {
            "name": "Immutable infrastructure",
            "definition": "A computer infrastructure (VMs, containers, network appliances, etc.) that can’t be altered once it’s deployed, which makes it easier to prevent and mitigate security vulnerabilities. This is often enforced via an automated process that overwrites unauthorized changes or through a system that won’t allow changes in the first place.\n\nContainers are an excellent example of immutable infrastructure because persistent changes to containers can only be made by creating a new version of the container or recreating the existing container from its image.",
            "url": "https://glossary.cncf.io/immutable_infrastructure/",
            "id": 20       
        },       
        {
            "name": "Infrastructure as a Service (IaaS)",
            "definition": "Infrastructure as a Service (IaaS) ia a cloud-computing model where the cloud providers own, operate and offer hardware and software for consumers on an on-demand and pay-as-you-go model. The resources offered are scalable physical or virtualized storage, compute and network resources.",
            "url": "https://en.wikipedia.org/wiki/Infrastructure_as_a_service",
            "id": 21       
        },       
        {
            "name": "Infrastructure as Code (IaC)",
            "definition": "Infrastructure as Code (IaC) is the process of managing and provisioning infrastructure based on machine-readable definition files as opposed to manual configuration done on hardware or through shell scripts or other, interactive configuration tools.",
            "url": "https://en.wikipedia.org/wiki/Infrastructure_as_code",
            "id": 22       
        },       
        {
            "name": "Kubernetes (K8s)",
            "definition": "Kubernetes (K8s) is an open-source tool for infrastructure automation. It’s like a data center operating system that manages applications running across a distributed system (just like the OS on your laptop that manages your apps). Kubernetes schedules containers across nodes in a cluster.\n\nIt defines infrastructure building blocks, called ‘primitives’ (exmples include app instances, load balancers, and persistent storage) which collectively provide mechanisms that deploy, maintain, and scale applications based on CPU, memory or custom metrics.\n\nAmazon, Google, IBM, Microsoft, Oracle, Red Hat, SUSE and VMware offer Kubernetes-based platforms or infrastructure as a service (IaaS) that deploy Kubernetes.",
            "url": "https://en.wikipedia.org/wiki/Kubernetes",
            "id": 23       
        },       
        {
            "name": "Cloud enabler",
            "definition": "A technology or manufacturer that serves as an organization’s backbone for all of its cloud computing products and services. It is a broad term for technology vendors and solutions that let a company build, deploy, integrate, and deliver cloud computing solutions.\n\nCloud enablers for infrastructure as a strive, for example, include high-capacity networks, low-cost computing, low cost storage devices, the widespread adoption of hardware virtualization and service-oriented architecture.",
            "url": "https://www.techslang.com/definition/what-is-a-cloud-enabler/",
            "id": 24       
        },       
        {
            "name": "Elasticity",
            "definition": "In cloud computing, elasticity is defined as 'the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible.\n\nScalability is the ability of the system to accommodate larger loads just by adding resources either making hardware stronger (scale up) or adding additional nodes (scale out). Elasticity is the ability to fit the resources needed to cope with loads dynamically usually in relation to scale out.'",
            "url": "https://en.wikipedia.org/wiki/Elasticity_(cloud_computing)",
            "id": 25       
        },       
        {
            "name": "Microservice",
            "definition": "A fine grained atomically deployable service accessed via a platform agnostic network API. In a microservices architecture, loose coupling reduces dependencies and the complexities around them. Therefore, it allows organizations developing software to grow fast, and big, as well as use off the shelf services easier.",
            "url": "https://en.wikipedia.org/wiki/Microservices",
            "id": 26       
        },       
        {
            "name": "Function as a Service (FaaS)",
            "definition": "Function as a Service (FaaS) is a type of serverless cloud computing service where code is executed in response to events or triggers but without the need for maintaining the complex infrastructure typically associated with building and launching applications.\n\nBuilding an application following this model is one way of achieving a 'serverless' architecture, and is typically used when building microservices applications. With FaaS, users manage only functions and data while the cloud provider manages the application.\n\nThis allows developers to get the functions they need without paying for services when code isn’t running. Some popular FaaS examples include: Amazon’s AWS Lambda, Google Cloud Functions and Microsoft Azure Functions.",
            "url": "https://en.wikipedia.org/wiki/Function_as_a_service",
            "id": 27       
        },       
        {
            "name": "Bare-metal server",
            "definition": "a physical computer server that is used by one consumer, or tenant, only. Each server offered for rental is a distinct physical piece of hardware that is a functional server on its own. They are not virtual servers running in multiple pieces of shared hardware.",
            "url": "https://en.wikipedia.org/wiki/Bare-metal_server",
            "id": 28       
        },       
        {
            "name": "Multicloud",
            "definition": "An organizational use of multiple cloud computing and storage services from different vendors in a single heterogeneous architecture to improve cloud infrastructure capabilities and cost. It also refers to the distribution of cloud assets, software, applications, etc. across several cloud-hosting environments.",
            "url": "https://en.wikipedia.org/wiki/Multicloud",
            "id": 29       
        },       
        {
            "name": "Managed services",
            "definition": "A software offering where operations and management (maintaining, and anticipating the need for, a range of processes and function) are outsourced to a third party. Examples include database as a service offerings like Amazon’s RDS or an external monitoring service like Datadog.",
            "url": "https://en.wikipedia.org/wiki/Managed_services",
            "id": 30       
        },       
        {
            "name": "Monolithic app",
            "definition": "An application where all functionality is contained in a single deployable program, which is often the simplest and easiest place to start when making an application. However, once the application grows in complexity, monoliths can become difficult to maintain. With more developers working on the same codebase, the likelihood of conflicting changes and the need for inter-silo and interpersonal communication between teams and developers increases.",
            "url": "https://en.wikipedia.org/wiki/Monolithic_application",
            "id": 31   
        }, 

        {
            "name": "Mutual TLS (mTLS)",
            "definition": "A method of mutual authentication that ensures that the party at each end of a network communication are who they claim to be by verifying they both have the correct private key. The information within their respective TLS certificates provides additional verification. mTLS is more often seen in micro services and business-to-business (B2B) applications, where a limited number of programmatic and homogeneous clients are connecting to specific web services, the operational burden is limited, and security requirements are usually much higher as compared to consumer environments. ",
            "url": "https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/",
            "id": 32     
        },     
        {
            "name": "Portability",
            "definition": "The ability of software to be used in different environments, which helps to avoid being locked-in to certain operating environments, such as operating systems, cloud providers or vendors. Portable software works in different operating environments without needing major reconfiguration. When software with the same functionality is produced for several computing platforms, portability is the key issue for development cost reduction.\n\nIn software engineering, ‘porting’ is the process of adapting software for the purpose of achieving some form of execution in a computing environment that is different from the one that a given program (meant for such execution) was originally designed for (e.g., different CPU, operating system, or third party library). The term is also used when software/hardware is changed to make them usable in different environments.",
            "url": "https://en.wikipedia.org/wiki/Software_portability",
            "id": 33     
        },  
        {
            "name": "Serverless",
            "definition": "A cloud computing and cloud native model in which the cloud provider allocates machine resources on demand, taking care of the servers on behalf of their customers. In this way, developers can build and run applications without having to manage servers. Although, ‘Serverless’ is a misnomer in the sense that servers are still used by cloud service providers to execute code for developers. However, developers of serverless applications are not concerned with capacity planning, configuration, management, maintenance, fault tolerance, or scaling of containers, VMs, or physical servers.\n\nServerless computing does not hold resources in volatile memory; computing is rather done in short bursts with the results persisted to storage. When an app is not in use, there are no computing resources allocated to the app. And pricing is based on the actual amount of resources consumed by an application.",
            "url": "https://en.wikipedia.org/wiki/Serverless_computing",
            "id": 34     
        },  
        {
            "name": "Service mesh",
            "definition": "A dedicated infrastructure layer for managing communications between services or microservices, using a proxy. A service mesh can provide a number of benefits, such as observability, reliability and secure connections or automating the retries and backoff for failed requests.",
            "url": "https://en.wikipedia.org/wiki/Service_mesh",
            "id": 35     
        },  
        {
            "name": "Service proxy",
            "definition": "A network component that acts as an intermediary for requests from a client that is seeking resources from microservice components. The service proxy applies some logic to the request traffic and then forwards that traffic to another service. It thus acts as a ‘go-between’ that collects information about network traffic and/or applies rules to it.",
            "url": "https://glossary.cncf.io/service_proxy/",
            "id": 36     
        },  
        {
            "name": "Site reliability engineering (SRE)",
            "definition": "Site reliability engineering (SRE) is a set of principles and practices which incorporates aspects of software engineering and applies them to infrastructure and operations problems.The main goals are to create scalable and highly reliable software systems.\n\nSite reliability engineering is closely related to DevOps, a set of practices that combine software development and IT operations, and SRE has also been described as a specific implementation of DevOps. However, while DevOps is focused on getting code to production, SRE ensures that the code running in production works properly.",
            "url": "https://en.wikipedia.org/wiki/Site_reliability_engineering",
            "id": 37     
        },  
        {
            "name": "Stateful vs. Stateless",
            "definition": "A stateless process or application can be understood in isolation. There is no stored knowledge of or reference to past transactions. Each transaction is made as if from scratch for the first time. Stateless applications provide one service or function and use content delivery network (CDN), web, or print servers to process these short-term requests. \n\nStateful applications and processes, however, are those that can be returned to again and again, like online banking or email. They’re performed with the context of previous transactions and the current transaction may be affected by what happened during previous transactions. For these reasons, stateful apps use the same servers each time they process a request from a user.  \n\nIf a stateful transaction is interrupted, the context and history have been stored so you can more or less pick up where you left off. Stateful apps track things like window location, setting preferences, and recent activity. You can think of stateful transactions as an ongoing periodic conversation with the same person. /n/n The majority of applications we use day to day are stateful, but as technology advances, microservices and containers make it easier to build and deploy applications in the cloud.",
            "url": "https://www.redhat.com/en/topics/cloud-native-apps/stateful-vs-stateless",
            "id": 38     
        },  
            {
            "name": "Version control",
            "definition": "Version control (also known as revision control, source control, or source code management) is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management.\n\nVersion control systems are most commonly run as stand-alone applications, but revision control is also embedded in various types of software, such as word processors and spreadsheets, collaborative web docs, and content management systems, e.g., Wikipedia's page history. Revision control enables reverting a document to a previous revision, which is critical for allowing editors to track each other's edits, correct mistakes, and defend against vandalism and spamming in wikis. Git is the most popular version control software but there are many competitors.",
            "url": "https://en.wikipedia.org/wiki/Version_control",
            "id": 39     
        }, 
        {
            "name": "Virtual machine (VM)",
            "definition": "In computing, a virtual machine (VM) is the virtualization/emulation of a computer system. Virtual machines are based on computer architectures and provide functionality of a physical computer, while not being bound to a particular piece of hardware. VMs rely on virtualization to create multiple virtual computers from a single physical computer. This allows infrastructure providers to maximize physical resources and easily create and tear down multiple VMs instances on a single machine.",
            "url": "https://en.wikipedia.org/wiki/Virtual_machine",
            "id": 40     
        },  
        {
            "name": "Gorilla testing",
            "definition": "A software testing technique that repeatedly applies inputs on a module to ensure it is functioning correctly and that there are no bugs. Gorilla testing is a manual testing procedure and is performed on selected modules of the software system with selected test cases.\n\nThe main objective is to test specific modules heavily and find any faults in their implementation. Since the tester manually applies the same test case repeatedly, it is also known as Torture Testing, Fault Tolerance Testing, or Frustrating Testing.",
            "url": "https://www.educative.io/edpresso/what-is-gorilla-testing",
            "id": 41     
        },  
        {
            "name": "Monkey testing",
            "definition": "In software testing, monkey testing is a technique where the user tests the application or system by providing random inputs and checking the behavior, or seeing whether the application or system will crash. Monkey testing is usually implemented as random, automated unit tests.",
            "url": "https://en.wikipedia.org/wiki/Monkey_testing",
            "id": 42     
        },  
        {
            "name": "Cisco Finesse",
            "definition": "A software application that offers features for Cisco contact center agents and supervisors in UCCE, PCCE and UCCX. It provides a web interface for agents and supervisors to login, change their state and receive calls. It also has some integration options with other platforms to display data and offer other features.\n\nCisco Finesse is a service that runs inside Cisco UCCX or as a separate virtual server in Cisco UCCE and PCCE. It offers call center agent functionality which includes managing agent's phone, answering incoming calls, making calls and other call control features.\n\nCisco Finesse is like a remote control, as it helps agents to control their Cisco phone remotely. They can answer a call, make a call, transfer an existing call without touching their Cisco IP Phone or Jabber Phone. However, it is actually the Cisco phone which offers all the telephony functionality for the call center agent. Cisco Finesse also helps agents to set their availability for taking calls from the queue.",
            "url": "https://developer.cisco.com/docs/finesse/#!finesse-overview/what-is-finesse",
            "id": 43     
        },  
        {
            "name": "Cisco JTAPI",
            "definition": "JTAPI serves as a programming interface standard developed by Sun Microsystems for use with Java-based computer–telephony applications. You use Cisco JTAPI to develop applications that\n\na) Control and observe Cisco Unified Communications Manager (CUCM) phones and\n\nb) route calls by using Computer–Telephony Integration (CTI) ports and route points (virtual devices).\n\nCisco Unified JTAPI gets used in a contact center to monitor device status and to issue routing instructions to send calls to the right place at the right time, to start and stop recording instructions while retrieving call statistics for analysis; and to screen-pop calls into CRM applications, automated scripting, and remote call control.\n\nCisco Unified JTAPI, used in an enterprise environment, combines user availability, location, and preferences for a uniquely tailored environment for presence-based routing. For example, in a financial environment, market data, business logic, and call control combine in a browser-based application to enable brokers and analysts to respond to rapid changes in the global financial markets.\n\nIn a healthcare environment, call control, doctor/patient lookup, and emergency response team paging combine in a browser-based console. Further, in a hospitality environment, caller data gets linked with POS systems to automate room or restaurant reservations, dispatch taxis, and schedule wakeup calls.",
            "url": "https://developer.cisco.com/site/jtapi/",
            "id": 44     
        },  
        {
            "name": "Cisco WebDialer",
            "definition": "Cisco WebDialer is installed on a Cisco Unified Communications Manager node and used along with Cisco Unified Communications Manager. It allows Cisco Unified IP Phone users to make calls from web and desktop applications. Cisco WebDialer uses hyperlinked telephone numbers in a company directory to allow users to make calls from a web page by clicking on the telephone number of the person that they are trying to call.",
            "url": "https://developer.cisco.com/site/webdialer/",
            "id": 45     
        },  
        {
            "name": "Link aggregation",
            "definition": "In computer networking, link aggregation is the combining (aggregating) of multiple network connections in parallel by any of several methods, in order to increase throughput beyond what a single connection could sustain, to provide redundancy in case one of the links should fail, or both. A link aggregation group (LAG) is the combined collection of physical ports.",
            "url": "https://en.wikipedia.org/wiki/Link_aggregation",
            "id": 46     
        },         
        {
            "name": "Hashing",
            "definition": "Hashing is a widely used concept within the IT world. It’s a multi-purpose technique used to generate a value based on a string that is computed through a mathematical function. The mathematical function used is called the hashing algorithm, and the value computed is called the hash value. A hash value is used because as long as you provide the same input string to a hashing algorithm, it will always generate exactly the same output hash value.\n\nWe can then use the computed hash value instead of the original string for simplicity. In networks, we run a lot of data through a hashing algorithm to scramble data before we transmit it (encrypt it). But the same technique can also be used to choose a physical link to use when they’re bundled into a logical interface.",
            "url": "https://en.wikipedia.org/wiki/Hash_function",
            "id": 47     
        },         
        {
            "name": "Bandwidth, Throughput and Goodput",
            "definition": "In computing, bandwidth is the maximum rate of data transfer across a given path.\n\nThroughput is all the bits that you can actually, physically transfer through your network, which can fall short of the bandwidth ideal. This includes all the needed headers and everything that is transported across your network.\n\nTo determine goodput, take all your throughput data and strip all the headers and all the application layer overheads; what’s left is the data that you can use: goodput.\n\nBandwidth > Throughput > Goodput",
            "url": "https://en.wikipedia.org/wiki/Goodput",
            "id": 48     
        },         
        {
            "name": "Trunking",
            "definition": "In telecommunications, trunking is a technology for providing network access to multiple clients simultaneously by sharing a set of circuits, carriers, channels, or frequencies, instead of providing individual circuits or channels for each client. This is reminiscent to the structure of a tree with one trunk and many branches.\n\nIn computer networking, port trunking is the use of multiple concurrent network connections to aggregate the link speed of each participating port and cable, also called link aggregation. Such high-bandwidth link groups may be used to interconnect switches or to connect high-performance servers to a network.\n\nIn the context of Ethernet VLANs, Cisco uses the term Ethernet trunking to mean carrying multiple VLANs through a single network link through the use of a trunking protocol. To allow for multiple VLANs on one link, frames from individual VLANs must be identified. The most common and preferred method, IEEE 802.1Q adds a tag to the Ethernet frame, labeling it as belonging to a certain VLAN. Since 802.1Q is an open standard, it is the only option in an environment with multiple-vendor equipment.",
            "url": "https://en.wikipedia.org/wiki/Trunking",
            "id": 49     
        },         
        {
            "name": "Capacity planning",
            "definition": "The process of determining the production capacity needed by an organization to meet changing demands for bandwidth, processing capability, services or similar items.",
            "url": "https://en.wikipedia.org/wiki/Capacity_planning",
            "id": 50     
        },        
        {
            "name": "Captive portal",
            "definition": "A web page accessed with a web browser that is displayed to newly connected users of a Wi-Fi or wired network before they are granted broader access to network resources. Captive portals are commonly used to present a landing or log-in page which may require authentication, payment, acceptance of an end-user license agreement, acceptable use policy, survey completion, or other valid credentials that both the host and user agree to adhere by.",
            "url": "https://en.wikipedia.org/wiki/Captive_portal",
            "id": 51     
        },        
        {
            "name": "Fragmentation",
            "definition": "In computer storage, fragmentation is a phenomenon in which storage space, main storage or secondary storage, is used inefficiently, reducing capacity or performance and often both. The exact consequences of fragmentation depend on the specific system of storage allocation in use and the particular form of fragmentation. In many cases, fragmentation leads to storage space being 'wasted', and in that case the term also refers to the wasted space itself.",
            "url": "https://en.wikipedia.org/wiki/Fragmentation_(computing)",
            "id": 52     
        },        
        {
            "name": "Jumbogram and Jumbo frame",
            "definition": "In packet-switched computer networks, a jumbogram is an internet-layer packet exceeding the standard maximum transmission unit (MTU) of the underlying network technology. While IPv4 has no facilities to exceed its theoretical IP MTU limit, the designers of IPv6 have provided a protocol extension to permit packets of larger size. An optional feature of IPv6, the jumbo payload option, allows the exchange of packets with payloads of up to one byte less than 4 GiB (232 − 1 = 4,294,967,295 bytes), by making use of a 32-bit length field.\n\nIn contrast, large packets (more than 1500 bytes of payload, the limit set by the IEEE 802.3 standard) for link-layer technologies are referred to as jumbo frames. Commonly, jumbo frames can carry up to 9000 bytes of payload, but smaller and larger variations exist and some care must be taken using the term. Many Gigabit Ethernet switches and Gigabit Ethernet network interface controllers and some Fast Ethernet switches and Fast Ethernet network interface cards can support jumbo frames.",
            "url": "https://en.wikipedia.org/wiki/Jumbo_frame",
            "id": 53     
        },        
        {
            "name": "Information Technology Infrastructure Library (ITIL)",
            "definition": "Information Technology Infrastructure Library (ITIL) is a library and set of detailed practices for IT activities such as IT service management (ITSM) and IT asset management (ITAM) that focus on aligning IT services with the needs of business.\n\nITIL describes processes, procedures, tasks, and checklists which are neither organization-specific nor technology-specific, but can be applied by an organization toward strategy, delivering value, and maintaining a minimum level of competency. It allows the organization to establish a baseline from which it can plan, implement, and measure. It is used to demonstrate compliance and to measure improvement.",
            "url": "https://en.wikipedia.org/wiki/ITIL",
            "id": 54     
        },          
        {
            "name": "Big data",
            "definition": "A tech term that describes large volumes of data in a structured, semi-structured, and unstructured form that can be leveraged for gleaning valuable business insights using machine learning and advanced analytics techniques. Big Data is characterized by the four V’s – Volume of the data, Variety of the data, Veracity, i.e. trustworthiness of the data, and Velocity.\n\nBig data also refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. Data with many fields (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.",
            "url": "https://en.wikipedia.org/wiki/Big_data",
            "id": 55     
        },          
        {
            "name": "Colo (Colocation Centre)",
            "definition": "A colocation center (also spelled co-location, or colo) or 'carrier hotel', is a type of data centre where equipment, space, and bandwidth are available for rental to retail customers. Colocation facilities provide space, power, cooling, and physical security for the server, storage, and networking equipment of other firms and also connect them to a variety of telecommunications and network service providers with a minimum of cost and complexity.\n\nColocation eliminates having to build a secure facility that provides power and air conditioning for company-owned servers. In addition, colocation centers are often located near major Internet connecting points and can provide access to multiple Tier 1 Internet backbones. Although most equipment monitoring is performed remotely by the customer, a colocation datacenter may offer equipment maintenance and troubleshooting arrangements.",
            "url": "https://en.wikipedia.org/wiki/Colocation_centre",
            "id": 56     
        },          
        {
            "name": "Data migration",
            "definition": "The process of moving data, applications or business elements between multiple formats, storage systems, warehouses and servers. Additionally, the validation of migrated data for completeness and the decommissioning of legacy data storage are considered part of the entire data migration process.\n\nData migration is a key consideration for any system implementation, upgrade, or consolidation, and it is typically performed in such a way as to be as automated as possible, freeing up human resources from tedious tasks. Data migration occurs for a variety of reasons, including server or storage equipment replacements, maintenance or upgrades, application migration, website consolidation, disaster recovery, and data center relocation.",
            "url": "https://en.wikipedia.org/wiki/Data_migration",
            "id": 57     
        },          
        {
            "name": "GCP (Google Cloud Platform)",
            "definition": "A Google cloud computing platform, which is a suite of public cloud computing services that offers management tools, computing, data storage, data analytics and machine learning. Google Cloud Platform provides infrastructure as a service, platform as a service, and serverless computing environments.",
            "url": "https://en.wikipedia.org/wiki/Google_Cloud_Platform",
            "id": 58     
        },          
        {
            "name": "Fibre Channel",
            "definition": "A high-speed data transfer protocol providing in-order, lossless delivery of raw block data. Fibre Channel is primarily used to connect computer data storage to servers in storage area networks (SAN) in commercial data centers.",
            "url": "https://en.wikipedia.org/wiki/Fibre_Channel",
            "id": 59     
        },          
        {
            "name": "Forward error correction (FEC)",
            "definition": "Forward error correction (FEC) or channel coding is a technique used for controlling errors in data transmission over unreliable or noisy communication channels. In EFC, the source (transmitter) sends redundant data and the destination (receiver) recognizes only the portion of the data that contains no apparent errors.",
            "url": "https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction",
            "id": 60     
        },          
        {
            "name": "Hypervisor",
            "definition": "A hypervisor (or virtual machine monitor, VMM, virtualizer) is software that allows multiple operating systems to share a single hardware host system. A hypervisor is similar to an emulator; it is computer software, firmware or hardware that creates and runs virtual machines. A computer on which a hypervisor runs one or more virtual machines is called a host machine, and each virtual machine is called a guest machine. The hypervisor presents the guest operating systems with a virtual operating platform and manages the execution of the guest operating systems.\n\nMultiple instances of a variety of operating systems may share the virtualized hardware resources: for example, Linux, Windows, and macOS instances can all run on a single physical x86 machine. This contrasts with operating-system–level virtualization, where all instances (usually called containers) must share a single kernel, though the guest operating systems can differ in user space, such as different Linux distributions with the same kernel.",
            "url": "https://en.wikipedia.org/wiki/Hypervisor",
            "id": 61     
        },          
        {
            "name": "YANG",
            "definition": "Yet Another Next Generation (YANG) is a data modeling language for the definition of data sent over network management protocols such as the NETCONF and RESTCONF. This data modeling language can be used to model both configuration data as well as state data of network elements. Furthermore, YANG can be used to define the format of event notifications emitted by network elements and it allows data modelers to define the signature of remote procedure calls that can be invoked on network elements via the NETCONF protocol. The language, being protocol independent, can then be converted into any encoding format, e.g. XML or JSON, that the network configuration protocol supports.",
            "url": "https://en.wikipedia.org/wiki/YANG",
            "id": 62     
        },          
        {
            "name": "YAML",
            "definition": "YAML is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted. YAML targets many of the same communications applications as Extensible Markup Language (XML) but has a minimal syntax. It uses both Python-style indentation to indicate nesting, and a more compact format that uses [...] for lists and {...} for maps, thus JSON files are valid as of YAML 1.2.\n\nThe official recommended filename extension for YAML files has been .yaml since 2006. Support for reading and writing YAML is available for many programming languages. Some source-code editors such as Vim, Emacs, and various integrated development environments have features that make editing YAML easier, such as folding up nested structures or automatically highlighting syntax errors.",
            "url": "https://en.wikipedia.org/wiki/YAML",
            "id": 63     
        },   
        {
            "name": "Blockchain",
            "definition": "A list of records, called blocks, that are linked together using cryptography. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. The timestamp proves that the transaction data existed when the block was published to get into its hash. As blocks each contain information about the block previous to it, they form a chain, with each additional block reinforcing the ones before it. Therefore, blockchains are resistant to modification of their data because once recorded, the data in any given block cannot be altered retroactively without altering all subsequent blocks.",
            "url": "https://en.wikipedia.org/wiki/Blockchain",
            "id": 64   
        },        
        {
            "name": "Net neutrality",
            "definition": "Network neutrality, most commonly called net neutrality, is the principle that Internet service providers (ISPs) must treat all Internet communications equally, and not charge users different rates based on content, website, platform, application, type of equipment, source address, destination address, or method of communication.\n\nWith net neutrality, ISPs may not intentionally block, slow down, or charge money for specific online content. Without net neutrality, ISPs may prioritize certain types of traffic, meter others, or potentially block traffic from specific services, while charging consumers for various tiers of service.",
            "url": "https://en.wikipedia.org/wiki/Net_neutrality",
            "id": 65      
        },           
        {
            "name": "Non-fungible token (NFT)",
            "definition": "A non-fungible token (NFT) is a unique, non-interchangeable unit of data stored on a blockchain, a form of digital ledger, that can be sold and traded. Types of NFT data units may be associated with digital files such as photos, videos, and audio. Because each token is uniquely identifiable, NFTs differ from blockchain cryptocurrencies, such as Bitcoin.\n\nNFT ledgers claim to provide a public certificate of authenticity or proof of ownership, but the legal rights conveyed by an NFT can be uncertain. NFTs do not restrict the sharing or copying of the underlying digital files, do not necessarily convey the copyright of the digital files, and do not prevent the creation of NFTs with identical associated files.",
            "url": "Non-fungible token",
            "id": 66     
        },         
        {
            "name": "Metaverse",
            "definition": "A metaverse is a network of 3D virtual worlds focused on social connection. In futurism and science fiction, it is often described as a hypothetical iteration of the Internet as a single, universal virtual world that is facilitated by the use of virtual and augmented reality headsets.\n\nThe term ‘metaverse’ has its origins in the 1992 science fiction novel Snow Crash as a portmanteau of ‘meta’ and ‘universe.’ Various metaverses have been developed for popular use such as virtual world platforms like Second Life. Some metaverse iterations involve integration between virtual and physical spaces and virtual economies. Demand for increased immersion means metaverse development is often linked to advancing virtual reality technology.",
            "url": "https://en.wikipedia.org/wiki/Metaverse",
            "id": 67      
        },          
        {
            "name": "Digital divide",
            "definition": "The digital divide is a gap between those who have access to digital technology and those who do not. These technologies include, but are not limited to smart phones, computers, and the internet. In the Information Age in which information and communication technologies (ICTs) have eclipsed manufacturing technologies as the basis for world economies and social connectivity, people without access to the Internet and other ICTs are at a socio-economic disadvantage because they are unable or less able to find and apply for jobs, shop and sell online, participate democratically, or research and learn.",
            "url": "https://en.wikipedia.org/wiki/Digital_divide",
            "id": 68     
        },            
        {
            "name": "Hyper-personalization",
            "definition": "Hyper-personalization is the concept of gathering real-time behavioral data of customers and leveraging artificial intelligence (AI) and to deliver more relevant content, product, and service information to each user. This approach takes personalized marketing a step further.",
            "url": "https://en.wikipedia.org/wiki/Personalization",
            "id": 69     
        },          
        {
            "name": "Gamification",
            "definition": "Gamification is the strategic attempt to enhance systems, services, organizations, and activities in order to create similar experiences to those experienced when playing games in order to motivate and engage users. This is generally accomplished through the application of game-design elements and game principles (dynamics and mechanics) in non-game contexts.",
            "url": "https://en.wikipedia.org/wiki/Gamification",
            "id": 70     
        },          
        {
            "name": "DIKW pyramid",
            "definition": "The DIKW pyramid (also known variously as the DIKW hierarchy, wisdom hierarchy, knowledge hierarchy, information hierarchy, information pyramid, and the data pyramid) refers loosely to a class of models for representing purported structural and/or functional relationships between data, information, knowledge, and wisdom. The DIKW acronym has worked into the lexical rotation from knowledge management. It demonstrates how the deep understanding of the subject emerges, passing through four qualitative stages: ‘D’ – data, ‘I’ – information, ‘K’ – knowledge and ‘W’ – wisdom.",
            "url": "https://en.wikipedia.org/wiki/DIKW_pyramid",
            "id": 71     
        },          
        {
            "name": "Robotic process automation",
            "definition": "Robotic process automation (RPA) is a form of business process automation technology based on metaphorical software robots (bots) or on artificial intelligence (AI)/digital workers. It is sometimes referred to as software robotics (not to be confused with robot software).\n\nIn traditional workflow automation tools, a software developer produces a list of actions to automate a task and interface to the back end system using internal application programming interfaces (APIs) or dedicated scripting language. In contrast, RPA systems develop the action list by watching the user perform that task in the application's graphical user interface (GUI), and then perform the automation by repeating those tasks directly in the GUI. This can lower the barrier to the use of automation in products that might not otherwise feature APIs for this purpose.\n\nRPA tools have strong technical similarities to graphical user interface testing tools. These tools also automate interactions with the GUI, and often do so by repeating a set of demonstration actions performed by a user. RPA tools differ from such systems in that they allow data to be handled in and between multiple applications, for instance, receiving email containing an invoice, extracting the data, and then typing that into a bookkeeping system.",
            "url": "https://en.wikipedia.org/wiki/Robotic_process_automation",
            "id": 72     
        },           
        {
            "name": "Neural networks",
            "definition": "Artificial neural networks (ANNs), usually simply called neural networks (NNs), are computing systems inspired by the biological neural networks that constitute animal brains.\n\nA neural network is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain. Each connection, like the synapses in a biological brain, can transmit a signal to other neurons. An artificial neuron receives a signal then processes it and can signal neurons connected to it.",
            "url": "https://en.wikipedia.org/wiki/Artificial_neural_network",
            "id": 73      
        },           
        {
            "name": "Hyperautomation",
            "definition": "Hyperautomation is the application of advanced technologies like robotic process automation (RPA), artificial intelligence (AI), machine learning (ML) and process mining to augment workers and automate processes in ways that are significantly more impactful than traditional automation capabilities. Hyperautomation is the combination of automation tools and technologies to deliver work.",
            "url": "https://en.wikipedia.org/wiki/Robotic_process_automation#Hyperautomation",
            "id": 74     
        },          
        {
            "name": "Full-stack observability",
            "definition": "Full-stack observability is the ability to understand at any time what is happening across a technology stack. By collecting, correlating, and aggregating all telemetry in the components, it provides insight into the behavior, performance, and health of a system. Through full-stack observability, teams can deeply understand the dependencies across domains and system topology.\n\nContrary to traditional monitoring systems, full-stack observability enables IT teams to proactively react, predict, and prevent problems using artificial intelligence and machine learning, which is all but a requirement considering that the amount of data collected would be nearly impossible otherwise. Presenting this data in the form of unified analytics and dashboards can give the observer a complete picture into the health of the system, for example, where issues occurred and solutions were introduced.",
            "url": "https://www.appdynamics.com/topics/what-is-full-stack-observability",
            "id": 75     
        },         
        {
            "name": "Extended reality (XR)",
            "definition": "Extended reality (XR) is a term referring to all real-and-virtual combined environments and human-machine interactions generated by computer technology and wearables. E.g. It includes representative forms such as augmented reality (AR), mixed reality (MR) and virtual reality (VR) and the areas interpolated among them. The levels of virtuality range from partially sensory inputs to immersive virtuality, also called VR.\n\nXR is a superset which includes the entire spectrum from ‘the complete real’ to ‘the complete virtual’ in the concept of reality–virtuality continuum introduced by Paul Milgram. Still, its connotation lies in the extension of human experiences especially relating to the senses of existence (represented by VR) and the acquisition of cognition (represented by AR). With the continuous development in human–computer interactions, this connotation is still evolving.\n\nXR is a rapid growing field being applied in a wide range of ways, such as entertainment, marketing, real-estate, training and remote work.",
            "url": "https://en.wikipedia.org/wiki/Extended_reality",
            "id": 76      
        },          
        {
            "name": "5G",
            "definition": "In telecommunications, 5G is the fifth-generation technology standard for broadband cellular networks, which cellular phone companies began deploying worldwide in 2019, and is the planned successor to the 4G networks which provide connectivity to most current cellphones. 5G networks are predicted to have more than 1.7 billion subscribers worldwide by 2025, according to the GSM Association.\n\nLike its predecessors, 5G networks are cellular networks, in which the service area is divided into small geographical areas called cells. All 5G wireless devices in a cell are connected to the Internet and telephone network by radio waves through a local antenna in the cell. The new networks is that they will have greater bandwidth, giving higher download speeds, eventually up to 10 gigabits per second (Gbit/s).\n\nIn addition to 5G being faster than existing networks, 5G has higher bandwidth and can thus connect more different devices, improving the quality of Internet services in crowded areas. Due to the increased bandwidth, it is expected the networks will increasingly be used as general internet service providers (ISPs) for laptops and desktop computers, competing with existing ISPs such as cable internet, and also will make possible new applications in internet-of-things (IoT) and machine-to-machine areas. Cellphones with 4G capability alone are not able to use the new networks, which require 5G-enabled wireless devices.",
            "url": "https://en.wikipedia.org/wiki/5G",
            "id": 77     
        },          
        {
            "name": "Voice-user interface (VUI)",
            "definition": "A voice-user interface (VUI) makes spoken human interaction with computers possible, using speech recognition to understand spoken commands and answer questions, and typically text to speech to play a reply. A voice command device (VCD) is a device controlled with a voice user interface.\n\nVoice user interfaces have been added to automobiles, home automation systems, computer operating systems, home appliances like washing machines and microwave ovens, and television remote controls. They are the primary way of interacting with virtual assistants on smartphones and smart speakers.",
            "url": "https://en.wikipedia.org/wiki/Voice_user_interface",
            "id": 78     
        },          
        {
            "name": "Web3",
            "definition": "Web3 (also known as Web 3.0 and sometimes stylized as web3) is an idea for a new iteration of the World Wide Web based on blockchain technology, which incorporates concepts such as decentralization and token-based economics. Some technologists and journalists have contrasted it with Web 2.0, wherein they say data and content are centralized in a small group of companies sometimes referred to as ‘Big Tech’.\n\nThe term ‘Web3’ was coined in 2014 by Ethereum co-founder Gavin Wood, and the idea gained interest in 2021 from cryptocurrency enthusiasts, large technology companies, and venture capital firms. Some experts argue that web3 will provide increased data security, scalability, and privacy for users and combat the influence of large technology companies. Others have raised concerns about a decentralized web, citing the potential for low moderation and the proliferation of harmful content, the centralization of wealth to a small group of investors and individuals, or a loss of privacy due to more expansive data collection.",
            "url": "https://en.wikipedia.org/wiki/Web3",
            "id": 79     
        },          
        {
            "name": "Multiexperience (MX)",
            "definition": "An experience composed by several modes (touch, voice, and gesture, for example), devices, and applications with which users interact through digital itineraries with different points of contact. The development of a multi-experience involves the creation of applications that are suitable to its purpose, basing on the specific categories of the point of contact, while guaranteeing a consistent user experience on various mobile, wearable, conversational and immersive (AR / VR) devices.\n\nThese devices currently support pressure detectors, luminosity, proximity, sound, inclination, movement, and orientation sensors that facilitate obtaining and integrating real data, as well as providing timely feedback. Multiexperience may embody the biggest UX challenge since the birth of the smartphone, as UI/UX Designers must move beyond the limitations of a GUI-only interface while taking into account the world as it will be experienced by users in the future.",
            "url": "https://uxplanet.org/erp-multiexperience-mx-610538ae1065",
            "id": 80     
        },          
        {
            "name": "Internet of senses",
            "definition": "A new era of connectivity in which people will be able to virtually feel the world without using gadgets, smartphones included. The Internet of Senses will rely on technologies including artificial intelligence (AI), virtual reality (VR), augmented reality (AR) and automation to interact with our senses of sight, sound, taste, smell and touch, and experts believe this will enable a myriad of new applications.",
            "url": "https://www.6gworld.com/exclusives/tasting-digital-how-the-way-you-sense-the-world-will-change-by-the-time-6g-is-real/",
            "id": 81     
        },         
        {
            "name": "Data mining",
            "definition": "Data mining is a process of extracting and discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.  Data mining is an interdisciplinary subfield of computer science and statistics with an overall goal of extracting information (with intelligent methods) from a data set and transforming the information into a comprehensible structure for further use.\n\nThe term ‘data mining’ is a misnomer, because the goal is the extraction of patterns and knowledge from large amounts of data, not the extraction (mining) of data itself. It also is a buzzword and is frequently applied to any form of large-scale data or information processing (collection, extraction, warehousing, analysis, and statistics) as well as any application of computer decision support system, including artificial intelligence (e.g., machine learning) and business intelligence.",
            "url": "https://en.wikipedia.org/wiki/Data_mining",
            "id": 82     
        },          
        {
            "name": "Machine learning operations (MLOps)",
            "definition": "MLOps or ML Ops is a set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently. The word is a compound of ‘machine learning’ and the continuous development practice of DevOps in the software field. Machine learning models are tested and developed in isolated experimental systems. When an algorithm is ready to be launched, MLOps is practiced between Data Scientists, DevOps, and Machine Learning engineers to transition the algorithm to production systems. \n\nSimilar to DevOps or DataOps approaches, MLOps seeks to increase automation and improve the quality of production models, while also focusing on business and regulatory requirements. While MLOps started as a set of best practices, it is slowly evolving into an independent approach to ML lifecycle management.\n\nMLOps applies to the entire lifecycle - from integrating with model generation (software development lifecycle, continuous integration/continuous delivery), orchestration, and deployment, to health, diagnostics, governance, and business metrics. According to Gartner, MLOps is a subset of ModelOps. MLOps is focused on the operationalization of ML models, while ModelOps covers the operationalization of all types of AI models.",
            "url": "https://en.wikipedia.org/wiki/MLOps",
            "id": 83     
        },          
        {
            "name": "Internet of things (IoT)",
            "definition": "The Internet of things (IoT) describes physical objects (or groups of such objects) with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks. Internet of things has been considered a misnomer because devices do not need to be connected to the public internet, they only need to be connected to a network and be individually addressable.\n\nThe field of IoT has evolved due to the convergence of multiple technologies, including ubiquitous computing, commodity sensors, increasingly powerful embedded systems, and machine learning. Traditional fields of embedded systems, wireless sensor networks, control systems, automation (including home and building automation), independently and collectively enable the Internet of things.\n\nIn the consumer market, IoT technology is most synonymous with products pertaining to the concept of the ‘smart home’, including devices and appliances (such as lighting fixtures, thermostats, home security systems, cameras, and other home appliances) that support one or more common ecosystems, and can be controlled via devices associated with that ecosystem, such as smartphones and smart speakers. IoT is also used in healthcare systems.",
            "url": "https://en.wikipedia.org/wiki/Internet_of_things",
            "id": 84     
        },          
        {
            "name": "Machine learning (ML)",
            "definition": "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.\n\nA subset of machine learning is closely related to computational statistics, which focuses on making predictions using computers; but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. \n\nData mining is a related field of study, focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning use data and neural networks in a way that mimics the working of a biological brain. In its application across business problems, machine learning is also referred to as predictive analytics.",
            "url": "https://en.wikipedia.org/wiki/Machine_learning",
            "id": 85     
        },           
        {
            "name": "Always On VPN (AOVPN)",
            "definition": "Microsoft’s Always On VPN is the revamp of DirectAccess remote access technology seeking to overcome the limitations of DirectAccess and achieve much wider adoption. With the new Always On VPN technology, Microsoft is looking to achieve a single solution of remote access that supports a wide array of clients. Like DirectAccess, the VPN connection is ‘Always On’ meaning there is no user input required unless multi-factor authentication is enabled. As soon as a client is connected to the Internet, the VPN connection is established.\n\nAOVPN’s range of supported clients, unlike DirectAccess, includes more than simply domain-joined clients: Domain-joined, Non Domain-joined, Azure AD-joined devices, BYOD. Microsoft’s AOVPN applies to to the Microsoft Windows Server and Windows operating systems. Such as Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2 and Windows 10.",
            "url": "https://docs.microsoft.com/en-us/windows-server/remote/remote-access/vpn/always-on-vpn/always-on-vpn-technology-overview",
            "id": 86    
        },           
        {
            "name": "API (Application Programming Interface)",
            "definition": "An API (Application Programming Interface) is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build or use such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API.",
            "url": "https://en.wikipedia.org/wiki/API",
            "id": 87     
        },        
        {
            "name": "Attribute",
            "definition": "In computing, an attribute is a specification that defines a property of an object, element, or file. It may also refer to or set the specific value for a given instance of such. For clarity, attributes should more correctly be considered metadata.\n\nAn attribute is frequently and generally a property of a property. However, in actual usage, the term attribute can and is often treated as equivalent to a property depending on the technology being discussed. An attribute of an object usually consists of a name and a value; of an element, a type or class name; of a file, a name and extension.",
            "url": "https://en.wikipedia.org/wiki/Attribute_(computing)",
            "id": 88     
        },        
        {
            "name": "Frontend and backend",
            "definition": "In software engineering, the terms frontend and backend (or sometimes referred to as back end or back-end) refer to the separation of concerns between the presentation layer (frontend), and the data access layer (backend) of a piece of software, or the physical infrastructure or hardware.\n\nIn the client–server model, the client is usually considered the frontend and the server is usually considered the backend, even when some presentation work is actually done on the server itself.",
            "url": "https://en.wikipedia.org/wiki/Frontend_and_backend",
            "id": 89     
        },        
        {
            "name": "Cache",
            "definition": "In computing, a cache is a hardware or software component that stores data so that future requests for that data can be served faster; the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere.\n\nA cache hit occurs when the requested data can be found in a cache, while a cache miss occurs when it cannot. Cache hits are served by reading data from the cache, which is faster than recomputing a result or reading from a slower data store; thus, the more requests that can be served from the cache, the faster the system performs.",
            "url": "https://en.wikipedia.org/wiki/Cache_(computing)",
            "id": 90     
        },        
        {
            "name": "Content management system (CMS)",
            "definition": "Computer software used to manage the creation and modification of digital content (content management). Features of CMS may include:\n\n\n\n- Format management facilitates turning scanned paper documents and legacy electronic documents into HTML or PDF documents.\n- Publishing functionality allows individuals to use a template or a set of templates approved by the organization, as well as wizards and other tools to create or modify content.\n- Revision features allow content to be updated and edited after initial publication. Revision control also tracks any changes made to files by individuals.\n\nA CMS typically has two major components: a content management application (CMA), as the front-end user interface that allows a user, even with limited expertise, to add, modify, and remove content from a website without the intervention of a webmaster; and a content delivery application (CDA), that compiles the content and updates the website.",
            "url": "https://en.wikipedia.org/wiki/Content_management_system",
            "id": 91     
        },  
        {
            "name": "Web crawler",
            "definition": "A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering).\n\nWeb search engines and some other websites use Web crawling or spidering software to update their web content or indices of other sites' web content. Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently.\n\nCrawlers consume resources on visited systems and often visit sites unprompted. Issues of schedule, load, and 'politeness' come into play when large collections of pages are accessed. Mechanisms exist for public sites not wishing to be crawled to make this known to the crawling agent. For example, including a robots.txt file can request bots to index only parts of a website, or nothing at all.",
            "url": "https://en.wikipedia.org/wiki/Web_crawler",
            "id": 92     
        },        
        {
            "name": "Customer relationship management (CRM)",
            "definition": "Customer relationship management (CRM) is a process in which a business or other organization administers its interactions with customers, typically using data analysis to study large amounts of information.\n\nCRM systems compile data from a range of different communication channels, including a company's website, telephone, email, live chat, marketing materials and more recently, social media. They allow businesses to learn more about their target audiences and how to best cater for their needs, thus retaining customers and driving sales growth.\n\nCRM may be used with past, present or potential customers. The concepts, procedures, and rules that a corporation follows when communicating with its consumers are referred to as CRM.",
            "url": "https://en.wikipedia.org/wiki/Customer_relationship_management",
            "id": 93     
        },        
        {
            "name": "CSS (Cascading Style Sheets)",
            "definition": "Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.\n\nCSS is designed to enable the separation of presentation and content, including layout, colors, and fonts. This separation can improve content accessibility; provide more flexibility and control in the specification of presentation characteristics; enable multiple web pages to share formatting by specifying the relevant CSS in a separate .css file, which reduces complexity and repetition in the structural content; and enable the .css file to be cached to improve the page load speed between the pages that share the file and its formatting.",
            "url": "https://en.wikipedia.org/wiki/CSS",
            "id": 94     
        },        
        {
            "name": "Call to action (CTA)",
            "definition": "A call to action (CTA) is a prompt on a website that tells the user to take some specified action. A call to action is typically written as a command or action phrase, such as ‘Sign Up’ or ‘Buy Now’ and generally takes the form of a button or hyperlink. In digital marketing this can take the form of the text on a button (a CTA button) or a web link and in email campaigns CTAs are often links to a webpage where the user can take further action.",
            "url": "https://www.optimizely.com/optimization-glossary/call-to-action",
            "id": 95     
        },        
        {
            "name": "GUI (Graphical User Interface)",
            "definition": "The graphical user interface (GUI) is a form of user interface that allows users to interact with electronic devices through graphical icons and audio indicator such as primary notation, instead of text-based user interfaces, typed command labels or text navigation. GUIs were introduced in reaction to the perceived steep learning curve of command-line interfaces (CLIs), which require commands to be typed on a computer keyboard.",
            "url": "https://en.wikipedia.org/wiki/Graphical_user_interface",
            "id": 96     
        },        
        {
            "name": "HTML (Hypertext Markup Language)",
            "definition": "The HyperText Markup Language, or HTML, is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript. Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.\n\nHTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags but use them to interpret the content of the page.\n\nHTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997. A form of HTML, known as HTML5, is used to display video and audio, primarily using the <canvas> element, in collaboration with JavaScript.",
            "url": "https://en.wikipedia.org/wiki/HTML",
            "id": 97     
        },        
        {
            "name": "Meta element",
            "definition": "Meta elements are tags used in HTML and XHTML documents to provide structured metadata about a Web page. They are part of a web page's head section. Multiple Meta elements with different attributes can be used on the same page. Meta elements can be used to specify page description, keywords and any other metadata not provided through the other head elements and attributes. The meta element has two uses: either to emulate the use of an HTTP response header field, or to embed additional metadata within the HTML document. Two examples:\n\n<meta name='generator' content='MediaWiki 1.39.0-wmf.7'>\n<meta name='referrer' content='origin-when-cross-origin'>",
            "url": "https://en.wikipedia.org/wiki/Meta_element",
            "id": 98     
        },        
        {
            "name": "OOTB (Out of the box)",
            "definition": "An out-of-the-box feature or functionality (also called OOTB or off the shelf), particularly in software, is a native feature or built-in functionality of a product that comes directly from the vendor and works immediately when the product is placed in service. In the context of software, out-of-the-box features and functionality are available for all users by default and do not require customization, modification, configuration, scripting, add-ons, modules, third-party tools, or additional fees in order to be used.",
            "url": "https://medium.com/swlh/out-of-box-vs-custom-software-solutions-143ad473d29d",
            "id": 99     
        },        
        {
            "name": "COTS (Commercial off-the-shelf)",
            "definition": "Commercial off-the-shelf or commercially available off-the-shelf (COTS) products are packaged or canned (ready-made) hardware or software, which are adapted aftermarket to the needs of the purchasing organization, rather than the commissioning of custom-made, or bespoke, solutions. A related term, Mil-COTS, refers to COTS products for use by the U.S. military.\n\nIn the context of the U.S. government, the Federal Acquisition Regulation (FAR) has defined ‘COTS’ as a formal term for commercial items, including services, available in the commercial marketplace that can be bought and used under government contract. For example, Microsoft is a COTS software provider. COTS purchases are alternatives to custom software or one-off developments – government-funded developments or otherwise.\n\nAlthough COTS products can be used out of the box, in practice the COTS product must be configured to achieve the needs of the business and integrated to existing organizational systems. Extending the functionality of COTS products via custom development is also an option, however this decision should be carefully considered due to the long term support and maintenance implications. Such customized functionality is not supported by the COTS vendor, so brings its own sets of issues when upgrading the COTS product.\n\nThe use of COTS has been mandated across many government and business programs, as such products may offer significant savings in procurement, development, and maintenance. In the 1990s, many regarded COTS as extremely effective in reducing the time and cost of software development.  COTS software came with many not-so-obvious tradeoffs— a reduction in initial cost and development time over an increase in software component-integration work, dependency on the vendor, security issues and incompatibilities from future changes.",
            "url": "https://en.wikipedia.org/wiki/Commercial_off-the-shelf",
            "id": 100     
        },        
        {
            "name": "Responsive design",
            "definition": "Responsive web design (RWD) or responsive design is an approach to web design that aims to make web pages render well on a variety of devices and window or screen sizes from minimum to maximum display size to ensure usability and satisfaction.\n\nA responsive design adapts the web-page layout to the viewing environment by using techniques such as fluid proportion-based grids, flexible images, and CSS3 media queries, an extension of the @media rule, in the following ways:\n\n\n1. The fluid grid concept calls for page element sizing to be in relative units like percentages, rather than absolute units like pixels or points.\n2. Flexible images are also sized in relative units, so as to prevent them from displaying outside their containing element.\n3. Media queries allow the page to use different CSS style rules based on characteristics of the device the site is being displayed on, e.g. width of the rendering surface (browser window width or a physical display size).\n4. Responsive layouts automatically adjust and adapt to any device screen size, whether it is a desktop, a laptop, a tablet, or a mobile phone.\n\n\nResponsive web design became more important as users of mobile devices came to account for the majority of web site visitors",
            "url": "https://en.wikipedia.org/wiki/Responsive_web_design",
            "id": 101     
        },        
        {
            "name": "UI vs. UX",
            "definition": "A user interface (UI) is a place where interactions between humans and machines occur. It allows users to effectively operate a machine to complete a task or achieve a specific goal, like making a purchase or downloading an app. The three most common UIs are the command line interface, graphic user interface, and voice-enabled user interface. Essential properties of a well-designed UI include clarity, familiarity, consistency, forgiveness and efficiency. The primary interface design techniques are prototyping and simulation.\n\nUser experience (UX) is the experience that a person has as they interact with a product. The term was coined by Don Norman back in the 90s when he worked at Apple. Don Norman says that ‘’User experience’ encompasses all aspects of the end-users interaction with the company, its services, and its products.’ UX designers incorporate the ideas of user persona and user journey into their research and design. These understandings help them to propose design solutions that works the best for their users.\n\nThe meanings of UX and UI imply that they are related design disciplines, yet they are very different in nature. The UI design is more concerned with the visual properties of design as well as the overall feel it conveys (i.e., is it aesthetically pleasing?). UX design is more analytical; It’s rooted in cognitive behavior and human psychology.",
            "url": "https://xd.adobe.com/ideas/process/ui-design/ui-vs-ux-design-understanding-similarities-and-differences/",
            "id": 102     
        },        
        {
            "name": "What You See is What You Get (WYSIWYG)",
            "definition": "In computing, WYSIWYG, an acronym for What You See Is What You Get, is a system in which editing software allows content to be edited in a form that resembles its appearance when printed or displayed as a finished product, such as a printed document, web page, or slide presentation. WYSIWYG implies a user interface that allows the user to view something very similar to the end result while the document is being created. In general, WYSIWYG implies the ability to directly manipulate the layout of a document without having to type or remember names of layout commands.",
            "url": "https://en.wikipedia.org/wiki/WYSIWYG",
            "id": 103     
        },        
        {
            "name": "Three-tier architecture",
            "definition": "Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: the presentation tier, or user interface; the application tier, where data is processed; and the data tier, where the data associated with the application is stored and managed.\n\nThe chief benefit of three-tier architecture is that because each tier runs on its own infrastructure, each tier can be developed simultaneously by a separate development team, and can be updated or scaled as needed without impacting the other tiers. Three-tier architecture is the predominant software architecture for traditional client-server applications.\n\nA 3-tier application is a program that is organized into three major parts: the workstation or presentation interface; the business logic; and the database and related programming. Each of these is distributed to one or more separate places on a network.",
            "url": "https://www.ibm.com/cloud/learn/three-tier-architecture",
            "id": 104     
        },        
        {
            "name": "Agile software development",
            "definition": "In software development, agile (sometimes written Agile) practices include requirements discovery and solutions improvement through the collaborative effort of self-organizing and cross-functional teams with their customer(s)/end user(s), adaptive planning, evolutionary development, early delivery, continual improvement, and flexible responses to changes in requirements, capacity, and understanding of the problems to be solved.\n\nPopularized in the 2001 Manifesto for Agile Software Development, these values and principles were derived from and underpin a broad range of software development frameworks, including Scrum and Kanban.",
            "url": "https://en.wikipedia.org/wiki/Agile_software_development",
            "id": 105     
        },        
        {
            "name": "Amelioration pattern",
            "definition": "In software engineering, an amelioration pattern is a design pattern that describes how to go from a bad solution to a better one. In other words, it is an anti-pattern formed when an existing software design pattern was edited (i.e. rearranged, added or deleted) to better suit a particular problem so as to achieve some further effect or behavior. In this sense, an amelioration pattern is transformational in character.",
            "url": "https://dl.acm.org/doi/10.5555/1035053.1035074",
            "id": 106     
        },        
        {
            "name": "Anti-pattern",
            "definition": "An anti-pattern in software engineering, project management, and business processes is a common response to a recurring problem that is usually ineffective and risks being highly counterproductive. The term, coined in 1995 by computer programmer Andrew Koenig, was inspired by the book Design Patterns (which highlights a number of design patterns in software development that its authors considered to be highly reliable and effective) and first published in his article in the Journal of Object-Oriented Programming. A further paper in 1996 presented by Michael Ackroyd at the Object World West Conference also documented anti-patterns.\n\nIt was, however, the 1998 book AntiPatterns that both popularized the idea and extended its scope beyond the field of software design to include software architecture and project management. Other authors have extended it further since to encompass environmental/organizational/cultural anti-patterns.",
            "url": "https://en.wikipedia.org/wiki/Anti-pattern",
            "id": 107     
        },        
        {
            "name": "Aspect-Oriented Programming (AOP)",
            "definition": "Aspect-Oriented Programming (AOP). Nearly all programming paradigms support some level of grouping and encapsulation of concerns into separate, independent entities. Aspect-oriented programming entails breaking down program logic into distinct parts (so-called concerns, which are cohesive areas of functionality). AOP aims to increase modularity by allowing the separation of cross-cutting concerns.\n\n Systems are composed of several components, each responsible for a specific piece of functionality. But often these components also carry additional responsibilities beyond their core functionality. System services such as logging, transaction management, and security often find their way into components whose core responsibilities is something else. These system services are commonly referred to as cross-cutting concerns because they tend to cut across multiple components in a system. Logging exemplifies a crosscutting concern because a logging strategy necessarily affects every logged part of the system. Logging thereby crosscuts all logged classes and methods. \n\nAspect-oriented programming allows for the creation of relationships between different classes. These relationships are arbitrary, but can be used to encapsulate the housekeeping code needed to create compatibility between two classes.\n\nAOP is a technique for building common, reusable routines that can be applied applicationwide. During development this facilitates separation of core application logic and common, repeatable tasks (input validation, logging, error handling, etc.). At runtime, you can use AOP to hot-patch applications that are vulnerable to SQL injection, or embed intrusion detection and audit logging capabilities directly into an application without modifying the underlying source code.",
            "url": "https://en.wikipedia.org/wiki/Aspect-oriented_programming",
            "id": 108     
        },        
        {
            "name": "Capability Maturity Model",
            "definition": "A methodology used to develop and refine an organization's software development process. The model describes a five-level evolutionary path of increasingly organized and systematically more mature processes.",
            "url": "https://en.wikipedia.org/wiki/Capability_Maturity_Model",
            "id": 109     
        },        
        {
            "name": "Data modeling",
            "definition": "Data modeling in software engineering is the process of creating a data model for an information system by applying certain formal techniques. Data modeling is a process used to define and analyze data requirements needed to support the business processes within the scope of corresponding information systems in organizations. Therefore, the process of data modeling involves professional data modelers working closely with business stakeholders, as well as potential users of the information system.\n\nData modeling techniques and methodologies are used to model data in a standard, consistent, predictable manner in order to manage it as a resource. The use of data modeling standards is strongly recommended for all projects requiring a standard means of defining and analyzing data within an organization, e.g., using data modeling:\n\n- to assist business analysts, programmers, testers, manual writers, IT package selectors, engineers, managers, related organizations and clients to understand and use an agreed upon semi-formal model that encompasses the concepts of the organization and how they relate to one another\n- to manage data as a resource\n- to integrate information systems\n- to design databases/data warehouses (aka data repositories)\n\nData modeling may be performed during various types of projects and in multiple phases of projects. Data models are progressive; there is no such thing as the final data model for a business or application. Instead a data model should be considered a living document that will change in response to a changing business. The data models should ideally be stored in a repository so that they can be retrieved, expanded, and edited over time.",
            "url": "https://en.wikipedia.org/wiki/Data_modeling",
            "id": 110     
        },        
        {
            "name": "Driver",
            "definition": "In computing, a device driver is a computer program that operates or controls a particular type of device that is attached to a computer or automaton. A driver provides a software interface to hardware devices, enabling operating systems and other computer programs to access hardware functions without needing to know precise details about the hardware being used.\n\nA driver communicates with the device through the computer bus or communications subsystem to which the hardware connects. When a calling program invokes a routine in the driver, the driver issues commands to the device (drives it). Once the device sends data back to the driver, the driver may invoke routines in the original calling program.\n\nDrivers are hardware dependent and operating-system-specific. They usually provide the interrupt handling required for any necessary asynchronous time-dependent hardware interface.\n\nPreviously, we have been describing a hardware device driver. Now, a driver in software provides a programming interface to control and manage specific lower level interfaces that are often linked to a specific type of hardware, or other low-level service. In the case of hardware, the specific subclass of drivers controlling physical or virtual hardware devices are known as device drivers. E.g., a client library for connecting to a database is often known as a driver, for example the MySQL native driver for PHP.",
            "url": "https://en.wikipedia.org/wiki/Device_driver",
            "id": 111     
        },        
        {
            "name": "Elegant solution",
            "definition": "An elegant solution is used in mathematics, engineering and software development to refer to a solution that solves the problem in the simplest and most effective manner. In many cases, it is possible for developers to created code that is more complicated than it needs to be. In such cases, this less-than-elegant code is more likely to cause other issues. For most developers, finding an elegant solution is a greater challenge than simply solving a problem.",
            "url": "https://www.techopedia.com/definition/14357/elegant-solution",
            "id": 112     
        },             
        {
            "name": "Exploratory engineering",
            "definition": "Exploratory engineering is a term coined by K. Eric Drexler to describe the process of designing and analyzing detailed hypothetical models of systems that are not feasible with current technologies or methods, but do seem to be clearly within the bounds of what science considers to be possible within the narrowly defined scope of operation of the hypothetical system model. It usually results in paper or video prototypes, or (more likely nowadays) computer simulations that are as convincing as possible to those that know the relevant science, given the lack of experimental confirmation. By analogy with protoscience, it might be considered a form of protoengineering.",
            "url": "https://en.wikipedia.org/wiki/Exploratory_engineering",
            "id": 113     
        },        
        {
            "name": "Exploratory model",
            "definition": "The exploratory model is an experimental, research-based systems development method used to develop and design a computer system or product. The exploratory model is based on planning and reviewing potential scenarios and approaches until the one that appears to be optimal is selected.",
            "url": "https://www.techopedia.com/definition/16383/exploratory-model",
            "id": 114     
        },        
        {
            "name": "Extreme programming (XP)",
            "definition": "A software development methodology intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development, it advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted.\n\nOther elements of extreme programming include: programming in pairs or doing extensive code review, unit testing of all code, not programming features until they are actually needed, a flat management structure, code simplicity and clarity, expecting changes in the customer's requirements as time passes and the problem is better understood, and frequent communication with the customer and among programmers.",
            "url": "https://en.wikipedia.org/wiki/Extreme_programming",
            "id": 115     
        },        
        {
            "name": "Feature creep",
            "definition": "Feature creep is the excessive ongoing expansion or addition of new features in a product, especially in computer software, video games and consumer and business electronics. These extra features go beyond the basic function of the product and can result in software bloat and over-complication, rather than simple design. The definition of what qualifies as 'feature creep' does vary among end users, where what is perceived as such by some users may be considered practical functionality by others.\n\nThe most common cause of feature creep is the desire to provide the consumer with a more useful or desirable product, in order to increase sales or distribution. However, once the product reaches the point at which it does everything that it is designed to do, the manufacturer is left with the choice between adding functions some users might consider unneeded (sometimes at the cost of efficiency), and sticking with the old version (at the cost of a perceived lack of improvement).\n\nAnother major cause of feature creep might be a compromise from a committee which decides to implement multiple, different viewpoints or use cases in the same product. Then, as more features are added to support each approach, it might be necessary to have cross-conversion features between the multiple paradigms, further complicating the total features.",
            "url": "https://en.wikipedia.org/wiki/Feature_creep",
            "id": 116     
        },        
        {
            "name": "Functional specification",
            "definition": "A functional specification (also, functional spec, specs, functional specifications document (FSD), functional requirements specification) in systems engineering and software development is a document that specifies the functions that a system or component must perform (often part of a requirements specification).\n\nThe documentation typically describes what is needed by the system user as well as requested properties of inputs and outputs (e.g. of the software system). A functional specification is the more technical response to a matching requirements document, e.g. the Product Requirements Document ‘PRD’. Thus it picks up the results of the requirements analysis stage. On more complex systems multiple levels of functional specifications will typically nest to each other, e.g. on the system level, on the module level and on the level of technical details.",
            "url": "https://en.wikipedia.org/wiki/Functional_specification",
            "id": 117     
        },        
        {
            "name": "Gantt chart",
            "definition": "A Gantt chart is a type of bar chart that illustrates a project schedule, named after its popularizer, Henry Gantt (1861–1919), who designed such a chart around the years 1910–1915. Modern Gantt charts also show the dependency relationships between activities and the current schedule status.",
            "url": "https://en.wikipedia.org/wiki/Gantt_chart",
            "id": 118     
        },        
        {
            "name": "Genetic programming (GP)",
            "definition": "A model of programming which uses biological principles to handle a complex problem, most appropriately with problems in which there are a large number of fluctuating variables, such as those related to artificial intelligence. Genetic programming involves techniques to create algorithms that can program themselves by simulating biological breeding and Darwinian evolution. Instead of programming a model that can solve a particular problem, genetic programming only provides a general objective and lets the model figure out the details itself.",
            "url": "https://en.wikipedia.org/wiki/Genetic_programming",
            "id": 119     
        },        
        {
            "name": "Generic programming",
            "definition": "Generic programming is a style of computer programming in which algorithms are written in terms of types to-be-specified-later that are then instantiated when needed for specific types provided as parameters. This approach, pioneered by the ML programming language in 1973, permits writing common functions or types that differ only in the set of types on which they operate when used, thus reducing duplication. Such software entities are known as generics in Ada, C#, Delphi, Eiffel, F#, Java, Nim, Python, Go, Rust, Swift, TypeScript and Visual Basic .NET. They are known as parametric polymorphism in ML, Scala, Julia, and Haskell (the Haskell community also uses the term 'generic' for a related but somewhat different concept); templates in C++ and D; and parameterized types in the influential 1994 book Design Patterns.\n\nThe term 'generic programming' was originally coined by David Musser and Alexander Stepanov in a more specific sense than the above, to describe a programming paradigm whereby fundamental requirements on types are abstracted from across concrete examples of algorithms and data structures and formalized as concepts, with generic functions implemented in terms of these concepts, typically using language genericity mechanisms as described above.",
            "url": "https://en.wikipedia.org/wiki/Generic_programming",
            "id": 120     
        },        
        {
            "name": "Gold code",
            "definition": "Program source code that is ready for commercial distribution. Gold code is the final form of software code before the software's commercial release. A software usually undergoes several development phases before it becomes gold code. First, software functions are individually developed and tested with each newly added function. Then, a graphical user interface is added so that users can perform functions via several means, including buttons, task bars and keyboard shortcuts. Finally, a team tests different function sequences to ensure there are no hidden bugs.\n\nWhen a vendor says its product ‘has gone gold’, it means the source code has been compiled into an executable program ready for sale. The next steps are to turn it into an installable product and create a CD or DVD ‘golden master’ (GM) for the disc manufacturer or into a file for Web downloads.",
            "url": "https://www.techopedia.com/definition/16387/gold-code",
            "id": 121     
        },        
        {
            "name": "Patch vs. Hotfix vs. Coldfix vs. Bugfix",
            "definition": "Patch vs Hotfix vs Coldfix vs Bugfix. Patches are often temporary fixes between full releases of software packages. Patches are used to correct both large and small issues that may or may not require fixing a software bug, installing new drivers, addressing new security vulnerabilities, addressing software stability issues or upgrading the software. Generally, patches are automatic updates that self-install packages in various sizes and are delivered on a set schedule. They can be included in the product’s new version release with additional updates and fixes.\n\nHotfixes can also solve many of the same issues as a patch, but it is applied to a ‘hot’ system—a live system—to fix an issue immediately and without creating system downtimes or outages. Normally, you’ll create a hotfix quickly, as an urgent measure against issues that need to be fixed immediately and outside of your normal development flow. Unlike patches, hotfixes address very specific issues like adding a new feature, bug, or security fix or changing database schema. Importantly, hotfixes are not always publicly released, in contrast to patches.\n\nWhere a hotfix is executed quickly without restarting any systems or hardware, a coldfix is just the opposite. Implementing a coldfix requires users to log out of the software while entire systems need to be rebooted for fixes to go into effect. They’re normally announced several days ahead of time to give users advanced notice the service will be unavailable while the fix is completed. Notices generally include estimated times the service will be back online.\n\nA bugfix sounds a lot like a hotfix, but the difference lies in the timing and execution of the correction. Bugfixes generally describe issues that are found and resolved during production or testing phases or even after deployment as part of the normal release cycle of a product. Hotfixes are applied only after the product has been released and is live. Implementing a bugfix, also known as a program temporary fix (PTF), can be as simple as adding missing parentheses in a piece of code. But the fix can become quite challenging if the symptoms don’t clearly point to a cause. Once you’ve uncovered the root cause and issued a bug fix, it’s not uncommon for your programmers to find that one bugfix can actually introduce a new bug.",
            "url": "https://www.bmc.com/blogs/patch-hotfix-coldfix-bugfix/",
            "id": 122     
        },        
        {
            "name": "Integrated development environment (IDE)",
            "definition": "An Integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. Some IDEs, such as NetBeans and Eclipse, contain the necessary compiler, interpreter, or both; others, such as SharpDevelop and Lazarus, do not.\n\nThe boundary between an IDE and other parts of the broader software development environment is not well-defined; sometimes a version control system or various tools to simplify the construction of a graphical user interface (GUI) are integrated. Many modern IDEs also have a class browser, an object browser, and a class hierarchy diagram for use in object-oriented software development.",
            "url": "https://en.wikipedia.org/wiki/Integrated_development_environment",
            "id": 123     
        },        
        {
            "name": "Independent software vendor (ISV)",
            "definition": "An independent software vendor, or ISV, is an individual or organization that develops, markets, and sells software solutions that run on one or more computer hardware providers like Macintosh, operating systems like iOS, or cloud platforms like Amazon Web Services.\n\nComputer hardware providers, operating systems, and cloud platforms will all test independent software vendors who want to offer their software solutions on their marketplace. But they’ll only allow, or ISV certify, the independent software vendors who can offer the most relevant and best software solutions on their marketplaces.\n\nFor example, Microsoft, a company that develops computer hardware (Xbox), operating systems (Windows), and a cloud platform (Azure), offers silver and gold ISV certifications to independent software vendors whose products can pass their rigorous quality tests and prove they can offer the top software solutions to Microsoft’s customers on each of their marketplaces.",
            "url": "https://en.wikipedia.org/wiki/Independent_software_vendor",
            "id": 124     
        },        
        {
            "name": "Joint application development (JAD)",
            "definition": "Joint Application Development, in short JAD, is the process which is used to design and develop computer based system/solutions. It collects requirements side by side as per business needs while developing new information systems for a company that means JAD involves the client or end-users in designing and development process. It also comprises of approaches for improving the quality of specification and user participation through a successive collaborative workshops called JAD sessions. Since client is involved throughout the development process it leads to faster development times and greater client satisfaction.",
            "url": "https://en.wikipedia.org/wiki/Joint_application_design",
            "id": 125     
        },           
        {
            "name": "KISS Principle (Keep It Simple, Stupid)",
            "definition": "KISS, an acronym for 'keep it simple, stupid', is a design principle noted by the U.S. Navy in 1960. The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided. The phrase has been associated with aircraft engineer Kelly Johnson. The term ‘KISS principle’ was in popular use by 1970. Variations on the phrase include: ‘Keep it simple, silly’, ‘keep it short and simple’, ‘keep it short and sweet’, ‘keep it simple and straightforward’, ‘keep it small and simple’, ‘keep it simple, soldier’, ‘keep it simple, sailor’, or ‘keep it sweet and simple’.",
            "url": "https://en.wikipedia.org/wiki/KISS_principle",
            "id": 126      
        },     
        {
            "name": "Source lines of code (SLOC)",
            "definition": "Source lines of code (SLOC), also known as lines of code (LOC), is a software metric used to measure the size of a computer program by counting the number of lines in the text of the program's source code. SLOC is typically used to predict the amount of effort that will be required to develop a program, as well as to estimate programming productivity or maintainability once the software is produced.",
            "url": "https://en.wikipedia.org/wiki/Source_lines_of_code",
            "id": 127      
        }, 
        {
            "name": "Lean software development",
            "definition": "Lean software development is a translation of lean manufacturing principles and practices to the software development domain. Adapted from the Toyota Production System, it is emerging with the support of a pro-lean subculture within the agile community. Lean offers a solid conceptual framework, values and principles, as well as good practices, derived from experience, that support agile organizations.\n\nLean development can be summarized by seven principles, very close in concept to lean manufacturing principles:\n\n\n1. Eliminate waste\n2. Amplify learning\n3. Decide as late as possible\n4. Deliver as fast as possible\n5. Empower the team\n6. Build integrity in\n7. Optimize the whole\n",
            "url": "https://en.wikipedia.org/wiki/Lean_software_development",
            "id": 128      
        }, 
        {
            "name": "Legacy system",
            "definition": "In computing, a legacy system is an old method, technology, computer system, or application program, ‘of, relating to, or being a previous or outdated computer system,’ yet still in use. Often referencing a system as ‘legacy’ means that it paved the way for the standards that would follow it. This can also imply that the system is out of date or in need of replacement.\n\nLegacy code is old computer source code. It could simply refer to an organization's existing code base which has been written over many years, or it could imply a codebase that is in some respect obsolete or supporting something obsolete. Long-lived code is susceptible to software rot, where changes to the runtime environment, or surrounding software or hardware may require maintenance or emulation of some kind to keep working. Legacy code may be present to support legacy hardware, a separate legacy system, or a legacy customer using an old feature or software version.",
            "url": "https://en.wikipedia.org/wiki/Legacy_system",
            "id": 129      
        }, 
        {
            "name": "Object-oriented programming (OOP)",
            "definition": "Object-oriented programming (OOP) is a programming paradigm based on the concept of ‘objects’, which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).\n\nA feature of objects is that an object's own procedures can access and often modify the data fields of itself (objects have a notion of this or self). In OOP, computer programs are designed by making them out of objects that interact with one another. OOP languages are diverse, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types.\n\nMany of the most widely used programming languages (such as C++, Java, Python, etc.) are multi-paradigm and they support object-oriented programming to a greater or lesser degree, typically in combination with imperative, procedural programming. Significant object-oriented languages include: Java, C++, C#, Python, R, PHP, Visual Basic.NET, JavaScript, Ruby, Perl, SIMSCRIPT, Object Pascal, Objective-C, Dart, Swift, Scala, Kotlin, Common Lisp, MATLAB, and Smalltalk.",
            "url": "https://en.wikipedia.org/wiki/Object-oriented_programming",
            "id": 130      
        },   
        {
            "name": "Pasta theory of programming",
            "definition": "Pasta theory of programming. The idea that various programming structures can be likened to the structures of well-known pasta dishes:\n\nUnstructured procedural programming is called spaghetti code. Spaghetti code is often considered a pejorative phrase for unstructured and difficult-to-maintain source code. In this sense, spaghetti code can be caused by several factors, such as volatile project requirements, lack of programming style rules, and software engineers with insufficient ability or experience.\n\nLasagna code refers to structured programming code whose layers are so complicated and intertwined that making a change in one layer would necessitate changes in all other layers.\n\nRavioli code is a term specific to object-oriented programming. It describes code that comprises well-structured classes that are easy to understand in isolation, but difficult to understand as a whole.",
            "url": "https://en.wikipedia.org/wiki/Spaghetti_code",
            "id": 131      
        },     
        {
            "name": "Polymorphism",
            "definition": "Polymorphism is an object-oriented programming concept that refers to the ability of a variable, function or object to take on multiple forms. A language that features polymorphism allows developers to program in the general rather than program in the specific.\n\nIn a programming language that exhibits polymorphism, objects of classes belonging to the same hierarchical tree (inherited from a common base class) may possess functions bearing the same name, but each having different behaviors.\n\nIn effect, polymorphism cuts down the work of the developer because he can now create a sort of general class with all the attributes and behaviors that he envisions for it. When the time comes for the developer to create more specific subclasses with certain unique attributes and behaviors, the developer can simply alter code in the specific portions where the behaviors differ. All other portions of the code can be left as is.\n\nTo know whether an object is polymorphic, you can perform a simple test. If the object successfully passes multiple is-a or instanceof tests, it’s polymorphic.",
            "url": "https://en.wikipedia.org/wiki/Polymorphism_(computer_science)",
            "id": 132      
        }, 
        {
            "name": "Duck typing",
            "definition": "Duck typing in computer programming is an application of the duck test—‘If it walks like a duck and it quacks like a duck, then it must be a duck’—to determine whether an object can be used for a particular purpose. With nominative typing, an object is of a given type if it is declared to be (or if a type's association with the object is inferred through mechanisms such as object inheritance).\n\nIn duck typing, an object is of a given type if it has all methods and properties required by that type. Duck typing can be viewed as a usage-based structural equivalence between a given object and the requirements of a type.",
            "url": "https://en.wikipedia.org/wiki/Duck_typing",
            "id": 133      
        }, 
        {
            "name": "Pseudocode",
            "definition": "In computer science, pseudocode is a plain language description of the steps in an algorithm or another system. Pseudocode often uses structural conventions of a normal programming language, but is intended for human reading rather than machine reading. It typically omits details that are essential for machine understanding of the algorithm, such as variable declarations and language-specific code.\n\n The purpose of using pseudocode is that it is easier for people to understand than conventional programming language code, and that it is an efficient and environment-independent description of the key principles of an algorithm. It is commonly used in textbooks and scientific publications to document algorithms and in planning of software and other algorithms.\n\nNo broad standard for pseudocode syntax exists, as a program in pseudocode is not an executable program; however, certain limited standards exist (such as for academic assessment). Pseudocode resembles skeleton programs, which can be compiled without errors. Flowcharts, drakon-charts and Unified Modelling Language (UML) charts can be thought of as a graphical alternative to pseudocode, but need more space on paper. Languages such as HAGGIS bridge the gap between pseudocode and code written in programming languages.",
            "url": "https://en.wikipedia.org/wiki/Pseudocode",
            "id": 134      
        }, 
        {
            "name": "Rapid application development (RAD)",
            "definition": "Rapid application development (RAD), also called rapid application building (RAB), is both a general term for adaptive software development approaches, and the name for James Martin's method of rapid development. In general, RAD approaches to software development put less emphasis on planning and more emphasis on an adaptive process. Prototypes are often used in addition to or sometimes even instead of design specifications.\n\nRAD is especially well suited for (although not limited to) developing software that is driven by user interface requirements. Graphical user interface builders are often called rapid application development tools. Other approaches to rapid development include the adaptive, agile, spiral, and unified models.",
            "url": "https://en.wikipedia.org/wiki/Rapid_application_development",
            "id": 135      
        }, 
        {
            "name": "Iterative and incremental development",
            "definition": "Iterative and incremental development is any combination of both iterative design or iterative method and incremental build model for development. Usage of the term began in software development, with a long-standing combination of the two terms iterative and incremental having been widely suggested for large development efforts. For example, the 1985 DOD-STD-2167 mentions (in section 4.1.2): ‘During software development, more than one iteration of the software development cycle may be in progress at the same time.’ and 'This process may be described as an evolutionary acquisition or incremental build approach.' In software, the relationship between iterations and increments is determined by the overall software development process.\n\nThe basic idea behind this method is to develop a system through repeated cycles (iterative) and in smaller portions at a time (incremental), allowing software developers to take advantage of what was learned during development of earlier parts or versions of the system. Learning comes from both the development and use of the system, where possible key steps in the process start with a simple implementation of a subset of the software requirements and iteratively enhance the evolving versions until the full system is implemented. At each iteration, design modifications are made and new functional capabilities are added, incrementally.",
            "url": "https://en.wikipedia.org/wiki/Iterative_and_incremental_development",
            "id": 136      
        },     
        {
            "name": "Rational Unified Process (RUP)",
            "definition": "Rational Unified Process (RUP) is a web-enabled program development methodology that is said to be like an online mentor that provides guidelines, templates, and examples for all aspects and stages of program development. RUP is an iterative software development process framework created by the Rational Software Corporation, a division of IBM since 2003. It is not a single concrete prescriptive process, but rather an adaptable process framework, intended to be tailored by the development organizations and software project teams that will select the elements of the process that are appropriate for their needs. RUP is a specific implementation of the Unified Process.",
            "url": "https://en.wikipedia.org/wiki/Rational_Unified_Process",
            "id": 137      
        }, 
        {
            "name": "Refactoring",
            "definition": "In computer programming and software design, code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality. Potential advantages of refactoring may include improved code readability and reduced complexity; these can improve the source code's maintainability and create a simpler, cleaner, or more expressive internal architecture or object model to improve extensibility. Another potential goal for refactoring is improved performance; software engineers face an ongoing challenge to write programs that perform faster or use less memory.\n\nTypically, refactoring applies a series of standardised basic micro-refactorings, each of which is (usually) a tiny change in a computer program's source code that either preserves the behaviour of the software, or at least does not modify its conformance to functional requirements. Many development environments provide automated support for performing the mechanical aspects of these basic refactorings. If done well, code refactoring may help software developers discover and fix hidden or dormant bugs or vulnerabilities in the system by simplifying the underlying logic and eliminating unnecessary levels of complexity. If done poorly, it may fail the requirement that external functionality not be changed, and may thus introduce new bugs.",
            "url": "https://en.wikipedia.org/wiki/Code_refactoring",
            "id": 138     
        }, 
        {
            "name": "Rewrite",
            "definition": "A rewrite in computer programming is the act or result of re-implementing a large portion of existing functionality without re-use of its source code. When the rewrite is not using existing code at all, it is common to speak of a rewrite from scratch.\n\nA piece of software is typically rewritten when one or more of the following apply:\n\n1) its source code is not available or is only available under an incompatible license\n2) its code cannot be adapted to a new target platform\n3) its existing code has become too difficult to handle and extend\n4) the task of debugging it seems too complicated\n5) the programmer finds it difficult to understand its source code\n6) developers learn new techniques or wish to do a big feature overhaul which requires much change\n7) developers learn that new codes written may extend content options that can fix or overwrite previous problems\n8) the programming language of the source code has to be changed\n\nSeveral software engineers, such as Joel Spolsky have warned against total rewrites, especially under schedule constraints or competitive pressures. While developers may initially welcome the chance to correct historical design mistakes, a rewrite also discards those parts of the design that work as required. A rewrite commits the development team to deliver not just new features, but all those that exist in the previous code, while potentially introducing new bugs or regressions of previously fixed bugs. A rewrite also interferes with the tracking of unfixed bugs in the old version.\n\nThe incremental rewrite is an alternative approach, in which developers gradually replace the existing code with calls into a new implementation, expanding that implementation until it fully replaces the old one. This approach avoids a broad loss of functionality during the rewrite. Cleanroom software engineering is another approach, which requires the team to work from an exhaustive written specification of the software's functionality, without access to its code.",
            "url": "https://en.wikipedia.org/wiki/Rewrite_(programming)",
            "id": 139      
        }, 
        {
            "name": "Regression testing",
            "definition": "Regression testing (rarely, non-regression testing) is re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change. If not, that would be called a regression.\n\nChanges that may require regression testing include bug fixes, software enhancements, configuration changes, and even substitution of electronic components. As regression test suites tend to grow with each found defect, test automation is frequently involved. Sometimes a change impact analysis is performed to determine an appropriate subset of tests (non-regression analysis).",
            "url": "https://en.wikipedia.org/wiki/Regression_testing",
            "id": 140      
        },     
        {
            "name": "Software development kit (SDK)",
            "definition": "A software development kit (SDK) is a collection of software development tools in one installable package. They facilitate the creation of applications by having a compiler, debugger and sometimes a software framework. They are normally specific to a hardware platform and operating system combination. To create applications with advanced functionalities such as advertisements, push notifications, etc; most application software developers use specific software development kits.\n\nSome SDKs are required for developing a platform-specific app. For example, the development of an Android app on the Java platform requires a Java Development Kit. For iOS applications (apps) the iOS SDK is required. For Universal Windows Platform the .NET Framework SDK might be used. There are also SDKs that add additional features and can be installed in apps to provide analytics, data about application activity, and monetization options.\n\nAn SDK can take the form of application programming interfaces (APIs) in the form of on-device libraries of reusable functions used to interface to a particular programming language, or it may be as complex as hardware-specific tools that can communicate with a particular embedded system. Common tools include debugging facilities and other utilities, often presented in an integrated development environment (IDE). SDKs may include sample software and/or technical notes along with documentation, and tutorials to help clarify points made by the primary reference material.\n\nSDKs often include licenses that make them unsuitable for building software intended to be developed under an incompatible license. For example, a proprietary SDK is generally incompatible with free software development, while a GPL-licensed SDK could be incompatible with proprietary software development, for legal reasons. However, SDKs built under the GNU Lesser General Public License (LGPL) are typically usable for proprietary development. In cases where the underlying technology is new, SDKs may include hardware.",
            "url": "https://en.wikipedia.org/wiki/Software_development_kit",
            "id": 141      
        }, 
        {
            "name": "Service pack",
            "definition": "In computing, a service pack comprises a collection of updates, fixes, or enhancements to a software program delivered in the form of a single installable package. Companies often release a service pack when the number of individual patches to a given program reaches a certain (arbitrary) limit, or the software release has shown to be stabilized with a limited number of remaining issues based on users' feedback and bug reports.\n\nIn large software applications such as office suites, operating systems, database software, or network management, it is not uncommon to have a service pack issued within the first year or two of a product's release. Installing a service pack is easier and less error-prone than installing many individual patches, even more so when updating multiple computers over a network, where service packs are common.\n\nService packs are usually numbered, and thus shortly referred to as SP1, SP2, SP3 etc. They may also bring, besides bug fixes, entirely new features, as is the case of SP2 of Windows XP (e.g. Windows Security Center), or SP3 and SP4 of the heavily database dependent Trainz 2009: World Builder Edition.",
            "url": "https://en.wikipedia.org/wiki/Service_pack",
            "id": 142      
        }, 
        {
            "name": "Shotgun debugging",
            "definition": "Shotgun debugging can be defined as a process of making relatively un-directed changes to software in the hope that a bug will be perturbed out of existence. It can also mean using the approach of trying several possible solutions of hardware or software problem at the same time, in the hope that one of the solutions (typically source code modifications) will work.\n\nShotgun debugging has a relatively low success rate and can be very time-consuming, except when used as an attempt to work around programming language features that one may be using improperly. When combined with domain expertise and a strong intuition for the underlying codebase, it can be a good starting point to gut-solve a buggy piece of code a few times before formally researching the corresponding error message. When used in this way, it may be a valuable technique that is faster than browsing through the Internet searching a particular error message every time.\n\nShotgun debugging can occur when working with multi-threaded applications. Attempting to debug a race condition by adding debugging code to the application is likely to change the speed of one thread in relation to another and could cause the problem to disappear. This is known as a Heisenbug. Although apparently a solution to the problem, it is a fix by pure chance and anything else that changes the behavior of the threads could cause it to resurface — for example on a computer with a different scheduler. Code added to any part of the program could easily revert the effect of the ‘fix’.",
            "url": "https://en.wikipedia.org/wiki/Shotgun_debugging",
            "id": 143      
        }, 
        {
            "name": "Programming by permutation",
            "definition": "Programming by permutation, sometimes called ‘programming by accident’ or ‘shotgunning’, is an approach to software development wherein a programming problem is solved by iteratively making small changes (permutations) and testing each change to see if it behaves as desired. This approach sometimes seems attractive when the programmer does not fully understand the code and believes that one or more small modifications may result in code that is correct.\n\nProgramming by permutation gives little or no assurance about the quality of the code produced—it is the polar opposite of formal verification. Programmers are often compelled to program by permutation when an API is insufficiently documented. This lack of clarity drives others to copy and paste from reference code which is assumed to be correct, but was itself written as a result of programming by permutation. In some cases where the programmer can logically explain that exactly one out of a small set of variations must work, programming by permutation leads to correct code (which then can be verified) and makes it unnecessary to think about the other (wrong) variations.",
            "url": "https://en.wikipedia.org/wiki/Programming_by_permutation",
            "id": 144      
        },   
        {
            "name": "Sanity testing",
            "definition": "In software development, a sanity test (a form of software testing which offers ‘quick, broad, and shallow testing’) evaluates the result of a subset of application functionality to determine whether it is possible and reasonable to proceed with further testing of the entire application. Sanity tests may sometimes be used interchangeably with smoke tests insofar as both terms denote tests which determine whether it is possible and reasonable to continue testing further.\n\nOn the other hand, a distinction is sometimes made that a smoke test is a non-exhaustive test that ascertains whether the most crucial functions of a program work before proceeding with further testing whereas a sanity test refers to whether specific functionality such as a particular bug fix works as expected without testing the wider functionality of the software. In other words, a sanity test determines whether the intended result of a code change works correctly while a smoke test ensures that nothing else important was broken in the process. Sanity testing and smoke testing avoid wasting time and effort by quickly determining whether an application is too flawed to merit more rigorous QA testing, but needs more developer debugging.\n\nGroups of sanity tests are often bundled together for automated unit testing of functions, libraries, or applications prior to merging development code into a testing or trunk version control branch, for automated building, or for continuous integration and continuous deployment.",
            "url": "https://en.wikipedia.org/wiki/Sanity_check#Software_development",
            "id": 145      
        },     
        {
            "name": "Smoke testing",
            "definition": "In computer programming and software testing, smoke testing (also confidence testing, sanity testing, build verification test (BVT) and build acceptance test) is preliminary testing to reveal simple failures severe enough to, for example, reject a prospective software release. Smoke tests are a subset of test cases that cover the most important functionality of a component or system, used to aid assessment of whether main functions of the software appear to work correctly.\n\n When used to determine if a computer program should be subjected to further, more fine-grained testing, a smoke test may be called an intake test. Alternatively, it is a set of tests run on each new build of a product to verify that the build is testable before the build is released into the hands of the test team. \n\nSmoke tests frequently run quickly, giving benefits of faster feedback, rather than running more extensive test suites, which would naturally take much longer. A daily build and smoke test is among industry best practices. Smoke testing is also done by testers before accepting a build for further testing. Microsoft claims that after code reviews, ‘smoke testing is the most cost-effective method for identifying and fixing defects in software’.\n\nOne can perform smoke tests either manually or using an automated tool. In the case of automated tools, the process that generates the build will often initiate the testing. Smoke tests can be functional tests or unit tests. Functional tests exercise the complete program with various inputs. Unit tests exercise individual functions, subroutines, or object methods. Functional tests may comprise a scripted series of program inputs, possibly even with an automated mechanism for controlling mouse movements. Unit tests can be implemented either as separate functions within the code itself, or else as a driver layer that links to the code without altering the code being tested.",
            "url": "https://en.wikipedia.org/wiki/Smoke_testing_(software)",
            "id": 146      
        }, 
        {
            "name": "Synchronize and stabilize",
            "definition": "Synchronize-and-stabilize is a software life cycle development model. It allows the teams to work efficiently in parallel on different individual application modules. This is done while frequently synchronizing the work as individual’s and as members of parallel teams and periodically stabilizing and/or debugging the code through out the development process.\n\nThis model has several advantages over the classic waterfall model, which follows a sequential method. It has proven to be a more flexible model when compared to other life cycle development models. The distinguishing feature of the synchronize and stabilize model is allowing changes and modifications at any point in the software development process.",
            "url": "https://www.techopedia.com/definition/26121/synchronize-and-stabilize",
            "id": 147      
        }, 
        {
            "name": "Total cost of ownership (TCO)",
            "definition": "Total cost of ownership (TCO) is a financial estimate intended to help buyers and owners determine the direct and indirect costs of a product or service. It is a management accounting concept that can be used in full cost accounting or even ecological economics where it includes social costs. TCO is applied to the analysis of information technology products, seeking to quantify the financial impact of deploying a product over its life cycle. This includes software and hardware as well as training, warranties, licenses, migration expenses, risks, testing costs, backup and recovery, decommissioning and much more.\n\nA TCO analysis includes total cost of acquisition and operating costs, as well as costs related to replacement or upgrades at the end of the life cycle. A TCO analysis is used to gauge the viability of any capital investment. An enterprise may use it as a product/process comparison tool. It is also used by credit markets and financing agencies. TCO directly relates to an enterprise's asset and/or related systems total costs across all projects and processes, thus giving a picture of the profitability over time.",
            "url": "https://en.wikipedia.org/wiki/Total_cost_of_ownership",
            "id": 148      
        },     
        {
            "name": "Write-only code",
            "definition": "Write-only code is source code so arcane, complex, or ill-structured that it cannot be reliably modified or even comprehended by anyone with the possible exception of the author. Similarly, write-only language is a pejorative term for a programming language alleged to have syntax or semantics sufficiently dense and bizarre that any routine of significant size is too difficult to understand by other programmers and cannot be safely edited.",
            "url": "https://en.wikipedia.org/wiki/Write-only_language",
            "id": 149      
        }, 
        {
            "name": "Rubber duck debugging",
            "definition": "In software engineering, rubber duck debugging is a method of debugging code by articulating a problem in spoken or written natural language. The name is a reference to a story in the book The Pragmatic Programmer in which a programmer would carry around a rubber duck and debug their code by forcing themselves to explain it, line-by-line, to the duck. Many other terms exist for this technique, often involving different (usually) inanimate objects, or pets such as a dog or a cat.\n\n.Many programmers have had the experience of explaining a problem to someone else, possibly even to someone who knows nothing about programming, and then hitting upon the solution in the process of explaining the problem. In describing what the code is supposed to do and observing what it actually does, any incongruity between these two becomes apparent. More generally, teaching a subject forces its evaluation from different perspectives and can provide a deeper understanding. By using an inanimate object, the programmer can try to accomplish this without having to interrupt anyone else. This approach has been taught in computer science and software engineering courses.",
            "url": "https://en.wikipedia.org/wiki/Rubber_duck_debugging",
            "id": 150      
        }, 
        {
            "name": "White hat vs. Black hat vs. Grey Hat",
            "definition": "White hat vs. Black hat vs. Grey Hat. A white hat (or a white hat hacker) is an ethical security hacker. Ethical hacking is a term meant to imply a broader category than just penetration testing. Under the owner's consent, white hat hackers aim to identify any vulnerabilities the current system has. Contrasted with the black hat, a malicious hacker, the name comes from Western films, where heroic and antagonistic cowboys might traditionally wear a white and a black hat, respectively. There is a third kind of hacker known as a grey hat who hacks with good intentions but at times without permission.",
            "url": "https://en.wikipedia.org/wiki/White_hat_(computer_security)",
            "id": 151      
        }, 
        {
            "name": "Black/White/Gray box testing",
            "definition": "A black-box tester is unaware of the internal structure of the application to be tested, while a white-box tester has access to the internal structure of the application. A gray-box tester partially knows the internal structure, which includes access to the documentation of internal data structures as well as the algorithms used.",
            "url": "https://en.wikipedia.org/wiki/Gray_box_testing",
            "id": 152      
        }, 
        {
            "name": "Anonymization",
            "definition": "Data anonymization is a type of information sanitization whose intent is privacy protection. It is the process of removing personally identifiable information from data sets, so that the people whom the data describe remain anonymous.\n\nData anonymization has been defined as a ‘process by which personal data is altered in such a way that a data subject can no longer be identified directly or indirectly, either by the data controller alone or in collaboration with any other party.’ Data anonymization may enable the transfer of information across a boundary, such as between two departments within an agency or between two agencies, while reducing the risk of unintended disclosure, and in certain environments in a manner that enables evaluation and analytics post-anonymization.",
            "url": "https://en.wikipedia.org/wiki/Data_anonymization",
            "id": 153      
        }, 
        {
            "name": "Bot",
            "definition": "An Internet bot, web robot, robot or simply bot, is a software application that runs automated tasks (scripts) over the Internet, usually with the intent to emulate human activity on the Internet, such as messaging, on a large scale. An Internet bot plays the client role in a client–server model whereas the server role is usually played by web servers. Internet bots are able to perform tasks, that are simple and repetitive, much faster than a person could ever do. The most extensive use of bots is for web crawling, in which an automated script fetches, analyzes and files information from web servers. More than half of all web traffic is generated by bots.\n\nEfforts by web servers to restrict bots vary. Some servers have a robots.txt file that contains the rules governing bot behavior on that server. Any bot that does not follow the rules could, in theory, be denied access to or removed from, the affected website. If the posted text file has no associated program/software/app, then adhering to the rules is entirely voluntary. There would be no way to enforce the rules or to ensure that a bot's creator or implementer reads or acknowledges the robots.txt file. Some bots are ‘good’ – e.g. search engine spiders – while others are used to launch malicious attacks on, for example, political campaigns.",
            "url": "https://en.wikipedia.org/wiki/Internet_bot",
            "id": 154      
        },   
        {
            "name": "Botnet",
            "definition": "A botnet is a number of Internet-connected devices, each of which runs one or more bots. Botnets can be used to perform Distributed Denial-of-Service (DDoS) attacks, steal data, send spam, and allow the attacker to access the device and its connection. The owner can control the botnet using command and control (C&C) software. The word ‘botnet’ is a portmanteau of the words ‘robot’ and ‘network’. The term is usually used with a negative or malicious connotation.\n\nA botnet is a logical collection of Internet-connected devices, such as computers, smartphones or Internet of things (IoT) devices whose security have been breached and control ceded to a third party. Each compromised device, known as a ‘bot’, is created when a device is penetrated by software from a malware (malicious software) distribution.\n\nThe controller of a botnet is able to direct the activities of these compromised computers through communication channels formed by standards-based network protocols, such as IRC and Hypertext Transfer Protocol (HTTP). Botnets are increasingly rented out by cyber criminals as commodities for a variety of purposes",
            "url": "https://en.wikipedia.org/wiki/Botnet",
            "id": 155      
        },     
        {
            "name": "Buffer overflow",
            "definition": "In information security and programming, a buffer overflow, or buffer overrun, is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory locations.\n\nBuffers are areas of memory set aside to hold data, often while moving it from one section of a program to another, or between programs. Buffer overflows can often be triggered by malformed inputs; if one assumes all inputs will be smaller than a certain size and the buffer is created to be that size, then an anomalous transaction that produces more data could cause it to write past the end of the buffer. If this overwrites adjacent data or executable code, this may result in erratic program behavior, including memory access errors, incorrect results, and crashes.\n\nExploiting the behavior of a buffer overflow is a well-known security exploit. On many systems, the memory layout of a program, or the system as a whole, is well defined. By sending in data designed to cause a buffer overflow, it is possible to write into areas known to hold executable code and replace it with malicious code, or to selectively overwrite data pertaining to the program's state, therefore causing behavior that was not intended by the original programmer. Buffers are widespread in operating system (OS) code, so it is possible to make attacks that perform privilege escalation and gain unlimited access to the computer's resources. The famed Morris worm in 1988 used this as one of its attack techniques.",
            "url": "https://en.wikipedia.org/wiki/Buffer_overflow",
            "id": 156      
        }, 
        {
            "name": "Doxing",
            "definition": "Doxing or doxxing is the act of publicly revealing previously private personal information about an individual or organization, usually via the Internet. Methods employed to acquire such information include searching publicly available databases and social media websites, hacking, social engineering and through websites specializing in revealing IP addresses through a fake link. Doxing may be carried out for reasons such as online shaming, extortion, and vigilante aid to law enforcement. It also may be associated with hacktivism.",
            "url": "https://en.wikipedia.org/wiki/Doxing",
            "id": 157      
        }, 
        {
            "name": "OAuth",
            "definition": "OAuth (Open Authorization) is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites but without giving them the passwords. Generally, OAuth provides clients a ‘secure delegated access’ to server resources on behalf of a resource owner. It specifies a process for resource owners to authorize third-party access to their server resources without providing credentials.\n\nDesigned specifically to work with Hypertext Transfer Protocol (HTTP), OAuth essentially allows access tokens to be issued to third-party clients by an authorization server, with the approval of the resource owner. The third party then uses the access token to access the protected resources hosted by the resource server. In particular, OAuth 2.0 provides specific authorization flows for web applications, desktop applications, mobile phones, and smart devices.",
            "url": "https://en.wikipedia.org/wiki/OAuth",
            "id": 158      
        },     
        {
            "name": "Tor",
            "definition": "Tor, short for The Onion Router, is free and open-source software for enabling anonymous communication. It directs Internet traffic through a free, worldwide, volunteer overlay network, consisting of more than six thousand relays, to conceal a user's location and usage from anyone performing network surveillance or traffic analysis. Using Tor makes it more difficult to trace a user's Internet activity. Tor's intended use is to protect the personal privacy of its users, as well as their freedom and ability to communicate confidentially through IP address anonymity using Tor exit nodes.",
            "url": "https://en.wikipedia.org/wiki/Tor_(network)",
            "id": 159      
        }, 
        {
            "name": "Troll",
            "definition": "In internet slang, a troll is a person who posts inflammatory, insincere, digressive, extraneous, or off-topic messages in an online community (such as social media (Twitter, Facebook, Instagram, etc.), a newsgroup, forum, chat room, online video game, or blog), with the intent of provoking readers into displaying emotional responses, or manipulating others' perception. This is typically for the troll's amusement, or to achieve a specific result such as disrupting a rival's online activities or manipulating a political process. Even so, Internet trolling can also be defined as purposefully causing confusion or harm to other users online, for no reason at all.\n\nApplication of the term troll is subjective. At times the word is incorrectly used to refer to anyone with controversial, or differing, opinions. Some readers may characterize a post as trolling, while others may regard the same post as a legitimate contribution to the discussion, even if controversial. More potent acts of trolling are blatant harassment or off-topic banter. The advice to ignore rather than engage with a troll is sometimes phrased as ‘Please don't feed the trolls.’",
            "url": "https://en.wikipedia.org/wiki/Internet_troll",
            "id": 160      
        }, 
        {
            "name": "Composite pattern",
            "definition": "In software engineering, the composite pattern is a partitioning design pattern. The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. The intent of a composite is to 'compose' objects into tree structures to represent part-whole hierarchies. Implementing the composite pattern lets clients treat individual objects and compositions uniformly.\n\nThe Composite design pattern is one of the twenty-three well-known GoF design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.",
            "url": "https://en.wikipedia.org/wiki/Composite_pattern",
            "id": 161      
        }, 
        {
            "name": "Unicorn developer",
            "definition": "A unicorn developer is defined as highly experienced specialist with a wide and diverse range of skills, and is thus a very rare, almost mythical, creature. A good example of a unicorn developer is a ‘true full-stack developer’ experienced in back-end development, front-end development, as well as architecting cloud environments and web infrastructure. Another example of a unicorn would be someone who is excellent at both design and development (an artist and engineer par excellence). Usually, building a good team is much better for a company than searching for a unicorn.",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "id": 162      
        }, 
        {
            "name": "'This changes everything'",
            "definition": "Nothing has changed. Pure marketing. Outside of Silicon Valley (SV) this can mean curing cancer, eliminating Malaria and solving world hunger but within SV it means a bigger iPhone, an iPhone the size of a tablet or an iPhone strapped to your wrist. Synonyms include ‘This changes everything. Again’ and ‘Changing the world’.",
            "url": "https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/media/this-changes-everything.jpeg?raw=true",
            "id": 163      
        }, 
        {
            "name": "Code ninja",
            "definition": "Code ninjas, also referred to as ninja developers, don’t limit themselves to just one programming language or one technology stack; they are ‘developer polyglots.’ The ninja is an expert in a particular programming language, but is comfortable using any other language. They know how to navigate the various stacks in order to solve whatever technical challenge they come across.\n\nOrganizations seek the most talented professionals for the lowest possible salary, but the type of knowledge a code ninja possesses comes with a steep price tag. That’s because they’re essentially full stack developers who can work within various technology stacks – a skillset that is in increasing demand and very well-compensated! Though the code ninja has broad knowledge rather than deep expertise in one or two areas, gaining knowledge across the aforementioned skill-sets takes years devotion. There is no such thing as a junior or semi-senior code ninja; you either are one, or you aren’t...yet.’\n\n'Code ninja’ can also be a euphemism used by recruiters who don't actually know what specifically they want in a software engineer, just someone who can pretty much do everything and anything that's handed to them.",
            "url": "https://www.codeninjas.com/",
            "id": 164      
        }, 
        {
            "name": "Brogrammer",
            "definition": "‘Brogrammer’, a portmanteau of bro and programmer, is a slang term for a computer programmer who engages in stereotypically male-oriented activities and macho behavior.\n\nIt is often used pejoratively, but some programmers self-describe themselves as a brogrammer positively as a word for ‘sociable or outgoing programmer’, and it also tends to represent a subculture within the greater tech industry. \n\nBrogrammer culture has been said to have created an entry barrier based on adherence to the image presented by its participants, rather than ability. It can be viewed as antithetical to geek culture, which emphasizes ability and passion for field over image.",
            "url": "https://en.wikipedia.org/wiki/Brogrammer",
            "id": 165      
        }, 
        {
            "name": "Vanity metrics",
            "definition": "Vanity metrics are metrics that make you look good to others but do not help you understand your own performance in a way that informs future strategies. These metrics are exciting to point to if you want to appear to be improving, but they often aren’t actionable and aren’t related to anything you can control or repeat in a meaningful way. Vanity metrics are most often contrasted against actionable metrics, which is data that helps you make decisions and helps your business reach its goals or grow.\n\nIt is important to mention: Any metric can be a vanity metric. There just happen to be some telltale signs. They are hollow metrics that look nice on the surface but hold little substance. For example, 10,000 total registered accounts might seem impressive, but that number loses face quickly if there are only 100 active monthly users.",
            "url": "https://www.tableau.com/learn/articles/vanity-metrics",
            "id": 166      
        }, 
        {
            "name": "DINK (Duel Income, No Kids)",
            "definition": "‘DINK’ is an acronym that stands for ‘double income, no kids’ or ‘dual income, no kids’. It describes a couple without children living together while both partners are receiving an income; because both of their wages are coming into the same household, they are free to live more comfortably than couples who live together and spend their money on raising their children.",
            "url": "https://en.wikipedia.org/wiki/DINK",
            "id": 167      
        }, 
        {
            "name": "Wantrepreneur",
            "definition": "Someone who would like to start a business and thinks and talks about doing so, but never gets started or manages to get any ideas off the ground. A wantrepeneur may also desire to start a company so he or she can garner social proof from it all, as opposed to an entrepreneur who has an innovative idea that could possibly make money.",
            "url": "https://theinvestorsbook.com/wantrepreneur.html",
            "id": 168      
        }, 
        {
            "name": "Vaporware",
            "definition": "In the computer industry, vaporware (or vapourware) is a product, typically computer hardware or software, that is announced to the general public but is late or never actually manufactured nor officially cancelled. Generally used to describe something that is inexistent. ‘The snake oil of tech’",
            "url": "https://en.wikipedia.org/wiki/Vaporware",
            "id": 169      
        }, 
        {
            "name": "Bootstrapping",
            "definition": "Bootstrapping is a self-starting process that is supposed to proceed without external input. For various examples, click 'Learn More', below.",
            "url": "https://en.wikipedia.org/wiki/Bootstrapping_(disambiguation)",
            "id": 170      
        }, 
        {
            "name": "Imagineering",
            "definition": "Devising and/or implementing a new or highly imaginative concept or technology. Originated at and often associated with Disney, ‘imagineer’ is a term to describe creative people such as architects, writers, interior designers, illustrators, concept artists, landscapers, archivists, costume designers, theatre technicians, special effects experts, graphic designers and more.",
            "url": "https://en.wikipedia.org/wiki/Imagineering",
            "id": 171      
        }, 
        {
            "name": "Digital nomad",
            "definition": "Digital nomads are people who conduct their life in a nomadic manner while engaging in remote work using digital telecommunications technology. Such people generally have minimal material possessions and work remotely in temporary housing, hotels, cafes, public libraries, co-working spaces, or recreational vehicles, using Wi-Fi, smartphones or mobile hotspots to access the Internet. \n\nSome digital nomads are perpetual travelers, while others are only nomadic for a short period of time. While some nomads travel through various countries, others focus on one area. Some may engage in vandwelling. In 2020, a research study found that 10.9 million American workers described themselves as digital nomads, an increase of 49% from 2019. Digital nomads are often younger remote workers, backpackers, retired or semi-retired persons, snowbirds, and/or entrepreneurs.",
            "url": "https://en.wikipedia.org/wiki/Digital_nomad",
            "id": 172      
        }, 
        {
            "name": "Mechatronics",
            "definition": "Mechatronics, also called mechatronics engineering, is an interdisciplinary branch of engineering that focuses on the integration of mechanical, electronic and electrical engineering systems, and also includes a combination of robotics, electronics, computer science, telecommunications, systems, control, and product engineering.\n\nAs technology advances over time, various subfields of engineering have succeeded in both adapting and multiplying. The intention of mechatronics is to produce a design solution that unifies each of these various subfields. Originally, the field of mechatronics was intended to be nothing more than a combination of mechanics and electronics, hence the name being a portmanteau of mechanics and electronics; however, as the complexity of technical systems continued to evolve, the definition had been broadened to include more technical areas.\n\nThe word mechatronics originated in Japanese-English and was created by Tetsuro Mori, an engineer of Yaskawa Electric Corporation. The word mechatronics was registered as trademark by the company in Japan with the registration number of ’46-32714’ in 1971. The company later released the right to use the word to the public, and the word began being used globally. Currently the word is translated into many languages and is considered an essential term for advanced automated industry. Many people treat mechatronics as a modern buzzword synonymous with automation, robotics and electromechanical engineering.",
            "url": "https://en.wikipedia.org/wiki/Mechatronics",
            "id": 173      
        }, 
        {
            "name": "Growth hacking",
            "definition": "Growth hacking is a subfield of marketing focused on the rapid growth of a company. It is referred to as both a process and a set of cross-disciplinary (digital) skills. The goal is to regularly conduct A/B testing that will lead to improving the customer journey, and replicate and scale the ideas that work and modify or abandon the ones that don't before investing a lot of resources. It started in relation to early-stage startups that need rapid growth within short time on tight budgets, and also reached bigger corporate companies.\n\nA growth hacking team is made up of marketers, developers, engineers and product managers that specifically focus on building and engaging the user base of a business. Growth hacking is not just a process for marketers. It can be applied to product development and to the continuous improvement of products as well as to growing an existing customer base. As such, it’s equally useful to everyone from product developers, to engineers, to designers, to salespeople and to managers.",
            "url": "https://en.wikipedia.org/wiki/Growth_hacking",
            "id": 174      
        }, 
        {
            "name": "The Woz",
            "definition": "Stephen Gary Wozniak, also known by his nickname ‘Woz’, is an American electronics engineer, computer programmer, inventor, philanthropist, and technology entrepreneur. In 1976, with business partner Steve Jobs, he co-founded Apple Inc., which later became the world's largest information technology company by revenue and the largest company in the world by market capitalization. Through his work at Apple in the 1970s and 1980s, he is widely recognized as one of the prominent pioneers of the personal-computer revolution.",
            "url": "https://en.wikipedia.org/wiki/Steve_Wozniak",
            "id": 175      
        }, 
        {
            "name": "Protective incompetence",
            "definition": "Being bad at something you don't like to do, so you don't have to do it.",
            "url": "http://www.paulgraham.com/start.html",
            "id": 176      
        }, 
        {
            "name": "I/O",
            "definition": "In computing, input/output (I/O, or informally io or IO) is the communication between an information processing system, such as a computer, and the outside world, possibly a human or another information processing system. Inputs are the signals or data received by the system and outputs are the signals or data sent from it. The term can also be used as part of an action; to ‘perform I/O’ is to perform an input or output operation.\n\nI/O devices are the pieces of hardware used by a human (or other system) to communicate with a computer. For instance, a keyboard or computer mouse is an input device for a computer, while monitors and printers are output devices. Devices for communication between computers, such as modems and network cards, typically perform both input and output operations.",
            "url": "https://en.wikipedia.org/wiki/Input/output",
            "id": 177      
        }, 
        {
            "name": "Dogfooding",
            "definition": "Eating your own dog food or 'dogfooding' is the practice of using one's own products or services. This can be a way for an organization to test its products in real-world usage using product management techniques. Hence dogfooding can act as quality control, and eventually a kind of testimonial advertising. Once in the market, dogfooding can demonstrate developers' confidence in their own products.",
            "url": "https://en.wikipedia.org/wiki/Eating_your_own_dog_food",
            "id": 178      
        }, 
        {
            "name": "SWOT analysis",
            "definition": "SWOT analysis (or SWOT matrix) is a strategic planning and strategic management technique used to help a person or organization identify strengths, weaknesses, opportunities, and threats related to business competition or project planning. It is sometimes called situational assessment or situational analysis. Additional acronyms using the same components include TOWS and WOTS-UP.\n\nThis technique is designed for use in the preliminary stages of decision-making processes and can be used as a tool for evaluation of the strategic position of organizations of many kinds (for-profit enterprises, local and national governments, NGOs, etc.). It is intended to identify the internal and external factors that are favorable and unfavorable to achieving the objectives of the venture or project. Users of a SWOT analysis often ask and answer questions to generate meaningful information for each category to make the tool useful and identify their competitive advantage. SWOT has been described as a tried-and-true tool of strategic analysis, but has also been criticized for its limitations, and alternatives have been developed.",
            "url": "https://en.wikipedia.org/wiki/SWOT_analysis",
            "id": 179      
        }, 
        {
            "name": "Bricked",
            "definition": "The word ‘brick’, when used in reference to consumer electronics, describes an electronic device such as a mobile device, game console, or router that, due to corrupted firmware, a hardware problem, or other damage, can no longer function, and thus is ‘bricked’. The device becomes as technologically useful as a brick, hence the name.",
            "url": "https://en.wikipedia.org/wiki/Brick_(electronics)",
            "id": 180      
        }, 
        {
            "name": "Rollback",
            "definition": "Rollback describes the process of returning a hardware product or software program back to an earlier, working state or version after encountering issues with a later version.",
            "url": "https://en.wikipedia.org/wiki/Rollback_(data_management)",
            "id": 181      
        }, 
        {
            "name": "Pistol ship",
            "definition": "In software jargon, ‘pistol ship’ (also ‘ship from the hip’) is used to describe the dangerous practice of publishing unchecked code. Shipping’ code is another way of saying ‘deploying’ or ‘delivering’ code, and to ‘pistol ship’ code is to ship it without checking it for errors or bugs. To do so is often an act of pride and/or laziness.",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "id": 182      
        }, 
        {
            "name": "Pair programming",
            "definition": "Pair programming is an agile software development technique in which two programmers work together at one workstation. One, the driver, writes code while the other, the observer or navigator, reviews each line of code as it is typed in. The two programmers switch roles frequently.\n\nWhile reviewing, the observer also considers the ‘strategic’ direction of the work, coming up with ideas for improvements and likely future problems to address. This is intended to free the driver to focus all of their attention on the ‘tactical’ aspects of completing the current task, using the observer as a safety net and guide.",
            "url": "https://en.wikipedia.org/wiki/Pair_programming",
            "id": 183      
        }, 
        {
            "name": "AWK",
            "definition": "AWK (awk) is a domain-specific language designed for text processing and typically used as a data extraction and reporting tool. Like sed and grep, it is a filter, and is a standard feature of most Unix-like operating systems.\n\nAWK was created at Bell Labs in the 1970s, and its name is derived from the surnames of its authors: Alfred Aho, Peter Weinberger, and Brian Kernighan. The acronym is pronounced the same as the bird auk, which is on the cover of The AWK Programming Language. When written in all lowercase letters, as awk, it refers to the Unix or Plan 9 program that runs scripts written in the AWK programming language.",
            "url": "https://en.wikipedia.org/wiki/AWK",
            "id": 184      
        }, 
        {
            "name": "grep",
            "definition": "grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines), which has the same effect. grep was originally developed for the Unix operating system, but later available for all Unix-like systems and some others such as OS-9. In December 2003, the Oxford English Dictionary Online added draft entries for 'grep' as both a noun and a verb.",
            "url": "https://en.wikipedia.org/wiki/Grep",
            "id": 185      
        }, 
        {
            "name": "Pipe (|)",
            "definition": "A pipe is an inter-process communication mechanism originating in Unix, which directs the output (standard out and, optionally, standard error) of one process to the input (standard in) of another. In this way, a series of commands can be ‘piped’ together, giving users the ability to quickly perform complex multi-stage processing from the command line or as part of a Unix shell script (‘bash file’). In most Unix shells (command interpreters), this is represented by the vertical bar character, |\n\n For example:\n\ncommand1 | command2 | command3",
            "url": "https://en.wikipedia.org/wiki/Pipeline_(Unix)",
            "id": 186      
        }, 
        {
            "name": "Technical debt",
            "definition": "In software development, technical debt (also known as design debt or code debt) is the implied cost of additional rework caused by choosing an easy (limited) solution now instead of using a better approach that would take longer.\n\nAnalogous with monetary debt, if technical debt is not repaid, it can accumulate ‘interest’, making it harder to implement changes. Unaddressed technical debt increases software entropy and cost of further rework. Similarly to monetary debt, technical debt is not necessarily a bad thing, and sometimes (e.g. as a proof-of-concept) is required to move projects forward. On the other hand, some experts claim that the ‘technical debt’ metaphor tends to minimize the ramifications, which results in insufficient prioritization of the necessary work to correct it.\n\nAs a change is started on a codebase, there is often the need to make other coordinated changes in other parts of the codebase or documentation. Changes required that are not completed are considered debt, and until paid, will incur interest on top of interest, making it cumbersome to build a project. Although the term is used in software development primarily, it can also be applied to other professions.",
            "url": "https://en.wikipedia.org/wiki/Technical_debt",
            "id": 187      
        }, 
        {
            "name": "Application streaming",
            "definition": "Application streaming is a form of on-demand software distribution. In these scenarios, only essential portions of an application's code need to be installed on the computer: while the end user performs actions in the application, the necessary code and files are delivered over the network as and when they are required.\n\nApplication streaming provides an extremely accurate metric of actual application usage, and rather than install the same applications on every client machine in the company, only the programs users actually want to run are delivered. As a result, licensing fees can often be reduced.\n\nApplication streaming is a related concept to application virtualization, where applications are run directly from a virtual machine on a central server that is completely separate from the local system. By contrast, application streaming runs the program locally, but still involves the centralized storage of application code.",
            "url": "https://en.wikipedia.org/wiki/Application_streaming",
            "id": 188      
        }, 
        {
            "name": "Amara's law",
            "definition": "An adage about forecasting the effects of technology. The law has been used in explaining nanotechnology. ‘We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run,’ coined by Roy Amara, past president of The Institute for the Future.",
            "url": "https://en.wikipedia.org/wiki/Roy_Amara",
            "id": 189      
        }, 
        {
            "name": "Application service provider (ASP)",
            "definition": "An application service provider (ASP), also known as Apps on tap, is a business providing computer-based services to customers over a network; such as access to a particular software application (such as customer relationship management) using a standard protocol (such as HTTP).\n\nThe need for ASPs has evolved from the increasing costs of specialized software that have far exceeded the price range of small to medium-sized businesses. As well, the growing complexities of software have led to huge costs in distributing the software to end-users. Through ASPs, the complexities and costs of such software can be cut down. In addition, the issues of upgrading have been eliminated from the end-firm by placing the onus on the ASP to maintain up-to-date services, 24 x 7 technical support, physical and electronic security and in-built support for business continuity and flexible working.",
            "url": "https://en.wikipedia.org/wiki/Application_service_provider",
            "id": 190      
        }, 
        {
            "name": "Augmented reality (AR)",
            "definition": "Augmented reality (AR) is an interactive experience of a real-world environment where the objects that reside in the real world are enhanced by computer-generated perceptual information, sometimes across multiple sensory modalities, including visual, auditory, haptic, somatosensory and olfactory. AR can be defined as a system that incorporates three basic features: a combination of real and virtual worlds, real-time interaction, and accurate 3D registration of virtual and real objects. \n\nThe overlaid sensory information can be constructive (i.e. additive to the natural environment), or destructive (i.e. masking of the natural environment). This experience is seamlessly interwoven with the physical world such that it is perceived as an immersive aspect of the real environment. In this way, augmented reality alters one's ongoing perception of a real-world environment, whereas virtual reality completely replaces the user's real-world environment with a simulated one. Augmented reality is related to two largely synonymous terms: mixed reality and computer-mediated reality.",
            "url": "https://en.wikipedia.org/wiki/Augmented_reality",
            "id": 191      
        }, 
        {
            "name": "Virtual reality",
            "definition": "Virtual reality (VR) is a simulated experience that can be similar to or completely different from the real world. Applications of virtual reality include entertainment (particularly video games), education (such as medical or military training) and business (such as virtual meetings). Other distinct types of VR-style technology include augmented reality and mixed reality, sometimes referred to as extended reality or XR.",
            "url": "https://en.wikipedia.org/wiki/Virtual_reality",
            "id": 192      
        }, 
        {
            "name": "Abandonware",
            "definition": "Abandonware is a product, typically software, ignored by its owner and manufacturer, and for which no official support is available.\n\nWithin an intellectual rights contextual background, abandonware is a software (or hardware) sub-case of the general concept of orphan works. Museums and various organizations dedicated to preserving this software continue to provide legal access.\n\nThe term ‘abandonware’ is broad, and encompasses many types of old software. Definitions of ‘abandoned’ vary, but in general it is like any item that is abandoned – it is ignored by the owner, and as such product support and possibly copyright enforcement are also ‘abandoned’.",
            "url": "https://en.wikipedia.org/wiki/Abandonware",
            "id": 193      
        }, 
        {
            "name": "Architecture neutral",
            "definition": "Software that is designed without regard to the target platform. Software is often written to maximize the performance of a specific hardware platform, but such software must be modified to make it run on other hardware. It is always a tradeoff. The more specialized the software, the faster the hardware performance but the more difficult to make the software work on other platforms.",
            "url": "https://en.wikipedia.org/wiki/Architecture_Neutral_Distribution_Format",
            "id": 194      
        }, 
        {
            "name": "Intermediate language (IL)",
            "definition": "A language that is generated from programming source code, but that cannot be directly executed by the CPU. Also called ‘bytecode’, ‘p-code’, ‘pseudocode’ or ‘pseudo language’, the intermediate language (IL) is platform independent. It can be run in any computer environment that has a runtime engine for the language.\n\nIn order to execute the intermediate language program, it must be interpreted a line at a time into machine language when it is run or compiled entirely into machine language just before it is run or compiled entirely ahead of time and run when required.\n\nVisual Basic and Java are notable examples of programming languages that generate an intermediate language. Microsoft's .NET and Common Language Infrastructure (CLI), the ECMA standard version of .NET, also generate an intermediate language.",
            "url": "https://en.wikipedia.org/wiki/Intermediate_representation#Intermediate_language",
            "id": 195      
        },
        { 
            "name": "Cross-platform software",
            "definition": "In computing, cross-platform software (also called multi-platform software, platform-agnostic software, or platform-independent software) is computer software that is designed to work in several computing platforms. Some cross-platform software requires a separate build for each platform, but some can be directly run on any platform without special preparation, being written in an interpreted language or compiled to portable bytecode for which the interpreters or run-time packages are common or standard components of all supported platforms.\n\nFor example, a cross-platform application may run on Microsoft Windows, Linux, and macOS. Cross-platform software may run on many platforms, or as few as two. Some frameworks for cross-platform development are Codename One, Kivy, Qt, Flutter, NativeScript, Xamarin, Phonegap, Ionic, and React Native.",
            "url": "https://en.wikipedia.org/wiki/Cross-platform_software",
            "id": 196      
        }, 
        {
            "name": "Coding best practices",
            "definition": "Coding best practices are a set of informal rules that the software development community employs to help improve software quality.Many computer programs remain in use for long periods of time so any rules need to facilitate both initial development and subsequent maintenance and enhancement by people other than the original authors.\n\nThere are a few best practices when it comes to learning how to code, and they center around these 7 concepts:\n\n1. Variable naming conventions\n2. Class and function naming conventions\n3. Clear and concise comments\n4. Indentations\n5. Portability\n6. Reusability and scalability\n7. Testing",
            "url": "https://en.wikipedia.org/wiki/Coding_best_practices",
            "id": 197      
        }, 
        {
            "name": "Best current practice (BCP)",
            "definition": "A Best Current Practice (BCP) is a de facto level of performance in engineering and information technology. It is more flexible than a standard, since techniques and tools are continually evolving. The Internet Engineering Task Force publishes Best Current Practice documents in a numbered document series. Each document in this series is paired with the currently valid Request for Comments (RFC) document. BCP was introduced in RFC-1818.\n\nBCPs are document guidelines, processes, methods, and other matters not suitable for standardization. The Internet standards process itself is defined in a series of BCPs, as is the formal organizational structure of the IETF, Internet Engineering Steering Group, Internet Architecture Board, and other groups involved in that process.\n\nIETF's separate Standard Track (STD) document series defines the fully standardized network protocols of the Internet, such as the Internet Protocol, the Transmission Control Protocol, and the Domain Name System. Each RFC number refers to a specific version of a document Standard Track, but the BCP number refers to the most recent revision of the document. Thus, citations often reference both the BCP number and the RFC number. Example citations for BCPs are: BCP 38, RFC 2827.",
            "url": "https://en.wikipedia.org/wiki/Best_current_practice",
            "id": 198      
        }, 
        {
            "name": "Abend",
            "definition": "(ABnormal END) Pronounced ‘ab-end’. An abend is an unexpected termination that causes the computer, smartphone or tablet to stop responding. The abend occurs either when the processor is presented with instructions or data it cannot recognize, or a program tries to address memory beyond a defined boundary. Abends are generally the result of erroneous software logic in the application or operating system.",
            "url": "https://www.pcmag.com/encyclopedia/term/abend",
            "id": 199      
        }, 
        {
            "name": "Application binary interface (ABI)",
            "definition": "A specification for a specific hardware platform combined with the operating system. It is one step beyond the application program interface (API), which defines the calls from the application to the operating system. The ABI defines the API plus the machine language for a particular CPU family. An API does not ensure runtime compatibility, but an ABI does, because it defines the machine format.",
            "url": "https://en.wikipedia.org/wiki/Application_binary_interface",
            "id": 200      
        }, 
        {
            "name": "Arduino",
            "definition": "Arduino is an open-source hardware and software company, project, and user community that designs and manufactures single-board microcontrollers and microcontroller kits for building digital devices. Its hardware products are licensed under a CC BY-SA license, while software is licensed under the GNU Lesser General Public License (LGPL) or the GNU General Public License (GPL), permitting the manufacture of Arduino boards and software distribution by anyone. Arduino boards are available commercially from the official website or through authorized distributors.\n\nArduino board designs use a variety of microprocessors and controllers. The boards are equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards ('shields') or breadboards (for prototyping) and other circuits. The boards feature serial communications interfaces, including Universal Serial Bus (USB) on some models, which are also used for loading programs. The microcontrollers can be programmed using the C and C++ programming languages, using a standard API which is also known as the Arduino language, inspired by the Processing language and used with a modified version of the Processing IDE. In addition to using traditional compiler toolchains, the Arduino project provides an integrated development environment (IDE) and a command line tool developed in Go.\n\nThe Arduino project began in 2005 as a tool for students at the Interaction Design Institute Ivrea, Italy, aiming to provide a low-cost and easy way for novices and professionals to create devices that interact with their environment using sensors and actuators. Common examples of such devices intended for beginner hobbyists include simple robots, thermostats and motion detectors. The name Arduino comes from a bar in Ivrea, Italy, where some of the founders of the project used to meet. The bar was named after Arduin of Ivrea, who was the margrave of the March of Ivrea and King of Italy from 1002 to 1014.",
            "url": "https://en.wikipedia.org/wiki/Arduino",
            "id": 201      
        }, 
        {
            "name": "Above the fold",
            "definition": "The part of a Web page that is visible without scrolling. The fold is an invisible line simulating where a newspaper is folded. This is a design consideration when laying out a Web page so that all the important information can be seen at once. The majority of monitors today have at least 1,080 lines of resolution, and the page size above the fold is roughly a thousand vertical lines. Contrast with ‘below the fold’, which is the non-visible content that must be scrolled to be seen.",
            "url": "https://en.wikipedia.org/wiki/Above_the_fold#In_web_design",
            "id": 202      
        }, 
        {
            "name": "Absolute address",
            "definition": "An explicit identification of hardware, such as a memory location, peripheral device, or location within a device. For example, memory byte 107,443, disk drive 2 and sector 238 are absolute addresses. Although the action may have been initiated through many ‘layers of abstraction’ at a higher level, some instruction in some software routine must use an absolute address to activate every hardware component in the computer. Absolute coding is writing programming code that refers to fixed locations.",
            "url": "https://en.wikipedia.org/wiki/Memory_address#absolute_address",
            "id": 203      
        }, 
        {
            "name": "Path",
            "definition": "A path is a string of characters used to uniquely identify a location in a directory structure. It is composed by following the directory tree hierarchy in which components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash (‘/‘), the backslash character ('\’), or colon (‘:’), though some operating systems may use a different delimiter. Paths are used extensively in computer science to represent the directory/file relationships common in modern operating systems and are essential in the construction of Uniform Resource Locators (URLs). Resources can be represented by either absolute or relative paths.\n\nAn absolute or full path points to the same location in a file system, regardless of the current working directory. To do that, it must include the root directory. By contrast, a relative path starts from some given working directory, avoiding the need to provide the full absolute path. A filename can be considered as a relative path based at the current working directory. If the working directory is not the file's parent directory, a file not found error will result if the file is addressed by its name.",
            "url": "https://en.wikipedia.org/wiki/Path_(computing)",
            "id": 204      
        }, 
        {
            "name": "Garbage collection (GC)",
            "definition": "In computer science, garbage collection (GC) is a form of automatic memory management. The garbage collector attempts to reclaim memory which was allocated by the program, but is no longer referenced—also called garbage. Garbage collection was invented by American computer scientist John McCarthy around 1959 to simplify manual memory management in Lisp.\n\nGarbage collection relieves the programmer from performing manual memory management where the programmer specifies what objects to deallocate and return to the memory system and when to do so. Other similar techniques include stack allocation, region inference, memory ownership, and combinations of multiple techniques. Garbage collection may take a significant proportion of total processing time in a program and, as a result, can have significant influence on performance.\n\nResources other than memory, such as network sockets, database handles, user interaction windows, file and device descriptors, are not typically handled by garbage collection. Methods for managing such resources, particularly destructors, may suffice to manage memory as well, leaving no need for GC. Some GC systems allow such other resources to be associated with a region of memory that, when collected, causes the work of reclaiming these resources.",
            "url": "https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)",
            "id": 205      
        }, 
        {
            "name": "AMD (Advanced Micro Devices, Inc.)",
            "definition": "An American multinational semiconductor company based in Santa Clara, California, that develops computer processors and related technologies for business and consumer markets. While it initially manufactured its own processors, the company later outsourced its manufacturing, a practice known as going fabless, after GlobalFoundries was spun off in 2009. AMD's main products include microprocessors, motherboard chipsets, embedded processors, graphics processors, and FPGAs for servers, workstations, personal computers, and embedded system applications.",
            "url": "https://en.wikipedia.org/wiki/Advanced_Micro_Devices",
            "id": 206      
        }, 
        {
            "name": "ARM",
            "definition": "The most widely used microprocessors worldwide. Designed by ARM Holdings plc, Cambridge, England (www.arm.com), the company was founded in 1990 by Acorn Computers, Apple and VLSI Technology. The ARM brand originally stood for Acorn RISC Machine and later Advanced RISC Machine.\n\nIn 2016, ARM was acquired by Japan-based Softbank, which agreed to sell the company to NVIDIA in 2020 for $40 billion, pending U.S. and U.K. approval. As of 2022, the deal is still pending due to U.S. antitrust concerns.\n\nLow Power Requirements - ARM chips are 32-bit and 64-bit RISC-based CPUs that are known for their low cost but primarily for their low power requirements. In some cases, an ARM-based smartphone using five watts of battery can perform as well or better than a CISC-based desktop computer requiring more than 100 watts.\n\nManufactured under license from ARM by more than a dozen semiconductor companies, billions of ARM-based devices are made every year, including smartphones, tablets, e-book readers, TVs and myriad other consumer and industrial products. Apple surprised the industry in 2020 by using its new ARM-based chip in its laptop and desktop computers.\n\nVery often, multiple ARM processing cores make up the CPU in a system-on-chip (SoC). For example, Qualcomm's Snapdragon and NVIDIA's Tegra are ARM-based smartphone and tablet SoCs.",
            "url": "https://en.wikipedia.org/wiki/ARM_architecture_family",
            "id": 207      
        }, 
        {
            "name": "Array vs. List",
            "definition": "Array\n\nIn computer science, an array type is a data type that represents a collection of elements (values or variables), each selected by one or more indices (identifying keys) that can be computed at run time during program execution. Such a collection is usually called an array variable, array value, or simply array. By analogy with the mathematical concepts vector and matrix, array types with one and two indices are often called vector type and matrix type, respectively. More generally, a multidimensional array type can be called a tensor type.\n\nList\n\nIn computer science, a list or sequence is an abstract data type that represents a finite number of ordered values, where the same value may occur more than once. An instance of a list is a computer representation of the mathematical concept of a tuple or finite sequence; the (potentially) infinite analog of a list is a stream. Lists are a basic example of containers, as they contain other values. If the same value occurs multiple times, each occurrence is considered a distinct item.\n\nSimilarities between Lists and Arrays\n\nThey can look the same: [3,4,3,6,3]. Both are used for storing data. Both are mutable. Both can be indexed and iterated through. Both can be sliced.\n\nDifferences\n\nThe main difference between these two data types is the operations you can perform on them. Arrays are specially optimized for arithmetic computations so if you’re going to perform similar operations you should consider using an array instead of a list. Lists are easier to modify while arrays are more difficult. In comparison to the list, an array has a more compact in-memory size. List memory allocation is dynamic and random, while array memory allocation is static and continuous. Also, lists are containers for elements having differing data types (heterogeneous) but arrays are used as containers for elements of the same data type (homogeneous).",
            "url": "https://learnpython.com/blog/python-array-vs-list/",
            "id": 208      
        }, 
        {
            "name": "Artificial empathy (AE)",
            "definition": "Artificial empathy (AE) or computational empathy is the development of AI systems—such as companion robots or virtual agents—that can detect emotions and respond to them in an empathic way.\n\nAlthough such technology can be perceived as scary or threatening, it could also have a significant advantage over humans for roles in which emotional expression can be important, such as in the health care sector. For example, care-givers who perform emotional labor above and beyond the requirements of paid labor can experience chronic stress or burnout, and can become desensitized to patients.\n\nA broader definition of artificial empathy is ‘the ability of nonhuman models to predict a person's internal state (e.g., cognitive, affective, physical) given the signals (s)he emits (e.g., facial expression, voice, gesture) or to predict a person's reaction (including, but not limited to internal states) when he or she is exposed to a given set of stimuli (e.g., facial expression, voice, gesture, graphics, music, etc.)’.",
            "url": "https://en.wikipedia.org/wiki/Artificial_empathy",
            "id": 209      
        }, 
        {
            "name": "Service set",
            "definition": "In IEEE 802.11 wireless local area networking standards (including Wi-Fi), a service set is a group of wireless network devices which share a service set identifier (SSID)—typically the natural language label that users see as a network name. (For example, all of the devices that together form and use a Wi‑Fi network called Foo are a service set.) A service set forms a logical network of nodes operating with shared link-layer networking parameters; they form one logical network segment. A service set is either a basic service set (BSS) or an extended service set (ESS).\n\nBasic service set\n\nA basic service set is a subgroup, within a service set, of devices that share physical-layer medium access characteristics (e.g. radio frequency, modulation scheme, security settings) such that they are wirelessly networked. The basic service set is defined by a basic service set identifier (BSSID) shared by all devices within it. A basic service set should not be confused with the coverage area of an access point, known as the basic service area (BSA).\n\nAn infrastructure BSS is created by an infrastructure device called an access point (AP) for other devices to join. The Wi‑Fi segments of common home and business networks are examples of this type.\n\nAn independent BSS (IBSS), or ad hoc network, is created by peer devices among themselves without network infrastructure. A temporary network created by a cellular telephone to share its Internet access with other devices is a common example.\n\nA mesh basic service set (MBSS) forms a self-contained network of mesh stations that share a mesh profile. Each node may also be an access point hosting its own basic service set, for example using the mesh BSS to provide Internet access for local users. From the point of view of a wireless client, an IEEE 802.11s wireless mesh network appears as a conventional infrastructure mode topology, and is centrally configured as such. The formation of the mesh's BSS, as well as wireless traffic management (including path selection and forwarding) is negotiated between the nodes of the mesh infrastructure. The mesh's BSS is distinct from the networks (which may also be wireless) used by a mesh's redistribution points to communicate with one another.\n\nExtended service set\n\nAn extended service set (ESS) is a wireless network, created by multiple access points, which appears to users as a single, seamless network, such as a network covering a home or office that is too large for reliable coverage by a single access point. It is a set of one or more infrastructure basic service sets on a common logical network segment (i.e. same IP subnet and VLAN). Key to the concept is that the participating basic service sets appear as a single network to the logical link control layer.\n\nThus, from the perspective of the logical link control layer, stations within an ESS may communicate with one another, and mobile stations may move transparently from one participating basic service set to another (within the same ESS). Extended service sets make possible distribution services such as centralized authentication. From the perspective of the link layer, all stations within an ESS are all on the same link, and transfer from one BSS to another is transparent to logical link control.",
            "url": "https://en.wikipedia.org/wiki/Service_set_(802.11_network)#Basic_service_set_types",
            "id": 210      
        }, 
        {
            "name": "Asimov's laws",
            "definition": "The famous author of science fiction Isaac Asimov (1920-1992) conceived three important principles pertaining to robots in the 1940s, known as ‘Asimov's Three Laws of Robotics’. The first law is ‘a robot must never harm human beings or, through inaction, allow a human being to be harmed’. The second law is ‘a robot must obey the orders from human beings except where such orders conflict with the first law’, and the third law is ‘a robot must protect its own existence as long as such protection does not conflict with the first and second laws’.",
            "url": "https://en.wikipedia.org/wiki/Three_Laws_of_Robotics",
            "id": 211      
        }, 
        {
            "name": "ASP.NET",
            "definition": "ASP.NET is an open-source, server-side web-application framework designed for web development to produce dynamic web pages. It was developed by Microsoft to allow programmers to build dynamic web sites, applications and services. The name stands for Active Server Pages Network Enabled Technologies.",
            "url": "https://en.wikipedia.org/wiki/ASP.NET",
            "id": 212      
        }, 
        {
            "name": "Assignment statement",
            "definition": "In programming, a compiler directive that places a value into a variable. For example, counter=0 creates a variable named counter and fills it with zeros. The VARIABLE=VALUE syntax is common among programming languages.",
            "url": "https://en.wikipedia.org/wiki/Assignment_(computer_science)",
            "id": 213      
        }, 
        {
            "name": "Public-key cryptography",
            "definition": "Public-key cryptography, or asymmetric cryptography, is a cryptographic system that uses pairs of keys. Each pair consists of a public key (which may be known to others) and a private key (which may not be known by anyone except the owner). The generation of such key pairs depends on cryptographic algorithms which are based on mathematical problems termed one-way functions. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security.\n\nIn such a system, any person can encrypt a message using the intended receiver's public key, but that encrypted message can only be decrypted with the receiver's private key. This allows, for instance, a server program to generate a cryptographic key intended for a suitable symmetric-key cryptography, then to use a client's openly-shared public key to encrypt that newly generated symmetric key. The server can then send this encrypted symmetric key over an insecure channel to the client; only the client can decrypt it using the client's private key (which pairs with the public key used by the server to encrypt the message). With the client and server both having the same symmetric key, they can safely use symmetric key encryption (likely much faster) to communicate over otherwise-insecure channels. This scheme has the advantage of not having to manually pre-share symmetric keys (a fundamentally difficult problem) while gaining the higher data throughput advantage of symmetric-key cryptography.\n\nWith public-key cryptography, robust authentication is also possible. A sender can combine a message with a private key to create a short digital signature on the message. Anyone with the sender's corresponding public key can combine that message with a claimed digital signature; if the signature matches the message, the origin of the message is verified (i.e., it must have been made by the owner of the corresponding private key).",
            "url": "https://en.wikipedia.org/wiki/Public-key_cryptography",
            "id": 214      
        }, 
        {
            "name": "Astroturfing",
            "definition": "Astroturfing is the practice of masking the sponsors of a message or organization (e.g., political, advertising, religious or public relations) to make it appear as though it originates from and is supported by grassroots participants. It is a practice intended to give the statements or organizations credibility by withholding information about the source's financial connection. The term astroturfing is derived from AstroTurf, a brand of synthetic carpeting designed to resemble natural grass, as a play on the word ‘grassroots’. The implication behind the use of the term is that instead of a ‘true’ or ‘natural’ grassroots effort behind the activity in question, there is a ‘fake’ or ‘artificial’ appearance of support.",
            "url": "https://en.wikipedia.org/wiki/Astroturfing",
            "id": 215      
        }, 
        {
            "name": "Active cooling",
            "definition": "Active cooling is a heat-reducing mechanism that is typically implemented in electronic devices and indoor buildings to ensure proper heat transfer and circulation from within. Unlike its counterpart passive cooling, active cooling is entirely dependent on energy consumption in order to operate. It uses various mechanical systems that consume energy to dissipate heat. It is commonly implemented in systems that are unable to maintain their temperature through passive means.\n\nActive cooling systems are usually powered through the use of electricity or thermal energy but it's possible for some systems to be powered by solar energy or even hydroelectric energy. They need to be well-maintained and sustainable in order for them to perform its necessary tasks or the possibility of damages within objects could occur. Various applications of commercial active cooling systems include indoor air conditioners, computer fans, and heat pumps.",
            "url": "https://en.wikipedia.org/wiki/Computer_cooling",
            "id": 216      
        }, 
        {
            "name": "Passive cooling",
            "definition": "Passive cooling is a design approach that focuses on heat gain control and heat dissipation in order to lower the thermal temperature, with low or no energy consumption. This approach works either by preventing heat from entering the interior (heat gain prevention) or by removing heat from the structure (natural cooling).\n\nPassive heatsink cooling involves attaching a block of machined or extruded metal to the part that needs cooling. A thermal adhesive may be used. More commonly for a personal computer CPU, a clamp holds the heatsink directly over the chip, with a thermal grease or thermal pad spread between. This block has fins and ridges to increase its surface area.\n\nThe heat conductivity of metal is much better than that of air, and it radiates heat better than the component that it is protecting (usually an integrated circuit or CPU). Fan-cooled aluminium heatsinks were originally the norm for desktop computers, but nowadays many heatsinks feature copper base-plates or are entirely made of copper.",
            "url": "https://en.wikipedia.org/wiki/Computer_cooling#Passive_cooling",
            "id": 217      
        }, 
        {
            "name": "Active Directory (AD)",
            "definition": "An advanced, hierarchical network directory service that comes with Windows servers and used for managing permissions and user access to network resources. Introduced in Windows 2000, Active Directory is a domain-based network that is structured like the Internet's Domain Naming System (DNS). Using the LDAP directory access protocol, a company's workgroups (departments, sections, offices, etc.) are assigned domain names similar to Web addresses, and any LDAP-compliant Windows, Mac, Unix or Linux client can access them.\n\nInitially, Active Directory was used only for centralized domain management. However, Active Directory eventually became an umbrella title for a broad range of directory-based identity-related services. Active Directory can function in a heterogeneous, enterprise network and encompass other directories including NDS and NIS+. Cisco supports Active Directory in its IOS router operating system.",
            "url": "https://en.wikipedia.org/wiki/Active_Directory",
            "id": 218      
        }, 
        {
            "name": "Ambient network",
            "definition": "Ambient networks is a network integration design that seeks to solve problems relating to switching between networks to maintain contact with the outside world. This project aims to develop a network software-driven infrastructure that will run on top of all current or future network physical infrastructures to provide a way for devices to connect to each other, and through each other to the outside world.\n\nExample:\n\nAlice has a PAN, a Personal Area Network on her body: she has a Bluetooth enabled PDA, mobile phone and laptop that she is carrying, and are all currently turned on, and forming a network. Her laptop also has the ability to connect using an available WLAN, and her mobile phone has the ability to connect through GPRS, though GPRS is slower and much more costly for Alice to use. She is now on the move, and her laptop is downloading her emails using the GPRS connection on the mobile:\n\n Laptop → (Bluetooth) → Mobile → (GPRS) → Mobile phone network\n\nWhile walking, she passes into an area covered by a free WLAN hotspot: Her PAN now immediately starts to initiate a connection with the hotspot. This is called ‘merging’ of the networks (that of the hotspot and that of her PAN). Once this merging is complete, the downloading of her email continues totally unaffected, but instead of using the expensive and slow GPRS connection, it is now using the newly established WLAN connection. If she now wants to browse the web with her PDA, the PDA will also use the WLAN connection of the laptop:\n\nPDA → (bluetooth) → Laptop → (WLAN) → Hotspot.",
            "url": "https://en.wikipedia.org/wiki/Ambient_network",
            "id": 219      
        }, 
        {
            "name": "Ambient intelligence (AmI)",
            "definition": "In computing, ambient intelligence (AmI) refers to electronic environments that are sensitive and responsive to the presence of people. Ambient intelligence was a projection on the future of consumer electronics, telecommunications and computing that was originally developed in the late 1990s by Eli Zelkha and his team at Palo Alto Ventures for the time frame 2010–2020. \n\nAmbient intelligence would allow devices to work in concert to support people in carrying out their everyday life activities, tasks and rituals in an intuitive way using information and intelligence that is hidden in the network connecting these devices (for example: The Internet of Things). As these devices grew smaller, more connected and more integrated into our environment, the technological framework behind them would disappear into our surroundings until only the user interface remains perceivable by users.\n\nThe ambient intelligence paradigm builds upon pervasive computing, ubiquitous computing, profiling, context awareness, and human-centric computer interaction design, and is characterized by systems and technologies that are embedded, context aware, personalized, adaptive and anticipatory. A typical context of ambient intelligence environment is home, but may also be extended to work spaces (offices, co-working), public spaces (based on technologies such as smart street lights), and hospital environments.",
            "url": "https://en.wikipedia.org/wiki/Ambient_intelligence",
            "id": 220      
        }, 
        {
            "name": "Acceptable use policy (AUP)",
            "definition": "An acceptable use policy (AUP), acceptable usage policy, Internet use policy IUP), or fair use policy is a set of rules applied by the owner, creator or administrator of a computer network website, or service. That restricts the ways in which the network, website or system may be used and sets guidelines as to how it should be used. AUP documents are written for corporations, businesses, universities, schools, internet service providers (ISPs), and website owners, often to reduce the potential for legal action that may be taken by a user, and often with little prospect of enforcement.\n\nAcceptable use policies are an integral part of the framework of information security policies; it is often common practice to ask new members of an organization to sign an AUP before they are given access to its information systems. For this reason, an AUP must be concise and clear. While at the same time covering the most important points about what users are, and are not allowed to do with the IT systems of an organization, it should refer users to the more comprehensive security policy where relevant. It should also, and very notably define what sanctions will be applied if a user breaks the AUP. Compliance with this policy should as usual, be measured by regular audits.",
            "url": "https://en.wikipedia.org/wiki/Acceptable_use_policy",
            "id": 221     
        }, 
        {
            "name": "Autonomous system (Internet)",
            "definition": "An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain, that presents a common and clearly defined routing policy to the Internet. Each AS is assigned an autonomous system number (ASN), for use in Border Gateway Protocol (BGP) routing. Autonomous System Numbers are assigned to Local Internet Registries (LIRs) and end user organizations by their respective Regional Internet Registries (RIRs), which in turn receive blocks of ASNs for reassignment from the Internet Assigned Numbers Authority (IANA). The IANA also maintains a registry of ASNs which are reserved for private use (and should therefore not be announced to the global Internet).\n\nOriginally, the definition required control by a single entity, typically an Internet service provider (ISP) or a very large organization with independent connections to multiple networks, that adhered to a single and clearly defined routing policy. In March 1996, the newer definition came into use because multiple organizations can run BGP using private AS numbers to an ISP that connects all those organizations to the Internet. Even though there may be multiple autonomous systems supported by the ISP, the Internet only sees the routing policy of the ISP. That ISP must have an officially registered ASN.\n\nThe number of unique autonomous networks in the routing system of the Internet exceeded 5,000 in 1999, 30,000 in late 2008, 35,000 in mid-2010, 42,000 in late 2012, 54,000 in mid-2016 and 60,000 in early 2018. The number of allocated ASNs exceeded 100,000 as of March 2021.",
            "url": "https://en.wikipedia.org/wiki/Autonomous_system_(Internet)",
            "id": 222      
        }, 
        {
            "name": "Actuator",
            "definition": "An actuator is a component of a machine that is responsible for moving and controlling a mechanism or system, for example by opening a valve. In simple terms, it is a ‘mover’.\n\nAn actuator requires a control signal and a source of energy. The control signal is relatively low energy and may be electric voltage or current, pneumatic, or hydraulic fluid pressure, or even human power. Its main energy source may be an electric current, hydraulic pressure, or pneumatic pressure. When it receives a control signal, an actuator responds by converting the source's energy into mechanical motion. In the electric, hydraulic, and pneumatic sense, it is a form of automation or automatic control.\n\nAn actuator is a mechanism by which a control system acts upon to perform an operation or task. The control system can be simple (a fixed mechanical or electronic system), software-based (e.g. a printer driver, robot control system), a human, or any other input. Along with sensors and controllers, actuators are an integral component in IoT (Internet of Things) interactions.",
            "url": "https://en.wikipedia.org/wiki/Actuator",
            "id": 223      
        }, 
        {
            "name": "Transceiver",
            "definition": "In radio communication, a transceiver is an electronic device which is a combination of a radio transmitter and a receiver, hence the name. It can both transmit and receive radio waves using an antenna, for communication purposes. These two related functions are often combined in a single device to reduce manufacturing costs. The term is also used for other devices which can both transmit and receive through a communications channel, such as optical transceivers which transmit and receive light in optical fiber systems, and bus transceivers which transmit and receive digital data in computer data buses.",
            "url": "https://en.wikipedia.org/wiki/Transceiver",
            "id": 224      
        }, 
        {
            "name": "Application delivery controller (ADC)",
            "definition": "Software running in commodity hardware or a specialized appliance that provides load balancing, authentication and accounting for application servers. Primarily a load balancer with enhanced features, an ADC resides in the DMZ behind the firewall or router and before the servers or web farm. You’ll often find these in a datacenter, as part of an application delivery network (ADN), that helps perform common tasks, such as those done by web accelerators to remove load from the web servers themselves.",
            "url": "https://en.wikipedia.org/wiki/Application_delivery_controller",
            "id": 225      
        }, 
        {
            "name": "Application integration",
            "definition": "Application integration is translating data and commands from the format of one application into the format of another. It is essentially data and command conversion on an ongoing basis between two or more incompatible systems. Implementing application integration has traditionally been done by tedious programming, or occasionally one package might support the interfaces of one or two other packages. However, the trend today is to use message brokers, applications servers and other specialized integration products that provide a common connecting point. Since the advent of the Web, these pre-packaged ‘middleware’ solutions have become widely used to Web enable the enterprise.\n\nIt may also refer to redesigning disparate information systems into one system that uses a common set of data structures and rules.",
            "url": "https://en.wikipedia.org/wiki/Enterprise_application_integration",
            "id": 226      
        }, 
        {
            "name": "Middleware",
            "definition": "Software that functions as a conversion or translation layer. Middleware is also a consolidator and integrator. It can be described as ‘software glue’. Custom-programmed middleware solutions have been developed for decades to enable one application to interface with another, which either runs on a different platform or comes from a different vendor.\n\nToday, there is a diverse group of middleware products including: transaction processing monitor (TP Monitor), messaging middleware, distributed processing, distributed database middleware, database middleware, common interfaces, application server middleware, universal computing, network logon and enterprise integration. For example illustrations, see https://www.pcmag.com/encyclopedia/term/middleware",
            "url": "https://en.wikipedia.org/wiki/Middleware",
            "id": 227      
        }, 
        {
            "name": "Message broker",
            "definition": "A message broker (also known as an integration broker or interface engine) is an intermediary computer program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. Message brokers are elements in telecommunication or computer networks where software applications communicate by exchanging formally-defined messages. Message brokers are a building block of message-oriented middleware (MOM) but are typically not a replacement for traditional middleware like MOM and remote procedure call (RPC).\n\nA message broker is an architectural pattern for message validation, transformation, and routing. It mediates communication among applications, minimizing the mutual awareness that applications should have of each other in order to be able to exchange messages, effectively implementing decoupling.\n\nThe primary purpose of a broker is to take incoming messages from applications and perform some action on them. Message brokers can decouple end-points, meet specific non-functional requirements, and facilitate reuse of intermediary functions. For example, a message broker may be used to manage a workload queue or message queue for multiple receivers, providing reliable storage, guaranteed message delivery and perhaps transaction management.",
            "url": "https://en.wikipedia.org/wiki/Message_broker",
            "id": 228      
        }, 
        {
            "name": "Network programmability",
            "definition": "Network programmability is the use of software to deploy, manage, and troubleshoot network elements. A programmable network is driven by an intelligent software stack that can take action based on business requests or network events. Network programmability can help communication service providers adapt to new trends including internet of things (IoT), 5G and edge computing.\n\nComplementary to network programmability is Software Defined Networking (SDN), which not only separates the control plane and forwarding plane of network elements but also provides (application programming interfaces) APIs to control and manage them.",
            "url": "https://www.redhat.com/en/blog/architects-guide-network-programmability",
            "id": 229      
        }, 
        {
            "name": "Proxy server",
            "definition": "In computer networking, a proxy server is a server application that acts as an intermediary between a client requesting a resource and the server providing that resource. Instead of connecting directly to a server that can fulfill a request for a resource, such as a file or web page, the client directs the request to the proxy server, which evaluates the request and performs the required network transactions.\n\nThis serves as a method to simplify or control the complexity of the request, or provide additional benefits such as load balancing, privacy, or security. Proxies were devised to add structure and encapsulation to distributed systems. A proxy server thus functions on behalf of the client when requesting service, potentially masking the true origin of the request to the resource server.",
            "url": "https://en.wikipedia.org/wiki/Proxy_server",
            "id": 230      
        }, 
        {
            "name": "Geo-fence",
            "definition": "A geofence is a virtual perimeter for a real-world geographic area. A geo-fence could be dynamically generated (as in a radius around a point location) or match a predefined set of boundaries (such as school zones or neighborhood boundaries).\n\nThe use of a geofence is called geofencing, and one example of use involves a location-aware device of a location-based service (LBS) user entering or exiting a geo-fence. This activity could trigger an alert to the device's user as well as messaging to the geo-fence operator. This info, which could contain the location of the device, could be sent to a mobile telephone or an email account.\n\nGeofencing uses technologies like GPS, or even IP address ranges to build their virtual fence. These virtual fences can be used to track the physical location of the device active in the particular region or the fence area. The location of the person using the device is taken as geocoding data and can be used further for advertising purposes.",
            "url": "https://en.wikipedia.org/wiki/Geo-fence",
            "id": 231      
        }, 
        {
            "name": "Stack",
            "definition": "In computing, a solution stack or software stack is a set of software subsystems or components needed to create a complete platform such that no additional software is needed to support applications. Applications are said to 'run on' or 'run on top of' the resulting platform.\n\nFor example, to develop a web application, the architect defines the stack as the target operating system, web server, database, and programming language. Another version of a software stack is operating system, middleware, database, and applications. Regularly, the components of a software stack are developed by different developers independently from one another.\n\nSome components/subsystems of an overall system are chosen together often enough that the particular set is referred to by a name representing the whole, rather than by naming the parts. Typically, the name is an acronym representing the individual components. Notable examples include ELK, LAMP, LAPP, MEAN, MERN and XAMPP.\n\nThe term ‘solution stack’ has, historically, occasionally included hardware components as part of a final product, mixing both the hardware and software in layers of support.\n\nA full-stack developer is expected to be able to work in all the layers of the stack. A full-stack web developer can be defined as a developer or engineer who works with both the front and back ends of a website or application. This means they can lead platform builds that involve databases, user-facing websites, and working with clients during the planning phase of projects.",
            "url": "https://en.wikipedia.org/wiki/Solution_stack",
            "id": 232      
        }, 
        {
            "name": "Scripting language",
            "definition": "A scripting language or script language is a programming language for a runtime system that automates the execution of tasks that would otherwise be performed individually by a human operator. Scripting languages are usually interpreted at runtime rather than compiled.\n\nA scripting language's primitives are usually elementary tasks or API calls, and the scripting language allows them to be combined into more programs. Environments that can be automated through scripting include application software, text editors, web pages, operating system shells, embedded systems, and computer games. A scripting language can be viewed as a domain-specific language for a particular environment; in the case of scripting an application, it is also known as an extension language. Scripting languages are also sometimes referred to as very high-level programming languages, as they sometimes operate at a high level of abstraction, or as control languages, particularly for job control languages on mainframes.\n\nThe term scripting language is also used in a wider sense, namely, to refer to dynamic high-level programming languages in general; some are strictly interpreted languages, while others use a form of compilation. In this context, the term script refers to a small program in such a language; typically, contained in a single file, and no larger than a few thousand lines of code.\n\nThe spectrum of scripting languages ranges from small to large, and from highly domain-specific language to general-purpose programming languages. A language may start as small and highly domain-specific and later develop into a portable and general-purpose language; conversely, a general-purpose language may later develop special domain-specific dialects.\n\nExamples of scripting languages include Bash, PowerShell, Python, JavaScript and Visual Basic for Applications (VBA).",
            "url": "https://en.wikipedia.org/wiki/Scripting_language",
            "id": 233      
        }, 
        {
            "name": "Polling",
            "definition": "Polling, or polled operation, in computer science, refers to actively sampling the status of an external device by a client program as a synchronous activity. Polling is most often used in terms of input/output (I/O), and is also referred to as polled I/O or software-driven I/O.\n\nPolling is a technique to determine, through continuous interrogation, whether a terminal or device is ready to transfer data. Contrast this with event-driven or interrupt-driven techniques, in which the system, when data is ready to be transferred, sends a signal and interrupts the system.",
            "url": "https://en.wikipedia.org/wiki/Polling_(computer_science)",
            "id": 234      
        }, 
        {
            "name": "Interrupt",
            "definition": "In digital computers, an interrupt (sometimes referred to as a trap) is a request for the processor to interrupt currently executing code (when permitted), so that the event can be processed in a timely manner. If the request is accepted, the processor will suspend its current activities, save its state, and execute a function called an interrupt handler (or an interrupt service routine, ISR) to deal with the event. This interruption is often temporary, allowing the software to resume normal activities after the interrupt handler finishes, although the interrupt could instead indicate a fatal error.\n\nInterrupts are commonly used by hardware devices to indicate electronic or physical state changes that require time-sensitive attention. Interrupts are also commonly used to implement computer multitasking, especially in real-time computing. Systems that use interrupts in these ways are said to be interrupt-driven.",
            "url": "https://en.wikipedia.org/wiki/Interrupt",
            "id": 235      
        }, 
        {
            "name": "Surface-mount technology (SMT)",
            "definition": "Surface-mount technology (SMT) is a method in which the electrical components are mounted directly onto the surface of a printed circuit board (PCB). An electrical component mounted in this manner is referred to as a surface-mount device (SMD). In industry, this approach has largely replaced the through-hole technology construction method of fitting components, in large part because SMT allows for increased manufacturing automation which reduces cost and improves quality. It also allows for more components to fit on a given area of substrate. Both technologies can be used on the same board, with the through-hole technology often used for components not suitable for surface mounting such as large transformers and heat-sinked power semiconductors.\n\nAn SMT component is usually smaller than its through-hole counterpart because it has either smaller leads or no leads at all. It may have short pins or leads of various styles, flat contacts, a matrix of solder balls (BGAs), or terminations on the body of the component.\n\nSurface mounting was originally called ‘planar mounting’.",
            "url": "https://en.wikipedia.org/wiki/Surface-mount_technology",
            "id": 236      
        }, 
        {
            "name": "Advanced persistent threat (APT)",
            "definition": "An advanced persistent threat (APT) is a stealthy threat actor, typically a nation state or state-sponsored group, which gains unauthorized access to a computer network and remains undetected for an extended period. In recent times, the term may also refer to non-state-sponsored groups conducting large-scale targeted intrusions for specific goals.\n\nSuch threat actors' motivations are typically political or economic. Every major business sector has recorded instances of cyberattacks by advanced actors with specific goals, whether to steal, spy, or disrupt. These targeted sectors include government, defense, financial services, legal services, industrial, telecoms, consumer goods and many more. Some groups utilize traditional espionage vectors, including social engineering, human intelligence and infiltration to gain access to a physical location to enable network attacks. The purpose of these attacks is to install custom malware (malicious software).\n\nThe median ‘dwell-time’, the time an APT attack goes undetected, is over 100 days globally.",
            "url": "https://en.wikipedia.org/wiki/Advanced_persistent_threat",
            "id": 237      
        }, 
        {
            "name": "Autostereoscopy",
            "definition": "Autostereoscopy is any method of displaying stereoscopic images (adding binocular perception of 3D depth) without the use of special headgear, glasses, something that affects vision, or anything for eyes on the part of the viewer. Because headgear is not required, it is also called ‘glasses-free 3D’ or ‘glassesless 3D’.\n\nThere are two broad approaches currently used to accommodate motion parallax and wider viewing angles: eye-tracking, and multiple views so that the display does not need to sense where the viewer's eyes are located. Examples of autostereoscopic displays technology include lenticular lens, parallax barrier, volumetric display, holographic and light field displays.",
            "url": "https://en.wikipedia.org/wiki/Autostereoscopy",
            "id": 238      
        }, 
        {
            "name": "Buffer underrun",
            "definition": "In computing, buffer underrun or buffer underflow is a state occurring when a buffer used to communicate between two devices or processes is fed with data at a lower speed than the data is being read from it. The term is distinct from buffer overflow, a condition where a portion of memory being used as a buffer has a fixed size but is filled with more than that amount of data. This requires the program or device reading from the buffer to pause its processing while the buffer refills. This can cause undesired and sometimes serious side effects because the data being buffered is generally not suited to stop-start access of this kind.\n\nIn relation to concurrent programming, a buffer underrun can be considered a form of resource starvation. The terms buffer ‘underrun’ and ‘buffer underflow’ are also used to mean ‘buffer underwrite’, a condition similar to buffer overflow, but where the program is tricked into writing before the beginning of the buffer, overriding potential data there, like permission bits.",
            "url": "https://en.wikipedia.org/wiki/Buffer_underrun",
            "id": 239      
        }, 
        {
            "name": "AV storm",
            "definition": "A serious degradation of system performance when an antivirus scan is scheduled to run at the same time in multiple virtual machines on the same computer. Advanced antivirus programs are aware of virtualization and can limit scans to a maximum number of VMs or coordinate scanning at different intervals.",
            "url": "https://www.youtube.com/watch?v=GpVRNZaLuRc",
            "id": 240      
        }, 
        {
            "name": "Artificial life",
            "definition": "Artificial life (often abbreviated ALife or A-Life) is a field of study wherein researchers examine systems related to natural life, its processes, and its evolution, through the use of simulations with computer models, robotics, and biochemistry. There are three main kinds of alife, named for their approaches: soft, from software; hard, from hardware; and wet, from biochemistry. Artificial life researchers study traditional biology by trying to recreate aspects of biological phenomena.\n\nArtificial life studies the fundamental processes of living systems in artificial environments in order to gain a deeper understanding of the complex information processing that define such systems. These topics are broad, but often include evolutionary dynamics, emergent properties of collective systems, biomimicry, as well as related issues about the philosophy of the nature of life and the use of lifelike properties in artistic works.\n\nThe modeling philosophy of artificial life strongly differs from traditional modeling by studying not only ‘life-as-we-know-it’ but also ‘life-as-it-might-be’.",
            "url": "https://en.wikipedia.org/wiki/Artificial_life",
            "id": 241      
        }, 
        {
            "name": "Brackets vs. Braces",
            "definition": "[ ]\n\nSquare brackets, or simply ‘brackets’.\n\nBrackets are used in many computer programming languages, primarily for array indexing. But they are also used to denote general tuples, sets and other structures, just as in mathematics. There may be several other uses as well, depending on the language at hand.\n\n{ }\n\nCurly brackets, or simply ‘braces’.\n\nIn many programming languages, curly brackets enclose groups of statements and create a local scope. Such languages (C, C#, C++ and many others) are therefore called curly bracket languages. They are also used to define structures and enumerated type in these languages.\n\nOne way to remember them apart is that braces look like they are ‘bracing’ under enormous pressure, almost buckling.",
            "url": "https://en.wikipedia.org/wiki/Bracket",
            "id": 242      
        }, 
        {
            "name": "Angle brackets",
            "definition": "Angle brackets are the < and > symbols that are on the comma and period keys on the keyboard. Angle brackets are also called ‘chevrons’, ‘pointy brackets’, ‘triangular brackets’, ‘diamond brackets’, ‘tuples’, ‘guillemets’, ‘left and right carets’, ‘broken brackets’, or ‘brokets’.\n\nThe ASCII less-than and greater-than characters <> are often used for angle brackets. In most cases only those characters are accepted by computer programs; the Unicode angle brackets are not recognized (for instance in HTML tags).\n\nIn C++, chevrons (actually less-than and greater-than) are used to surround arguments to templates. In HTML, chevrons (actually 'greater than' and 'less than' symbols) are used to bracket meta text. For example <b> denotes that the following text should be displayed as bold. Pairs of meta text tags are required – much as brackets themselves are usually in pairs. The end of the bold text segment would be indicated by </b>. This use is sometimes extended as an informal mechanism for communicating mood or tone in digital formats such as messaging, for example adding <sighs> at the end of a sentence.",
            "url": "https://en.wikipedia.org/wiki/Bracket#Angle_brackets",
            "id": 243      
        }, 
        {
            "name": "AWS Lambda",
            "definition": "An Amazon AWS service that runs the customer's program code without them having to provision and manage a server in the AWS system. It is a prime example of function as a service (FaaS).\n\nAWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced in November 2014.\n\nNode.js, Python, Java, Go, Ruby and C# (through .NET) are all officially supported, as of 2018. For pricing, AWS Lambda is metered by rounding up to the nearest millisecond with no minimum execution time.",
            "url": "https://en.wikipedia.org/wiki/AWS_Lambda",
            "id": 244      
        }, 
        {
            "name": "Software agent",
            "definition": "In computer science, a software agent is a computer program that acts for a user or other program in a relationship of agency, which derives from the Latin ‘agere’ (to do): an agreement to act on one's behalf. Such ‘action on behalf of’ implies the authority to decide which, if any, action is appropriate. Agents are colloquially known as bots, from robot. They may be embodied, as when execution is paired with a robot body, or as software such as a chatbot executing on a phone (e.g. Siri) or other computing device. Software agents may be autonomous or work together with other agents or people. Software agents interacting with people (e.g. chatbots, human-robot interaction environments) may possess human-like qualities such as natural language understanding and speech, personality or embody humanoid form.\n\nRelated and derived concepts include intelligent agents (in particular exhibiting some aspects of artificial intelligence, such as reasoning), autonomous agents (capable of modifying the methods of achieving their objectives), distributed agents (being executed on physically distinct computers), multi-agent systems (distributed agents that work together to achieve an objective that could not be accomplished by a single agent acting alone), and mobile agents (agents that can relocate their execution onto different processors).",
            "url": "https://en.wikipedia.org/wiki/Software_agent",
            "id": 245      
        }, 
        {
            "name": "Sorting",
            "definition": "In computer science, arranging in an ordered sequence is called ‘sorting’. Sorting is a common operation in many applications, and efficient algorithms to perform it have been developed.\n\nThe most common uses of sorted sequences are:\n\n1. Making lookup or search efficient;\n2. Making merging of sequences efficient;\n3. Enable processing of data in a defined order;\n\nCommon sorting algorithms:\n\nBubble/Shell sort: Exchange two adjacent elements if they are out of order. Repeat until array is sorted.\n\nInsertion sort: Scan successive elements for an out-of-order item, then insert the item in the proper place.\n\nSelection sort: Find the smallest (or biggest) element in the array, and put it in the proper place. Swap it with the value in the first position. Repeat until array is sorted.\n\nQuick sort: Partition the array into two segments. In the first segment, all elements are less than or equal to the pivot value. In the second segment, all elements are greater than or equal to the pivot value. Finally, sort the two segments recursively.\n\nMerge sort: Divide the list of elements in two parts, sort the two parts individually and then merge it.\n\nThe opposite of sorting, rearranging a sequence of items in a random or meaningless order, is called shuffling.",
            "url": "https://en.wikipedia.org/wiki/Sorting",
            "id": 246      
        }, 
        {
            "name": "Isotropic vs. Anisotropic",
            "definition": "Isotropic and anisotropic are terms that describe whether or not the properties of materials depend on direction. When a property is the same in all directions, the material is isotropic. When a property varies according to direction, the material is anisotropic. The terms come from the Greek isos (equal) and tropos (way). The ‘an’ in ‘anisotropic’ means ‘not’.\n\nProperties that are isotropic in some materials and anisotropic in others include refractive index, absorbance, electrical conductivity, tensile strength, Young’s modulus, etc.\n\nKeep in mind, a material may be isotropic for one property, yet anisotropic for another. For example, a piece of polarized glass is isotropic for mechanical properties, yet anisotropic for light filtration. Also, scale is important. For example, the universe is generally isotropic and homogenous with respect to cosmic blackbody radiation, but when you examine regions more closely, you see heterogeneity and anisotropy.\n\nAn isotropic antenna is an omnidirectional antenna: it radiates equal power in all directions, while an anisotropic antenna is a directional antenna: the power level is not the same in all directions.",
            "url": "https://study.com/learn/lesson/isotropic-anisotropic.html",
            "id": 247      
        }, 
        {
            "name": "Artificial immune systems (AIS)",
            "definition": "In artificial intelligence, artificial immune systems (AIS) are a class of computationally intelligent, rule-based machine learning systems inspired by the principles and processes of the vertebrate immune system. The algorithms are typically modeled after the immune system's characteristics of learning and memory for use in problem-solving.",
            "url": "https://en.wikipedia.org/wiki/Artificial_immune_system",
            "id": 248      
        }, 
        {
            "name": "Aliasing",
            "definition": "In computing, aliasing describes a situation in which a data location in memory can be accessed through different symbolic names in the program. Thus, modifying the data through one name implicitly modifies the values associated with all aliased names, which may not be expected by the programmer. As a result, aliasing makes it particularly difficult to understand, analyze and optimize programs. Aliasing analysers intend to make and compute useful information for understanding aliasing in programs.",
            "url": "https://en.wikipedia.org/wiki/Aliasing_(computing)",
            "id": 249      
        }, 
        {
            "name": "alias",
            "definition": "In computing, alias is a command in various command-line interpreters (shells), which enables a replacement of a word by another string. It is mainly used for abbreviating a system command, or for adding default arguments to a regularly used command. alias is available in Unix shells, AmigaDOS, 4DOS/4NT, KolibriOS, Windows PowerShell, ReactOS, and the EFI shell. Aliasing functionality in the MS-DOS and Microsoft Windows operating systems is provided by the DOSKey command-line utility.\n\nAn alias will last for the life of the shell session. Regularly used aliases can be set from the shell's rc file (such as .bashrc) so that they will be available upon the start of the corresponding shell session. The alias commands may either be written in the config file directly or sourced from a separate file.\n\nExample:\n\nalias gc='git commit'",
            "url": "https://en.wikipedia.org/wiki/Alias_(command)",
            "id": 250      
        }, 
        {
            "name": "Alice (software)",
            "definition": "An open source, object-oriented development environment for building 3D animations, games and virtual worlds. Running under Windows, Mac and Linux, it is based on Java and is programmed by dragging and dropping predefined functions into a work area. Designed to teach fundamental concepts to novices, such as the relationship between programming statements and objects, Alice is supported by textbooks, tutorials, lessons and tests.\n\n The software was developed first at University of Virginia in 1994, then Carnegie Mellon (from 1997), by a research group led by Randy Pausch. According to Pausch, the name ‘Alice’ comes from author Lewis Carroll, who wrote Alice’s Adventures in Wonderland.\n\n‘Carroll was a mathematician, novelist, and photographer. Most important, he could do intellectually difficult things but also realized the most powerful thing was to be able to communicate clearly and in an entertaining way. This inspires our efforts to make something as complex as computer programming easy and fun.’",
            "url": "https://en.wikipedia.org/wiki/Randy_Pausch",
            "id": 251      
        }, 
        {
            "name": "",
            "definition": "In computer science, a high-level programming language is a programming language with strong abstraction from the details of the computer. In contrast to low-level programming languages, it may use natural language elements, be easier to use, or may automate (or even hide entirely) significant areas of computing systems (e.g. memory management), making the process of developing a program simpler and more understandable than when using a lower-level language. The amount of abstraction provided defines how ‘high-level’ a programming language is.\n\nExamples of high-level programming languages in active use today include Python, Visual Basic, Delphi, Perl, PHP, ECMAScript, Ruby, C#, Java and many others.\n\nThe terms high-level and low-level are inherently relative. Some decades ago, the C language, and similar languages, were most often considered ‘high-level’, as it supported concepts such as expression evaluation, parameterised recursive functions, and data types and structures, while assembly language was considered ‘low-level’. Today, many programmers might refer to C as low-level, as it lacks a large runtime-system (no garbage collection, etc.), basically supports only scalar operations, and provides direct memory addressing. It, therefore, readily blends with assembly language and the machine level of CPUs and microcontrollers.",
            "url": "High-level programming language",
            "id": 252      
        }, 
        {
            "name": "Machine code",
            "definition": "In computer programming, machine code is any low-level programming language, consisting of machine language instructions, which are used to control a computer's central processing unit (CPU). Each instruction causes the CPU to perform a very specific task, such as a load, a store, a jump, or an arithmetic logic unit (ALU) operation on one or more units of data in the CPU's registers or memory.\n\nMachine code is a strictly numerical language which is designed to run as fast as possible, and may be considered as the lowest-level representation of a compiled or assembled computer program or as a primitive and hardware-dependent programming language. While it is possible to write programs directly in machine code, managing individual bits and calculating numerical addresses and constants manually is tedious and error-prone. For this reason, programs are very rarely written directly in machine code in modern contexts, but may be done for low level debugging, program patching (especially when assembler source is not available) and assembly language disassembly.\n\nThe majority of practical programs today are written in higher-level languages or assembly language. The source code is then translated to executable machine code by utilities such as compilers, assemblers, and linkers, with the important exception of interpreted programs, which are not translated into machine code. However, the interpreter itself, which may be seen as an executor or processor performing the instructions of the source code, typically consists of directly executable machine code (generated from assembly or high-level language source code).",
            "url": "https://en.wikipedia.org/wiki/Machine_code",
            "id": 253      
        }, 
        {
            "name": "Assembly language",
            "definition": "In computer programming, assembly language (or assembler language), is any low-level programming language in which there is a very strong correspondence between the instructions in the language and the architecture's machine code instructions. Assembly language usually has one statement per machine instruction (1:1), but constants, comments, assembler directives, symbolic labels of, e.g., memory locations, registers, and macros are generally also supported.\n\nAssembly code is converted into executable machine code by a utility program referred to as an assembler. The term ‘assembler’ is generally attributed to Wilkes, Wheeler and Gill in their 1951 book The Preparation of Programs for an Electronic Digital Computer, who, however, used the term to mean ‘a program that assembles another program consisting of several sections into a single program’. The conversion process is referred to as assembly, as in assembling the source code. The computational step when an assembler is processing a program is called assembly time. Assembly language may also be called symbolic machine code.\n\nBecause assembly depends on the machine code instructions, each assembly language is specific to a particular computer architecture.",
            "url": "",
            "id": 254      
        }, 
        {
            "name": "Microcode",
            "definition": "In processor design, microcode is a technique that interposes a layer of computer organization between the central processing unit (CPU) hardware and the programmer-visible instruction set architecture of a computer. Microcode is a layer of hardware-level instructions that implement higher-level machine code instructions or internal finite-state machine sequencing in many digital processing elements. Microcode is used in general-purpose central processing units, although in current desktop CPUs, it is only a fallback path for cases that the faster hardwired control unit cannot handle.\n\nMicrocode typically resides in special high-speed memory and translates machine instructions, state machine data or other input into sequences of detailed circuit-level operations. It separates the machine instructions from the underlying electronics so that instructions can be designed and altered more freely. It also facilitates the building of complex multi-step instructions, while reducing the complexity of computer circuits. Writing microcode is often called microprogramming and the microcode in a particular processor implementation is sometimes called a microprogram.",
            "url": "https://en.wikipedia.org/wiki/Microcode",
            "id": 255      
        }, 
        {
            "name": "Optical computer",
            "definition": "A computer in which all internal circuits use light instead of electricity. Long predicted, an all-optical computer is not expected for some time as there are enormous hurdles to overcome. However, there are definite advantages of optical circuits over electrical ones. Light beams are neither affected by external radiation, nor by themselves. In fact, light beams can cross each other, allowing for simpler travel paths between inputs and outputs.",
            "url": "https://en.wikipedia.org/wiki/Optical_computing",
            "id": 256      
        }, 
        {
            "name": "AWGTHTGTTA",
            "definition": "Internet slang for 'Are we going to have to go through this again?'",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "id": 257      
        }, 
        {
            "name": "AX Wi-Fi",
            "definition": "Another name for 802.11ax\n\nIEEE 802.11ax, officially marketed by the Wi-Fi Alliance as Wi-Fi 6 (2.4 GHz and 5 GHz) and Wi-Fi 6E (6 GHz), is an IEEE standard for wireless local-area networks (WLANs) and the successor of 802.11ac. It is also known as High Efficiency Wi-Fi, for the overall improvements to Wi-Fi 6 clients under dense environments. It is designed to operate in license-exempt bands between 1 and 7.125 GHz, including the 2.4 and 5 GHz bands already in common use as well as the much wider 6 GHz band (5.925–7.125 GHz in the US).\n\nThe main goal of this standard is enhancing throughput-per-area in high-density scenarios, such as corporate offices, shopping malls and dense residential apartments. While the nominal data rate improvement against 802.11ac is only 37%, the overall throughput improvement (over an entire network) is 300% (hence High Efficiency).  This also translates to 75% lower latency.\n\nThe quadrupling of overall throughput is made possible by a higher spectral efficiency. The key feature underpinning 802.11ax is orthogonal frequency-division multiple access (OFDMA), which is equivalent to cellular technology applied into Wi-Fi. Other improvements on spectrum utilization are better power-control methods to avoid interference with neighboring networks, higher order 1024‑QAM, up-link direction added with the down-link of MIMO and MU-MIMO to further increase throughput, as well as dependability improvements of power consumption and security protocols such as Target Wake Time and WPA3.",
            "url": "https://en.wikipedia.org/wiki/Wi-Fi_6",
            "id": 258      
        }, 
        {
            "name": "Alpha testing",
            "definition": "The alpha phase of the release life cycle is the first phase of software testing (alpha is the first letter of the Greek alphabet, used as the number 1). In this phase, developers generally test the software using white-box techniques. Additional validation is then performed using black-box or gray-box techniques, by another testing team. Moving to black-box testing inside the organization is known as alpha release.\n\nAlpha software is not thoroughly tested by the developer before it is released to customers. Alpha software may contain serious errors, and any resulting instability could cause crashes or data loss. Alpha software may not contain all of the features that are planned for the final version. In general, external availability of alpha software is uncommon in proprietary software, while open source software often has publicly available alpha versions. The alpha phase usually ends with a feature freeze, indicating that no more features will be added to the software. At this time, the software is said to be feature complete. A beta test is carried out following acceptance testing at the supplier's site (alpha test) and immediately before the general release of the software as a product. In general an alpha version or release of a software package intends to do something particular, mostly does so, yet isn't guaranteed to do so fully.",
            "url": "https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha",
            "id": 259      
        }, 
        {
            "name": "Beta testing",
            "definition": "Beta, named after the second letter of the Greek alphabet, is the software development phase following alpha. Software in the beta stage is also known as betaware. A beta phase generally begins when the software is feature complete but likely to contain a number of known or unknown bugs. Software in the beta phase will generally have many more bugs in it than completed software and speed or performance issues, and may still cause crashes or data loss.\n\nThe focus of beta testing is reducing impacts to users, often incorporating usability testing. The process of delivering a beta version to the users is called beta release and is typically the first time that the software is available outside of the organization that developed it. Software beta releases can be either public or private, depending on whether they are openly available or only available to a limited audience. Beta version software is often useful for demonstrations and previews within an organization and to prospective customers. Some developers refer to this stage as a preview, preview release, prototype, technical preview or technology preview (TP), or early access.\n\nBeta testers are people who actively report issues of beta software. They are usually customers or representatives of prospective customers of the organization that develops the software. Beta testers tend to volunteer their services free of charge but often receive versions of the product they test, discounts on the release version, or other incentives.\n\nSome software is kept in so-called perpetual beta, where new features are continually added to the software without establishing a final 'stable' release. As the Internet has facilitated rapid and inexpensive distribution of software, companies have begun to take a looser approach to use of the word beta.",
            "url": "https://en.wikipedia.org/wiki/Software_release_life_cycle#Beta",
            "id": 260      
        }, 
        {
            "name": "Feature complete (FC)",
            "definition": "A feature complete (FC) version of a piece of software has all of its planned or primary features implemented but is not yet final due to bugs, performance or stability issues. This occurs at the end of alpha testing of development. Usually a feature complete software still has to undergo beta testing and bug fixing, as well as performance or stability enhancing before it can go to release candidate, and finally gold status.",
            "url": "https://en.wikipedia.org/wiki/Software_release_life_cycle#Feature_complete",
            "id": 261      
        }, 
        {
            "name": "Release candidate (RC)",
            "definition": "A release candidate (RC), also known as ‘going silver’, is a beta version with potential to be a stable product, which is ready to release unless significant bugs emerge. In this stage of product stabilization, all product features have been designed, coded and tested through one or more beta cycles with no known showstopper-class bugs. A release is called code complete when the development team agrees that no entirely new source code will be added to this release. There could still be source code changes to fix defects, changes to documentation and data files, and peripheral code for test cases or utilities. Beta testers, if privately selected, will often be credited for using the release candidate as though it were a finished product. Beta testing is conducted in a client's or customer's location and to test the software from a user's perspective.",
            "url": "",
            "id": 262      
        }, 
        {
            "name": "Alphanumerish",
            "definition": "From ‘alphanumeric’, meaning a combination of letters and digits, alphanumerish uses digits and single letters as shorthand for words. It came about as more and more people began to routinely send short messages on tiny pager, PDA and cellphone screens. For example, 2U means ‘to you’ and UR means ‘you are’.",
            "url": "https://en.wikipedia.org/wiki/SMS_language",
            "id": 263      
        }, 
        {
            "name": "Fiber Bragg grating",
            "definition": "A Fiber Bragg grating (FBG) is a type of distributed Bragg reflector constructed in a short segment of optical fiber that reflects particular wavelengths of light and transmits all others. This is achieved by creating a periodic variation in the refractive index of the fiber core, which generates a wavelength-specific dielectric mirror. Hence a fiber Bragg grating can be used as an inline optical fiber to block certain wavelengths, can be used for sensing applications, or it can be used as wavelength-specific reflector.",
            "url": "https://en.wikipedia.org/wiki/Fiber_Bragg_grating",
            "id": 264      
        }, 
        {
            "name": "Blacksurfing",
            "definition": "Using white or light gray text on a black or other darker background in order to lessen the amount of energy used by a monitor or to lessen the strain on one’s eyes caused by glaring white backgrounds.",
            "url": "https://www.pcmag.com/encyclopedia/term/blacksurfing",
            "id": 265      
        }, 
        {
            "name": "Blackholing",
            "definition": "In networking, a black hole refers to a place in the network where incoming or outgoing traffic is silently discarded (or ‘dropped’), without informing the source that the data did not reach its intended recipient. When examining the topology of the network, the black holes themselves are invisible, and can only be detected by monitoring the lost traffic; hence the name.\n\nThe most common form of black hole is simply an IP address that specifies a host machine that is not running or an address to which no host has been assigned. A null route or black hole route is a network route (routing table entry) that goes nowhere. Matching packets are dropped (ignored) rather than forwarded, acting as a kind of very limited firewall. The act of using null routes is often called blackhole filtering.",
            "url": "https://en.wikipedia.org/wiki/Black_hole_(networking)",
            "id": 266      
        }, 
        {
            "name": "Naming fiascos",
            "definition": "The thoughtless naming of technical concepts and products in the computer industry. Not just products, but the shortsighted naming of routines and statements programmers use when writing source code causes massive headaches later when others try to read it. Not to be forgotten is the constant renaming of the same application by marketers who believe new names mean new business.",
            "url": "https://www.pcmag.com/encyclopedia/term/naming-fiascos",
            "id": 267      
        }, 
        {
            "name": "Bleeding edge",
            "definition": "A pun on ‘leading edge’. It implies that using the latest technology is often risky because it has not been tested with enough users and may not perform as expected. Introducing an advanced product or service is also risky because the user community may not be ready for it or really want it.",
            "url": "https://en.wikipedia.org/wiki/Emerging_technologies#In_the_media",
            "id": 268      
        }, 
        {
            "name": "Breadboard",
            "definition": "A breadboard, or protoboard, is a construction base for prototyping of electronics. Originally the word referred to a literal bread board, a polished piece of wood used when slicing bread. In the 1970s the solderless breadboard (a.k.a. plugboard, a terminal array board) became available and nowadays the term ‘breadboard’ is commonly used to refer to these.\n\nBecause the solderless breadboard does not require soldering, it is reusable. This makes it easy to use for creating temporary prototypes and experimenting with circuit design. For this reason, solderless breadboards are also popular with students and in technological education. Older breadboard types did not have this property. A stripboard (Veroboard) and similar prototyping printed circuit boards, which are used to build semi-permanent soldered prototypes or one-offs, cannot easily be reused. A variety of electronic systems may be prototyped by using breadboards, from small analog and digital circuits to complete central processing units (CPUs).",
            "url": "https://en.wikipedia.org/wiki/Breadboard",
            "id": 269      
        }, 
        {
            "name": "Blind signature",
            "definition": "A method used with digital signatures when the privacy of the sender's message is extremely important and when the signing is applied to the message by a third party rather than the message creator. Before handing the message over for signing, the sender uses a blinding algorithm to scramble the message. A blind signature allows a third party to sign a message and verify that the message came from a particular sender but without them knowing the message contents.",
            "url": "https://en.wikipedia.org/wiki/Blind_signature",
            "id": 270      
        }, 
        {
            "name": "Breakout box",
            "definition": "A breakout box is a piece of electrical test equipment used to support integration testing, expedite maintenance, and streamline the troubleshooting process at the system, subsystem, and component level by simplifying the access to test signals. Breakout boxes span a wide spectrum of functionality. Some serve to break out every signal connection coming into a unit while others breakout only specific signals commonly monitored for either testing or troubleshooting purposes. Some have electrical connectors and others have optical fiber connectors.\n\nA breakout box serves as a troubleshooting tool to determine the wiring of an electrical connector interface on a networking device or computer. Typically, a breakout box is inserted between two electrical devices to determine which signal or power interconnects are active. Breakout boxes are extremely useful in troubleshooting connection problems resulting from manufacturing errors (e.g., miswiring) or defective interconnects resulting from broken wiring. Breakout boxes are specific examples of a more general category of network testing equipment called ‘status monitors’.",
            "url": "https://en.wikipedia.org/wiki/Breakout_box",
            "id": 271      
        }, 
        {
            "name": "Blitzscaling",
            "definition": "Increasing the capacity of a system by a large magnitude in a short amount of time. Quite often blitzscaling refers to quickly expanding a website as it becomes extremely popular. It may also refer to making content available across a wider array of servers.",
            "url": "https://en.wikipedia.org/wiki/Reid_Hoffman#Blitzscaling",
            "id": 272      
        }, 
        {
            "name": "Binary large object (BLOB or blob)",
            "definition": "A binary large object (BLOB or blob) is a collection of binary data stored as a single entity. Blobs are typically images, audio or other multimedia objects, though sometimes binary executable code is stored as a blob. They can exist as persistent values inside some databases or version control system, or exist at runtime as program variables in some programming languages. It is not to be confused with a binary file stored in a file system.\n\nDepending on the implementation and culture around usage, the concept might be alternately referred to as a ‘basic large object’ or ‘binary data type’. The term is used in NoSQL databases, especially in key-value store databases such as Redis. The term is also used by languages that allow runtime manipulation of Blobs, like JavaScript. \n\nIn the world of free and open-source software, the term is also borrowed to refer to proprietary device drivers, which are distributed without their source code, exclusively through binary code; in such use, the term ‘binary blob’ is common.\n\nContrast with CLOB (Character Large OBject) A database field that holds a large amount of text (character data). A CLOB is also known as a ‘memo field’ in some database programs. ",
            "url": "https://en.wikipedia.org/wiki/Binary_large_object",
            "id": 273      
        }, 
        {
            "name": "Front and back office application",
            "definition": "A front office application is any software that faces the customer directly. It provides functionality and data necessary to take orders, configure complex products and provide effective service and support to customers. It includes customer relationship management (CRM), sales force automation, customer support and field service.\n\nIn turn, a back office application does not interact directly with the customer. It provides functionality for internal operations such as enterprise resource planning (ERP), inventory control, manufacturing and all of the supply chain activities associated with procuring goods, services and raw materials. If an ERP system includes order entry and customer service capabilities, that system would bridge both back office and front office.",
            "url": "https://en.wikipedia.org/wiki/Front_and_back_office_application",
            "id": 274      
        }, 
        {
            "name": "Software bloat",
            "definition": "Software bloat is a process whereby successive versions of a computer program become perceptibly slower, use more memory, disk space or processing power, or have higher hardware requirements than the previous version, while making only dubious user-perceptible improvements or suffering from feature creep. The term is not applied consistently; it is often used as a pejorative by end users (bloatware) to describe undesired user interface changes even if those changes had little or no effect on the hardware requirements. In long-lived software, perceived bloat can occur from the software servicing a large, diverse marketplace with many differing requirements. Most end users will feel they only need some limited subset of the available functions, and will regard the others as unnecessary bloat, even if end users with different requirements require those functions.\n\nActual (measurable) bloat can occur due to de-emphasising algorithmic efficiency in favour of other concerns like developer productivity, or possibly through the introduction of new layers of abstraction like a virtual machine or other scripting engine for the purposes of convenience when developer constraints are reduced. The perception of improved developer productivity, in the case of practising development within virtual machine environments, comes from the developers no longer taking resource constraints and usage into consideration during design and development; this allows the product to be completed faster but it results in increases to the end user's hardware requirements to compensate.\n\nThe term ‘bloatware’ is also used to describe unwanted pre-installed software or bundled programs.",
            "url": "https://en.wikipedia.org/wiki/Software_bloat",
            "id": 275      
        }, 
        {
            "name": "Bricks, clicks and flips",
            "definition": "A business model by which a company integrates both offline (bricks) and online (clicks) presences, sometimes with the third extra physical catalogs (flips).\n\nBy the mid-2010s, many (physical store) retailers offered ordering via their website, mobile phone apps, as well as by voice over the telephone. The wide uptake of smartphones made the model even more popular, as customers could browse and order from their smartphone whenever they had spare time. The model has historically also been known by such terms as clicks and bricks, click and mortar, bricks, clicks and flips, and WAMBAM, i.e. ‘web application meets bricks and mortar’.",
            "url": "https://en.wikipedia.org/wiki/Omnichannel_retail_strategy",
            "id": 276      
        }, 
        {
            "name": "Backhaul",
            "definition": "In a hierarchical telecommunications network, the backhaul portion of the network comprises the intermediate links between the core network, or backbone network, and the small subnetworks at the edge of the network.\n\nThe original definition of backhaul was to transmit a telephone call or data beyond its normal destination point and then back again in order to utilize available personnel (operators, agents, etc.) or network equipment not available at the destination location. For example, depending on distances and service arrangements, it might be cheaper to send a telephone call on a private line to a location way beyond the destination and then dial up the destination, which is back in the other direction.\n\nThe term evolved into a more generic meaning and often refers to transmitting from a remote site or network to a central or main site. It implies a high-capacity line; for example, to backhaul from a wireless mesh network to the wired network means aggregating all the traffic on the wireless mesh over one or more high-speed lines to a private network or the Internet.",
            "url": "https://en.wikipedia.org/wiki/Backhaul_(telecommunications)",
            "id": 277      
        }, 
        {
            "name": "Bridgeware",
            "definition": "Hardware or software that converts data or translates programs from one format into another.",
            "url": "https://www.oxfordreference.com/view/10.1093/oi/authority.20110803095527158",
            "id": 278      
        }, 
        {
            "name": "Liveware",
            "definition": "Human beings. Also called ‘warmware’ and ‘meatware’.",
            "url": "https://en.wikipedia.org/wiki/Liveware",
            "id": 279      
        }, 
        {
            "name": "Grayware",
            "definition": "Grayware (sometimes spelled as greyware) is a term, coming into use around 2004, that applies to any unwanted application or file that can worsen the performance of computers and may cause security risks but which is not typically considered malware. Greyware are applications that behave in an annoying or undesirable manner, and yet are less serious or troublesome than malware. Grayware encompasses spyware, adware, fraudulent dialers, joke programs (‘jokeware’), remote access tools and other unwanted programs that may harm the performance of computers or cause inconvenience.",
            "url": "https://en.wikipedia.org/wiki/Privacy-invasive_software",
            "id": 280      
        }, 
        {
            "name": "Crippleware",
            "definition": "Crippleware has been defined in realms of both computer software and hardware. In software, crippleware means that ‘vital features of the program such as printing or the ability to save files are disabled until the user purchases a registration key’. While crippleware allows consumers to see the software before they buy, they are unable to test its complete functionality because of the disabled functions.\n\nHardware crippleware is ‘a hardware device that has not been designed to its full capability’. The functionality of the hardware device is limited to encourage consumers to pay for a more expensive upgraded version. Usually the hardware device considered to be crippleware can be upgraded to better or its full potential by way of a trivial change, such as removing a jumper wire. The manufacturer would most likely release the crippleware as a low-end or economy version of their product.",
            "url": "https://en.wikipedia.org/wiki/Crippleware",
            "id": 281      
        }, 
        {
            "name": "Dribbleware",
            "definition": "(1) Software that is publicly previewed well in advance of its actual release. Dribbleware is one stage beyond vaporware.\n\n(2) Software that is released in small increments, each version having a few modest enhancements.",
            "url": "https://en.wikipedia.org/wiki/Dribbleware",
            "id": 282      
        }, 
        {
            "name": "Evolware",
            "definition": "A future computing architecture that can modify its own circuitry to improve performance for solving the problems it is given. As far fetched as it sounds, self modification of hardware is already possible. For example, FPGAs are a type of logic chip that can be reprogrammed in place. Exactly how that would be done is based on some pretty complicated software.",
            "url": "https://www.youtube.com/watch?v=Raw6AYil79Q",
            "id": 283      
        }, 
        {
            "name": "Expireware",
            "definition": "Software with a built-in expiration, which is determined by some number of days after installation or by a specific number of user sessions.",
            "url": "https://de.wikipedia.org/wiki/Expireware",
            "id": 284      
        }, 
        {
            "name": "Greenware",
            "definition": "An umbrella term for environment friendly hardware and software. For example, e-books that hold the equivalent of thousands of sheets of paper are greenware.",
            "url": "https://en.wikipedia.org/wiki/Greenware_(computing)",
            "id": 285      
        }, 
        {
            "name": "Careware",
            "definition": "Careware (also called charityware, helpware, or goodware) is software licensed in a way that benefits a charity. Some careware is distributed free, and the author suggests that some payment be made to either a nominated charity, or a charity of the user's choice. Commercial careware, on the other hand, includes a levy for charity on top of the distribution charge. It can also be a barter of some kind, or even a pledge to be kind to strangers.",
            "url": "https://en.wikipedia.org/wiki/Careware",
            "id": 286      
        }, 
        {
            "name": "Donationware",
            "definition": "Donationware is a licensing model that supplies fully operational unrestricted software to the user and requests an optional donation be paid to the programmer or a third-party beneficiary (usually a non-profit). The amount of the donation may also be stipulated by the author, or it may be left to the discretion of the user, based on individual perceptions of the software's value. Since donationware comes fully operational (i.e. not crippleware/Freemium) when payment is optional, it is a type of freeware. Sometimes referred to as ‘guiltware’.",
            "url": "https://en.wikipedia.org/wiki/Donationware",
            "id": 287      
        }, 
        {
            "name": "Freemium",
            "definition": "Freemium, a portmanteau of the words ‘free’ and ‘premium’, is a pricing strategy by which a basic product or service is provided free of charge, but money (a premium) is charged for additional features, services, or virtual (online) or physical (offline) goods that expand the functionality of the free version of the software. This business model has been used in the software industry since the 1980s. A subset of this model used by the video game industry is called free-to-play.",
            "url": "https://en.wikipedia.org/wiki/Freemium",
            "id": 288      
        }, 
        {
            "name": "Grid computing",
            "definition": "Grid computing is the use of widely distributed computer resources to reach a common goal. A computing grid can be thought of as a distributed system with non-interactive workloads that involve many files. Grid computing is distinguished from conventional high-performance computing systems such as cluster computing in that grid computers have each node set to perform a different task/application.\n\nGrid computers also tend to be more heterogeneous and geographically dispersed (thus not physically coupled) than cluster computers. Although a single grid can be dedicated to a particular application, commonly a grid is used for a variety of purposes. Grids are often constructed with general-purpose grid middleware software libraries. Grid sizes can be quite large. Grid computing software is sometimes referred to as 'griddleware’.",
            "url": "https://en.wikipedia.org/wiki/Grid_computing",
            "id": 289      
        }, 
        {
            "name": "Nagware",
            "definition": "Nagware (also known as begware, annoyware or a nagscreen) is a pejorative term for shareware that persistently reminds the user to purchase a license. It usually does this by popping up a message when the user starts the program, or intermittently while the user is using the application.\n\nThese messages can appear as windows obscuring part of the screen, or as message boxes that can quickly be closed. Some nagware keeps the message up for a certain time period, forcing the user to wait to continue to use the program. Unlicensed programs that support printing may superimpose a watermark on the printed output, typically stating that the output was produced by an unlicensed copy.\n\nSome titles display a dialog box with payment information and a message that paying will remove the notice, which is usually displayed either upon startup or after an interval while the application is running. These notices are designed to annoy the user into paying.",
            "url": "https://en.wikipedia.org/wiki/Shareware#Nagware",
            "id": 290      
        }, 
        {
            "name": "Push technology",
            "definition": "Push technology or server push, is a style of Internet-based communication where the request for a given transaction is initiated by the publisher or central server. It is contrasted with pull/get, where the request for the transmission of information is initiated by the receiver or client.\n\nPush services are often based on information preferences expressed in advance. This is called a publish/subscribe model. A client ‘subscribes’ to various information ‘channels’ provided by a server; whenever new content is available on one of those channels, the server pushes that information out to the client.\n\nPush is sometimes emulated with a polling technique, particularly under circumstances where a real push is not possible, such as sites with security policies that require rejection of incoming HTTP/S requests.",
            "url": "https://en.wikipedia.org/wiki/Push_technology",
            "id": 291      
        }, 
        {
            "name": "Computer-supported cooperative work (CSCW)",
            "definition": "Computer-supported cooperative work (CSCW) is the study of how people utilize technology collaboratively, often towards a shared goal. CSCW addresses how computer systems can support collaborative activity and coordination. More specifically, the field of CSCW seeks to analyze and draw connections between currently understood human psychological and social behaviors and available collaborative tools, or groupware. Often the goal of CSCW is to help promote and utilize technology in a collaborative way, and help create new tools to succeed in that goal. These parallels allow CSCW research to inform future design patterns or assist in the development of entirely new tools.",
            "url": "https://en.wikipedia.org/wiki/Computer-supported_cooperative_work",
            "id": 292      
        }, 
        {
            "name": "BI software (Business Intelligence software)",
            "definition": "Software that enables users to obtain enterprise-wide information more easily. Such products are considered a step up from the typical decision support tools because they more tightly integrate querying, reporting, OLAP, data mining and data warehousing functions.\n\nMany products claim BI capabilities, but the end goal is to let users slice and dice the information from their organization's numerous databases without having to wait for their IT departments to develop complex queries.\n\nBusiness intelligence was the 1990s buzzword for the management information system (MIS) of the 1970s and the decision support system (DSS) and executive information system (EIS) of the 1980s. MIS implementations often failed because the hardware was too slow and the software was not sophisticated. Countless DSS, EIS and OLAP tools followed, which added functionality, but were often point solutions to the problem. BI implies yet more integration and ease of use (of course, no matter what the subject, every new approach in the information field is touted as the one providing more integration and greater ease of use).",
            "url": "https://en.wikipedia.org/wiki/Predictive_analytics",
            "id": 293      
        }, 
        {
            "name": "Backronym",
            "definition": "(BACKward acRONYM) A reverse acronym. Instead of turning a multi-word term into letters, such as ‘central processing unit’ into CPU, a given set of letters becomes a multi-word term. For example, TEMPEST was a code name that was turned into ‘Telecommunications Electronics Material Protected from Emanating Spurious Transmissions’. DVD originally meant ‘Digital Video Disc’ but was later changed to ‘Digital Versatile Disc’.",
            "url": "https://en.wikipedia.org/wiki/Backronym",
            "id": 294      
        }, 
        {
            "name": "Software brittleness",
            "definition": "Older software that has been patched so many times that even small changes to the source code make the program fail. The term stems from metal that has been worked and reworked so often that it becomes brittle.\n\nThe term may also refer to software that was designed with very little error checking or a rigid set of assumptions that are no longer valid. In such cases, even minor variations of input may cause the program to crash.",
            "url": "https://en.wikipedia.org/wiki/Software_brittleness",
            "id": 295      
        }, 
        {
            "name": "Backscatter spam",
            "definition": "A spam method that relies on mail servers returning messages to the sender. The spammer forges a valid email address in the ‘From’ field of the spam message and makes the ‘To’ address a phony email recipient, but to a real company. Since there is no email account with the phony name, the receiving company's mail server bounces back the message before sending it to the spam filter. As a result, the spam winds up in the inbox of the intended recipient as undelivered mail. Also called ‘bounce spam’ and ‘reverse non-delivery report spam’ (reverse NDR spam).",
            "url": "https://en.wikipedia.org/wiki/Backscatter_(email)",
            "id": 296      
        }, 
        {
            "name": "Big Blue",
            "definition": "A nickname for IBM coined from its blue and white logo and the blue covers on most of its earlier mainframes.",
            "url": "https://en.wikipedia.org/wiki/IBM",
            "id": 297      
        }, 
        {
            "name": "Endianness",
            "definition": "In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory. Endianness is primarily expressed as big-endian (BE) or little-endian (LE). A big-endian system stores the most significant byte of a word at the smallest memory address and the least significant byte at the largest. A little-endian system, in contrast, stores the least-significant byte at the smallest address.\n\nBi-endianness is a feature supported by numerous computer architectures that feature switchable endianness in data fetches and stores or for instruction fetches. Other orderings are generically called middle-endian or mixed-endian.",
            "url": "https://en.wikipedia.org/wiki/Endianness",
            "id": 298      
        }, 
        {
            "name": "Big Mother",
            "definition": "Keeping track of children via technology. Examples of Big Mother are tracking software in smartphones, nannycams and video cameras in day care centers, community playgrounds and other venues. The term was coined from ‘Big Brother’ in George Orwell's ‘1984’ novel about an authoritarian and oppressive state.",
            "url": "https://www.techopedia.com/definition/15390/big-mother",
            "id": 299      
        }, 
        {
            "name": "Forward chaining",
            "definition": "In AI, a form of reasoning that starts with what is known and works toward a solution. Known as bottom-up approach. Contrast with backward chaining.",
            "url": "https://en.wikipedia.org/wiki/Forward_chaining",
            "id": 300      
        },
        {
            "name": "Backward chaining",
            "definition": "In AI, a form of reasoning that starts with the conclusion and works backward. The goal is broken into many subgoals or sub-subgoals which can be solved more easily. Known as top-down approach. Contrast with forward chaining.",
            "url": "https://en.wikipedia.org/wiki/Backward_chaining",
            "id": 301      
        },
        {
            "name": "No-code development platform (NCDP)",
            "definition": "No-code development platforms (NCDPs) allow programmers and non-programmers to create application software through graphical user interfaces and configuration instead of traditional computer programming. No-code development platforms are closely related to low-code development platforms as both are designed to expedite the application development process.\n\nHowever, unlike low-code, no-code development platforms require no code writing at all, generally offering prebuilt templates that businesses can build apps with. These platforms have both increased in popularity as companies deal with the parallel trends of an increasingly mobile workforce and a limited supply of competent software developers.\n\nNo-code development platforms are closely related to visual programming languages.",
            "url": "https://en.wikipedia.org/wiki/No-code_development_platform",
            "id": 302      
        },
        {
            "name": "Visual programming",
            "definition": "Developing programs with tools that allow menus, buttons, icons and other screen components to be selected from a palette. Also called a ‘GUI builder’, visual programming tools allow the user interface elements to be dragged, dropped and resized the way objects are drawn in graphics programs. Traditional source code may be completely eliminated, or it may be embedded within the graphics components.\n\nMany programming environments include a visual editor for the user interface. Although the program logic is written in a traditional language, the screen elements are programmed visually.",
            "url": "https://en.wikipedia.org/wiki/Visual_programming_language",
            "id": 303      
        },
        {
            "name": "Brochureware",
            "definition": "A website that advertises a product but contains only the equivalent of a paper brochure with no interaction. A website can be much more elaborate. For example, it can zoom into images for more detail, make recommendations based on user input, provide downloads of software demos, compute and process the sale and remember the questions users asked the last time they visited. All this is missing in brochureware.",
            "url": "https://en.wikipedia.org/wiki/Brochureware",
            "id": 304      
        },
        {
            "name": "Blook",
            "definition": "(BLog bOOK)\n\n(1) A collection of blog postings that is published as a printed book.\n\n(2) Chapters in a printed book that have been sequentially posted to a blog.",
            "url": "https://en.wikipedia.org/wiki/Blook",
            "id": 305      
        },
        {
            "name": "Blue/Black screen of death (BSoD)",
            "definition": "A blue screen of death (BSoD), officially known as a stop error or blue screen error, is an error screen that the Windows operating system displays in the event of a fatal system error. It indicates a system crash, in which the operating system has reached a critical condition where it can no longer operate safely, e.g., hardware failure or an unexpected termination of a crucial process.\n\nThe black screen of death (BSoD) is a fatal system error displayed by some versions of the Microsoft Windows operating system after encountering a critical system error which can cause the system to shut down.",
            "url": "https://en.wikipedia.org/wiki/Blue_screen_of_death",
            "id": 306      
        },
        {
            "name": "Microarray",
            "definition": "A multiplex lab-on-a-chip semiconductor device that is used to detect the DNA makeup of a human cell. DNA chains comprise molecules that pair with each other, and micro arrays contain millions of DNA strands designed to mate with their other half as the liquefied human cells are poured over them. This ‘hybridization’ process is then detectable by a laser.\n\nMicro arrays are revolutionizing medicine by being able to pinpoint a very specific disease or the susceptibility to it. Also called ‘biochips’, Affymetrix (www.affymetrix.com) pioneered this technology with its GeneChip family. See Human Genome Project.",
            "url": "https://en.wikipedia.org/wiki/Microarray",
            "id": 307      
        },
        {
            "name": "Hard coding",
            "definition": "Hard coding (also hard-coding or hardcoding) is the software development practice of embedding data directly into the source code of a program or other executable object, as opposed to obtaining the data from external sources or generating it at runtime. Hard-coded data typically can only be modified by editing the source code and recompiling the executable, although it can be changed in memory or on disk using a debugger or hex editor.\n\nData that are hard-coded is best for unchanging pieces of information, such as physical constants, version numbers and static text elements. Softcoded data, on the other hand, encode arbitrary information through user input, text files, INI files, HTTP server responses, configuration files, preprocessor macros, external constants, databases, command-line arguments, and are determined at runtime.",
            "url": "https://en.wikipedia.org/wiki/Hard_coding",
            "id": 308      
        },
        {
            "name": "HTTP return codes",
            "definition": "A status code that is returned from the Web server (HTTP server) to the client program, typically the browser. It indicates the status of the request and reports errors and necessary information so that the client software can respond.\n\nExamples include:\n\n200 - OK\n303 - Redirected\n404 - Not found\n500 - Internal error",
            "url": "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes",
            "id": 309      
        },
        {
            "name": "BSON (Binary JSON)",
            "definition": "BSON is a computer data interchange format. The name ‘BSON’ is based on the term JSON and stands for ‘Binary JSON’. It is a binary form for representing simple or complex data structures including associative arrays (also known as name-value pairs), integer indexed arrays, and a suite of fundamental scalar types. BSON originated in 2009 at MongoDB.\n\nSeveral scalar data types are of specific interest to MongoDB and the format is used both as a data storage and network transfer format for the MongoDB database, but it can be used independently outside of MongoDB. Implementations are available in a variety of languages such as C, C++, C#, D, Delphi, Erlang, Go, Haskell, Java, JavaScript, Julia, Lua, OCaml, Perl, PHP, Python, Ruby, Rust, Scala, Smalltalk, and Swift.",
            "url": "https://en.wikipedia.org/wiki/BSON",
            "id": 310      
        },
        {
            "name": "Die",
            "definition": "A die, in the context of integrated circuits, is an unpackaged, bare chip, a small block or square of semiconducting material (silicone) on which a given functional circuit is fabricated. Typically, integrated circuits are produced in large batches on a single wafer of electronic-grade silicon (EGS) or other semiconductor (such as GaAs) through processes such as photolithography. The wafer is cut (diced) into many pieces, each containing one copy of the circuit. Each of these pieces is called a die.\n\nThere are three commonly used plural forms: dice, dies and die. To simplify handling and integration onto a printed circuit board, most dies are packaged in various forms.",
            "url": "https://en.wikipedia.org/wiki/Die_(integrated_circuit)",
            "id": 311      
        },
        {
            "name": "Bluetooth Low Energy (Bluetooth LE or BLE)",
            "definition": "Bluetooth Low Energy (Bluetooth LE, colloquially BLE, formerly marketed as Bluetooth Smart) is a wireless personal area network technology used extensively in IoT (Internet of Things).\n\nUsing smaller batteries, Bluetooth LE devices can operate for months or years before requiring replacement. Operating in the 2.4GHz frequency band, Bluetooth LE supports peer-to-peer and star topologies. It is independent of classic Bluetooth and has no compatibility, but Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) and LE can coexist.\n\nProducts with the ‘Smart only’ branding are Bluetooth LE only, while ‘Smart Ready’ devices support both classic Bluetooth and Bluetooth LE.\n\nUntil 2020, the primary audio codec in Bluetooth had been the subband codec (SBC). Bluetooth LE Audio introduced the Low Complexity Communications Codec (LC3) that promises better quality using less energy. As a result, products such as hearing aids can use smaller batteries.",
            "url": "https://en.wikipedia.org/wiki/Bluetooth_Low_Energy",
            "id": 312      
        },
        {
            "name": "Baseband",
            "definition": "Electronic data in their original form. Baseband refers to analog or digital data before being intermixed with other data (multiplexing and modulation).\n\nFor example, the output of an analog microphone is baseband. When an FM station's carrier frequency is stripped away in the radio (demodulated), the original audio signal that you hear is the baseband signal (frequency modulation).\n\nEthernet transmission is considered baseband, because signals are not intermixed and occupy the full bandwidth of the line. In fact, ‘base’ is part of the Ethernet version name (see 10Base-T and 100Base-T).\n\nWhen a compressed digital audio signal such as MP3 is transcoded to another format, it is decompressed back to the original bit rate (the baseband signal) before it is compressed into the new format (baseband processing).",
            "url": "https://en.wikipedia.org/wiki/Baseband",
            "id": 313      
        },
        {
            "name": "Baselining",
            "definition": "Baselining is a method for analyzing computer network performance. The method is marked by comparing current performance to a historical metric, or ‘baseline’. If the performance of a network switch or other network components is measured over a period of time, that performance figure can be used as a comparative baseline for configuration changes.\n\nBaselining is useful for many performance management tasks, including:\n\na) Monitoring daily network performance\nb) Measuring trends in network performance\nc) Assessing whether network performance is meeting requirements laid out in a service agreement",
            "url": "https://www.pcmag.com/encyclopedia/term/baselining",
            "id": 314      
        },
        {
            "name": "Bastion host",
            "definition": "A bastion host is a special-purpose computer on a network specifically designed and configured to withstand attacks, so named by analogy to the military fortification. The computer generally hosts a single application or process, for example, a proxy server or load balancer, and all other services are removed or limited to reduce the threat to the computer.\n\nIt is hardened in this manner primarily due to its location and purpose, which is either on the outside of a firewall or inside of a demilitarized zone (DMZ) and usually involves access from untrusted networks or computers. These computers are also equipped with special networking interfaces to withstand high-bandwidth attacks through the internet.",
            "url": "",
            "id": 315      
        },
        {
            "name": "Bistable",
            "definition": "Pronounced ‘bye-stable’. With regard to electronics, it refers to technologies that maintain their binary state without power, although they require power to change it. For example, non-volatile storage, such as flash memory, maintains its 0 or 1 state without power. A flip-flop is a bistable circuit, and E Ink and cholesteric LCDs are bistable display technologies.",
            "url": "https://en.wikipedia.org/wiki/Flip-flop_(electronics)",
            "id": 316      
        },
        {
            "name": "BLUF (bottom line up front)",
            "definition": "BLUF (bottom line up front) is the practice of beginning a message with its key information (the 'bottom line'). This provides the reader with the most important information first. By extension, that information is also called a BLUF. It differs from an abstract or executive summary in that it is simpler and more concise, similar to a thesis statement, and it resembles the inverted pyramid practice in journalism.\n\nBLUF is a standard in U.S. military communication whose aim is to make military messages precise and powerful. It differs from an older, more-traditional style in which conclusions and recommendations are included at the end, following the arguments and considerations of facts. The BLUF concept is not exclusive to writing since it can also be used in conversations and interviews.",
            "url": "https://en.wikipedia.org/wiki/BLUF_(communication)",
            "id": 317      
        },
        {
            "name": "Bug compatibility",
            "definition": "Computer hardware or software is said to be bug compatible if it exactly replicates even an undesirable feature of a previous version. An aspect of maintaining backward compatibility with an older system is that such systems' client programs often do not only depend on their specified interfaces but also bugs and unintended behaviour. That must also be preserved by the newer replacement.",
            "url": "https://en.wikipedia.org/wiki/Bug_compatibility",
            "id": 318      
        },
        {
            "name": "Software rot",
            "definition": "Software rot, also known as code rot, software erosion, software decay, or software entropy is either a slow deterioration of software quality over time or its diminishing responsiveness that will eventually lead to software becoming faulty, unusable, or in need of upgrade. This is not a physical phenomenon: the software does not actually decay, but rather suffers from a lack of being responsive and updated with respect to the changing environment in which it resides.\n\nA related concept, ‘bit rot’, also called ‘format rot’, is the inability to access digital data because hardware and software do not exist to read the format. For example, files saved on tape cartridges might not be retrievable because the drives are not available. Although computers no longer come with a built-in floppy disk drive, floppies are still readable because an external drive can be plugged into a PC via USB.\n\nOne way to prevent archival bit rot is to be aware of format changes. Whenever a file format is updated, the application that reads it will also be changed. Within a few years of such an occurrence, users should open important documents and save them in the new format.",
            "url": "https://en.wikipedia.org/wiki/Software_rot",
            "id": 319      
        },
        {
            "name": "Places with ‘Silicon’ names",
            "definition": "Places with ‘Silicon’ names\n\nThe following list contains places with ‘Silicon’ names, that is, places with nicknames inspired by the ‘Silicon Valley’ nickname given to part of the San Francisco Bay Area:\n\nSilicon Beach - Southern California, USA\nSilicon Alley - New York City, USA\nPhilicon Valley - Philadelphia, USA\nSilicon Forest - Northern Oregon, USA\nSilicon Hills - Austin, Texas, USA\nSilicon Desert - Phoenix, Arizona, USA\nSilicon Slopes - Salt Lake City, USA\nSilicon Mountain - Colorado, USA\nSilicon Peach, Atlanta, USA\nSilicon Border - Mexicali, Mexico\nSilicon Valley North - Ottawa, Ontario, Canada\nSilicon Glen - Scotland, USA\nSilicon Gorge - South West England\nSilicon Fen - Cambridge, England\nSilicon Wadi - Israel\nSilicon Saxony - Dresden, Germany\nSilicon Cape - Cape Town, South Africa\nSilicon Lagoon - Lagos, Nigeria\nSilicon Mountain - Buea, Cameroon\nSilicon Savannah - Nairobi, Kenya\nSilicon Island - Kyushu, Japan\nSilicon Peninsula - Dalian, China\nSilicon Valley of India - Bangalore, India\nBrazilian Silicon Valley - Campinas, Brazil\nChilecon Valley - Santiago, Chile\nMexican Silicon Valley - Jalisco, Mexico\nSilicon Docks - Dublin, Ireland\n\nApologies to any we have missed!",
            "url": "https://en.wikipedia.org/wiki/List_of_technology_centers",
            "id": 320      
        },
        {
            "name": "Boilerplate code",
            "definition": "In computer programming, boilerplate code, or simply boilerplate, are sections of code that are repeated in multiple places with little to no variation. When using languages that are considered verbose, the programmer must write a lot of boilerplate code to accomplish only minor functionality.\n\nThe need for boilerplate can be reduced through high-level mechanisms such as metaprogramming (which has the computer automatically write the needed boilerplate code or insert it at compile time), convention over configuration (which provides good default values, reducing the need to specify program details in every project) and model-driven engineering (which uses models and model-to-code generators, eliminating the need for manual boilerplate code).",
            "url": "https://en.wikipedia.org/wiki/Boilerplate_code",
            "id": 321      
        },
        {
            "name": "Burn-in",
            "definition": "To test a new electronic system by running it for some length of time. Although electronics can give out at any time, weak components often fail within the first few hours of use. For example, when a computer is built to order, it is often turned on and allowed to run for several hours before being released to the customer.",
            "url": "https://en.wikipedia.org/wiki/Burn-in",
            "id": 322      
        },
        {
            "name": "Error correcting code (ECC)",
            "definition": "In computing, telecommunication, information theory, and coding theory, an error correction code, sometimes error correcting code (ECC), is used for controlling errors in data over unreliable or noisy communication channels. The central idea is the sender encodes the message with redundant information in the form of an ECC. The redundancy allows the receiver to detect a limited number of errors that may occur anywhere in the message, and often to correct these errors without retransmission. The American mathematician Richard Hamming pioneered this field in the 1940s and invented the first error-correcting code in 1950: the Hamming (7,4) code.\n\nECC contrasts with error detection in that errors that are encountered can be corrected, not simply detected. The advantage is that a system using ECC does not require a reverse channel to request retransmission of data when an error occurs. The downside is that there is a fixed overhead that is added to the message, thereby requiring a higher forward-channel bandwidth. ECC is therefore applied in situations where retransmissions are costly or impossible, such as one-way communication links and when transmitting to multiple receivers in multicast. Long-latency connections also benefit; in the case of a satellite orbiting around Uranus, retransmission due to errors can create a delay of five hours. ECC information is usually added to mass storage devices to enable recovery of corrupted data, is widely used in modems, and is used on systems where the primary memory is ECC memory.",
            "url": "https://en.wikipedia.org/wiki/Error_correction_code",
            "id": 323      
        },
        {
            "name": "Behavior-driven development (BDD)",
            "definition": "Software development that focuses on the way an application should ultimately behave and which focuses on and builds toward that goal. Behavior driven development (BDD) pays attention to the objectives of the business and collaborates with the users regarding the appearance and function of the app. It encourages teams to use conversation and concrete examples to formalize a shared understanding of how the application should behave.",
            "url": "https://en.wikipedia.org/wiki/Behavior-driven_development",
            "id": 324      
        },
        {
            "name": "Test-driven development (TDD)",
            "definition": "Test-driven development (TDD) is a software development process relying on software requirements being converted to test cases before software is fully developed, and tracking all software development by repeatedly testing the software against all test cases. This is as opposed to software being developed first and test cases created later.\n\nSoftware engineer Kent Beck, who is credited with having developed or ‘rediscovered’ the technique, stated in 2003 that TDD encourages simple designs and inspires confidence. Programmers also apply the concept to improving and debugging legacy code developed with older techniques.",
            "url": "",
            "id": 325      
        },
        {
            "name": "BYOD",
            "definition": "(Bring Your Own Device) Refers to employees who bring their personal devices to work, whether laptop, smartphone or tablet, in order to interface to the corporate network. A huge amount of company data is accessed using employee-owned equipment.",
            "url": "https://en.wikipedia.org/wiki/Bring_your_own_device",
            "id": 326      
        },
        {
            "name": "Standard operating environment (SOE)",
            "definition": "A uniform configuration of hardware and software throughout an organization. It is designed to eliminate software and data incompatibilities and improve troubleshooting. It implies the use of the same primary applications and Web browser as well as the same operating system, database management system and other system software.",
            "url": "https://en.wikipedia.org/wiki/Standard_Operating_Environment",
            "id": 327      
        },
        {
            "name": "Source-to-source compiler (S2S compiler)",
            "definition": "A source-to-source translator, source-to-source compiler (S2S compiler), transcompiler, or transpiler is a type of translator that takes the source code of a program written in a programming language as its input and produces an equivalent source code in the same or a different programming language. A source-to-source translator converts between programming languages that operate at approximately the same level of abstraction, while a traditional compiler translates from a higher level programming language to a lower level programming language.\n\nFor example, a source-to-source translator may perform a translation of a program from Python to JavaScript, while a traditional compiler translates from a language like C to assembler or Java to bytecode. An automatic parallelizing compiler will frequently take in a high level language program as an input and then transform the code and annotate it with parallel code annotations (e.g., OpenMP) or language constructs (e.g. Fortran's forall statements).",
            "url": "https://en.wikipedia.org/wiki/Source-to-source_compiler",
            "id": 328      
        },
        {
            "name": "CoffeeScript",
            "definition": "CoffeeScript is a programming language that compiles to JavaScript. Inspired by Ruby, Python, and Haskell it was created by Jeremy Ashkenas in an effort to enhance JavaScript's brevity and readability. Specific additional features include list comprehension and destructuring assignment.\n\nIn 2011, Brendan Eich, who created the JavaScript programming language and co-founded Mozilla, referenced CoffeeScript as an influence on his thoughts about the future of JavaScript.\n\nCoffeeScript supports a form of Literate Programming, using the .coffee.md or .litcoffee file extension. This allows CoffeeScript source code to be written in Markdown. The compiler will treat any indented blocks (Markdown's way of indicating source code) as code, and ignore the rest as comments.\n\nThe LiveScript programming language is an indirect descendant of CoffeeScript.",
            "url": "https://en.wikipedia.org/wiki/CoffeeScript",
            "id": 329      
        },
        {
            "name": "Syntactic sugar",
            "definition": "In computer science, syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express. It makes the language ‘sweeter’ for human use: things can be expressed more clearly, more concisely, or in an alternative style that some may prefer.\n\nFor example, many programming languages provide special syntax for referencing and updating array elements. Abstractly, an array reference is a procedure of two arguments: an array and a subscript vector, which could be expressed as get_array(Array, vector(i,j)). Instead, many languages provide syntax such as Array[i,j]. Similarly an array element update is a procedure consisting of three arguments, for example set_array(Array, vector(i,j), value), but many languages provide syntax such as Array[i,j] = value.\n\nA construct in a language is syntactic sugar if it can be removed from the language without any effect on what the language can do: functionality and expressive power will remain the same.\n\nLanguage processors, including compilers and static analyzers, often expand sugared constructs into more fundamental constructs before processing, a process sometimes called ‘desugaring’.",
            "url": "https://en.wikipedia.org/wiki/Syntactic_sugar",
            "id": 330      
        },
        {
            "name": "TypeScript",
            "definition": "TypeScript is a programming language developed and maintained by Microsoft. It is a strict syntactical superset of JavaScript and adds optional static typing to the language. It is designed for the development of large applications and transpiles to JavaScript. As it is a superset of JavaScript, existing JavaScript programs are also valid TypeScript programs.\n\nTypeScript may be used to develop JavaScript applications for both client-side and server-side execution. Multiple options are available for transpilation. The default TypeScript Checker can be used, or a compiler can be invoked to convert TypeScript to JavaScript.",
            "url": "https://en.wikipedia.org/wiki/TypeScript",
            "id": 331      
        },
        {
            "name": "Copyleft",
            "definition": "Copyleft is the practice of granting the right to freely distribute and modify intellectual property with the requirement that the same rights be preserved in derivative works created from that property and also includes the source code. Copyleft in the form of licenses can be used to maintain copyright conditions for works ranging from computer software, to documents, art, scientific discoveries and even certain patents. Copyleft is an arrangement whereby software or artistic work may be used, modified, and distributed freely on condition that anything derived from it is bound by the same conditions.",
            "url": "https://en.wikipedia.org/wiki/Copyleft",
            "id": 332      
        },
        {
            "name": "Cord-cutting",
            "definition": "In broadcast television, cord-cutting refers to the pattern of viewers cancelling their subscriptions to multichannel television services available over cable or satellite, dropping pay television channels or reducing the number of hours of subscription TV viewed in response to competition from rival media available over the Internet. This content is either free or significantly cheaper than the same content provided via cable.\n\nA ‘cord cutter’ is person who switches from a pay TV subscription (cable, satellite or telephone company) to an Internet-based streaming service such as Netflix. A ‘cord never’ or ‘never-connected’ is someone who never had such a subscription, while ‘cord shavers’ are subscribers who have reduced their pay TV fees by eliminating certain channels. A ‘cord stacker’ is someone who subscribes to both pay TV and one or more streaming services.",
            "url": "https://en.wikipedia.org/wiki/Cord-cutting",
            "id": 333      
        },
        {
            "name": "Anti-laser",
            "definition": "A reverse laser. Also called a ‘coherent perfect absorber (CPA)’, it accepts laser light and converts it to heat or electricity. In 2011, a team at Yale University built the first working model. Coherent perfect absorbers can be used to build absorptive interferometers, which could be useful in detectors, transducers, and optical switches.\n\nAnother potential application is in radiology, where the principle of the CPA might be used to precisely target electromagnetic radiation inside human tissues for therapeutic or imaging purposes. Moreover, the CPA concept might be exploited to achieve perfect focusing of acoustic or electromagnetic signals on receivers even when they are embedded in complex environments.",
            "url": "https://en.wikipedia.org/wiki/Coherent_perfect_absorber",
            "id": 334      
        },
        {
            "name": "Change request",
            "definition": "A change request (aka Change Control Request, or CCR) is a document containing a call for an adjustment of a system; it is of great importance in the change management process. It can be a petition for modifying the behavior of a system due to normal business changes or because there is a bug in the system.",
            "url": "",
            "id": 335      
        },
        {
            "name": "Hot swapping (software)",
            "definition": "Hot swapping can also refer to the ability to alter the running code of a program without needing to interrupt its execution. Interactive programming is a programming paradigm that makes extensive use of hot swapping, so the programming activity becomes part of the program flow itself.\n\nOnly a few programming languages support hot swapping natively, including Pike, Lisp, Erlang, Smalltalk, Visual Basic 6 (Not VB.net), Java and most recently Elm and Elixir. Microsoft Visual Studio supports a kind of hot swapping called Edit and Continue, which is supported by C#, VB.NET and C/C++ when running under a debugger.\n\nHot swapping is the central method in live coding, where programming is an integral part of the runtime process. In general, all programming languages used in live coding, such as SuperCollider, TidalCycles, or Extempore support hot swapping.\n\nSome web-based frameworks, such as Django, support detecting module changes and reloading them on the fly. However, although the same as hotswapping for most intents and purposes, this is technically just a cache purge, triggered by a new file. This does not apply to markup and programming languages such as HTML and PHP respectively, in the general case, as these files are normally re-interpreted on each use by default. There are a few CMSs and other PHP-based frameworks (such as Drupal) that employ caching, however. In these cases, similar abilities and exceptions apply.",
            "url": "https://en.wikipedia.org/wiki/Hot_swapping#Software",
            "id": 336      
        },
        {
            "name": "Chaos theory",
            "definition": "Chaos theory is an interdisciplinary scientific theory and branch of mathematics focused on underlying patterns and deterministic laws, of dynamical systems, that are highly sensitive to initial conditions, that were once thought to have completely random states of disorder and irregularities.\n\nChaos theory states that within the apparent randomness of chaotic complex systems, there are underlying patterns, interconnectedness, constant feedback loops, repetition, self-similarity, fractals, and self-organization.\n\nA process in a chaotic system seems to produce random outputs when repeated, but are not random. The difference is due to minute variations of the inputs that ultimately cause changes in the outputs. The more nuances are captured, the more chaotic a system may appear, because those exact same input conditions are not repeated the next time.",
            "url": "https://en.wikipedia.org/wiki/Chaos_theory",
            "id": 337      
        },
        {
            "name": "Cobrowsing",
            "definition": "Cobrowsing (short for collaborative browsing), is the act of synchronizing browser access to the same sites. As one user browses the Web, the other users trail along automatically and link to and view the same pages from their own Web browsers. For example, call center agents might use collaborative browsing to help customers navigate the company website. It is typically accomplished with a browser extension.",
            "url": "https://en.wikipedia.org/wiki/Cobrowsing",
            "id": 338      
        },
        {
            "name": "Cache coherency",
            "definition": "Managing a cache so that data are not lost or overwritten. For example, when data are updated in a cache but not yet transferred to the target memory or disk, the chance of corruption is greater. Accomplished by well-designed algorithms that keep track of every read and write event, cache coherency is even more critical in symmetric multiprocessing (SMP) where memory is shared by multiple processors.",
            "url": "https://en.wikipedia.org/wiki/Cache_coherence",
            "id": 339      
        },
        {
            "name": "Qi (standard)",
            "definition": "Pronounced ‘chee’ from Chinese, meaning ‘life force’, Developed by the Wireless Power Consortium (WPC) (www.wirelesspowerconsortium.com), Qi is an open interface standard that defines wireless power transfer methods. Introduced in 2009, Qi is based on ‘closely coupled’ electromagnetic induction that requires the device to be aligned on top of the coil on the charging pad. \n\nUnder development at the WPC are a ‘medium-coupled’ version of Qi that operates at a distance of up to approximately 15mm and a loosely-coupled version (Qi 3D) that can be up to 50mm apart. Typical applications are in vehicles and for mounting under table and desktop surfaces. Hundreds of devices are are already Qi certified, including Google Nexus and Samsung phones. Loosely coupled products not certified by the WPC have also been announced.",
            "url": "https://en.wikipedia.org/wiki/Qi_(standard)",
            "id": 340      
        },
        {
            "name": "Comfort noise",
            "definition": "A very low-volume auditory tone injected into the receiving end of voice over IP (VoIP) communications to prevent the listener from thinking the line went dead. There was always a slight background noise in analog phone lines. However, digital methods have replaced analog, and without the comfort noise, the line can seem disconnected during pauses in conversation, or when someone is on hold (without music) or when the other party puts the phone down for a moment.",
            "url": "https://en.wikipedia.org/wiki/Comfort_noise",
            "id": 341      
        },
        {
            "name": "BeiDou",
            "definition": "BeiDou is a satellite-based radio navigation system developed by the China Space Science and Technology Group. Pronounced ‘by-dough’, there have been three independent BeiDou systems. BeiDou-1, using four GEO satellites, started in 2000 and ended in 2012. BeiDou-2, originally known as COMPASS, began in 2007 and was designed for five GEO, 27 MEO and three IGSO (geosynchronous) satellites. Completed in 2020, BeiDou-3 uses three GEO, three IGSO and 24 MEO satellites.\n\nAccuracy is within inches. This third iteration of the Beidou Navigation Satellite System provides for global coverage for timing and navigation, offering an alternative to Russia's GLONASS, the European Galileo positioning system, and the US's GPS.\n\nBeiDou is Chinese for ‘Big Dipper’. The North Star, which has been used for centuries for navigation, is located in the Big Dipper.",
            "url": "https://en.wikipedia.org/wiki/BeiDou",
            "id": 342      
        },
        {
            "name": "Cleanroom software engineering",
            "definition": "The cleanroom software engineering process is a software development process intended to produce software with a certifiable level of reliability. The cleanroom process was originally developed by Harlan Mills and several of his colleagues, including Alan Hevner, at IBM. The focus of the cleanroom process is on defect prevention, rather than defect removal.\n\nThe name ‘cleanroom’ was chosen to evoke the cleanrooms used in the electronics industry to prevent the introduction of defects during the fabrication of semiconductors. The cleanroom process first saw use in the mid to late 1980s. Demonstration projects within the military began in the early 1990s. Recent work on the cleanroom process has examined fusing cleanroom with the automated verification capabilities provided by specifications expressed in CSP.\n\nThe basic principles of the cleanroom process are:\n\n- Software development based on formal methods\n- Incremental implementation under statistical quality control\n- Statistically sound testing",
            "url": "https://en.wikipedia.org/wiki/Cleanroom_software_engineering",
            "id": 343      
        },
        {
            "name": "Cramming (fraud)",
            "definition": "Cramming is a form of fraud in which small charges are added to a bill by a third party without the subscriber's consent, approval, authorization or disclosure. These may be disguised as a tax, some other common fee or a bogus service, and may be several dollars or even just a few cents. The crammer's intent is that the subscriber will overlook and ultimately pay these small charges without them knowing what it's all about.",
            "url": "https://en.wikipedia.org/wiki/Cramming_(fraud)",
            "id": 344      
        },
        {
            "name": "Camel case",
            "definition": "The spelling of a hardware or software product with multiple capital letters; for example, ‘BlackBerry’, ‘InterBase’ and ‘CardSpace’. Also called 'BumpyCaps’, ‘CamelCaps’, ‘InterCaps’ and ‘MixedCase’. CamelCase purists claim that the word always begins with lower case, such as ‘camelCase’ and not ‘CamelCase’.",
            "url": "https://en.wikipedia.org/wiki/Camel_case",
            "id": 345      
        },
        {
            "name": "LoRa (LOngRAnge)",
            "definition": "LoRa and LoRaWAN together define a Low Power, Wide Area (LPWA) networking protocol designed to wirelessly connect battery operated ‘things’ to the internet in regional, national or global networks, and targets key Internet of things (IoT) requirements such as bi-directional communication, end-to-end security, mobility and localization services. The low power, low bit rate, and IoT use distinguish this type of network from a wireless WAN that is designed to connect users or businesses, and carry more data, using more power. The LoRaWAN data rate ranges from 0.3 kbit/s to 50 kbit/s per channel.\n\nLoRa (from ‘long range’) is the physical proprietary radio modulation technique. It is based on spread-spectrum modulation techniques derived from chirp spread spectrum (CSS) technology. It was developed by Cycleo (patent 9647718-B2), a company of Grenoble, France, later acquired by Semtech.\n\nLoRaWAN defines the software communication protocol and system architecture. The continued development of the LoRaWAN protocol is managed by the open, non-profit LoRa Alliance, of which SemTech is a founding member.",
            "url": "https://en.wikipedia.org/wiki/LoRa",
            "id": 346      
        },
        {
            "name": "Preparedness paradox",
            "definition": "The preparedness paradox is the proposition that if a society or individual acts effectively to mitigate a potential disaster such as a pandemic, natural disaster or other catastrophe so that it causes less harm, the avoided danger will be perceived as having been much less serious because of the limited damage actually caused.\n\nThe paradox is the incorrect perception that there had been no need for careful preparation as there was little harm, although in reality the limitation of the harm was due to preparation. Several cognitive biases can consequently hamper proper preparation for future risks.",
            "url": "https://en.wikipedia.org/wiki/Preparedness_paradox",
            "id": 347      
        },
        {
            "name": "Shebang (or Hashbang)",
            "definition": "In computing, a shebang is the character sequence consisting of the characters number sign and exclamation mark (#!) at the beginning of a script. It is also called sharp-exclamation, sha-bang, hashbang, pound-bang, or hash-pling.\n\nWhen a text file with a shebang is used as if it is an executable in a Unix-like operating system, the program loader mechanism parses the rest of the file's initial line as an interpreter directive. The loader executes the specified interpreter program, passing to it as an argument using the path that was initially used when attempting to run the script, so that the program may use the file as input data. For example, if a script is named with the path path/to/script, and it starts with the following line, #!/bin/sh, then the program loader is instructed to run the program /bin/sh, passing path/to/script as the first argument. In Linux, this behavior is the result of both kernel and user-space code.\n\nThe shebang line is usually ignored by the interpreter, because the ‘#’ character is a comment marker in many scripting languages; some language interpreters that do not use the hash mark to begin comments still may ignore the shebang line in recognition of its purpose.",
            "url": "https://en.wikipedia.org/wiki/Shebang_(Unix)",
            "id": 348      
        },
        {
            "name": "POSIX (Portable Operating System Interface)",
            "definition": "The Portable Operating System Interface (POSIX) is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems. POSIX defines both the system-level and user-level application programming interfaces (API), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems. POSIX is also a trademark of the IEEE. POSIX is intended to be used by both application and system developers.",
            "url": "https://en.wikipedia.org/wiki/POSIX",
            "id": 349      
        },
        {
            "name": "Compound document",
            "definition": "A single document that contains a combination of data structures such as text, graphics, spreadsheets, sound and video clips. The document may embed the additional data types or reference external files by pointers of some kind. SGML and HTML are examples of compound document formats.",
            "url": "https://en.wikipedia.org/wiki/Compound_document",
            "id": 350      
        },
        {
            "name": "Parkerian Hexad",
            "definition": "Six fundamental, atomic, non-overlapping attributes of information that are protected by information security measures. Defined by Donn B. Parker, renowned security consultant and writer; they are: confidentiality, possession, integrity, authenticity, availability and utility.\n\nThe Parkerian Hexad adds three additional attributes to the three classic security attributes of the CIA triad (confidentiality, integrity, availability).",
            "url": "https://en.wikipedia.org/wiki/Parkerian_Hexad",
            "id": 351      
        },
        {
            "name": "CIA triad",
            "definition": "The CIA triad of confidentiality, integrity, and availability is at the heart of information security. \n\nThe members of the classic InfoSec triad—confidentiality, integrity, and availability—are interchangeably referred to in the literature as security attributes, properties, security goals, fundamental aspects, information criteria, critical information characteristics and basic building blocks.\n\nThe triad seems to have first been mentioned in a National Institute of Standards and Technology (NIST) publication in 1977.",
            "url": "https://en.wikipedia.org/wiki/Information_security#Key_concepts",
            "id": 352      
        },
        {
            "name": "Clamshell",
            "definition": "A portable device comprising two parts hinged together. Flip phones and laptop computers are sometimes called clamshells because they 'open and close like a clam.'",
            "url": "https://en.wikipedia.org/wiki/Clamshell_design",
            "id": 353      
        },
        {
            "name": "Exception handling",
            "definition": "In computing and computer programming, exception handling is the process of responding to the occurrence of exceptions – anomalous or exceptional conditions requiring special processing – during the execution of a program. In general, an exception breaks the normal flow of execution and executes a pre-registered exception handler; the details of how this is done depend on whether it is a hardware or software exception and how the software exception is implemented.\n\nException handling, if provided, is facilitated by specialized programming language constructs, hardware mechanisms like interrupts, or operating system (OS) inter-process communication (IPC) facilities like signals. Some exceptions, especially hardware ones, may be handled so gracefully that execution can resume where it was interrupted.\n\nSoftware exception handling and the support provided by software tools differs somewhat from what is understood by exception handling in hardware, but similar concepts are involved. In programming language mechanisms for exception handling, the term exception is typically used in a specific sense to denote a data structure storing information about an exceptional condition. One mechanism to transfer control, or raise an exception, is known as a throw. The exception is said to be thrown. Execution is transferred to a ‘catch’.",
            "url": "https://en.wikipedia.org/wiki/Exception_handling",
            "id": 354      
        },
        {
            "name": "Dark web",
            "definition": "The dark web is the World Wide Web content that exists on darknets: overlay networks that use the Internet but require specific software, configurations, or authorization to access. Through the dark web, private computer networks can communicate and conduct business anonymously without divulging identifying information, such as a user's location. The dark web forms a small part of the deep web, the part of the Web not indexed by web search engines, although sometimes the term deep web is mistakenly used to refer specifically to the dark web.\n\nThe darknets which constitute the dark web include small, friend-to-friend peer-to-peer networks, as well as large, popular networks such as Tor, Freenet, I2P, and Riffle operated by public organizations and individuals. Users of the dark web refer to the regular web as Clearnet due to its unencrypted nature. The Tor dark web or onionland uses the traffic anonymization technique of onion routing under the network's top-level domain suffix .onion.",
            "url": "https://en.wikipedia.org/wiki/Dark_web",
            "id": 355      
        },
        {
            "name": "Concurrent computing",
            "definition": "Concurrent computing is a form of computing in which several computations are executed concurrently—during overlapping time periods—instead of sequentially—with one completing before the next starts.\n\nThis is a property of a system—whether a program, computer, or a network—where there is a separate execution point or 'thread of control' for each process. A concurrent system is one where a computation can advance without waiting for all other computations to complete.\n\nConcurrent computing is a form of modular programming. In its paradigm an overall computation is factored into subcomputations that may be executed concurrently. Pioneers in the field of concurrent computing include Edsger Dijkstra, Per Brinch Hansen, and C.A.R. Hoare.",
            "url": "https://en.wikipedia.org/wiki/Concurrent_computing",
            "id": 356      
        },
        {
            "name": "Open / closed architecture",
            "definition": "Open architecture is a type of computer architecture or software architecture intended to make adding, upgrading, and swapping components with other computers easy. Open architecture systems may use a standardized system bus or they may incorporate a proprietary bus standard such as that used on the Apple II, with up to a dozen slots that allow multiple hardware manufacturers to produce add-ons, and for the user to freely install them.\n\nBy contrast, closed architectures, if they are expandable at all, have one or two ‘expansion ports’ using a proprietary connector design that may require a license fee from the manufacturer, or enhancements may only be installable by technicians with specialized tools or training.\n\nComputer platforms may include systems with both open and closed architectures.",
            "url": "https://en.wikipedia.org/wiki/Open_architecture",
            "id": 357      
        },
        {
            "name": "Open platform",
            "definition": "In computing, an open platform describes a software system which is based on open standards, such as published and fully documented external application programming interfaces (API) that allow using the software to function in other ways than the original programmer intended, without requiring modification of the source code. Using these interfaces, a third party could integrate with the platform to add functionality. The opposite is a closed platform.\n\nAn open platform does not mean it is open source, however most open platforms have multiple implementations of APIs. An open platform can consist of software components or modules that are either proprietary or open source or both.\n\nUsing an open platform, a developer could add features or functionality that the platform vendor had not completed or had not conceived of. An open platform allows the developer to change existing functionality, as the specifications are publicly available open standards.",
            "url": "https://en.wikipedia.org/wiki/Open_platform",
            "id": 358      
        },
        {
            "name": "Cloud broker",
            "definition": "Cloud Broker is an entity that manages the use, performance and delivery of cloud services, and negotiates relationships between cloud providers and cloud consumers. As cloud computing evolves, the integration of cloud services may be too complex for cloud consumers to manage alone.\n\nIn such cases, ‘a cloud consumer may request cloud services from a cloud broker, instead of contacting a cloud provider directly,’ according to NIST Cloud Computing Reference Architecture.\n\nCloud Brokers provides a single point of entry to manage multiple cloud services for business or technical purposes. The two important unique features of a cloud broker are the ability to provide a single consistent interface to multiple differing cloud providers and the clear visibility that the broker allows into which company is providing the services in the background.",
            "url": "https://en.wikipedia.org/wiki/Cloud_broker",
            "id": 359      
        },
        {
            "name": "Cloud Computing Manifesto",
            "definition": "The Cloud Computing Manifesto is a manifesto containing a ‘public declaration of principles and intentions’ for cloud computing providers and vendors, annotated as ‘a call to action for the worldwide cloud community’ and ‘dedicated belief that the cloud should be open’. It follows the earlier development of the Cloud Computing Bill of Rights which addresses similar issues from the users' point of view.\n\nA declaration of core principles for cloud computing providers. Introduced in 2009 and endorsed by hundreds of hardware and software companies, the Manifesto was created to promote the use of open standards by cloud providers.",
            "url": "https://en.wikipedia.org/wiki/Cloud_Computing_Manifesto",
            "id": 360      
        },
        {
            "name": "Cloud bursting",
            "definition": "In cloud computing, cloud bursting is a configuration that’s set up between a private cloud and a public cloud to deal with peaks in IT demand. If an organization using a private cloud reaches 100 percent of its resource capacity, the overflow traffic is directed to a public cloud so there’s no interruption of services.\n\nIn addition to flexibility and self-service functionality, the key advantage to cloud bursting is economical savings. You only pay for the additional resources when there is a demand for those resources - no more spending on extra capacity you’re not using or trying to predict demand peaks and fluctuations. An application can be applied to the private cloud, then burst to the public cloud only when necessary to meet peak demands.\n\nPlus, cloud bursting can also be used to shoulder processing burdens by moving basic applications to the public cloud to free up local resources for business-critical applications. When using cloud bursting, you should consider security and compliance requirements, latency, load balancing, and platform compatibility.",
            "url": "https://www.atlassian.com/microservices/cloud-computing/cloud-bursting",
            "id": 361      
        },
        {
            "name": "Cloud spanning",
            "definition": "Cloud spanning is a type of cloud delivery model in which an application is deployed and executed over multiple simultaneous cloud platforms and infrastructure (including private, public or combination of both environments i.e. hybrid environments). Cloud spanning enables a cloud application to distribute its computations and components across one or more cloud environments.",
            "url": "https://www.techopedia.com/definition/26534/cloud-spanning",
            "id": 362      
        },
        {
            "name": "Beamforming",
            "definition": "Beamforming or spatial filtering directs the signals on transmitters and receivers with multiple antennas to improve transmission speed. It is accomplished by detecting the signals and sending feedback to the transmitter to adjust the phase and amplitude of the signals at its antennas.\n\nBeamforming is a signal processing technique used in sensor arrays for directional signal transmission or reception. This is achieved by combining elements in an antenna array in such a way that signals at particular angles experience constructive interference while others experience destructive interference. Beamforming can be used at both the transmitting and receiving ends in order to achieve spatial selectivity. The improvement compared with omnidirectional reception/transmission is known as the directivity of the array.\n\nBeamforming can be used for radio or sound waves. It has found numerous applications in radar, sonar, seismology, wireless communications, radio astronomy, acoustics and biomedicine. Adaptive beamforming is used to detect and estimate the signal of interest at the output of a sensor array by means of optimal (e.g. least-squares) spatial filtering and interference rejection.",
            "url": "https://en.wikipedia.org/wiki/Beamforming",
            "id": 363      
        },
        {
            "name": "Biomimetics",
            "definition": "Biomimetics, or biomimicry, is imitating nature in man-made systems. Examples are a film similar to the coating on a moth's eyeballs that minimizes screen glare, a directional microphone that mimics the moving hairs on crickets, and a waterproof coating that emulates the grooves and wax coating on a butterfly's wings.\n\nA very notable example is the Eastgate Center in Harare, Zimbabwe. Built in 1996, this shopping and office complex was constructed using principles discovered in termite mounds in the desert. Termites maintain an almost perfectly uniform temperature for their food inside their tunnels, even though outside temperatures range from near freezing at night to over 100 degrees Fahrenheit in the day. The even temperature is accomplished by continuously opening and closing a series of vents throughout the day. Eastgate uses 10% of the energy of a traditional building to keep cool.",
            "url": "https://en.wikipedia.org/wiki/Biomimetics",
            "id": 364      
        },
        {
            "name": "Bone conduction",
            "definition": "Transmitting sound via the bones in the skull to the inner ear. Bone conduction speakers rest against the side of the head near the ears, but not in them. Dating back to the 1920s, bone conduction has been used for hearing aids and is still used for people who cannot tolerate a device inserted in their ears.",
            "url": "https://en.wikipedia.org/wiki/Bone_conduction",
            "id": 365      
        },
        {
            "name": "Boss key",
            "definition": "A boss key, or boss button, is a special keyboard shortcut used in PC games or other programs to hide the program quickly, possibly displaying a special screen that appears to be a normal productivity program (such as a spreadsheet application). One of the earliest implementations was by Friendlyware, a suite of entertainment and general interest programs written in BASIC and sold with the original IBM AT and XT computers from 1982 to 1985. When activated (by pressing F10), an ASCII bar graph with generic ‘Productivity’ and ‘Time’ labels appeared. Pressing F10 again would return to the Friendlyware application.",
            "url": "https://en.wikipedia.org/wiki/Boss_key",
            "id": 366      
        },
        {
            "name": "Btrfs",
            "definition": "An advanced Linux file system designed for the ultra-large storage requirements of the 21st century. Btrfs features includes ‘copy-on-write’ (COW) (which makes a copy of the data when modified by another application or user), dynamic resizing, along with RAID, compression and snapshot support. Also called ‘B-Tree FS’, ‘Butter FS’ and ‘Butterface’.",
            "url": "https://en.wikipedia.org/wiki/Btrfs",
            "id": 367      
        },
        {
            "name": "Gender changer",
            "definition": "A gender changer or ‘gender-bender’, is a hardware device placed between two cable connectors of the same type and gender. An example is a cable connector shell with either two female or two male connectors on it (male-to-male or female-to-female), used to correct the mismatches that result when interconnecting two devices or cables with the same gender of connector.",
            "url": "https://en.wikipedia.org/wiki/Gender_changer",
            "id": 368      
        },
        {
            "name": "Capacitor",
            "definition": "An electronic component that stores an electric charge and releases it when required. It comes in a huge variety of sizes and types for use in regulating power as well as for conditioning, smoothing and isolating signals. Capacitors are made from many different materials, and virtually every electrical and electronic system uses them.\n\nCapacitors act like tiny storage batteries that charge and discharge rapidly. Made of two plates separated by a thin insulator or sometimes air, when one plate is charged negative and the other positive, a charge builds up and remains after the current is removed. When power is required, the circuit is switched to conduct current between the plates, and the charge is released.",
            "url": "https://en.wikipedia.org/wiki/Capacitor",
            "id": 369      
        },
        {
            "name": "Automata-based programming (Shalyto's approach)",
            "definition": "Automata-based programming is a programming technology. Its defining characteristic is the use of finite state machines to describe program behavior. The transition graphs of state machines are used in all stages of software development (specification, implementation, debugging and documentation). Automata-based programming technology was introduced by Anatoly Shalyto in 1991. \n\nThe main approach to automata-based programming is to construct computer programs the same way the automation of technological processes (and other kinds of processes too) is done. Switch-technology was developed to support automata-based programming. Automata-based programming is considered to be rather general purpose program development methodology than just another one finite state machine implementation.",
            "url": "https://en.wikipedia.org/wiki/Automata-based_programming_(Shalyto%27s_approach)",
            "id": 370      
        },
        {
            "name": "Cellular automaton",
            "definition": "A state machine that consists of an array of cells, each of which can be in one of a finite number of possible states. The cells are updated synchronously in discrete time steps, according to a local, identical interaction rule. The state of a cell at the next time step is determined by the current states of a surrounding neighborhood of cells.\n\nThe transitions are usually specified in the form of a rule table that defines the cell's next state for each possible neighborhood configuration. The cellular array (grid) is typically from one to three dimensions. Highly parallel, locally connected and using simple elemental units, cellular automata can perform so-called cellular computing.",
            "url": "https://en.wikipedia.org/wiki/Cellular_automaton",
            "id": 371      
        },
        {
            "name": "Channel coding",
            "definition": "Encoding a communications channel to ensure error-free transmission. Channel coding modifies the outgoing message, which is known as ‘forward error correction’ (FEC). At the receiving end, the channel coding bits are used to verify the validity of the message and correct most errors. Channel coding improves the signal-to-noise ratio (SNR).\n\nConvolutional Codes\nConvolutional codes were introduced in 1955 by Peter Elias. The input bits are transformed by predefined algorithms and decoded at the receiving end. Viterbi and BCJR are the common convolutional algorithms. See Viterbi decoder.\n\nLDPC\nIntroduced by Robert Gallager in 1960 and rediscovered more than 30 years later, the low-density parity check (LDPC) method creates a block parity bit that takes little processing to decode. Also known as ‘Gallager codes’.\n\nTurbo Codes\nTurbo codes were introduced in 1993 by Claude Berrou and were licensed by France Telecom until 2013. There are several turbo code variations; however, the primary method passes the input bits through two convolutional decoders. The two decoders exchange probabilistic information to assist each other similar to the way a turbo engine works.\n\nPolar Codes\nPolar codes were introduced in 2009 by Turkish professor Erdal Arikan. Creating a ‘virtual channel’ that is the polar opposite of the main transmission stream, polar codes require more processing at both ends. However, they offer high performance and have been adopted by the 3GPP for the 5G New Radio (NR) control channels.",
            "url": "https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction",
            "id": 372     
        },
        {
            "name": "Collapsed backbone",
            "definition": "A network configuration that provides a backbone in a centralized location, to which all subnetworks are attached. A collapsed backbone is implemented in a router or switch that uses a high-speed backplane that can handle the simultaneous traffic of all or most of its ports at full wire speed.",
            "url": "https://en.wikipedia.org/wiki/Backbone_network#Collapsed_backbone",
            "id": 373      
        },
        {
            "name": "Dynamic frequency scaling",
            "definition": "Dynamic frequency scaling (also known as CPU throttling) is a power management technique in computer architecture whereby the frequency of a microprocessor can be automatically adjusted ‘on the fly’ depending on the actual needs, to conserve power and reduce the amount of heat generated by the chip. Dynamic frequency scaling helps preserve battery on mobile devices and decrease cooling cost and noise on quiet computing settings, or can be useful as a security measure for overheated systems (e.g. after poor overclocking).\n\nDynamic frequency scaling almost always appear in conjunction with dynamic voltage scaling, since higher frequencies require higher supply voltages for the digital circuit to yield correct results. The combined topic is known as dynamic voltage and frequency scaling (DVFS).\n\nProcessor throttling is also known as ‘automatic underclocking’. Automatic overclocking (boosting) is also technically a form of dynamic frequency scaling, but it's relatively new and usually not discussed with throttling.",
            "url": "https://en.wikipedia.org/wiki/Dynamic_frequency_scaling",
            "id": 374      
        },
        {
            "name": "Computational sprinting",
            "definition": "Pushing a chip beyond its normal operating mode in order to perform a short burst of computations that lasts only a few seconds. Decompressing a file or decoding an image takes an enormous amount of arithmetic operations that if speeded up would allow a smartphone or similar device to perform the function as if it were a desktop computer. After the sprint, the hardware has to rest so the heat cannot melt the ultra-fine lines and minuscule elements in the chip.",
            "url": "https://www.computer.org/csdl/proceedings-article/hpca/2012/06169031/12OmNBNM8Re",
            "id": 375      
        },
        {
            "name": "Cupertino effect",
            "definition": "An incorrect AutoCorrect insertion. The term comes from the case where typing ‘cooperation’ produced the word ‘Cupertino’ as the correct spelling (Cupertino is a town in California, and its name is often used as a metonym for Apple Inc., as the firm's corporate headquarters are located in the city.)",
            "url": "https://en.wikipedia.org/wiki/Cupertino_effect",
            "id": 377      
        },
        {
            "name": "Splinternet",
            "definition": "The splinternet (also referred to as cyber-balkanization or internet balkanization) is a characterization of the Internet as splintering and dividing due to various factors, such as technology, commerce, politics, nationalism, religion, and divergent national interests. ‘Powerful forces are threatening to balkanise it, writes the Economist weekly, and it may soon splinter along geographic and commercial boundaries. \n\nThe Chinese government erected the ‘Great Firewall’ for political reasons, and Russia has enacted the Sovereign Internet Law that allows it to partition itself from the rest of the Internet, while other nations, such as the US and Australia, discuss plans to create similar firewalls.",
            "url": "https://en.wikipedia.org/wiki/Splinternet",
            "id": 378      
        },
        {
            "name": "Digilanti",
            "definition": "People who voluntarily police the Internet to make it better and safer. Also called ‘online vigilante’ and ‘digital vigilante’. Digilantis use their expertise to expose spammers, deceitful websites, bogus software and other annoying or harmful scams. Coined from the term ‘digerati’, which means ‘digital elite’.",
            "url": "https://en.wikipedia.org/wiki/Internet_vigilantism",
            "id": 379      
        },
        {
            "name": "Digerati",
            "definition": "The ‘digital elite’. The digerati are people who are extremely knowledgeable about computers. It often refers to the movers and shakers in the industry. Digerati is the high-tech equivalent of ‘literati’, which refers to scholars and intellectuals, or ‘glitterati’, the rich and famous.",
            "url": "https://en.wikipedia.org/wiki/Digerati",
            "id": 380      
        },
        {
            "name": "Magic",
            "definition": "In the context of computer programming, magic is an informal term for abstraction; it is used to describe code that handles complex tasks while hiding that complexity to present a simple interface. The term is somewhat tongue-in-cheek, and often carries bad connotations, implying that the true behavior of the code is not immediately apparent.\n\n‘Magic’ refers to procedures which make calculations based on data not clearly provided to them, by accessing other modules, memory positions or global variables that they are not supposed to (in other words, they are not referentially transparent). According to most recent software architecture models, even when using structured programming, it is usually preferred to make each function behave the same way every time the same arguments are passed to it, thereby following one of the basic principles of functional programming. When a function breaks this rule, it is often said to contain ‘magic’.",
            "url": "https://en.wikipedia.org/wiki/Magic_(programming)",
            "id": 381      
        },
        {
            "name": "Lurker",
            "definition": "In Internet culture, a lurker is typically a member of an online community who observes, but does not participate. The exact definition depends on context. Lurkers make up a large proportion of all users in online communities. Lurking allows users to learn the conventions of an online community before they participate, improving their socialization when they eventually ‘de-lurk’. However, a lack of social contact while lurking sometimes causes loneliness or apathy among lurkers.\n\nLurkers are referred to using many names, including browsers, read-only participants, non-public participants, legitimate peripheral participants, vicarious learners, or sleepers.",
            "url": "https://en.wikipedia.org/wiki/Lurker",
            "id": 382      
        },
        {
            "name": "Dirty data",
            "definition": "Dirty data, also known as rogue data, are inaccurate, incomplete or inconsistent data, especially in a computer system or database.\n\nDirty data can contain such mistakes as spelling or punctuation errors, incorrect data associated with a field, incomplete or outdated data, or even data that has been duplicated in the database. They can be cleaned through a process known as data cleansing.",
            "url": "https://en.wikipedia.org/wiki/Dirty_data",
            "id": 383      
        },
        {
            "name": "Data furnace",
            "definition": "The data furnace is a proposed method of heating residential homes or offices by running computers in them, which release considerable amounts of waste heat. Data furnaces can theoretically be cheaper than storing computers in huge data centers because the higher cost of electricity in residential areas (when compared to industrial zones) can be offset by charging the home owner for the heat that the data center gives off.\n\nWith a large-scale, distributed deployment of data furnaces (DFs), the machines can be used as local caches, thereby removing some burden from the large, national datacenters. They can also be used to distribute massive computational processing that is required by various industries and sciences.",
            "url": "https://en.wikipedia.org/wiki/Data_furnace",
            "id": 384      
        },
        {
            "name": "Dangling pointer",
            "definition": "Dangling pointers and wild pointers in computer programming are links or pointers to an instruction, table element, index item, etc. that no longer contains the same content. If the reference is not a currently valid address, or if it is valid but there is no content in that location, it may cause the computer to crash if the software is not programmed carefully.",
            "url": "https://en.wikipedia.org/wiki/Dangling_pointer",
            "id": 385      
        },
        {
            "name": "Framekiller",
            "definition": "A framekiller (or framebuster or framebreaker) is a technique used by websites and web applications to prevent their web pages from being displayed within a frame. A frame is a subdivision of a Web browser window and can act like a smaller window. A framekiller is usually JavaScript code embedded in a Web page used to prevent a website from being loaded from within a frameset without permission or as an attack, as with clickjacking.",
            "url": "https://en.wikipedia.org/wiki/Framekiller",
            "id": 386      
        },
        {
            "name": "Priority queue",
            "definition": "In computer science, a priority queue is an abstract data-type similar to a regular queue or stack data structure in which each element additionally has a ‘priority’ associated with it. In a priority queue, an element with high priority is served before an element with low priority. In some implementations, if two elements have the same priority, they are served according to the order in which they were enqueued; in other implementations ordering of elements with the same priority remains undefined.\n\nWhile coders often implement priority queues with heaps, they are conceptually distinct from heaps. A priority queue is a concept like ‘a list’ or ‘a map’; just as a list can be implemented with a linked list or with an array, a priority queue can be implemented with a heap or with a variety of other methods such as an unordered array.",
            "url": "https://en.wikipedia.org/wiki/Priority_queue",
            "id": 387      
        },
        {
            "name": "FIFO",
            "definition": "In computing and in systems theory, FIFO is an acronym for 'first in, first out' (the first in is the first out) is a method for organizing the manipulation of a data structure (often, specifically a data buffer) where the oldest (first) entry, or ‘head’ of the queue, is processed first.\n\nSuch processing is analogous to servicing people in a queue area on a first-come, first-served (FCFS) basis, i.e. in the same sequence in which they arrive at the queue's tail.\n\nFCFS is also the jargon term for the FIFO operating system scheduling algorithm, which gives every process central processing unit (CPU) time in the order in which it is demanded. FIFO's opposite is LIFO, last-in-first-out, where the youngest entry or ‘top of the stack’ is processed first. A priority queue is neither FIFO nor LIFO but may adopt similar behaviour temporarily or by default. Queueing theory encompasses these methods for processing data structures, as well as interactions between strict-FIFO queues.",
            "url": "https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)",
            "id": 388      
        },
        {
            "name": "Fair queuing",
            "definition": "Fair queuing is a family of scheduling algorithms used in some process and network schedulers. The algorithm is designed to achieve fairness when a limited resource is shared, for example to prevent flows with large packets or processes that generate small jobs from consuming more throughput or CPU time than other flows or processes.\n\nFair queuing is implemented in some advanced network switches and routers.",
            "url": "https://en.wikipedia.org/wiki/Fair_queuing",
            "id": 389      
        },
        {
            "name": "Weighted round robin",
            "definition": "Weighted round robin (WRR) is a network scheduler for data flows, but also used to schedule processes.\n\nWeighted round robin is a generalisation of round-robin scheduling. It serves a set of queues or tasks. Whereas round-robin cycles over the queues or tasks and gives one service opportunity per cycle, weighted round robin offers to each a fixed number of opportunities, as specified by the configured weight which serves to influence the portion of capacity received by each queue or task. In computer networks, a service opportunity is the emission of one packet, if the selected queue is non-empty.\n\nIf all packets have the same size, WRR is the simplest approximation of generalized processor sharing (GPS). Several variations of WRR exist. The main ones are the classical WRR, and the interleaved WRR.",
            "url": "https://en.wikipedia.org/wiki/Weighted_round_robin",
            "id": 390      
        },
        {
            "name": "Griddleware",
            "definition": "Griddleware is grid computing software, which distributes a single problem to multiple computers and assembles the results.\n\nGrid computing is the use of widely distributed computer resources to reach a common goal. A computing grid can be thought of as a distributed system with non-interactive workloads that involve many files.\n\nGrid computing is distinguished from conventional high-performance computing systems such as cluster computing in that grid computers have each node set to perform a different task/application. Grid computers also tend to be more heterogeneous and geographically dispersed (thus not physically coupled) than cluster computers.\n\nAlthough a single grid can be dedicated to a particular application, commonly a grid is used for a variety of purposes. Grids are often constructed with general-purpose grid middleware software libraries. Grid sizes can be quite large.",
            "url": "https://www.pcmag.com/encyclopedia/term/griddleware",
            "id": 391      
        },
        {
            "name": "Gold-chipped supercomputer",
            "definition": "A reference to chip-enabled credit and debit cards that have superseded the cards that had only magnetic stripes. However, the term is misleading and downright erroneous. There is no more than a few pennies worth of gold in the chip, if that, and the processors used in these cards are low-end microcontrollers that hardly qualify as supercomputers. In fact, they are at the other end of the spectrum.",
            "url": "https://en.wikipedia.org/wiki/Smart_card",
            "id": 392      
        },
        {
            "name": "Glocalization",
            "definition": "(GLObal loCALIZATION) Specializing a website or product for a particular country by translating everything into that language. It also refers to targeting the contents to the culture of the country.",
            "url": "https://en.wikipedia.org/wiki/Glocalization",
            "id": 393      
        },
        {
            "name": "Electromagnetic hypersensitivity",
            "definition": "A claimed sensitivity to and adverse reaction from wireless signals. Also called ‘gadget allergies’, symptoms can be headaches, nausea, ringing in the ear (tinnitus), fatigue, irritability, fainting and pain throughout the body. In order to feel improvement, some people have moved into remote areas; however, it is difficult to avoid wireless signals no matter where one lives on the planet. It remains a controversial subject.",
            "url": "https://en.wikipedia.org/wiki/Electromagnetic_hypersensitivity",
            "id": 394      
        },
        {
            "name": "initRD",
            "definition": "(INITial RAM Disk) The first file system loaded in a Linux operating system. In desktop computers, the initrd is temporary and another ‘root’ file system is loaded. In embedded systems, initrd is the only file system.",
            "url": "https://en.wikipedia.org/wiki/Initial_ramdisk",
            "id": 395      
        },
        {
            "name": "Infoxication",
            "definition": "Information overload (also known as infobesity, infoxication, information anxiety, and information explosion) is the difficulty in understanding an issue and effectively making decisions when one has too much information (TMI) about that issue, and is generally associated with the excessive quantity of daily information. \n\nInformation overload can also be a symptom of the high-tech age, where there is (potentially) too much information for one person to absorb in a world of expanding digital technology. Information overload primarily comes from the gigantic amount of content on the Internet, including search engine results, blogs and social media. Web pages bombard the senses with ads, and junk email (spam) adds chaos. Combine the digital information with the traditional sources such as TV, magazines, newsletters and junk postal mail, and information overload is a fact of modern life in the developed world",
            "url": "https://en.wikipedia.org/wiki/Information_overload",
            "id": 396      
        },
        {
            "name": "Data smog",
            "definition": "How information overload from the Internet can make it increasingly difficult to separate fact from fiction. The amount of information and disinformation on the Web and social media grows every year, potentially making the act of separating fact from fiction an arduous task of ever-increasing difficulty.",
            "url": "https://en.wikipedia.org/wiki/Data_Smog",
            "id": 397      
        },
        {
            "name": "Idempotent",
            "definition": "An operation that produces the same results no matter how many times it is performed. For example, a database query that does not change any data in the database is idempotent.\n\nFunctions can be designed as idempotent if all that is desired is to ensure a certain operation has been completed. For example, with an idempotent delete function, if a request to delete a file is successfully completed for one program, all subsequent requests to delete that file from other programs would return the same success confirmation message. In a non-idempotent delete function, an error would be returned for the second and subsequent requests indicating that the file was not there.",
            "url": "https://en.wikipedia.org/wiki/Idempotence",
            "id": 398      
        },
        {
            "name": "Kludge",
            "definition": "Spelled ‘kludge’ or ‘kluge’ and pronounced ‘klooj’, it is a workaround or quick-and-dirty solution that is clumsy, inelegant, inefficient, difficult to extend and hard to maintain. This term is used in diverse fields such as computer science, aerospace engineering, Internet slang, evolutionary neuroscience, and government.",
            "url": "https://en.wikipedia.org/wiki/Kludge",
            "id": 399      
        },
        {
            "name": "Lazy loading",
            "definition": "Lazy loading (also known as asynchronous loading) is a design pattern commonly used in computer programming and mostly in web design and development to defer initialization of an object until the point at which it is needed.\n\nIt can contribute to efficiency in the program's operation if properly and appropriately used. This makes it ideal in use cases where network content is accessed and initialization times are to be kept at a minimum, such as in the case of web pages. For example, deferring loading of images on a web page until they are needed can make the initial display of the web page faster. The opposite of lazy loading is eager loading.",
            "url": "https://en.wikipedia.org/wiki/Lazy_loading",
            "id": 400      
        },
        {
            "name": "Last mile",
            "definition": "The connection between the customer and the telephone company, cable company or ISP. The last mile has traditionally used copper-based telephone wire or coaxial cable, but optical fiber is increasingly used, and wireless technologies offer an alternative. Also called ‘first mile’.",
            "url": "https://en.wikipedia.org/wiki/Last_mile_(telecommunications)",
            "id": 401      
        },
        {
            "name": "Metafile",
            "definition": "A file that contains other files. It generally refers to graphics files that can hold vector drawings and bitmaps. For example, Windows Metafiles (WMFs) and Enhanced Metafiles (EMFs) can store pictures in vector graphics and bitmap formats as well as text. A Computer Graphics Metafile (CGM) also stores both types of graphics. See Windows Metafile and CGM.\n\nA metafile that can hold a variety of audio and video formats or any mix of audio, video and text is often called a ‘container’. For example, AVI, MPEG and Ogg are A/V container formats.",
            "url": "https://en.wikipedia.org/wiki/Container_format_(computing)",
            "id": 402     
        },
        {
            "name": "Markup language",
            "definition": "A set of labels that are embedded within text to distinguish individual elements or groups of elements for display or identification purposes. The labels are typically known as ‘tags’.\n\nFor rendering (displaying and printing), markup languages indicate where font and other layout changes start and stop. For content identification, markup languages turn a text document into the equivalent of a database record in which individual data elements can be located for processing. In a database, elements are placed in a predefined structure. In a document, data elements reside in a freeform structure like text and must be identified with tags that mark their beginning and end.\n\nSGML is the granddaddy markup language that served as the foundation for HTML and XML. HTML is used for rendering the document, and XML is used for identifying the content of the document.",
            "url": "https://en.wikipedia.org/wiki/Markup_language",
            "id": 403     
        },
        {
            "name": "Marshalling",
            "definition": "In computer science, marshalling or marshaling (US spelling) is the process of transforming the memory representation of an object into a data format suitable for storage or transmission. It is typically used when data must be moved between different parts of a computer program or from one program to another.\n\nMarshalling can be somewhat similar or synonymous to serialization. Marshalling is describing an intent or process to transfer some object from a client to server, intent is to have the same object that is present in one running program, to be present in another running program, i.e. object on a client to be transferred to and present on the server. Serialization does not necessarily have this intent since it is only concerned about transforming data into a, for example, stream of bytes. One could say that marshalling might be done in some other way from serialization, but some form of serialization is usually used.",
            "url": "https://en.wikipedia.org/wiki/Marshalling_(computer_science)",
            "id": 404     
        },
        {
            "name": "Captology",
            "definition": "(Computers As Persuasive TechnOLOGY) Captology refers to using computers to change people's attitudes and behavior. With regard to e-commerce, for instance, customer reviews alongside products encourage people to make purchases, as well as the convenience of ‘1-Click Ordering’, using Amazon as an example. The term was coined by B.J. Fogg in his 2003 book entitled ‘Persuasive Technology: Using Computers to Change What We Think and Do.’\n\nMACrosuasion and MICrosuasion\n\nFogg defines macrosuasion as being the overall persuasive goal of the product (buy more, return again, share this information, etc.). The small elements within the software that help achieve the macrosuasion goal (default buttons, hints, positive feedback, etc.) are called microsuasion.",
            "url": "https://en.wikipedia.org/wiki/Captology",
            "id": 405      
        },
        {
            "name": "Machine learning",
            "definition": "An application of artificial intelligence (AI). Machine learning systems ‘learn’ about a subject by being fed a huge amount of data samples. The machine learning software, which is mostly implemented using a ‘neural network’ architecture, keeps modifying its own data relationships in the training stages in order to improve the data recognition capability of the resulting AI that performs the actual processing. ‘Deep learning’ is the most intense form of machine learning, which uses many layers of recognition. See deep learning and neural network.\n\nMachine learning (ML) is used to develop pattern recognition systems (face, handwriting, voice, etc.) in many areas, including search engines, medical diagnosis, ad serving, spam filtering and sales forecasting. Today's virtual assistants are the result of both machine learning and handcrafting’, the latter providing predefined frameworks for responses.\n\nThe final algorithm from multiple machine learning phases is generally much more difficult, if not impossible, to flow chart and debug than the routine ‘if this-do that’ logic in regular data processing applications. As more samples become available and more fine tuning is applied, the resulting recognition system becomes more accurate.",
            "url": "https://en.wikipedia.org/wiki/Machine_learning",
            "id": 406      
        },
        {
            "name": "Mosquito noise",
            "definition": "A distortion that appears near crisp edges of objects in MPEG and other video frames that are compressed with the discrete cosine transform (DCT). It occurs at decompression when the decoding engine has to approximate the discarded data by inverting the transform model. The mosquito noise appears as random aliasing in these areas and requires sophisticated detection circuits to eliminate it. As TVs get larger, mosquito noise and other artifacts become more noticeable.",
            "url": "https://en.wikipedia.org/wiki/Compression_artifact#Mosquito_noise",
            "id": 407      
        },
        {
            "name": "Microprocessor",
            "definition": "A microprocessor is a computer processor where the data processing logic and control is included on a single integrated circuit, or a small number of integrated circuits. The microprocessor contains the arithmetic, logic, and control circuitry required to perform the functions of a computer's central processing unit.\n\nThe integrated circuit is capable of interpreting and executing program instructions and performing arithmetic operations. The microprocessor is a multipurpose, clock-driven, register-based, digital integrated circuit that accepts binary data as input, processes it according to instructions stored in its memory, and provides results (also in binary form) as output.\n\nBefore microprocessors, small computers had been built using racks of circuit boards with many medium- and small-scale integrated circuits. The integration of a whole CPU onto a single or a few integrated circuits greatly reduced the cost of processing power.\n\nMicroarchitecture, the basic design of a microprocessor, includes the design of the instruction pipeline and execution techniques, number and style of on-board caches and caching techniques and type and speed of the system bus. The microarchitecture also defines the process technology and base materials used for the construction of transistors, electronic components and interconnects.",
            "url": "https://en.wikipedia.org/wiki/Microprocessor",
            "id": 408      
        },
        {
            "name": "Nomophobia",
            "definition": "(No Mobile PHOBIA) The anxiety some people feel when they cannot get a signal from a cellphone tower, run out of battery or forget to take their phone.",
            "url": "https://en.wikipedia.org/wiki/Nomophobia",
            "id": 409      
        },
        {
            "name": "Neologism",
            "definition": "A new meaning for an existing word, otherwise known as semantic shifting, or semantic extension. The high-tech field routinely creates new meanings for words. Before 1980, there was no doubt that a ‘mouse’ referred only to a furry rodent.\n\nA neologism may also refer to a relatively recent or isolated term, word, or phrase that may be in the process of entering common use, but that has not been fully accepted into mainstream language. Neologisms are often driven by changes in culture and technology.",
            "url": "https://en.wikipedia.org/wiki/Neologism",
            "id": 410      
        },
        {
            "name": "Uniform Resource Identifier (URI)",
            "definition": "A Uniform Resource Identifier (URI) is a unique sequence of characters that identifies a logical or physical resource used by web technologies. Some URIs provide a means of locating and retrieving information resources on a network (either on the Internet or on another private network, such as a computer filesystem or an Intranet); these are Uniform Resource Locators (URLs), a specific type of URI. Examples of URIs include:\n\nhttps://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top\n\nmailto:John.Doe@example.com\n\ntel:+1-816-555-1212\n\ntelnet://192.0.2.16:80/",
            "url": "https://en.wikipedia.org/wiki/Uniform_Resource_Identifier",
            "id": 411     
        },
        {
            "name": "NaaS",
            "definition": "(Network as a Service) A communications carrier that leases its network and billing systems to application service providers (ASPs) and other Web service organizations.\n\nNaaS brings software defined networking (SDN), programmable networking and API-based operation to WAN services, transport, hybrid cloud, multi-cloud, Private Network Interconnect, and Internet Exchanges.\n\nHistoric definitions focused on fundamental concepts of NaaS including: NaaS describes services for network transport connectivity. NaaS involves the optimization of resource allocations by considering network and computing resources as a unified whole.",
            "url": "https://en.wikipedia.org/wiki/Network_as_a_service",
            "id": 412     
        },
        {
            "name": "Orthogonality",
            "definition": "In computer programming, orthogonality means that operations change just one thing without affecting others. The term is most-frequently used regarding assembly instruction sets, as orthogonal instruction set.\n\nOrthogonality in a programming language means that a relatively small set of primitive constructs can be combined in a relatively small number of ways to build the control and data structures of the language. It is associated with simplicity; the more orthogonal the design, the fewer exceptions. This makes it easier to learn, read and write programs in a programming language. The meaning of an orthogonal feature is independent of context; the key parameters are symmetry and consistency (for example, a pointer is an orthogonal concept).",
            "url": "https://en.wikipedia.org/wiki/Orthogonality_(programming)",
            "id": 413     
        },
        {
            "name": "Ordinateur",
            "definition": "The word ordinateur means ‘organizer’ in French, but it also means ‘computer’. Considering how much a computer is used to organize time and information rather than solving mathematical problems (computing), ‘organizer’ might have been the more accurate word in English.\n\nAlthough in Latin America the word for computer is ‘computadora’, in Spain it is ‘ordenador’, the same as the French word.",
            "url": "https://en.wiktionary.org/wiki/ordinateur",
            "id": 414      
        },
        {
            "name": "Out-of-band data",
            "definition": "In computer networking, out-of-band (OOB) data is the data transferred through a stream that is independent from the main in-band data stream. An out-of-band data mechanism provides a conceptually independent channel, which allows any data sent via that mechanism to be kept separate from in-band data. The out-of-band data mechanism should be provided as an inherent characteristic of the data channel and transmission protocol, rather than requiring a separate channel and endpoints to be established. The term ‘out-of-band data’ probably derives from out-of-band signaling, as used in the telecommunications industry.\n\nOut-of-band data transmitted with the primary data stream is considered a control signal and demands immediate attention. The receiving side must pass the out-of-band data to the appropriate software routine in front of any other data that has been buffered and not yet processed, because the command must be executed as soon as possible.",
            "url": "https://en.wikipedia.org/wiki/Out-of-band_data",
            "id": 415      
        },
        {
            "name": "Onboard intelligence",
            "definition": "The capability of a device to solve a problem itself without passing the request to another computer in the network. Onboard intelligence also refers to artificial intelligence that's built into a device design, rather than outsourced to remote technology.",
            "url": "https://www.techopedia.com/definition/33391/onboard-intelligence",
            "id": 416      
        },
        {
            "name": "OAM multiplexing",
            "definition": "(Orbital Angular Momentum multiplexing) Transmitting multiple beams (channels) over the same light frequency in an optical fiber. The channels are differentiated based on their spiral rotation (angular momentum).",
            "url": "https://en.wikipedia.org/wiki/Orbital_angular_momentum_multiplexing",
            "id": 417      
        },
        {
            "name": "Prosumer",
            "definition": "A prosumer is an individual who both consumes and produces. The term is a portmanteau of the words producer and consumer.\n\nProsumers have been defined as ‘individuals who consume and produce value, either for self-consumption or consumption by others, and can receive implicit or explicit incentives from organizations involved in the exchange’.\n\nResearch has identified six types of prosumers: DIY prosumers, self-service prosumers, customizing prosumers, collaborative prosumers, monetised prosumers, and economic prosumers.\n\nIdentifiable trends and movements outside of the mainstream economy that have adopted prosumer terminology and techniques include:\n\n1. the open source software movement creates software on their own, prime example is the successful operating system Linux which now dominates the server domain\n\n2. a Do It Yourself (DIY) approach as a means of economic self-sufficiency or simply as a way to survive on diminished income\n\n3. Fablab movement, self-fabrication capabilities especially 3d printing\n\n4. self-sufficient barter networks\n\n5. the voluntary simplicity movement that seeks personal, social, and environmental goals through prosumer activities such as growing one's own food, repairing clothing and appliances rather than buying new items and playing musical instruments rather than listening to recorded music\n",
            "url": "https://en.wikipedia.org/wiki/Prosumer",
            "id": 418      
        },
        {
            "name": "Problem-oriented language",
            "definition": "A computer language designed to handle a particular class of problem. For example, COBOL was designed for business, FORTRAN for scientific and GPSS for simulation.",
            "url": "http://www.forth.org/POL.pdf",
            "id": 419      
        },
        {
            "name": "Primitive data type",
            "definition": "In computer science, primitive data types are a set of basic data types from which all other data types are constructed. Specifically it often refers to the limited set of data representations in use by a particular processor, which all compiled programs must use. Strings (alphanumeric characters), integers and Boolean (yes/no) are examples of primitive data types.\n\nMost processors support a similar set of primitive data types, although the specific representations vary. More generally ‘primitive data types’ may refer to the standard data types built into a programming language. Data types which are not primitive are referred to as derived or composite data types.",
            "url": "https://en.wikipedia.org/wiki/Primitive_data_type",
            "id": 420      
        },
        {
            "name": "Poisson distribution",
            "definition": "A statistical method developed by the 18th century French mathematician S. D. Poisson, which is used for predicting the probable distribution of a series of events. For example, when the average transaction volume in a communications system can be estimated, Poisson distribution is used to determine the probable minimum and maximum number of transactions that can occur within a given time period.",
            "url": "https://en.wikipedia.org/wiki/Poisson_distribution",
            "id": 421     
        },
        {
            "name": "Phlashing",
            "definition": "Hacking the software in flash memory firmware. Phlashing takes advantages of code vulnerabilities in embedded systems and renders the device inoperable. From ‘flashing’, which means to install an operating system into flash memory.\n\nPhlashing may also refer to a permanent denial of service (DoS) attack that exploits a vulnerability in network-based firmware updates. Such an attack is currently theoretical but if carried out could damage and render the target device inoperable, to the point where its hardware would need to be replaced for it to be usable.",
            "url": "https://en.wikipedia.org/wiki/Denial-of-service_attack#Permanent_denial-of-service_attacks",
            "id": 422     
        },
        {
            "name": "Query language",
            "definition": "Query languages, data query languages or database query languages (DQLs) are computer languages used to make queries in databases and information systems. It may be in the form of typed commands such as the widely used Structured Query Language (SQL), a predefined query menu or a query by example (QBE). Query languages are usually included in DBMSs, and stand-alone packages are available for interrogating non-DBMS files.",
            "url": "https://en.wikipedia.org/wiki/Query_language",
            "id": 423     
        },
        {
            "name": "Recursion",
            "definition": "In programming, the ability of a subroutine or program module to call itself. Recursion is used to write routines that solve problems by repeatedly processing the output of the same process.",
            "url": "https://en.wikipedia.org/wiki/Recursion_(computer_science)",
            "id": 424      
        },
        {
            "name": "Re-entrant code",
            "definition": "A programming routine that can be used by multiple programs simultaneously. It is used in operating systems and other system software as well as in multithreading, where concurrent events are taking place. It is written so that none of its code is modifiable (no values are changed) and it does not keep track of anything. The calling programs keep track of their own progress (variables, flags, etc.), thus one copy of the re-entrant routine can be shared by any number of users or processes.\n\nConceptually, re-entrant coding is as if several people were each baking a cake from a single copy of a recipe on the wall. Everyone follows the master recipe but keeps track of their individual progress by jotting down the step they are working on so they can pick up where they left off. The master recipe is never disturbed.",
            "url": "https://en.wikipedia.org/wiki/Reentrancy_(computing)",
            "id": 425      
        },
        {
            "name": "Rasterisation",
            "definition": "Rasterization (or rasterisation) is the task of taking an image described in a vector graphics format (shapes) and converting it into a raster image (a series of pixels, dots or lines, which, when displayed together, create the image which was represented via shapes).\n\nThe rasterized image may then be displayed on a computer display, video display or printer, or stored in a bitmap file format. Rasterization may refer to the technique of drawing 3D models, or the conversion of 2D rendering primitives such as polygons, line segments into a rasterized format.\n\nThe term is derived from German Raster ('framework, schema'), from the Latin rāstrum, ‘scraper, rake’.",
            "url": "https://en.wikipedia.org/wiki/Rasterisation",
            "id": 426      
        },
        {
            "name": "Race condition",
            "definition": "A race condition or race hazard is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events. It becomes a bug when one or more of the possible behaviors is undesirable.\n\nThe term race condition was already in use by 1954, for example in David A. Huffman's doctoral thesis ‘The synthesis of sequential switching circuits’.\n\nRace conditions can occur especially in logic circuits, multithreaded, or distributed software programs.",
            "url": "https://en.wikipedia.org/wiki/Race_condition",
            "id": 427      
        },
        {
            "name": "Lint",
            "definition": "Lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs. The term originates from a Unix utility that examined C language source code.\n\nLint-like tools are especially useful for dynamically typed languages like JavaScript and Python. Because the compilers of such languages typically do not enforce as many and as strict rules prior to execution, linter tools can also be used as simple debuggers for finding common errors (e.g. syntactic discrepancies) as well as hard-to-find errors such as heisenbugs (drawing attention to suspicious code as ‘possible errors’). Lint-like tools generally perform static analysis of source code.\n\nLint-like tools have also been developed for other aspects of language, including grammar and style guides.",
            "url": "https://en.wikipedia.org/wiki/Lint_(software)",
            "id": 428      
        },
        {
            "name": "Systems programmer",
            "definition": "In the IT department of a large organization, systems programmers are technical experts on some or all of the computer's system software (operating systems, networks, DBMSs, etc.). They are responsible for the efficient performance of the computer systems.\n\nIn a user organization, systems programmers generally do not write applications. However, they may write utility programs that are used behind the scenes and often perform technical tasks that integrate vendors' software. They also act as technical advisors to systems analysts, application programmers and operations personnel. For example, they would know whether additional tasks could be added to the existing hardware and would recommend conversion to new system software (OS, DBMS, etc.) in order to optimize performance.\n\nIn mainframe environments, there is typically one systems programmer to 10 or more application programmers, and systems programmers generally enjoy higher salaries. In smaller environments, users rely on vendors or consultants for systems programming assistance. In fact, end users are actually performing systems programmer functions when they install new software or hardware on their own computers.",
            "url": "https://en.wikipedia.org/wiki/Systems_programming",
            "id": 429      
        },
        {
            "name": "Spiral development",
            "definition": "A software development method that combines elements of agile development and the waterfall method, the latter associated with the traditional system development life cycle (SDLC). The spiral method conforms to the SDLC by including version releases and concurrent documentation and testing. However, like the agile method, it provides incremental, staged improvements in functionality.",
            "url": "https://en.wikipedia.org/wiki/Spiral_model",
            "id": 430      
        },
        {
            "name": "Five nines",
            "definition": "Refers to 99.999 percent uptime that many network providers are fond of stating as the reliability of their networks. Whether five nines is truly what is delivered at all times may be debatable, because that means no more than 26 seconds of downtime per month. In any event, five nines means that everything in the datacenter is fully redundant, including AC power, air conditioning, network equipment and computer hardware.\n\nNines ratings range from a maximum of 72 hours of downtime per month (one nine) to no more than 2.6 milliseconds per month (nine nines).",
            "url": "https://en.wikipedia.org/wiki/High_availability#Percentage_calculation",
            "id": 431     
        },
        {
            "name": "6DOF",
            "definition": "(6 Degrees Of Freedom) The amount of motion supported in a robotics or virtual reality system. Six degrees provides X, Y and Z (horizontal, vertical and depth) and pitch, yaw and roll. Three degrees of freedom (3DOF) provides X, Y and Z only.",
            "url": "https://en.wikipedia.org/wiki/Six_degrees_of_freedom",
            "id": 432     
        },
        {
            "name": "Secure code",
            "definition": "Program source code that is written to withstand attacks. The amount of effort that goes into writing a secure program is substantially greater than writing code without such concern. Normally, programmers deal with a solution to a data processing or transmission task without worrying about every line of code being a potential attack vector.",
            "url": "https://en.wikipedia.org/wiki/Secure_coding",
            "id": 433     
        },
        {
            "name": "Software-defined networking (SDN)",
            "definition": "Software-defined networking (SDN) technology is an approach to network management that enables dynamic, programmatically efficient network configuration in order to improve network performance and monitoring, making it more like cloud computing than traditional network management. \n\nSDN is meant to address the static architecture of traditional networks and attempts to centralize network intelligence in one network component by disassociating the forwarding process of network packets (data plane) from the routing process (control plane). The control plane consists of one or more controllers, which are considered the brain of the SDN network where the whole intelligence is incorporated.",
            "url": "https://en.wikipedia.org/wiki/Software-defined_networking",
            "id": 434      
        },
        {
            "name": "Scraping",
            "definition": "Extracting data from output sent to the screen or printer rather than from the original files or databases. Scraping is a way to obtain data from any source without having access to the original file, but only at the time it is being printed or displayed. Scraping differs from capturing the screen. A screen capture creates an image of the screen, whereas scraping extracts the actual text.",
            "url": "https://en.wikipedia.org/wiki/Data_scraping",
            "id": 435      
        },
        {
            "name": "Sanitization",
            "definition": "To remove sensitive data from an information system, a database or an extract from a database.\n\nThe main strategies for erasing personal data from devices are physical destruction, cryptographic erasure, and data erasure. While the term data sanitization may lead some to believe that it only includes data on electronic media, the term also broadly covers physical media, such as paper copies. These data types are termed soft for electronic files and hard for physical media paper copies. Data sanitization methods are also applied for the cleaning of sensitive data, such as through heuristic-based methods, machine-learning based methods, and k-source anonymity.",
            "url": "https://en.wikipedia.org/wiki/Data_sanitization",
            "id": 436      
        },
        {
            "name": "Softlifting",
            "definition": "Making illegal copies of purchased software for a few family members or friends. Also called ‘softloading’, it is software piracy on a small scale per transaction, and it is often thought to cause little harm. However, because softlifting is so common, it greatly contributes to the total damage brought about by software piracy worldwide.",
            "url": "https://en.wikipedia.org/wiki/Copyright_infringement",
            "id": 437      
        },
        {
            "name": "Simplex",
            "definition": "One way transmission. Contrast with half-duplex (both directions, but one at a time) and full-duplex (both directions simultaneously).",
            "url": "https://en.wikipedia.org/wiki/Simplex_communication",
            "id": 438      
        },
        {
            "name": "Shovelware",
            "definition": "The many ‘extra’ programs pre-installed on some PCs that offer little value (they are ‘shoveled’ in without regard to quality). Shovelware first appeared in the late 1980s when tons of shareware programs were copied onto CD-ROMs and advertised in magazines or sold at computer flea markets. The term also applies to multiple software titles sold as a bundle. Shovelware is often geared to first-time buyers, who think they are getting more for their money.",
            "url": "https://en.wikipedia.org/wiki/Shovelware",
            "id": 439      
        },
        {
            "name": "Shoulder surfing",
            "definition": "Looking over someone's shoulder to obtain passwords, PINs and other security codes being entered. Often performed with binoculars, ATMs and other data entry terminals may make it more difficult by requiring a 90 degree viewing angle to read the screen or moving the digit keys around on touchscreens.",
            "url": "https://en.wikipedia.org/wiki/Shoulder_surfing_(computer_security)",
            "id": 440      
        },
        {
            "name": "Shim",
            "definition": "Software that allows an older version of a program, framework or protocol to use the newer updated version, or vice versa. A shim is often a library that transparently intercepts API calls and changes the arguments passed, handles the operation itself or redirects the operation elsewhere. Shims can also be used for running programs on different software platforms than they were developed for.",
            "url": "https://en.wikipedia.org/wiki/Shim_(computing)",
            "id": 441     
        },
        {
            "name": "Polyfill",
            "definition": "In web development, a polyfill is code that implements a feature on web browsers that do not support the feature. Most often, it refers to a JavaScript library that implements an HTML5 or CSS web standard, either an established standard (supported by some browsers) on older browsers, or a proposed standard (not supported by any browsers) on existing browsers.\n\nPolyfills allow web developers to use an API regardless of whether or not it is supported by a browser, and usually with minimal overhead. Typically they first check if a browser supports an API, and use it if available, otherwise using their own implementation. Polyfills themselves use other, more supported features, and thus different polyfills may be needed for different browsers. The term is also used as a verb: polyfilling is providing a polyfill for a feature.",
            "url": "https://en.wikipedia.org/wiki/Polyfill_(programming)",
            "id": 442     
        },
        {
            "name": "Shadow IT",
            "definition": "In big organizations, shadow IT refers to information technology (IT) systems deployed by departments other than the central IT department, to work around the perceived or actual shortcomings of the central information systems. Shadow IT often introduces security and compliance concerns.\n\nShadow IT may also refer to employees selecting their own software applications, especially from a cloud provider (SaaS). The internal IT department is either not aware of the application or does not oversee the software in any manner.",
            "url": "https://en.wikipedia.org/wiki/Shadow_IT",
            "id": 443     
        },
        {
            "name": "10-foot user interface",
            "definition": "In computing, 10-foot user interface (’10-foot UI’), also known as a 3-meter user interface (especially for international marketing), is a graphical user interface designed for televisions. Compared to desktop computer and smartphone user interfaces, it uses text and other interface elements which are much larger in order to accommodate a typical television viewing distance of 10 feet (3 meters). Additionally, the limitations of a television's remote control necessitate extra user experience considerations to minimize user effort.",
            "url": "https://en.wikipedia.org/wiki/10-foot_user_interface",
            "id": 444      
        },
        {
            "name": "Coupled",
            "definition": "The degree to which hardware and software components are linked together and dependent upon each other. In programming, coupling refers to the degree of direct knowledge that one component has of another.",
            "url": "https://en.wikipedia.org/wiki/Loose_coupling#In_programming",
            "id": 445      
        },
        {
            "name": "Throbber",
            "definition": "A throbber, also known as a loading icon, is an animated graphical control element used to show that a computer program is performing an action in the background (such as downloading content, conducting intensive calculations or communicating with an external device). In contrast to a progress bar, a throbber does not indicate how much of the action has been completed.",
            "url": "https://en.wikipedia.org/wiki/Throbber",
            "id": 446      
        },
        {
            "name": "Upconvert",
            "definition": "To convert one set of values to a higher set of values. For example, HDTV sets upconvert broadcast TV (480i) and DVD content (480i or 480p) to the highest format the set supports (720p, 1080i or 1080p). A/V receivers also provide upconversion.\n\nAlso called ‘upscaling’. In a home theater, the DVD player, A/V receiver and HDTV provide upconversion capabilities. If the units are all of similar quality, it may make little difference which one performs the upconversion. For example, if the HDTV does the best job, the DVD and receiver upconversion can be turned off. Contrast with downconvert.",
            "url": "https://en.wikipedia.org/wiki/Video_scaler",
            "id": 447      
        },
        {
            "name": "Unified Computing System (UCS)",
            "definition": "Cisco Unified Computing System (UCS) is a data center server computer product line composed of server hardware, virtualization support, switching fabric, and management software, introduced in 2009 by Cisco Systems. The products are marketed for scalability by integrating many components of a data center that can be managed as a single unit.\n\nThe Cisco fabric interconnects (FI) provide network connectivity for the chassis, blade servers and rack servers connected to it through different speeds of Ethernet and Fibre Channel over Ethernet (FCoE). Management of the system devices is handled by the UCS Manager software integrated with fabric interconnects.\n\nCisco UCS supports several hypervisors including VMware ESXi, Microsoft Hyper-V and Citrix Systems' Xen server. Virtual machines can be moved from one physical chassis to another, applications may be moved between virtual machines, and management may even be conducted remotely from an iPhone using SiMU - Simple iPhone Management of UCS. In addition to the embedded software, administrators may also manage the system from VMware's vSphere.\n\nIn 2017 Cisco announced a partnership with Docker to include its enterprise software in UCS products to directly provide operating-system-level virtualization (containerization). Also in 2017, Cisco announced a cloud-hosted management offering for UCS infrastructure called Cisco Intersight. This platform augmented the UCS management platform.",
            "url": "https://en.wikipedia.org/wiki/Cisco_Unified_Computing_System",
            "id": 448      
        },
        {
            "name": "Vampire device",
            "definition": "An electronic device that draws current even though the power switch is turned off. A huge majority of electronic equipment today qualifies as vampire devices because they continue to use electricity to power LEDs as well as perform routine processing.\n\nFor example, many AC to DC power adapters use current even though their target devices are turned off. The only way to kill the power to vampire devices is to unplug them from the wall or plug them into a power strip that can be turned off.",
            "url": "https://www.duke-energy.com/energy-education/energy-savings-and-efficiency/energy-vampires",
            "id": 449      
        },
        {
            "name": "Virtual appliance",
            "definition": "A virtual appliance is the software equivalent of a hardware device that performs a fixed set of functions. It is a pre-configured virtual machine image, ready to run on a hypervisor; virtual appliances are a subset of the broader class of software appliances. Installation of a software appliance on a virtual machine and packaging that into an image creates a virtual appliance.\n\nThe regular process of deploying a new application in a virtualized computer is to set up a new virtual machine (VM) partition, install the operating system and then the application. The processes are time consuming and configuration mistakes can be made. In contrast, virtual appliance deployment is faster because the appliance image (application and OS) is copied to the virtual machine pre-installed and pre-configured. The application and OS have already been tested together, and running the software is less error prone.",
            "url": "https://en.wikipedia.org/wiki/Virtual_appliance",
            "id": 450      
        },
        {
            "name": "Vertical / Horizontal market software",
            "definition": "Vertical market software packages are designed for a particular industry such as banking, insurance or manufacturing. Horizontal market software packages, on the other hand, such as word processors and spreadsheets, are used in all industries (banking, insurance, etc.). Such products are also called ‘productivity software’.",
            "url": "https://en.wikipedia.org/wiki/Vertical_market_software",
            "id": 451     
        },
        {
            "name": "x86",
            "definition": "The world's predominant hardware platform for laptops, desktops and servers. The x86 line was developed by Intel and includes the Core, Xeon, Pentium, Atom and original 8086 family (hence the ’86’). With an even greater market share than x86, ARM is the hardware platform for mobile devices and appliances (see ARM).\n\nAMD also manufactures x86 CPUs with brands such as Athlon, Sempron and Opteron. Although Intel and AMD are primary sources, x86 chips are also made by others.\n\nThe term ‘x86’ may also refer to 32-bits when contrasting 32-bit with 64-bit hardware for Windows PCs (see x64).",
            "url": "https://en.wikipedia.org/wiki/X86",
            "id": 452     
        },
        {
            "name": "Proof of stake (PoS)",
            "definition": "Proof-of-stake (PoS) protocols are a class of consensus mechanisms for blockchains that work by selecting validators in proportion to their quantity of holdings in the associated cryptocurrency. This is done to avoid the computational cost of proof-of-work schemes.",
            "url": "https://en.wikipedia.org/wiki/Proof_of_stake",
            "id": 453     
        },
        {
            "name": "Proof of work",
            "definition": "Proof-of-work (PoW) is a form of cryptographic proof in which one party (the prover) proves to others (the verifiers) that a certain amount of a specific computational effort has been expended. Verifiers can subsequently confirm this expenditure with minimal effort on their part.",
            "url": "https://en.wikipedia.org/wiki/Proof_of_work",
            "id": 454      
        },
        {
            "name": "Escape character",
            "definition": "In computing and telecommunication, an escape character is a character that invokes an alternative interpretation on the following characters in a character sequence. An escape character is a particular case of metacharacters. Generally, the judgement of whether something is an escape character or not depends on the context.\n\nIn the telecommunications field, escape characters are used to indicate that the following characters are encoded differently. This is used to alter control characters that would otherwise be noticed and acted on by the underlying telecommunications hardware. In this context, the use of escape characters is often referred to as quoting.\n\nAn escape character may not have its own meaning, so all escape sequences are of two or more characters. Escape characters are part of the syntax for many programming languages, data formats, and communication protocols. For a given alphabet an escape character's purpose is to start character sequences (so named escape sequences), which have to be interpreted differently from the same characters occurring without the prefixed escape character.\n\nFor example, in many programming languages, an escape character also forms some escape sequences which are referred to as control characters. For example, line break, or newline, has an escape sequence of '\\n'.",
            "url": "https://en.wikipedia.org/wiki/Escape_character",
            "id": 455      
        },
        {
            "name": "Indexed vs. Associative arrays",
            "definition": "An array is a collection of objects that contain a group of variables stored under the same name. All the elements belong to the same data type, i.e. string, integers, or lists. Keys are unique in the case of both indexed and associative arrays. \n\nAn indexed array uses indexes to identify its elements. An associative array uses keys to identify its elements.\n\nIndexed arrays store and assign values in a numeric fashion with count starting from zero. It is basically an array wherein each of the keys is associated with its own specific value. \n\nAn associative array is stored in the form of key-value pair. This type of array is where the key is stored in the numeric or string format. In an associative array, the association between a key and a value is often known as a ‘mapping’, and the same word mapping may also be used to refer to the process of creating a new association.\n\nThe basic approach to building a multi-dimensional array is the same whether it's a normal, indexed array or uses associative indexing. Essentially, you assign an array as the value of an array element. The development of an associative multi-dimensional array is a little more complex, because the keys are often not the ordered integers you find in an indexed array.",
            "url": "https://en.wikipedia.org/wiki/Associative_array",
            "id": 456      
        },
        {
            "name": "Relational operator",
            "definition": "In computer science, a relational operator is a programming language construct or operator that tests or defines some kind of relation between two entities. These include numerical equality (e.g., 5 = 5) and inequalities (e.g., 4 ≥ 3).\n\nIn programming languages that include a distinct boolean data type in their type system, like Pascal, Ada, or Java, these operators usually evaluate to true or false, depending on if the conditional relationship between the two operands holds or not. In languages such as C, relational operators return the integers 0 or 1, where 0 stands for false and any non-zero value stands for true.\n\nAn expression created using a relational operator forms what is termed a relational expression or a condition.",
            "url": "https://en.wikipedia.org/wiki/Relational_operator",
            "id": 457      
        },
        {
            "name": "Hyperconverged infrastructure (HCI)",
            "definition": "Hyperconverged infrastructure combines compute, storage, and networking in a single system and is used frequently in data centers. Enterprises can choose an appliance from a single vendor or install hardware-agnostic hyperconvergence software on white-box servers.",
            "url": "https://en.wikipedia.org/wiki/Hyper-converged_infrastructure",
            "id": 458      
        },
        {
            "name": "Secure access service edge (SASE)",
            "definition": "Secure access service edge (SASE) is a network architecture that rolls software-defined wide area networking (SD-WAN) and security into a cloud service that promises simplified WAN deployment, improved efficiency and security, and to provide appropriate bandwidth per application.",
            "url": "https://en.wikipedia.org/wiki/Secure_access_service_edge",
            "id": 459      
        },
        {
            "name": "alt tag",
            "definition": "The alt attribute, or alt tag, is the HTML attribute used in HTML and XHTML documents to specify alternative text (alt text) that is to be rendered when the element to which it is applied cannot be rendered.\n\nThe alt attribute is used by ‘screen reader’ software so that a person who is listening to the content of a webpage (for instance, a person who is blind) can interact with this element. Additionally, it substitutes the image when copy-pasted as text and makes images more machine-readable, which improves search engine optimization. Every image should have an alt attribute to be accessible, but it need not contain text. It can be an empty or null attribute: alt=‘’.",
            "url": "https://en.wikipedia.org/wiki/Alt_attribute",
            "id": 460      
        },
        {
            "name": "Minimum viable product (MVP)",
            "definition": "The most pared-down version of a product that can be released to the market. When adopting this approach, developers will focus on the core features and functions that are essential. Once the product is released and user feedback is gathered, they will continue to build the complete set of features.",
            "url": "https://en.wikipedia.org/wiki/Minimum_viable_product",
            "id": 461     
        },
        {
            "name": "Bounding box",
            "definition": "The bounding box of an element is the smallest possible rectangle (aligned with the axes of that element's user coordinate system) that entirely encloses it and its descendants.",
            "url": "https://en.wikipedia.org/wiki/Minimum_bounding_box",
            "id": 462     
        },
        {
            "name": "Constructor",
            "definition": "In class-based object-oriented programming, a constructor (abbreviation: ctor) is a special type of subroutine called to create an object. It prepares the new object for use, often accepting arguments that the constructor uses to set required member variables.",
            "url": "https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)",
            "id": 463     
        },
        {
            "name": "Artifact",
            "definition": "An artifact is one of many kinds of tangible by-products produced during the development of software. Some artifacts (e.g., use cases, class diagrams, and other Unified Modeling Language (UML) models, requirements and design documents) help describe the function, architecture, and design of software. Other artifacts are concerned with the process of development itself—such as project plans, business cases, and risk assessments.",
            "url": "https://en.wikipedia.org/wiki/Artifact_(software_development)",
            "id": 464      
        },
        {
            "name": "Branching",
            "definition": "Branching, in version control and software configuration management, is the duplication of an object under version control (such as a source code file or a directory tree). Each object can thereafter be modified separately and in parallel so that the objects become different. In this context the objects are called branches. The users of the version control system can branch any branch.\n\nBranches are also known as trees, streams or codelines. The originating branch is sometimes called the parent branch, the upstream branch (or simply upstream, especially if the branches are maintained by different organizations or individuals), or the backing stream.",
            "url": "https://en.wikipedia.org/wiki/Branching_(version_control)",
            "id": 465      
        },
        {
            "name": "Management, control and data planes",
            "definition": "These terms are abstract logical concepts to describe network operations.\n\nThe management plane consists of all the functions you use to control and monitor devices. They are mostly logical concepts but SDN (Software Defined Networking) separates them into actual devices. Network programmability involves manipulating the management plane.\n\nThe control plane is the part of a network that carries signaling traffic and is responsible for routing. This includes the routing protocols such as Spanning Tree Protocol (STP), Address Resolution Protocol (ARP), Routing Information Protocol (RIP), Dynamic Host Configuration Protocol (DHCP) etc.\n\nThe data plane refers to all the functions and processes that forward packets/frames from one interface to another. This includes decrementing Time To Live (TTL), recomputing IP header checksums, decapsulation/encapsulation etc. Sometimes referred to as the forwarding plane.",
            "url": "https://en.wikipedia.org/wiki/Control_plane",
            "id": 466      
        },
        {
            "name": "Encapsulation",
            "definition": "Encapsulation is a technical term with a different meaning depending on if it is used in reference to network or software engineering.\n\nIn computer networking, encapsulation is a method of designing modular communication protocols in which logically separate functions in the network are abstracted from their underlying structures by inclusion or information hiding within higher-level objects. In other words, encapsulation ‘takes information from a higher layer and adds a header to it, treating the higher layer information as data’.\n\nIn object-oriented programming (OOP) languages, and other related fields, encapsulation refers to one of two related but distinct notions, and sometimes to the combination thereof:\n\n- A language mechanism for restricting direct access to some of the object's components. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing direct access to them by clients in a way that could expose hidden implementation details or violate state invariance maintained by the methods.\n\n- A language construct that facilitates the bundling of data with the methods (or other functions) operating on that data.",
            "url": "https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)",
            "id": 467      
        },
        {
            "name": "Object-oriented analysis and design (OOAD)",
            "definition": "Object-oriented analysis and design (OOAD) is the process of gathering software requirements and developing specifications in terms of a system’s object model and interactions. It is a technical approach for analyzing and designing an application, system, or business by applying object-oriented programming, as well as using visual modeling throughout the software development process to guide stakeholder communication and product quality.\n\nOOAD in modern software engineering is typically conducted in an iterative and incremental way. The outputs of OOAD activities are analysis models (for OOA) and design models (for OOD) respectively. The intention is for these to be continuously refined and evolved, driven by key factors like risks and business value.",
            "url": "https://en.wikipedia.org/wiki/Object-oriented_analysis_and_design",
            "id": 468      
        },
        {
            "name": "Inheritance", 
            "definition": "In object-oriented programming, inheritance is the mechanism of basing an object or class upon another object (prototype-based inheritance) or class (class-based inheritance), retaining similar implementation. Using inheritance, a subclass can access the properties and functions of the base class (parent class) it is derived from and can also override those functions or properties. There are different levels and ways to implement inheritance in programming languages:\n\nSingle inheritance: A class is inherited from just its parent class\n\nMultiple inheritance: A class is derived from more than one parent class\n\nMulti-level inheritance: A class in inherited from a child class. For example, class C is inherited from a derived class B, which is inherited from parent class A.\n\nHierarchical inheritance: Multiple child classes or subclasses inherit properties from the same parent class.",
            "url": "https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)",
            "id": 469      
        },
        {
            "name": "Lexical analysis",
            "definition": "In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning). A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer. A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth.",
            "url": "https://en.wikipedia.org/wiki/Lexical_analysis",
            "id": 470      
        },
        {
            "name": "Dynamic typing vs. static typing",
            "definition": "There are two main differences between dynamic typing and static typing.\n\nFirst, dynamically-typed languages perform type checking at runtime, while statically typed languages perform type checking at compile time. This means that scripts written in dynamically-typed languages can compile even if they contain errors that will prevent the script from running properly (if at all). If a script written in a statically-typed language contains errors, it will fail to compile until the errors have been fixed.\n\nSecond, statically-typed languages require you to declare the data types of your variables before you use them, while dynamically-typed languages do not. Thus, a variable in a dynamically typed language can be reassigned to different data types.",
            "url": "https://en.wikipedia.org/wiki/Type_system#Type_checking",
            "id": 471     
        },
        {
            "name": "Cliff effect",
            "definition": "In telecommunications, the (digital) cliff effect or brickwall effect is a sudden loss of digital signal reception. Unlike analog signals, which gradually fade when signal strength decreases or electromagnetic interference or multipath increases, a digital signal provides data which is either perfect or non-existent at the receiving end. It is named for a graph of reception quality versus signal quality, where the digital signal ‘falls off a cliff’ instead of having a gradual rolloff.",
            "url": "https://en.wikipedia.org/wiki/Cliff_effect",
            "id": 472     
        },
        {
            "name": "Control flow",
            "definition": "In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. The emphasis on explicit control flow distinguishes an imperative programming language from a declarative programming language.\n\nWithin an imperative programming language, a control flow statement is a statement that results in a choice being made as to which of two or more paths to follow. For non-strict functional languages, functions and language constructs exist to achieve the same result, but they are usually not termed control flow statements.",
            "url": "https://en.wikipedia.org/wiki/Control_flow",
            "id": 473     
        },
        {
            "name": "Microframework",
            "definition": "A microframework is a term used to refer to minimalistic web application frameworks. It is contrasted with full-stack frameworks.\n\nIt lacks most of the functionality which is common to expect in a full-fledged web application framework, such as:\n\n• Accounts, authentication, authorization, roles\n• Database abstraction via an object-relational mapping\n• Input validation and input sanitation\n•	Web template engine\n\nTypically, a microframework facilitates receiving an HTTP request, routing the HTTP request to the appropriate controller, dispatching the controller, and returning an HTTP response. Microframeworks are often specifically designed for building the APIs for another service or application.",
            "url": "https://en.wikipedia.org/wiki/Microframework",
            "id": 474      
        },
        {
            "name": "Unified API",
            "definition": "A Unified API combines APIs for multiple providers and gives you a single API to access all their endpoints. It is a ‘meta’ data model designed to enable developers to talk to many other systems’ APIs through one interface.\n\nA Unified API aggregates many APIs in the same software category, making integration easier with a standard endpoint, authentication, and normalized data. This results in a consistent developer experience with less integration hassle.\n\nA good unified API has three things: normalization, flexibility, and transparency.",
            "url": "https://blog.apideck.com/what-is-a-unified-api",
            "id": 475      
        },
        {
            "name": "Code on demand",
            "definition": "In distributed computing, code on demand is any technology that sends executable software code from a server computer to a client computer upon request from the client's software. Some well-known examples of the code on demand paradigm on the web are Java applets, Adobe's ActionScript language for the Flash Player, and JavaScript.\n\nThe program code lies inactive on a web server until a user (client) requests a web page that contains a link to the code using the client's web browser. Upon this request, the web page and the program are transported to the user's machine using HTTP. When the page is displayed, the code is started in the browser and executes locally, inside the user's computer until it is stopped (e.g., by the user leaving the web page).\n\nCode on demand is a specific use of mobile code, within the field of code mobility.",
            "url": "https://en.wikipedia.org/wiki/Code_on_demand",
            "id": 476      
        },
        {
            "name": "Brownfield",
            "definition": "Brownfield development is a term commonly used in the information technology industry to describe problem spaces needing the development and deployment of new software systems in the immediate presence of existing (legacy) software applications/systems. This implies that any new software architecture must take into account and coexist with live software already in situ.\n\nBrownfield development adds a number of improvements to conventional software engineering practices. These traditionally assume a 'clean sheet of paper' or 'greenfield land' target environment throughout the design and implementation phases of software development. Brownfield extends such traditions by insisting that the context (local landscape) of the system being created be factored into any development exercise. This requires a detailed knowledge of the systems, services and data in the immediate vicinity of the solution under construction.",
            "url": "https://en.wikipedia.org/wiki/Brownfield_(software_development)",
            "id": 477      
        },
        {
            "name": "In situ",
            "definition": "In computer science an in situ operation is one that occurs without interrupting the normal state of a system. For example, a file backup may be restored over a running system, without needing to take the system down to perform the restore. In the context of a database, a restore would allow the database system to continue to be available to users while a restore happened. An in situ upgrade would allow an operating system, firmware or application to be upgraded while the system was still running, perhaps without the need to reboot it, depending on the sophistication of the system.\n\nAnother use of the term in-situ that appears in Computer Science focuses primarily on the use of technology and user interfaces to provide continuous access to situationally relevant information in various locations and contexts. Examples include athletes viewing biometric data on smartwatches to improve their performance, a presenter looking at tips on a smart glass to reduce their speaking rate during a speech, or technicians receiving online and stepwise instructions for repairing an engine.",
            "url": "https://en.wikipedia.org/wiki/In_situ#Computer_science",
            "id": 478      
        },
        {
            "name": "WebSocket",
            "definition": "WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. The current API specification allowing web applications to use this protocol is known as WebSockets. It is a living standard maintained by the WHATWG and a successor to The WebSocket API from the W3C.\n\nWebSocket is distinct from HTTP. Both protocols are located at layer 7 in the OSI model and depend on TCP at layer 4. Although they are different, RFC 6455 states that WebSocket ‘is designed to work over HTTP ports 443 and 80 as well as to support HTTP proxies and intermediaries’, thus making it compatible with HTTP. To achieve compatibility, the WebSocket handshake uses the HTTP Upgrade header to change from the HTTP protocol to the WebSocket protocol.\n\nThe WebSocket protocol enables interaction between a web browser (or other client application) and a web server with lower overhead than half-duplex alternatives such as HTTP polling, facilitating real-time data transfer from and to the server. This is made possible by providing a standardized way for the server to send content to the client without being first requested by the client, and allowing messages to be passed back and forth while keeping the connection open. In this way, a two-way ongoing conversation can take place between the client and the server. The communications are usually done over TCP port number 443 (or 80 in the case of unsecured connections), which is beneficial for environments that block non-web Internet connections using a firewall.\n\nMost browsers support the WebSocket protocol.",
            "url": "https://en.wikipedia.org/wiki/WebSocket",
            "id": 479      
        },
        {
            "name": "Network socket",
            "definition": "A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an application programming interface (API) for the networking architecture. Sockets are created only during the lifetime of a process of an application running in the node.\n\nBecause of the standardization of the TCP/IP protocols in the development of the Internet, the term network socket is most commonly used in the context of the Internet protocol suite, and is therefore often also referred to as Internet socket. In this context, a socket is externally identified to other hosts by its socket address, which is the triad of transport protocol, IP address, and port number.\n\nThe term socket is also used for the software endpoint of node-internal inter-process communication (IPC), which often uses the same API as a network socket.",
            "url": "https://en.wikipedia.org/wiki/Network_socket",
            "id": 480      
        },
        {
            "name": "Service-oriented architecture",
            "definition": "In software engineering, SOA (service-oriented architecture) is an architectural style that focus on discrete services instead of a monolithic design. By consequence, it is as well applied in the field of software design where services are provided to the other components by application components, through a communication protocol over a network. A service is a discrete unit of functionality that can be accessed remotely and acted upon and updated independently, such as retrieving a credit card statement online. SOA is also intended to be independent of vendors, products and technologies.\n\nService orientation is a way of thinking in terms of services and service-based development and the outcomes of services.\n\nA service has four properties according to one of many definitions of SOA:\n\n1. It logically represents a repeatable business activity with a specified outcome.\n2. It is self-contained.\n3. It is a black box for its consumers, meaning the consumer does not have to be aware of the service's inner workings.\n4. It may be composed of other services.\n\nDifferent services can be used in conjunction as a service mesh to provide the functionality of a large software application, a principle SOA shares with modular programming. Service-oriented architecture integrates distributed, separately maintained and deployed software components. It is enabled by technologies and standards that facilitate components' communication and cooperation over a network, especially over an IP network.\n\nSOA is related to the idea of an API (application programming interface), an interface or communication protocol between different parts of a computer program intended to simplify the implementation and maintenance of software. An API can be thought of as the service, and the SOA the architecture that allows the service to operate.",
            "url": "https://en.wikipedia.org/wiki/Service-oriented_architecture",
            "id": 481     
        },
        {
            "name": "AI winter",
            "definition": "In the history of artificial intelligence, an AI winter is a period of reduced funding and interest in artificial intelligence research. The term was coined by analogy to the idea of a nuclear winter. The field has experienced several hype cycles, followed by disappointment and criticism, followed by funding cuts, followed by renewed interest years or decades later.\n\nEnthusiasm and optimism about AI has generally increased since its low point in the early 1990s. Beginning about 2012, interest in artificial intelligence (and especially the sub-field of machine learning) from the research and corporate communities led to a dramatic increase in funding and investment.",
            "url": "https://en.wikipedia.org/wiki/AI_winter",
            "id": 482     
        },
        {
            "name": "Expert system",
            "definition": "In artificial intelligence, an expert system is a computer system emulating the decision-making ability of a human expert. Expert systems are designed to solve complex problems by reasoning through bodies of knowledge, represented mainly as if–then rules rather than through conventional procedural code. The first expert systems were created in the 1970s and then proliferated in the 1980s. Expert systems were among the first truly successful forms of artificial intelligence (AI) software. \n\nAn expert system is divided into two subsystems: the inference engine and the knowledge base. The knowledge base represents facts and rules. The inference engine applies the rules to the known facts to deduce new facts. Inference engines can also include explanation and debugging abilities.",
            "url": "https://en.wikipedia.org/wiki/Expert_system",
            "id": 483     
        },
        {
            "name": "Initialization vector (IV)",
            "definition": "In cryptography, an initialization vector (IV) or starting variable (SV) is an input to a cryptographic primitive being used to provide the initial state. The IV is typically required to be random or pseudorandom, but sometimes an IV only needs to be unpredictable or unique. Randomization is crucial for some encryption schemes to achieve semantic security, a property whereby repeated usage of the scheme under the same key does not allow an attacker to infer relationships between (potentially similar) segments of the encrypted message. For block ciphers, the use of an IV is described by the modes of operation.",
            "url": "https://en.wikipedia.org/wiki/Initialization_vector",
            "id": 484      
        },
        {
            "name": "Block Cipher vs Stream Cipher",
            "definition": "Block and stream ciphers are two ways that you can encrypt data. Also known as bulk ciphers, they’re two categories of symmetric encryption algorithms. (Reminder: with symmetric encryption, you use the same key to encrypt and decrypt data.) Block and stream ciphers are two separate routes to the same end goal of securing your data. The big difference between the two is how the data gets encrypted — and there are advantages and disadvantages to each method — and the types of environments they operate in.\n\nA block cipher breaks down plaintext messages into fixed-size blocks before converting them into ciphertext using a key. A stream cipher, on the other hand, breaks a plaintext message down into single bits, which then are converted individually into ciphertext using key bits.",
            "url": "https://www.thesslstore.com/blog/block-cipher-vs-stream-cipher/",
            "id": 485      
        },
        {
            "name": "Combinatorial explosion",
            "definition": "In mathematics, a combinatorial explosion is the rapid growth of the complexity of a problem due to how the combinatorics of the problem is affected by the input, constraints, and bounds of the problem. Combinatorial explosion is sometimes used to justify the intractability of certain problems. Examples of such problems include certain mathematical functions, the analysis of some puzzles and games, and some pathological examples which can be modelled as the Ackermann function.",
            "url": "https://en.wikipedia.org/wiki/Combinatorial_explosion",
            "id": 486      
        },
        {
            "name": "Kolmogorov complexity",
            "definition": "In algorithmic information theory (a subfield of computer science and mathematics), the Kolmogorov complexity of an object, such as a piece of text, is the length of a shortest computer program (in a predetermined programming language) that produces the object as output. It is a measure of the computational resources needed to specify the object, and is also known as algorithmic complexity, Solomonoff–Kolmogorov–Chaitin complexity, program-size complexity, descriptive complexity, or algorithmic entropy. It is named after Andrey Kolmogorov, who first published on the subject in 1963.",
            "url": "https://en.wikipedia.org/wiki/Kolmogorov_complexity",
            "id": 487      
        },
        {
            "name": "Inductive reasoning",
            "definition": "Inductive reasoning is a method of reasoning in which a body of observations is considered to derive a general principle. It consists of making broad generalizations based on specific observations. Inductive reasoning is distinct from deductive reasoning. If the premises are correct, the conclusion of a deductive argument is certain; in contrast, the truth of the conclusion of an inductive argument is probable, based upon the evidence given.",
            "url": "https://en.wikipedia.org/wiki/Inductive_reasoning#cite_note-1",
            "id": 488      
        },
        {
            "name": "Bayes' theorem",
            "definition": "In probability theory and statistics, Bayes' theorem (alternatively Bayes' law or Bayes' rule; recently Bayes–Price theorem), named after Thomas Bayes, describes the probability of an event, based on prior knowledge of conditions that might be related to the event. For example, if the risk of developing health problems is known to increase with age, Bayes' theorem allows the risk to an individual of a known age to be assessed more accurately (by conditioning it on their age) than simply assuming that the individual is typical of the population as a whole.\n\nOne of the many applications of Bayes' theorem is Bayesian inference, a particular approach to statistical inference. When applied, the probabilities involved in the theorem may have different probability interpretations. With Bayesian probability interpretation, the theorem expresses how a degree of belief, expressed as a probability, should rationally change to account for the availability of related evidence. Bayesian inference is fundamental to Bayesian statistics, being considered ‘to the theory of probability what Pythagoras's theorem is to geometry.’",
            "url": "https://en.wikipedia.org/wiki/Bayes%27_theorem",
            "id": 489      
        },
        {
            "name": "Posterior probability",
            "definition": "The posterior probability is a type of conditional probability that results from updating the prior probability with information summarized by the likelihood, through an application of Bayes' theorem. From an epistemological perspective, the posterior probability contains everything there is to know about an uncertain proposition (such as a scientific hypothesis, or parameter values), given prior knowledge and a mathematical model describing the observations available at a particular time. After the arrival of new information, the current posterior probability may serve as the prior in another round of Bayesian updating.\n\nIn the context of Bayesian statistics, the posterior probability distribution usually describes the epistemic uncertainty about statistical parameters conditional on a collection of observed data. From a given posterior distribution, various point and interval estimates can be derived, such as the maximum a posteriori (MAP) or the highest posterior density interval (HPDI). But while conceptually simple, the posterior distribution is generally not tractable and therefore needs to be either analytically or numerically approximated.",
            "url": "https://en.wikipedia.org/wiki/Posterior_probability",
            "id": 489      
        },
        {
            "name": "Monte Carlo method",
            "definition": "Monte Carlo methods, or Monte Carlo experiments, are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. They are often used in physical and mathematical problems and are most useful when it is difficult or impossible to use other approaches. Monte Carlo methods are mainly used in three problem classes: optimization, numerical integration, and generating draws from a probability distribution.\n\nIn principle, Monte Carlo methods can be used to solve any problem having a probabilistic interpretation. By the law of large numbers, integrals described by the expected value of some random variable can be approximated by taking the empirical mean (a.k.a. the sample mean) of independent samples of the variable.\n\nDespite its conceptual and algorithmic simplicity, the computational cost associated with a Monte Carlo simulation can be staggeringly high. In general the method requires many samples to get a good approximation, which may incur an arbitrarily large total runtime if the processing time of a single sample is high. Although this is a severe limitation in very complex problems, the embarrassingly parallel nature of the algorithm allows this large cost to be reduced (perhaps to a feasible level) through parallel computing strategies in local processors, clusters, cloud computing, GPU, FPGA etc.",
            "url": "https://en.wikipedia.org/wiki/Monte_Carlo_method",
            "id": 490      
        },
        {
            "name": "John McCarthy",
            "definition": "John McCarthy (September 4, 1927 – October 24, 2011) was an American computer scientist and cognitive scientist. He was one of the founders of the discipline of artificial intelligence. He co-authored the document that coined the term ‘artificial intelligence’ (AI), developed the programming language family Lisp, significantly influenced the design of the language ALGOL, popularized time-sharing, and invented garbage collection.\n\nSeveral Key Theme’s in McCarthy’s Work\n\n- The idea that the world can be represented symbolically for a machine and reasoned about by that machine.\n- The division of the AI problem into two parts: epistemological (representation) and heuristic (search).\n- The importance of formal (mathematical) representation, particularly the use of logic for representation.\n- The use of reification—the conceptual turning of abstract structures (such as situations) into concrete instances that can be reasoned about. The situation calculus, where the state of the universe is compressed into a single constant, is an example of such reification.\n- The development of abstract and general mechanisms (proof checkers, logic, circumscription, common sense) in contrast with domain-specific tools and languages.\n- The relatively complete analysis of artificial domains (programming languages, puzzles, chess) instead of a (necessarily) incomplete analysis of natural situations.\n- The importance of environments for interactive exploration. This is illustrated not so much by an explicit campaign position of McCarthy's as by the systems whose creation he led, such as the AI lab, Lisp, and timesharing.\n\nAwards and honors\n\n- Turing Award from the Association for Computing Machinery (1971)\n- Kyoto Prize (1988)\n- National Medal of Science (USA) in Mathematical, Statistical, and Computational Sciences (1990)\n- Inducted as a Fellow of the Computer History Museum ‘for his co-founding of the fields of Artificial Intelligence (AI) and timesharing systems, and for major contributions to mathematics and computer science’. (1999)\n- Benjamin Franklin Medal in Computer and Cognitive Science from the Franklin Institute (2003)\n- Inducted into IEEE Intelligent Systems' AI's Hall of Fame (2011), for the ‘significant contributions to the field of AI and intelligent systems’.",
            "url": "https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)",
            "id": 491      
        },
        {
            "name": "Vendor lock-in",
            "definition": "In economics, vendor lock-in, also known as proprietary lock-in or customer lock-in, makes a customer dependent on a vendor for products, unable to use another vendor without substantial switching costs.\n\nThe use of open standards and alternative options makes systems tolerant of change, so that decisions can be postponed until more information is available or unforeseen events are addressed. Vendor lock-in does the opposite: it makes it difficult to move from one solution to another.\n\nLock-in costs that create barriers to market entry may result in antitrust action against a monopoly.\n\nRelated to vendor lock-in is the concept of technology lock-in, which is a non-monopoly (mere technology), collective (on a society level) kind of lock-in:\n\nTechnological lock-in is the idea that the more a society adopts a certain technology, the more unlikely users are to switch.\n\nExamples of technology lock-in:\n\n- The continued prevalence of the QWERTY keyboard layout is said to be caused by technological lock-in.\n\n- Carbon lock-in is the theory that society has become reliant on carbon intensive technologies, thereby hindering renewable energy commercialization.\n\n- Converting one lossy file format into another incurs a generation loss that reduces quality. This is in effect a switching cost. Therefore, if valuable content is encoded in the format, this creates a need for continued compatibility with it.",
            "url": "https://en.wikipedia.org/wiki/Vendor_lock-in",
            "id": 492      
        },
        {
            "name": "Bill shock",
            "definition": "In telecommunications, bill shock is the negative reaction a subscriber can experience if their bill has unexpected charges. Bill shock can happen when, for example, a user grossly overuses data applications without an appropriate data plan, or uses a mobile device while roaming (whether domestically or internationally) without understanding the voice or data roaming charges involved.\n\nBill shock is the most common compelling event to start managing cloud costs. How to avoid cloud bill shock:\n\n1. Lock it down. Restrict management console access to a select few individuals and put in a process that routes requests for additions and modifications through to these people.\n2. Use the monitoring tools and enable monitoring alerts.\n3. Review your bills regularly.",
            "url": "https://harness.io/blog/continuous-efficiency-capabilities",
            "id": 493      
        },
        {
            "name": "Data sovereignty",
            "definition": "Data sovereignty is the idea that data are subject to the laws and governance structures within the nation it is collected. The concept of data sovereignty is closely linked with data security, cloud computing, network sovereignty and technological sovereignty.\n\n A common criticism of data sovereignty brought forward by corporate actors is that it impedes and has the potential to destroy processes in cloud computing. Since cloud storage might be dispersed and disseminated in a variety of locations at any given time, it is argued that governance of cloud computing is difficult under data sovereignty laws. For example, data held in the cloud may be illegal in some jurisdictions but legal in others.\n\nAccording to Professor Susan Ariel Aaronson, research professor and director of the Digital Trade and Data Governance Hub at George Washington University, governments are seeking to regulate the commercial use of personal data without enacting clear rules governing public sector use. The hoarding of data by nations or firms may reduce data generativity and the public benefits of data analysis.\n\nWith the rise of cloud computing, many countries have passed various laws around control and storage of data, which all reflects measures of data sovereignty. More than 100 countries have some sort of data sovereignty laws in place. As part of Canada's IT strategy for the years 2016–2020, data localization measures were discussed as a way to uphold citizens' privacy.\n\nWith self-sovereign identity (SSI) the individual identity holders can fully create and control their credentials, although a nation can still issue a digital identity in that paradigm.",
            "url": "https://en.wikipedia.org/wiki/Data_sovereignty",
            "id": 494      
        },
        {
            "name": "Multi-access edge computing (MEC)",
            "definition": "Multi-access edge computing (MEC), formerly mobile edge computing, is an ETSI-defined network architecture concept that enables cloud computing capabilities and an IT service environment at the edge of the cellular network and, more in general at the edge of any network.\n\nThe basic idea behind MEC is that by running applications and performing related processing tasks closer to the cellular customer, network congestion is reduced and applications perform better. MEC technology is designed to be implemented at the cellular base stations or other edge nodes, and enables flexible and rapid deployment of new applications and services for customers. Combining elements of information technology and telecommunications networking, MEC also allows cellular operators to open their radio access network (RAN) to authorized third parties, such as application developers and content providers.\n\nTechnical standards for MEC are being developed by the European Telecommunications Standards Institute.",
            "url": "https://en.wikipedia.org/wiki/Multi-access_edge_computing",
            "id": 495      
        },
        {
            "name": "Usenet",
            "definition": "Usenet is a worldwide distributed discussion system available on computers. It was developed from the general-purpose Unix-to-Unix Copy (UUCP) dial-up network architecture. Tom Truscott and Jim Ellis conceived the idea in 1979, and it was established in 1980. Users read and post messages (called articles or posts, and collectively termed news) to one or more topic categories, known as newsgroups. Usenet resembles a bulletin board system (BBS) in many respects and is the precursor to the Internet forums that have become widely used. Discussions are threaded, as with web forums and BBSs, though posts are stored on the server sequentially.\n\nA major difference between a BBS or web message board and Usenet is the absence of a central server and dedicated administrator or hosting provider. Usenet is distributed among a large, constantly changing set of news servers that store and forward messages to one another via ‘news feeds’. Individual users may read messages from and post to a local (or simply preferred) news server, which can be operated by anyone, and those posts will automatically be forwarded to any other news servers peered with the local one, while the local server will receive any news its peers have that it currently lacks. This results in the automatic proliferation of content posted by any user on any server to any other user subscribed to the same newsgroups on other servers.\n\nUsenet is culturally and historically significant in the networked world, having given rise to, or popularized, many widely recognized concepts and terms such as ‘FAQ’, ‘flame’, ‘sockpuppet’, and ‘spam’. In the early 1990s, shortly before access to the Internet became commonly affordable, Usenet connections via Fidonet's dial-up BBS networks made long-distance or worldwide discussions and other communication widespread, not needing a server, just (local) telephone service.\n\nThe name Usenet comes from the term ‘users network’. The first Usenet group was NET.general, which quickly became net.general. The first commercial spam on Usenet was from immigration attorneys Canter and Siegel advertising green card services. On the Internet, Usenet is transported via the Network News Transfer Protocol (NNTP) on TCP Port 119 for standard, unprotected connections and on TCP port 563 for SSL encrypted connections.",
            "url": "https://en.wikipedia.org/wiki/Usenet",
            "id": 496      
        },
        {
            "name": "Distributed cloud",
            "definition": "A distributed cloud is an architecture where multiple clouds are used to meet compliance needs, performance requirements, or support edge computing while being centrally managed from the public cloud provider.\n\nIn essence, a distributed cloud service is a public cloud that runs in multiple locations, including:\n\n- The public cloud provider’s infrastructure\n- In another cloud provider’s data center\n- On third party or colocation center hardware\n\nAlthough there are multiple locations and geographies involved, all of the cloud services are managed as on from a single control plane that handles the differences and inconsistencies in such a hybrid, multi-cloud environment. This distribution of services enables an organization to meet very specific requirements for response time and performance, regulatory or governance compliance mandate, or other demand requiring cloud infrastructure to be located anywhere other than the cloud provider’s typical availability zones.\n\nThe growth of the internet of things (IoT) and edge computing have been a major driver for distributed cloud deployments. Artificial intelligence (AI) applications that move large amounts of data from edge locations to the cloud require cloud services to be close as possible to edge locations, and moving cloud resources to the edge location itself can greatly increase performance for these applications.\n\nAdditionally, the ever-increasing number of government regulations such as the EU’s GDPR can demand that data be located in specific jurisdictions which may or may not be supported by a given public cloud provider, thus making a distributed cloud a necessity.\n\nBy bringing cloud services closer to a given user, application, or data, distributed clouds can offer reduced latency, lowered or eliminated network congestion and guaranteed quality of service (QoS) for mission critical application and mobile users.",
            "url": "https://www.vmware.com/topics/glossary/content/distributed-cloud.html#:~:text=A%20distributed%20cloud%20is%20an,from%20the%20public%20cloud%20provider.",
            "id": 497      
        },
        {
            "name": "Cybersecurity mesh (CSM)",
            "definition": "A cybersecurity mesh (CSM) is a progressive strategy to protect computer networks from hackers. It ensures that you have more than one defense perimeter to protect the nodes within your network. With cybersecurity mesh, you can protect technological systems managed in isolation, such as perimeter firewalls, network security devices, and security software. CSM helps secure access points and ensures that there are no recorded cases of data breaches, both known and unknown. This allows for the detection of attacks in real-time.\n\nGartner defines cybersecurity mesh architecture as ‘a composable and scalable approach to extending security controls, even to widely distributed assets. Its flexibility is especially suitable for increasingly modular approaches consistent with hybrid multicloud architectures. CSMA enables a more composable, flexible and resilient security ecosystem. Rather than every security tool running in a silo, a cybersecurity mesh enables tools to interoperate through several supportive layers, such as consolidated policy management, security intelligence and identity fabric.’",
            "url": "https://www.techtarget.com/searchsecurity/tip/What-is-cybersecurity-mesh-and-how-can-it-help-you",
            "id": 498      
        },
        {
            "name": "Total Experience (TX)",
            "definition": "The term Total Experience (abbreviation TX) describes all aspects of the impressions and the experience of all users, in the context of an organization. In particular, this includes the previously separate disciplines of customer experience (CX), employee experience (EX), user experience (UX) and multi-experience (MX)",
            "url": "https://www.walkme.com/glossary/total-experience/",
            "id": 499      
        },
        {
            "name": "Decentralized autonomous organization (DAO)",
            "definition": "A decentralized autonomous organization (DAO), sometimes called a decentralized autonomous corporation (DAC), is an organization constructed by rules encoded as a computer program that is often transparent, controlled by the organization's members and not influenced by a central government. In general terms, DAOs are member-owned communities without centralized leadership. A DAO's financial transaction records and program rules are maintained on a blockchain. The precise legal status of this type of business organization is unclear.\n\nA well-known example, intended for venture capital funding, was The DAO, which amassed 3.6 million ether (ETH)—Ethereum's mining reward—then worth more than US$70 million in May 2016, and was hacked and drained of US$50 million in cryptocurrency weeks later. The hack was reversed in the following weeks, and the money restored, via a hard fork of the Ethereum blockchain. Most Ethereum miners and clients switched to the new fork while the original chain became Ethereum Classic.",
            "url": "https://en.wikipedia.org/wiki/Decentralized_autonomous_organization",
            "id": 500      
        },
        {
            "name": "Artificial general intelligence (AGI)",
            "definition": "Artificial general intelligence (AGI) is the ability of an intelligent agent to understand or learn any intellectual task that a human being can. It is a primary goal of some artificial intelligence research and a common topic in science fiction and futures studies. AGI can also be referred to as strong AI, full AI, or general intelligent action, although some academic sources reserve the term ‘strong AI’ for computer programs that experience sentience or consciousness.\n\nIn contrast to strong AI, weak AI or ‘narrow AI’ is not intended to have general cognitive abilities; rather, weak AI is any program that is designed to solve exactly one problem. (Academic sources reserve ‘weak AI’ for programs that do not experience consciousness or do not have a mind in the same sense people do.) A 2020 survey identified 72 active AGI R&D projects spread across 37 countries.",
            "url": "https://en.wikipedia.org/wiki/Artificial_general_intelligence",
            "id": 501     
        },
        {
            "name": "Superintelligence",
            "definition": "A superintelligence is a hypothetical agent that possesses intelligence far surpassing that of the brightest and most gifted human minds. ‘Superintelligence’ may also refer to a property of problem-solving systems (e.g., superintelligent language translators or engineering assistants) whether or not these high-level intellectual competencies are embodied in agents that act in the world. A superintelligence may or may not be created by an intelligence explosion and associated with a technological singularity. University of Oxford philosopher Nick Bostrom defines superintelligence as ‘any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest’. \n\nTechnological researchers disagree about how likely present-day human intelligence is to be surpassed. Some argue that advances in artificial intelligence (AI) will probably result in general reasoning systems that lack human cognitive limitations. Others believe that humans will evolve or directly modify their biology so as to achieve radically greater intelligence. A number of futures studies scenarios combine elements from both of these possibilities, suggesting that humans are likely to interface with computers, or upload their minds to computers, in a way that enables substantial intelligence amplification.\n\nSome researchers believe that superintelligence will likely follow shortly after the development of artificial general intelligence. The first generally intelligent machines are likely to immediately hold an enormous advantage in at least some forms of mental capability, including the capacity of perfect recall, a vastly superior knowledge base, and the ability to multitask in ways not possible to biological entities. This may give them the opportunity to—either as a single being or as a new species—become much more powerful than humans, and to displace them.\n\nA number of scientists and forecasters argue for prioritizing early research into the possible benefits and risks of human and machine cognitive enhancement, because of the potential social impact of such technologies in both raising the level of collective human intelligence and in intelligently ushering the age of super intelligence as a whole.",
            "url": "https://en.wikipedia.org/wiki/Superintelligence",
            "id": 502    
        },
        {
            "name": "Human Level Machine Intelligence (HLMI)",
            "definition": "Human-Level Machine Intelligence (HLMI), also known as Human-Level Artificial intelligence, refers to computer systems that can operate with the intelligence of an average human being. These programs can complete tasks or make decisions as successfully as the average human can.",
            "url": "https://arxiv.org/abs/2108.03793",
            "id": 503     
        },
        {
            "name": "Whole brain emulation (WBE)",
            "definition": "Mind uploading, also known as whole brain emulation (WBE), is the theoretical futuristic process of scanning a physical structure of the brain accurately enough to create an emulation of the mental state (including long-term memory and ‘self’) and transferring or copying it to a computer in a digital form. The computer would then run a simulation of the brain's information processing, such that it would respond in essentially the same way as the original brain and experience having a sentient conscious mind.",
            "url": "https://en.wikipedia.org/wiki/Mind_uploading",
            "id": 504     
        },
        {
            "name": "Perceptual control theory (PCT)",
            "definition": "Perceptual control theory (PCT) is a model of behavior based on the properties of negative feedback control loops. A control loop maintains a sensed variable at or near a reference value by means of the effects of its outputs upon that variable, as mediated by physical properties of the environment. In engineering control theory, reference values are set by a user outside the system. An example is a thermostat. In a living organism, reference values for controlled perceptual variables are endogenously maintained. Biological homeostasis and reflexes are simple, low-level examples.\n\nThe discovery of mathematical principles of control introduced a way to model a negative feedback loop closed through the environment (circular causation), which differs fundamentally from theories of behaviorism and cognitive psychology which model stimuli as causes of behavior (linear causation). PCT research is published in experimental psychology, neuroscience, ethology, anthropology, linguistics, sociology, robotics, developmental psychology, organizational psychology and management, and a number of other fields. PCT has been applied to design and administration of educational systems, and has led to a psychotherapy called the method of levels.",
            "url": "https://en.wikipedia.org/wiki/Perceptual_control_theory",
            "id": 505     
        },
        {
            "name": "Reinforcement learning",
            "definition": "Reinforcement learning (RL) is an area of machine learning concerned with how intelligent agents ought to take actions in an environment in order to maximize the notion of cumulative reward. Reinforcement learning is one of three basic machine learning paradigms, alongside supervised learning and unsupervised learning.\n\nReinforcement learning differs from supervised learning in not needing labelled input/output pairs be presented, and in not needing sub-optimal actions to be explicitly corrected. Instead the focus is on finding a balance between exploration (of uncharted territory) and exploitation (of current knowledge). Partially supervised RL algorithms can combine the advantages of supervised and RL algorithms.",
            "url": "https://en.wikipedia.org/wiki/Reinforcement_learning",
            "id": 506     
        },
        {
            "name": "Neuromorphic",
            "definition": "Neuromorphic engineering, also known as neuromorphic computing, is the use of very-large-scale integration (VLSI) systems containing electronic analog circuits to mimic neuro-biological architectures present in the nervous system. A neuromorphic computer/chip is any device that uses physical artificial neurons (made from silicon) to do computations. In recent times, the term neuromorphic has been used to describe analog, digital, mixed-mode analog/digital VLSI, and software systems that implement models of neural systems (for perception, motor control, or multisensory integration). The implementation of neuromorphic computing on the hardware level can be realized by oxide-based memristors, spintronic memories, threshold switches, and transistors. Training software-based neuromorphic systems of spiking neural networks can be achieved using error backpropagation, e.g., using Python based frameworks such as snnTorch, or using canonical learning rules from the biological learning literature, e.g., using BindsNet.\n\nA key aspect of neuromorphic engineering is understanding how the morphology of individual neurons, circuits, applications, and overall architectures creates desirable computations, affects how information is represented, influences robustness to damage, incorporates learning and development, adapts to local change (plasticity), and facilitates evolutionary change.\n\nNeuromorphic engineering is an interdisciplinary subject that takes inspiration from biology, physics, mathematics, computer science, and electronic engineering to design artificial neural systems, such as vision systems, head-eye systems, auditory processors, and autonomous robots, whose physical architecture and design principles are based on those of biological nervous systems. It was developed by Carver Mead in the late 1980s.",
            "url": "https://en.wikipedia.org/wiki/Neuromorphic_engineering",
            "id": 507     
        },
        {
            "name": "Seed AI",
            "definition": "Seed AI is a hypothesized type of strong artificial intelligence capable of recursive self-improvement. Having improved itself it would become better at improving itself, potentially leading to an exponential increase in intelligence. No such AI currently exists, but researchers are working to make seed AI a reality.\n\nModern compilers optimize for efficiency and raw speed, but this is not sufficient for the sort of open-ended recursive self-enhancement needed to create superintelligence, as a true seed AI would need to be able to do. Existing optimizers can transform code into a functionally equivalent, more efficient form, but cannot identify the intent of an algorithm and rewrite it for more effective results. The optimized version of a given compiler may compile faster, but it cannot compile better. That is, an optimized version of a compiler will never spot new optimization tricks that earlier versions failed to see or innovate new ways of improving its own program. Seed AI must be able to understand the purpose behind the various elements of its design, and design entirely new modules that will make it genuinely more intelligent and more effective in fulfilling its purpose.\n\nCreating seed AI is the goal of several organizations. The Singularity Institute for Artificial Intelligence is the most prominent of those explicitly working to create seed AI. Others include the Artificial General Intelligence Research Institute, creator of the Novamente AI engine, and Adaptive Artificial Intelligence Incorporated.",
            "url": "https://towardsdatascience.com/seed-ai-history-philosophy-and-state-of-the-art-22b5294b21b5",
            "id": 508     
        },
        {
            "name": "Emulator",
            "definition": "In computing, an emulator is hardware or software that enables one computer system (called the host) to behave like another computer system (called the guest). An emulator typically enables the host system to run software or use peripheral devices designed for the guest system. Emulation refers to the ability of a computer program in an electronic device to emulate (or imitate) another program or device.\n\nMany printers, for example, are designed to emulate HP LaserJet printers because so much software is written for HP printers. If a non-HP printer emulates an HP printer, any software written for a real HP printer will also run in the non-HP printer emulation and produce equivalent printing. Since at least the 1990s, many video game enthusiasts and hobbyists have used emulators to play classic arcade games from the 1980s using the games' original 1980s machine code and data, which is interpreted by a current-era system, and to emulate old video game consoles.\n\nA hardware emulator is an emulator which takes the form of a hardware device. Examples include the DOS-compatible card installed in some 1990s-era Macintosh computers, such as the Centris 610 or Performa 630, that allowed them to run personal computer (PC) software programs and field-programmable gate array-based hardware emulators. The Church-Turing thesis implies that theoretically, any operating environment can be emulated within any other environment, assuming memory limitations are ignored. However, in practice, it can be quite difficult, particularly when the exact behavior of the system to be emulated is not documented and has to be deduced through reverse engineering. It also says nothing about timing constraints; if the emulator does not perform as quickly as it did using the original hardware, the software inside the emulation may run much more slowly (possibly triggering timer interrupts that alter behavior).",
            "url": "https://en.wikipedia.org/wiki/Emulator",
            "id": 509     
        },
        {
            "name": "Cyborg",
            "definition": "A cyborg—a portmanteau of cybernetic and organism—is a being with both organic and biomechatronic body parts. The term was coined in 1960 by Manfred Clynes and Nathan S. Kline. Cyborgization is the enhancement of a biological being with mechanical or non-genetically delivered biological devices or capabilities. It includes organ or limb replacements, internal electronics, advanced nanomachines, and enhanced or additional capabilities, limbs, or senses.",
            "url": "https://en.wikipedia.org/wiki/Cyborg",
            "id": 510     
        },
        {
            "name": "Collective intelligence",
            "definition": "Collective intelligence (CI) is shared or group intelligence (GI) that emerges from the collaboration, collective efforts, and competition of many individuals and appears in consensus decision making. The term appears in sociobiology, political science and in context of mass peer review and crowdsourcing applications. It may involve consensus, social capital and formalisms such as voting systems, social media and other means of quantifying mass activity. Collective IQ is a measure of collective intelligence, although it is often used interchangeably with the term collective intelligence. Collective intelligence has also been attributed to bacteria and animals.\n\nIt can be understood as an emergent property from the synergies among: 1) data-information-knowledge; 2) software-hardware; and 3) individuals (those with new insights as well as recognized authorities) that continually learns from feedback to produce just-in-time knowledge for better decisions than these three elements acting alone; or more narrowly as an emergent property between people and ways of processing information. This notion of collective intelligence is referred to as ‘symbiotic intelligence’ by Norman Lee Johnson. The concept is used in sociology, business, computer science and mass communications: it also appears in science fiction. Pierre Lévy defines collective intelligence as, ‘It is a form of universally distributed intelligence, constantly enhanced, coordinated in real time, and resulting in the effective mobilization of skills. I'll add the following indispensable characteristic to this definition: The basis and goal of collective intelligence is mutual recognition and enrichment of individuals rather than the cult of fetishized or hypostatized communities.’ According to researchers Pierre Lévy and Derrick de Kerckhove, it refers to capacity of networked ICTs (Information communication technologies) to enhance the collective pool of social knowledge by simultaneously expanding the extent of human interactions. A broader definition was provided by Geoff Mulgan in a series of lectures and reports from 2006 onwards and in the book Big Mind which proposed a framework for analysing any thinking system, including both human and machine intelligence, in terms of functional elements (observation, prediction, creativity, judgement etc.), learning loops and forms of organisation. The aim was to provide a way to diagnose, and improve, the collective intelligence of a city, business, NGO or parliament.\n\nCollective intelligence strongly contributes to the shift of knowledge and power from the individual to the collective. According to Eric S. Raymond (1998) and JC Herz (2005), open source intelligence will eventually generate superior outcomes to knowledge generated by proprietary software developed within corporations (Flew 2008). Media theorist Henry Jenkins sees collective intelligence as an 'alternative source of media power', related to convergence culture. He draws attention to education and the way people are learning to participate in knowledge cultures outside formal learning settings. Henry Jenkins criticizes schools which promote 'autonomous problem solvers and self-contained learners' while remaining hostile to learning through the means of collective intelligence. Both Pierre Lévy (2007) and Henry Jenkins (2008) support the claim that collective intelligence is important for democratization, as it is interlinked with knowledge-based culture and sustained by collective idea sharing, and thus contributes to a better understanding of diverse society.",
            "url": "https://en.wikipedia.org/wiki/Collective_intelligence",
            "id": 511     
        },
        {
            "name": "Technological singularity",
            "definition": "The technological singularity—or simply the singularity—is a hypothetical point in time at which technological growth will become radically faster and uncontrollable, resulting in unforeseeable changes to human civilization. According to the most popular version of the singularity hypothesis, I.J. Good's intelligence explosion model, an upgradable intelligent agent will eventually enter a 'runaway reaction' of self-improvement cycles, each new and more intelligent generation appearing more and more rapidly, causing an ‘explosion’ in intelligence and resulting in a powerful superintelligence that qualitatively far surpasses all human intelligence.\n\nThe first person to use the concept of a ‘singularity’ in the technological context was John von Neumann. Stanislaw Ulam reports a discussion with von Neumann ‘centered on the accelerating progress of technology and changes in the mode of human life, which gives the appearance of approaching some essential singularity in the history of the race beyond which human affairs, as we know them, could not continue’. Subsequent authors have echoed this viewpoint.\n\nThe concept and the term ‘singularity’ were popularized by Vernor Vinge in his 1993 essay The Coming Technological Singularity, in which he wrote that it would signal the end of the human era, as the new superintelligence would continue to upgrade itself and would advance technologically at an incomprehensible rate. He wrote that he would be surprised if it occurred before 2005 or after 2030.\n\nScientists, such as Stephen Hawking, have expressed concern that full artificial intelligence (AI) could result in human extinction. The consequences of the singularity and its potential benefit or harm to the human race have been intensely debated.",
            "url": "https://en.wikipedia.org/wiki/Technological_singularity",
            "id": 512     
        },
        {
            "name": "traceroute",
            "definition": "In computing, ‘traceroute’ and ‘tracert’ are computer network diagnostic commands for displaying possible routes (paths) and measuring transit delays of packets across an Internet Protocol (IP) network. The history of the route is recorded as the round-trip times of the packets received from each successive host (remote node) in the route (path); the sum of the mean times in each hop is a measure of the total time spent to establish the connection. Traceroute proceeds unless all (usually three) sent packets are lost more than twice; then the connection is lost and the route cannot be evaluated. Ping, on the other hand, only computes the final round-trip times from the destination point.\n\nFor Internet Protocol Version 6 (IPv6) the tool sometimes has the name traceroute6 and tracert6.",
            "url": "https://en.wikipedia.org/wiki/Traceroute",
            "id": 513     
        },
        {
            "name": "SOAP",
            "definition": "SOAP (formerly a backronym for Simple Object Access Protocol) is a messaging protocol specification for exchanging structured information in the implementation of web services in computer networks. It uses XML Information Set for its message format, and relies on application layer protocols, most often Hypertext Transfer Protocol (HTTP), although some legacy systems communicate over Simple Mail Transfer Protocol (SMTP), for message negotiation and transmission.\n\nSOAP allows developers to invoke processes running on different operating systems (such as Windows, macOS, and Linux) to authenticate, authorize, and communicate using Extensible Markup Language (XML). Since Web protocols like HTTP are installed and running on practically all operating systems, SOAP allows clients to invoke web services and receive responses independent of language and platforms.",
            "url": "https://en.wikipedia.org/wiki/SOAP",
            "id": 514     
        },
        {
            "name": "Webhook",
            "definition": "A webhook in web development is a method of augmenting or altering the behavior of a web page or web application with custom callbacks. These callbacks may be maintained, modified, and managed by third-party users and developers who may not necessarily be affiliated with the originating website or application. The term 'webhook' was coined by Jeff Lindsay in 2007 from the computer programming term hook.\n\nWebhooks are ‘user-defined HTTP callbacks’. They are usually triggered by some event, such as pushing code to a repository or a comment being posted to a blog. When that event occurs, the source site makes an HTTP request to the URL configured for the webhook. Users can configure them to cause events on one site to invoke behavior on another.\n\nCommon uses are to trigger builds with continuous integration systems or to notify bug tracking systems. Because webhooks use HTTP, they can be integrated into web services without adding new infrastructure. The request is done as a HTTP POST request and the format is usually JSON.",
            "url": "https://en.wikipedia.org/wiki/Webhook",
            "id": 515     
        },
        {
            "name": "Document Object Model (DOM)",
            "definition": "The Document Object Model (DOM) is a cross-platform and language-independent interface that treats an XML or HTML document as a tree structure wherein each node is an object representing a part of the document. The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects. DOM methods allow programmatic access to the tree; with them one can change the structure, style or content of a document. Nodes can have event handlers attached to them. Once an event is triggered, the event handlers get executed.",
            "url": "https://en.wikipedia.org/wiki/Document_Object_Model",
            "id": 516     
        },
        {
            "name": "LAMP",
            "definition": "LAMP (Linux, Apache, MySQL, PHP/Perl/Python) is an acronym denoting one of the most common software stacks for many of the web's most popular applications. However, LAMP now refers to a generic software stack model and its components are largely interchangeable.\n\nEach letter in the acronym stands for one of its four open-source building blocks:\n\n- Linux for the operating system\n- Apache HTTP Server\n- MySQL for the relational database management system\n- PHP, Perl, or Python programming language\n\nThe components of the LAMP stack are present in the software repositories of most Linux distributions.",
            "url": "https://en.wikipedia.org/wiki/LAMP_(software_bundle)",
            "id": 517     
        },
        {
            "name": "MEAN",
            "definition": "MEAN (MongoDB, Express.js, AngularJS (or Angular), and Node.js) is a free and open-source JavaScript software stack for building dynamic web sites and web applications. A variation known as MERN replaces Angular with React.\n\nBecause all components of the MEAN stack support programs that are written in JavaScript, MEAN applications can be written in one language for both server-side and client-side execution environments.\n\nThough often compared directly to other popular web development stacks such as the LAMP stack, the components of the MEAN stack are higher-level including a web application presentation layer and not including an operating system layer.",
            "url": "https://en.wikipedia.org/wiki/MEAN_(solution_stack)",
            "id": 518     
        },
        {
            "name": "Header",
            "definition": "In information technology, header refers to supplemental data placed at the beginning of a block of data being stored or transmitted. In data transmission, the data following the header is sometimes called the payload or body. It is vital that header composition follows a clear and unambiguous specification or format, to allow for parsing.",
            "url": "https://en.wikipedia.org/wiki/Header_(computing)",
            "id": 519     
        },
        {
            "name": "Northbound/Southbound interfaces",
            "definition": "In computer networking and computer architecture, a northbound interface of a component is an interface that allows the component to communicate with a higher level component, using the latter component's southbound interface. The northbound interface conceptualizes the lower level details (e.g., data or functions) used by, or in, the component, allowing the component to interface with higher level layers.",
            "url": "https://en.wikipedia.org/wiki/Northbound_interface",
            "id": 520     
        },
        {
            "name": "Network functions virtualization (NFV)",
            "definition": "Network functions virtualization (NFV) is a network architecture concept that leverages the IT virtualization technologies to virtualize entire classes of network node functions into building blocks that may connect, or chain together, to create and deliver communication services.\n\nNFV relies upon traditional server-virtualization techniques such as those used in enterprise IT. A virtualized network function, or VNF, is implemented within one or more virtual machines or containers running different software and processes, on top of commercial off the shelf (COTS) high-volume servers, switches and storage devices, or even cloud computing infrastructure, instead of having custom hardware appliances for each network function thereby avoiding vendor lock-in.",
            "url": "https://en.wikipedia.org/wiki/Network_function_virtualization",
            "id": 521     
        },
        {
            "name": "Inter-process communication (IPC)",
            "definition": "In computer science, inter-process communication or interprocess communication (IPC) refers specifically to the mechanisms an operating system provides to allow the processes to manage shared data. Typically, applications can use IPC, categorized as clients and servers, where the client requests data and the server responds to client requests. Many applications are both clients and servers, as commonly seen in distributed computing.\n\nIPC is very important to the design process for microkernels and nanokernels, which reduce the number of functionalities provided by the kernel. Those functionalities are then obtained by communicating with servers via IPC, leading to a large increase in communication when compared to a regular monolithic kernel. IPC interfaces generally encompass variable analytic framework structures. These processes ensure compatibility between the multi-vector protocols upon which IPC models rely.\n\nAn IPC mechanism is either synchronous or asynchronous. Synchronization primitives may be used to have synchronous behavior with an asynchronous IPC mechanism.",
            "url": "https://en.wikipedia.org/wiki/Inter-process_communication",
            "id": 522     
        },
        {
            "name": "Cartesian coordinate system",
            "definition": "A Cartesian coordinate system in a plane is a coordinate system that specifies each point uniquely by a pair of numerical coordinates, which are the signed distances to the point from two fixed perpendicular oriented lines, measured in the same unit of length. Each reference coordinate line is called a coordinate axis or just axis (plural axes) of the system, and the point where they meet is its origin, at ordered pair (0, 0). The coordinates can also be defined as the positions of the perpendicular projections of the point onto the two axes, expressed as signed distances from the origin.\n\nOne can use the same principle to specify the position of any point in three-dimensional space by three Cartesian coordinates, its signed distances to three mutually perpendicular planes (or, equivalently, by its perpendicular projection onto three mutually perpendicular lines). In general, n Cartesian coordinates (an element of real n-space) specify the point in an n-dimensional Euclidean space for any dimension n. These coordinates are equal, up to sign, to distances from the point to n mutually perpendicular hyperplanes.\n\nThe invention of Cartesian coordinates in the 17th century by René Descartes (Latinized name: Cartesius) revolutionized mathematics by providing the first systematic link between Euclidean geometry and algebra. Using the Cartesian coordinate system, geometric shapes (such as curves) can be described by Cartesian equations: algebraic equations involving the coordinates of the points lying on the shape. For example, a circle of radius 2, centered at the origin of the plane, may be described as the set of all points whose coordinates x and y satisfy the equation x2 + y2 = 4.\n\nCartesian coordinates are the foundation of analytic geometry, and provide enlightening geometric interpretations for many other branches of mathematics, such as linear algebra, complex analysis, differential geometry, multivariate calculus, group theory and more. A familiar example is the concept of the graph of a function. Cartesian coordinates are also essential tools for most applied disciplines that deal with geometry, including astronomy, physics, engineering and many more. They are the most common coordinate system used in computer graphics, computer-aided geometric design and other geometry-related data processing.",
            "url": "https://en.wikipedia.org/wiki/Cartesian_coordinate_system",
            "id": 523     
        },
        {
            "name": "CAP theorem",
            "definition": "In theoretical computer science, the CAP theorem, also named Brewer's theorem after computer scientist Eric Brewer, states that any distributed data store can provide only two of the following three guarantees:\n\n1. Consistency: Every read receives the most recent write or an error.\n\n2. Availability: Every request receives a (non-error) response, without the guarantee that it contains the most recent write.\n\n3. Partition tolerance: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.\n\nWhen a network partition failure happens, it must be decided whether A) cancel the operation and thus decrease the availability but ensure consistency or to B) proceed with the operation and thus provide availability but risk inconsistency.\n\nThus, if there is a network partition, one has to choose between consistency and availability. Note that consistency as defined in the CAP theorem is quite different from the consistency guaranteed in ACID database transactions.\n\nEric Brewer argues that the often-used 'two out of three' concept can be somewhat misleading because system designers need only to sacrifice consistency or availability in the presence of partitions, but that in many systems partitions are rare.",
            "url": "https://en.wikipedia.org/wiki/CAP_theorem",
            "id": 524     
        },
        {
            "name": "Hypermedia",
            "definition": "Hypermedia, an extension of the term hypertext, is a nonlinear medium of information that includes graphics, audio, video, plain text and hyperlinks. This designation contrasts with the broader term multimedia, which may include non-interactive linear presentations as well as hypermedia. It is also related to the field of electronic literature. The term was first used in a 1965 article written by Ted Nelson.\n\nThe World Wide Web is a classic example of hypermedia to access web content, whereas a non-interactive cinema presentation is an example of standard multimedia due to the absence of hyperlinks.\n\nThe first hypermedia work was, arguably, the Aspen Movie Map. Bill Atkinson's HyperCard popularized hypermedia writing, while a variety of literary hypertext and hypertext works, fiction and non-fiction, demonstrated the promise of links. Most modern hypermedia is delivered via electronic pages from a variety of systems including media players, web browsers, and stand-alone applications (i.e., software that does not require network access). Audio hypermedia is emerging with voice command devices and voice browsing.",
            "url": "https://en.wikipedia.org/wiki/Hypermedia",
            "id": 525     
        },
        {
            "name": "OpenFlow",
            "definition": "OpenFlow is a communications protocol that gives access to the forwarding plane of a network switch or router over the network.\n\nOpenFlow enables network controllers to determine the path of network packets across a network of switches. The controllers are distinct from the switches. This separation of the control from the forwarding allows for more sophisticated traffic management than is feasible using access control lists (ACLs) and routing protocols. Also, OpenFlow allows switches from different vendors — often each with their own proprietary interfaces and scripting languages — to be managed remotely using a single, open protocol. The protocol's inventors consider OpenFlow an enabler of software-defined networking (SDN).",
            "url": "https://en.wikipedia.org/wiki/OpenFlow",
            "id": 526     
        },
        {
            "name": "Interface to the Routing System (i2rs)",
            "definition": "According to the final charter of its IETF working group, Interface to the Routing System (abbreviated ‘i2rs’ or ‘I2RS’) facilitates real-time or event driven interaction with the routing system through a collection of protocol-based control or management interfaces. These allow information, policies, and operational parameters to be injected into and retrieved (as read or by notification) from the routing system while retaining data consistency and coherency across the routers and routing infrastructure, and among multiple interactions with the routing system. The I2RS interfaces will co-exist with existing configuration and management systems and interfaces.\n\nIt is envisioned that users of the I2RS interfaces will be management applications, network controllers, and user applications that makespecific demands on the network.\n\nThe I2RS working group works to develop a high-level architecture that describes the basic building-blocks necessary to enable the specific usecases, and that will lead to an understanding of the abstract informational models and requirements for encodings and protocols for the I2RS interfaces. Small and well-scoped use cases are critical toconstrain the scope of the work and achieve sufficient focus for the working group to deliver successful outcomes. Initial work within the working group will be limited to a single administrative domain.",
            "url": "https://datatracker.ietf.org/wg/i2rs/about/",
            "id": 527     
        },
        {
            "name": "Routing information base (RIB)",
            "definition": "In computer networking, a routing table, or routing information base (RIB), is a data table stored in a router or a network host that lists the routes to particular network destinations, and in some cases, metrics (distances) associated with those routes. The routing table contains information about the topology of the network immediately around it.\n\nThe construction of routing tables is the primary goal of routing protocols. Static routes are entries made in a routing table by non-automatic means and which are fixed rather than being the result of routing protocols and associated network topology-discovery procedures.",
            "url": "https://en.wikipedia.org/wiki/Routing_table",
            "id": 528     
        },
        {
            "name": "Path Computation Element (PCE)",
            "definition": "In computer networks, a Path Computation Element (PCE) is a system component, application, or network node that is capable of determining and finding a suitable route for conveying data between a source and a destination.Routing can be subject to a set of constraints, such as quality of service (QoS), policy, or price. Constraint-based path computation is a strategic component of traffic engineering in MPLS, GMPLS and Segment Routing networks. It is used to determine the path through the network that traffic should follow, and provides the route for each Label Switched Path (LSP) that is set up.\n\nPath computation has previously been performed either in a management system or at the head end of each LSP. But path computation in large, multi-domain networks may be very complex and may require more computational power and network information than is typically available at a network element, yet may still need to be more dynamic than can be provided by a management system.\n\nThus, a PCE is an entity capable of computing paths for a single or set of services. A PCE might be a network node, network management station, or dedicated computational platform that is resource-aware and has the ability to consider multiple constraints for sophisticated path computation. PCE applications compute label switched paths for MPLS and GMPLS traffic engineering. The various components of the PCE architecture are in the process of being standardized by the IETF's PCE Working Group.\n\nPCE represents a vision of networks that separates route computations from the signaling of end-to-end connections and from actual packet forwarding.",
            "url": "https://en.wikipedia.org/wiki/Path_computation_element",
            "id": 529     
        },
        {
            "name": "Bidirectional Forwarding Detection (BFD)",
            "definition": "Bidirectional Forwarding Detection (BFD) is a network protocol that is used to detect faults between two routers or switches connected by a link. It provides low-overhead detection of faults even on physical media that doesn't support failure detection of any kind, such as Ethernet, virtual circuits, tunnels and MPLS Label Switched Paths.\n\nBFD establishes a session between two endpoints over a particular link. If more than one link exists between two systems, multiple BFD sessions may be established to monitor each one of them. The session is established with a three-way handshake, and is torn down the same way. Authentication may be enabled on the session. A choice of simple password, MD5 or SHA1 authentication is available.",
            "url": "https://en.wikipedia.org/wiki/Bidirectional_Forwarding_Detection",
            "id": 530     
        },
        {
            "name": "Intent-based networking (IBN)",
            "definition": "Intent-based networking (IBN) is an emerging technology concept that aims to apply a deeper level of intelligence and intended state to replace the manual processes of configuring networks and reacting to network issues. Instead, network administrators define an outcome or business objective—the intent—and the network’s software figures out how to achieve that goal, thanks to artificial intelligence and machine learning.\n\nIBN systems not only automate time-consuming tasks and provide real-time visibility into a network’s activity to validate a given intent, they also predict potential deviations to that intent, and prescribe the action required to ensure that intent. This greater intelligence makes the network faster and more agile, and reduces errors.",
            "url": "https://www.vmware.com/topics/glossary/content/intent-based-networking.html",
            "id": 531     
        },
        {
            "name": "Web Services Description Language (WSDL)",
            "definition": "The Web Services Description Language (WSDL) is an XML-based interface description language that is used for describing the functionality offered by a web service. The acronym is also used for any specific WSDL description of a web service (also referred to as a WSDL file), which provides a machine-readable description of how the service can be called, what parameters it expects, and what data structures it returns. Therefore, its purpose is roughly similar to that of a type signature in a programming language.\n\nThe latest version of WSDL, which became a W3C recommendation in 2007, is WSDL 2.0. The meaning of the acronym has changed from version 1.1 where the ‘D’ stood for ‘Definition’.",
            "url": "https://en.wikipedia.org/wiki/Web_Services_Description_Language",
            "id": 532     
        },
        {
            "name": "Message authentication code",
            "definition": "In cryptography, a message authentication code (MAC), sometimes known as a tag, is a short piece of information used for authenticating a message. In other words, to confirm that the message came from the stated sender (its authenticity) and has not been changed. The MAC value protects a message's data integrity, as well as its authenticity, by allowing verifiers (who also possess the secret key) to detect any changes to the message content.\n\nThe term message integrity code (MIC) is frequently substituted for the term MAC, especially in communications to distinguish it from the use of the latter as media access control address (MAC address). However, some authors use MIC to refer to a message digest, which aims only to uniquely but opaquely identify a single message. RFC 4949 recommends avoiding the term message integrity code (MIC), and instead using checksum, error detection code, hash, keyed hash, message authentication code, or protected checksum.\n\nInformally, a message authentication code system consists of three algorithms:\n\n1. A key generation algorithm selects a key from the key space uniformly at random.\n2. A signing algorithm efficiently returns a tag given the key and the message.\n3. A verifying algorithm efficiently verifies the authenticity of the message given the key and the tag. That is, return accepted when the message and tag are not tampered with or forged, and otherwise return rejected.",
            "url": "https://en.wikipedia.org/wiki/Message_authentication_code",
            "id": 533     
        },
        {
            "name": "Authenticated Encryption (AE) and Authenticated Encryption with Associated Data (AEAD)",
            "definition": "Authenticated Encryption (AE) and Authenticated Encryption with Associated Data (AEAD) are forms of encryption which simultaneously assure the confidentiality and authenticity of data.\n\nA typical programming interface for an AE implementation provides encryption via input (plaintext, key, and optionally a header in plaintext) that will not be encrypted, but will be covered by authenticity protection, with output in the form of ciphertext and authentication tag (message authentication code or MAC). Decryption is provided through input comprising ciphertext, key, authentication tag, and optionally a header (if used during the encryption), with an output of plaintext, or an error if the authentication tag does not match the supplied ciphertext or header. The header part is intended to provide authenticity and integrity protection for networking or storage metadata for which confidentiality is unnecessary, but authenticity is desired.\n\nAEAD is a variant of AE that allows a recipient to check the integrity of both the encrypted and unencrypted information in a message. AEAD binds associated data (AD) to the ciphertext and to the context where it is supposed to appear so that attempts to ‘cut-and-paste’ a valid ciphertext into a different context are detected and rejected. It is required, for example, by network packets or frames where the header needs visibility, the payload needs confidentiality, and both need integrity and authenticity.",
            "url": "https://en.wikipedia.org/wiki/Authenticated_encryption",
            "id": 534     
        },
        {
            "name": "Nonce value",
            "definition": "In cryptography, a nonce (number once) is an arbitrary number that can be used just once in a cryptographic communication. It is often a random or pseudo-random number issued in an authentication protocol to ensure that old communications cannot be reused in replay attacks. They can also be useful as initialization vectors and in cryptographic hash functions.",
            "url": "https://en.wikipedia.org/wiki/Cryptographic_nonce",
            "id": 535     
        },
        {
            "name": "QUIC",
            "definition": "QUIC (pronounced ‘quick’) is a general-purpose transport layer network protocol initially designed by Jim Roskind at Google, implemented, and deployed in 2012, announced publicly in 2013 as experimentation broadened, and described at an IETF meeting. QUIC is used by more than half of all connections from the Chrome web browser to Google's servers. Microsoft Edge (a derivative of the open-source Chromium browser) and Firefox support it. Safari implements the protocol, however it is not enabled by default.\n\nAlthough its name was initially proposed as the acronym for ‘Quick UDP Internet Connections’, IETF's use of the word QUIC is not an acronym; it is simply the name of the protocol. QUIC improves performance of connection-oriented web applications that are currently using TCP. It does this by establishing a number of multiplexed connections between two endpoints using User Datagram Protocol (UDP), and is designed to obsolete TCP at the transport layer for many applications, thus earning the protocol the occasional nickname ‘TCP/2’.\n\nQUIC works hand-in-hand with HTTP/2's multiplexed connections, allowing multiple streams of data to reach all the endpoints independently, and hence independent of packet losses involving other streams. In contrast, HTTP/2 hosted on Transmission Control Protocol (TCP) can suffer head-of-line-blocking delays of all multiplexed streams if any of the TCP packets are delayed or lost.\n\nQUIC's secondary goals include reduced connection and transport latency, and bandwidth estimation in each direction to avoid congestion. It also moves congestion control algorithms into the user space at both endpoints, rather than the kernel space, which it is claimed will allow these algorithms to improve more rapidly. Additionally, the protocol can be extended with forward error correction (FEC) to further improve performance when errors are expected, and this is seen as the next step in the protocol's evolution.",
            "url": "https://en.wikipedia.org/wiki/QUIC",
            "id": 536     
        },
        {
            "name": "XML",
            "definition": "Extensible Markup Language (XML) is a markup language and file format for storing, transmitting, and reconstructing arbitrary data. It defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. The World Wide Web Consortium's XML 1.0 Specification of 1998 and several other related specifications—all of them free open standards—define XML.\n\nThe design goals of XML emphasize simplicity, generality, and usability across the Internet. It is a textual data format with strong support via Unicode for different human languages. Although the design of XML focuses on documents, the language is widely used for the representation of arbitrary data structures such as those used in web services.\n\nSeveral schema systems exist to aid in the definition of XML-based languages, while programmers have developed many application programming interfaces (APIs) to aid the processing of XML data.",
            "url": "https://en.wikipedia.org/wiki/XML",
            "id": 537     
        },
        {
            "name": "XSD",
            "definition": "XSD (XML Schema Definition), a recommendation of the World Wide Web Consortium (W3C), specifies how to formally describe the elements in an Extensible Markup Language (XML) document. It can be used by programmers to verify each piece of item content in a document, to assure it adheres to the description of the element it is placed in.\n\nLike all XML schema languages, XSD can be used to express a set of rules to which an XML document must conform to be considered 'valid' according to that schema. However, unlike most other schema languages, XSD was also designed with the intent that determination of a document's validity would produce a collection of information adhering to specific data types. Such a post-validation infoset can be useful in the development of XML document processing software.\n\nThe schema can be used to generate code, referred to as XML Data Binding. This code allows contents of XML documents to be treated as objects within the programming environment.",
            "url": "https://en.wikipedia.org/wiki/XML_Schema_(W3C)",
            "id": 538     
        },
        {
            "name": "pyATS",
            "definition": "Originally developed for internal Cisco engineering use, pyATS is at the core of Cisco's Test Automation Solution. It's currently used as the de-facto test framework for internal Cisco engineers across differentplatform/functions, running millions of CI/CD, sanity, regression, scale, HA, solution tests on a monthly basis. pyATS is also used by thousands of network engineers and developers world-wide, outside of Cisco.\n\nIn Cisco, pyATS provides sanity, feature, solution, system, and scale test & verification automation for products ranging from routers/switches, to access points, firewalls and cable CPEs.\n\npyATS is built using extensible layers like lego blocks; pyATS solution consists of…\n\n1. a foundational platform (eg, the original pyATS framework)\n2. a standard open-source, platform/vendor agnostic library system (Genie)\n3. a web dashboard to manage your test suites, testbeds, test results and their insights (XPRESSO)\n4. multiple bindings to other frameworks in the form of libraries, extensions, plugins and APIs.\n\n…enabling users to build their own business logic and solutions on top of the infrastructure stack.",
            "url": "https://developer.cisco.com/docs/pyats/",
            "id": 539     
        },
        {
            "name": "Database Source of Truth (SOT)",
            "definition": "In information science and information technology, single source of truth (SSOT) architecture, or single point of truth (SPOT) architecture, for information systems is the practice of structuring information models and associated data schemas such that every data element is mastered (or edited) in only one place, providing data normalization to a canonical form (for example, in database normalization or content transclusion). Any possible linkages to this data element (possibly in other areas of the relational schema or even in distant federated databases) are by reference only. Because all other locations of the data just refer back to the primary 'source of truth' location, updates to the data element in the primary location propagate to the entire system, providing multiple advantages simultaneously: greater efficiency/productivity, easy prevention of mistaken inconsistencies (such as a duplicate value/copy somewhere being forgotten), and greatly simplified version control. Without SSOT architecture, rampant forking impairs clarity and productivity, imposing laborious maintenance needs.\n\nDeployment of an SSOT architecture is becoming increasingly important in enterprise settings where incorrectly linked duplicate or de-normalized data elements (a direct consequence of intentional or unintentional denormalization of any explicit data model) pose a risk for retrieval of outdated, and therefore incorrect, information.",
            "url": "",
            "id": 540     
        },
        {
            "name": "Metaobject",
            "definition": "In computer science, a metaobject is an object that manipulates, creates, describes, or implements objects (including itself). The object that the metaobject pertains to is called the base object. Some information that a metaobject might define includes the base object's type, interface, class, methods, attributes, parse tree, etc. Metaobjects are examples of the computer science concept of reflection, where a system has access (usually at run time) to its own internal structure. Reflection enables a system to essentially rewrite itself on the fly, to alter its own implementation as it executes.\n\nA metaobject protocol (MOP) provides the vocabulary (protocol) to access and manipulate the structure and behaviour of systems of objects. Typical functions of a metaobject protocol include:\n\n- Create or delete a new class\n- Create a new property or method\n- Cause a class to inherit from a different class (‘change the class structure’)\n- Generate or change the code defining the methods of a class",
            "url": "https://en.wikipedia.org/wiki/Metaobject",
            "id": 541     
        },
        {
            "name": "Remote procedure call (RPC)",
            "definition": "In distributed computing, a remote procedure call (RPC) is when a computer program causes a procedure (subroutine) to execute in a different address space (commonly on another computer on a shared network), which is coded as if it were a normal (local) procedure call, without the programmer explicitly coding the details for the remote interaction. That is, the programmer writes essentially the same code whether the subroutine is local to the executing program, or remote. This is a form of client–server interaction (caller is client, executor is server), typically implemented via a request–response message-passing system. In the object-oriented programming paradigm, RPCs are represented by remote method invocation (RMI). The RPC model implies a level of location transparency, namely that calling procedures are largely the same whether they are local or remote, but usually, they are not identical, so local calls can be distinguished from remote calls. Remote calls are usually orders of magnitude slower and less reliable than local calls, so distinguishing them is important.\n\nRPCs are a form of inter-process communication (IPC), in that different processes have different address spaces: if on the same host machine, they have distinct virtual address spaces, even though the physical address space is the same; while if they are on different hosts, the physical address space is different. Many different (often incompatible) technologies have been used to implement the concept.",
            "url": "https://en.wikipedia.org/wiki/Remote_procedure_call",
            "id": 542     
        },
        {
            "name": "Parallel computing",
            "definition": "Parallel computing is a type of computation in which many calculations or processes are carried out simultaneously. Large problems can often be divided into smaller ones, which can then be solved at the same time. There are several different forms of parallel computing: bit-level, instruction-level, data, and task parallelism. Parallelism has long been employed in high-performance computing, but has gained broader interest due to the physical constraints preventing frequency scaling. As power consumption (and consequently heat generation) by computers has become a concern in recent years, parallel computing has become the dominant paradigm in computer architecture, mainly in the form of multi-core processors.\n\nParallel computing is closely related to concurrent computing—they are frequently used together, and often conflated, though the two are distinct: it is possible to have parallelism without concurrency, and concurrency without parallelism (such as multitasking by time-sharing on a single-core CPU). In parallel computing, a computational task is typically broken down into several, often many, very similar sub-tasks that can be processed independently and whose results are combined afterwards, upon completion. In contrast, in concurrent computing, the various processes often do not address related tasks; when they do, as is typical in distributed computing, the separate tasks may have a varied nature and often require some inter-process communication during execution.",
            "url": "https://en.wikipedia.org/wiki/Parallel_computing",
            "id": 543     
        },
        {
            "name": "Concept drift",
            "definition": "In predictive analytics and machine learning, concept drift means that the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes. The term concept refers to the quantity to be predicted. More generally, it can also refer to other phenomena of interest besides the target concept, such as an input, but, in the context of concept drift, the term commonly refers to the target variable.\n\nConcept drift generally occurs when the covariates that comprise the data set begin to explain the variation of your target set less accurately — there may be some confounding variables that have emerged, and that one simply cannot account for, which renders the model accuracy to progressively decrease with time. Generally, it is advised to perform health checks as part of the post-production analysis and to re-train the model with new assumptions upon signs of concept drift.\n\nTo prevent deterioration in prediction accuracy because of concept drift, reactive and tracking solutions can be adopted. Reactive solutions retrain the model in reaction to a triggering mechanism, such as a change-detection test, to explicitly detect concept drift as a change in the statistics of the data-generating process. When concept drift is detected, the current model is no longer up-to-date and must be replaced by a new one to restore prediction accuracy. A shortcoming of reactive approaches is that performance may decay until the change is detected. Tracking solutions seek to track the changes in the concept by continually updating the model. Methods for achieving this include online machine learning, frequent retraining on the most recently observed samples, and maintaining an ensemble of classifiers where one new classifier is trained on the most recent batch of examples and replaces the oldest classifier in the ensemble.",
            "url": "https://en.wikipedia.org/wiki/Concept_drift",
            "id": 544     
        },
        {
            "name": "Data drift",
            "definition": "Data drift is unexpected and undocumented changes to data structure, semantics, and infrastructure that is a result of modern data architectures. It breaks processes and corrupts data, but can also reveal new opportunities for data use.\n\nData drift is a variation in the production data from the data that was used to test and validate the model before deploying it in production and is one of the top reasons model accuracy degrades over time. For machine learning models, data drift is the change in model input data that leads to model performance degradation. Monitoring data drift helps detect these model performance issues.\n\nCauses of data drift include:\n\n1. Upstream process changes, such as a sensor being replaced that changes the units of measurement from inches to centimeters.\n2. Data quality issues, such as a broken sensor always reading 0.\n3. Natural drift in the data, such as mean temperature changing with the seasons.\n4. Change in relation between features, or covariate shift.",
            "url": "https://towardsdatascience.com/why-data-drift-detection-is-important-and-how-do-you-automate-it-in-5-simple-steps-96d611095d93",
            "id": 545     
        },
        {
            "name": "Zombie API",
            "definition": "A zombie API is a forgotten and deprecated API which should have been disabled but is instead still active and thus exploitable by new kinds of API attacks. This can lead to account takeover or fraudulent transactions. A zombie API is often left behind to typically handle migrations from one version of an application to another. An example would be the release of a new application version, which because of its enhanced capabilities, required a new API. To ensure a smooth migration, the old API is maintained ‘active’ to give developers time to phase over to the new API. The challenge for the security team is to track those ‘old’ APIs and deactivate them in time. Most often, they are just forgotten and are a great entry door for hackers to use.",
            "url": "https://www.traceable.ai/blog-post/how-zombie-apis-pose-a-forgotten-vulnerability",
            "id": 546     
        },
        {
            "name": "Shadow API",
            "definition": "Shadow APIs are APIs that exist outside of an organization’s official security and operational maintenance processes. There are countless scenarios that can lead to a shadow API. For example, a developer may need to quickly stand up an API to resolve an immediate problem or maybe to develop a proof of concept for a larger project. Regardless of the motivation, the lure of quickly deploying a new API endpoint makes it easy for developers to get their work done in the moment and worry about security and maintenance later.\n\nIn many ways, this is the AppSec and DevOps version of the shadow IT problem and brings with it many of the same risks. Security teams can’t defend assets that they don’t know about, and shadow APIs will not receive the appropriate security testing, monitoring and protection. Likewise, a newly or quickly deployed API endpoint may not be properly secured and hardened. As with any new code, the API may have vulnerabilities or misconfigurations that can leave the door open to attackers, who constantly scour applications and APIs for new or vulnerable endpoints.",
            "url": "https://www.threatx.com/blog/from-zombie-to-rogue-apis-how-to-reduce-your-api-security-risks/",
            "id": 547     
        },
        {
            "name": "Rogue API",
            "definition": "A rogue API is an API that does not behave in the manner in which it is intended to. It is possible that it will provide unexpected results, or that it will not operate at all. Whatever the case, a rogue API can pose a slew of issues for developers who attempt to make use of the service.\n\nSome ways to combat rogue APIs include:\n\n1. Verify that the API is authentic\n2. Check that the API is trustworthy\n3. Make sure that the API is well-documented\n4. Check for positive reviews of the API",
            "url": "https://datamagazine.co.uk/in-combat-with-rogue-apis/",
            "id": 548     
        },
        {
            "name": "Swagger",
            "definition": "Swagger is a suite of tools for API developers from SmartBear Software and a former specification upon which the OpenAPI Specification is based. Swagger's open-source tooling usage can be broken up into different use cases: development, interaction with APIs, and documentation.\n\nDeveloping APIs\n\nWhen creating APIs, Swagger tooling may be used to automatically generate an Open API document based on the code itself. This embeds the API description in the source code of a project and is informally called code-first or bottom-up API development.\n\nInteracting with APIs\n\nUsing the Swagger Codegen project, end users generate client SDKs directly from the OpenAPI document, reducing the need for human-generated client code. As of August 2017, the Swagger Codegen project supported over 50 different languages and formats for client SDK generation.\n\nDocumenting APIs\n\nWhen described by an OpenAPI document, Swagger open-source tooling may be used to interact directly with the API through the Swagger UI. This project allows connections directly to live APIs through an interactive, HTML-based user interface. Requests can be made directly from the UI and the options explored by the user of the interface.",
            "url": "https://en.wikipedia.org/wiki/Swagger_(software)",
            "id": 549     
        },
        {
            "name": "Non Maximum Suppression (NMS)",
            "definition": "Non Maximum Suppression (NMS) is a technique used in numerous computer vision tasks. It is a class of algorithms to select one entity (e.g., bounding boxes) out of many overlapping entities. We can choose the selection criteria to arrive at the desired results. The criteria are most commonly some form of probability number and some form of overlap measure (e.g. Intersection over Union).\n\nMost object detection algorithms use NMS to whittle down many detected bounding boxes to only a few. At the most basic level, most object detectors do some form of windowing. Thousands of windows (anchors) of various sizes and shapes are generated.\n\nThese windows supposedly contain only one object, and a classifier is used to obtain a probability/score for each class. Once the detector outputs a large number of bounding boxes, it is necessary to filter out the best ones. NMS is the most commonly used algorithm for this task.",
            "url": "https://medium.com/analytics-vidhya/non-max-suppression-nms-6623e6572536",
            "id": 550     
        },
        {
            "name": "Singleton pattern",
            "definition": "In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one ‘single’ instance. This is useful when exactly one object is needed to coordinate actions across the system. The term comes from the mathematical concept of a singleton.\n\nThe singleton design pattern is one of the twenty-three well-known ‘Gang of Four’ design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software with the aim of making it easier to implement, change, test, and reuse objects.",
            "url": "https://en.wikipedia.org/wiki/Singleton_pattern",
            "id": 551     
        },
        {
            "name": "Creational pattern",
            "definition": "In software engineering, creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or in added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.\n\nCreational design patterns are composed of two dominant ideas. One is encapsulating knowledge about which concrete classes the system uses. Another is hiding how instances of these concrete classes are created and combined.\n\nCreational design patterns are further categorized into object-creational patterns and class-creational patterns, where object-creational patterns deal with object creation and class-creational patterns deal with class-instantiation. In greater details, object-creational patterns defer part of its object creation to another object, while class-creational patterns defer its object creation to subclasses.",
            "url": "https://en.wikipedia.org/wiki/Creational_pattern",
            "id": 552     
        },
        {
            "name": "Software framework",
            "definition": "In computer programming, a software framework is an abstraction in which software, providing generic functionality, can be selectively changed by additional user-written code, thus providing application-specific software. It provides a standard way to build and deploy applications and is a universal, reusable software environment that provides particular functionality as part of a larger software platform to facilitate the development of software applications, products and solutions. Software frameworks may include support programs, compilers, code libraries, toolsets, and application programming interfaces (APIs) that bring together all the different components to enable development of a project or system.\n\nFrameworks have 4 key distinguishing features that separate them from normal libraries:\n\n1. inversion of control: In a framework, unlike in libraries or in standard user applications, the overall program's flow of control is not dictated by the caller, but by the framework. This is usually achieved with the Template Method Pattern.\n2. default behaviour: This can be provided with the invariant methods of the Template Method Pattern in an abstract class which is provided by the framework.\n3. extensibility: A user can extend the framework – usually by selective overriding – or programmers can add specialized user code to provide specific functionality. This is usually achieved by a hook method in a subclass that overrides a template method in the superclass.\n4. non-modifiable framework code: The framework code, in general, is not supposed to be modified, while accepting user-implemented extensions. In other words, users can extend the framework, but cannot modify its code.",
            "url": "https://en.wikipedia.org/wiki/Software_framework",
            "id": 553     
        },
        {
            "name": "Extensibility",
            "definition": "Extensibility is a software engineering and systems design principle that provides for future growth. Extensibility is a measure of the ability to extend a system and the level of effort required to implement the extension. Extensions can be through the addition of new functionality or through modification of existing functionality. The principle provides for enhancements without impairing existing system functions.\n\nAn extensible system is one whose internal structure and dataflow are minimally or not affected by new or modified functionality, for example recompiling or changing the original source code might be unnecessary when changing a system’s behavior, either by the creator or other programmers. Because software systems are long lived and will be modified for new features and added functionalities demanded by users, extensibility enables developers to expand or add to the software’s capabilities and facilitates systematic reuse. Some of its approaches include facilities for allowing users’ own program routines to be inserted and the abilities to define new data types as well as to define new formatting markup tags.",
            "url": "https://en.wikipedia.org/wiki/Extensibility",
            "id": 554     
        },
        {
            "name": "Loose coupling",
            "definition": "In computing and systems design, a loosely coupled system is one\n\n1. in which components are weakly associated (have breakable relationships) with each other, and thus changes in one component least affect existence or performance of another component.\n2. in which each of its components has, or makes use of, little or no knowledge of the definitions of other separate components. Sub-areas include the coupling of classes, interfaces, data, and services. Loose coupling is the opposite of tight coupling.\n\nComponents in a loosely coupled system can be replaced with alternative implementations that provide the same services. Components in a loosely coupled system are less constrained to the same platform, language, operating system, or build environment.\n\nIf systems are decoupled in time, it is difficult to also provide transactional integrity; additional coordination protocols are required. Data replication across different systems provides loose coupling (in availability), but creates issues in maintaining consistency (data synchronization).",
            "url": "https://en.wikipedia.org/wiki/Loose_coupling",
            "id": 555     
        },
        {
            "name": "Monorepo",
            "definition": "In version control systems, a monorepo (‘mono’ meaning 'single' and ‘repo’ being short for 'repository') is a software development strategy where code for many projects is stored in the same repository. This software engineering practice dates back to at least the early 2000s, when it was known as a 'shared codebase'. A related concept is the monolith, but while a monolith combines its sub-projects into one large project, a monorepo may contain independent projects.\n\nGoogle, Meta, Microsoft, Uber, Airbnb, and Twitter all employ very large monorepos with varying strategies to scale build systems and version control software with a large volume of code and daily changes.",
            "url": "https://en.wikipedia.org/wiki/Monorepo",
            "id": 556     
        },
        {
            "name": "Von Neumann architecture",
            "definition": "The Von Neumann architecture — also known as the Von Neumann model or Princeton architecture — is a computer architecture based on a 1945 description by John von Neumann, and by others, in the First Draft of a Report on the EDVAC. The document describes a design architecture for an electronic digital computer with these components:\n\n- A processing unit with both an arithmetic logic unit and processor registers\n- A control unit that includes an instruction register and a program counter\n- Memory that stores data and instructions\n- External mass storage\n- Input and output mechanisms\n\nThe term ‘von Neumann architecture’ has evolved to refer to any stored-program computer in which an instruction fetch and a data operation cannot occur at the same time (since they share a common bus). This is referred to as the von Neumann bottleneck, which often limits the performance of the corresponding system.\n\nA von Neumann language in computing is any of those programming languages that are high-level abstract isomorphic copies of von Neumann architectures. As of 2009, most current programming languages fit into this description , likely as a consequence of the extensive domination of the von Neumann computer architecture during the past 50 years.",
            "url": "https://en.wikipedia.org/wiki/Von_Neumann_architecture",
            "id": 557     
        },
        {
            "name": "Computronium",
            "definition": "Computronium is a material hypothesized by Norman Margolus and Tommaso Toffoli of MIT in 1991 to be used as ‘programmable matter’, a substrate for computer modeling of virtually any real object.\n\nIt also refers to a arrangement of matter that is the best possible form of computing device for that amount of matter. In this context, the term can refer both to a theoretically perfect arrangement of hypothetical materials that would have been developed using nanotechnology at the molecular, atomic, or subatomic level (in which case this interpretation of computronium could be unobtainium), and to the best possible achievable form using currently available and used computational materials.",
            "url": "https://en.wikipedia.org/wiki/Computronium",
            "id": 558     
        },
        {
            "name": "Halting problem",
            "definition": "In computability theory, the halting problem is the problem of determining, from a description of an arbitrary computer program and an input, whether the program will finish running, or continue to run forever. Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program-input pairs cannot exist.\n\nFor any program f that might determine if programs halt, a ‘pathological’ program g, called with some input, can pass its own source and its input to f and then specifically do the opposite of what f predicts g will do. No f can exist that handles this case. A key part of the proof is a mathematical definition of a computer and program, which is known as a Turing machine; the halting problem is undecidable over Turing machines. It is one of the first cases of decision problems proven to be unsolvable. This proof is significant to practical computing efforts, defining a class of applications which no programming invention can possibly perform perfectly.\n\nJack Copeland attributes the introduction of the term halting problem to the work of Martin Davis in the 1950s.",
            "url": "https://en.wikipedia.org/wiki/Halting_problem",
            "id": 559     
        },
        {
            "name": "Evolutionary algorithm",
            "definition": "In computational intelligence (CI), an evolutionary algorithm (EA) is a subset of evolutionary computation, a generic population-based metaheuristic optimization algorithm. An EA uses mechanisms inspired by biological evolution, such as reproduction, mutation, recombination, and selection. Candidate solutions to the optimization problem play the role of individuals in a population, and the fitness function determines the quality of the solutions (see also loss function). Evolution of the population then takes place after the repeated application of the above operators.\n\nEvolutionary algorithms often perform well approximating solutions to all types of problems because they ideally do not make any assumption about the underlying fitness landscape. Techniques from evolutionary algorithms applied to the modeling of biological evolution are generally limited to explorations of microevolutionary processes and planning models based upon cellular processes. In most real applications of EAs, computational complexity is a prohibiting factor. In fact, this computational complexity is due to fitness function evaluation. Fitness approximation is one of the solutions to overcome this difficulty. However, seemingly simple EA can solve often complex problems; therefore, there may be no direct link between algorithm complexity and problem complexity.",
            "url": "https://en.wikipedia.org/wiki/Evolutionary_algorithm",
            "id": 560     
        },
        {
            "name": "Heuristic",
            "definition": "A heuristic (from Ancient Greek (heurískō) 'I find, discover'), or heuristic technique, is any approach to problem solving or self-discovery that employs a practical method that is not guaranteed to be optimal, perfect, or rational, but is nevertheless sufficient for reaching an immediate, short-term goal or approximation. Where finding an optimal solution is impossible or impractical, heuristic methods can be used to speed up the process of finding a satisfactory solution. Heuristics can be mental shortcuts that ease the cognitive load of making a decision.\n\nExamples that employ heuristics include using trial and error, a rule of thumb or an educated guess.\n\nHeuristics are the strategies derived from previous experiences with similar problems. These strategies depend on using readily accessible, though loosely applicable, information to control problem solving in human beings, machines and abstract issues. When an individual applies a heuristic in practice, it generally performs as expected. However it can alternatively create systematic errors.",
            "url": "https://en.wikipedia.org/wiki/Heuristic",
            "id": 561     
        },
        {
            "name": "Cloud access security broker (CASB)",
            "definition": "A cloud access security broker (CASB) (sometimes pronounced cas-bee) is on-premises or cloud based software that sits between cloud service users and cloud applications, and monitors all activity and enforces security policies. A CASB can offer services such as monitoring user activity, warning administrators about potentially hazardous actions, enforcing security policy compliance, and automatically preventing malware.\n\nCASBs consolidate multiple types of security policy enforcement. Example security policies include authentication, single sign-on, authorization, credential mapping, device profiling, encryption, tokenization, logging, alerting, malware detection/prevention and so on.",
            "url": "https://en.wikipedia.org/wiki/Cloud_access_security_broker",
            "id": 562     
        },
        {
            "name": "System on a chip (SoC)",
            "definition": "A system on a chip or system-on-chip (SoC) is an integrated circuit that integrates most or all components of a computer or other electronic system. These components almost always include a central processing unit (CPU), memory interfaces, on-chip input/output devices, input/output interfaces, and secondary storage interfaces, often alongside other components such as radio modems and a graphics processing unit (GPU) – all on a single substrate or microchip. It may contain digital, analog, mixed-signal, and often radio frequency signal processing functions (otherwise it is considered only an application processor).",
            "url": "https://en.wikipedia.org/wiki/System_on_a_chip",
            "id": 563     
        },
        {
            "name": "Ostrich algorithm",
            "definition": "In computer science, the ostrich algorithm is a strategy of ignoring potential problems on the basis that they may be exceedingly rare. It is named after the ostrich effect which is defined as ‘to stick one's head in the sand and pretend there is no problem’. It is used when it is more cost-effective to allow the problem to occur than to attempt its prevention.\n\nThis approach may be used in dealing with deadlocks in concurrent programming if they are believed to be very rare and the cost of detection or prevention is high. For example, if each PC deadlocks once per 10 years, a single reboot may be less painful than the restrictions needed to prevent it.\n\nA set of processes is deadlocked if each process in the set is waiting for an event that only another process in the set can cause. Usually the event is the release of a currently held resource and none of the processes can run, release resources, and be awakened.\n\nThe ostrich algorithm pretends there is no problem and is reasonable to use if deadlocks occur very rarely and the cost of their prevention would be high. The UNIX and Windows operating systems take this approach.\n\nAlthough using the ostrich algorithm is one of the methods of dealing with deadlocks, other effective methods exist such as dynamic avoidance, banker's algorithm, detection and recovery, and prevention.",
            "url": "https://en.wikipedia.org/wiki/Ostrich_algorithm",
            "id": 564     
        },
        {
            "name": "Logarithm",
            "definition": "In mathematics, the logarithm is the inverse function to exponentiation. That means the logarithm of a given number x is the exponent to which another fixed number, the base b, must be raised, to produce that number x.\n\nAnalysis of algorithms is a branch of computer science that studies the performance of algorithms (computer programs solving a certain problem). Logarithms are valuable for describing algorithms that divide a problem into smaller ones, and join the solutions of the subproblems.",
            "url": "https://en.wikipedia.org/wiki/Logarithm#Computational_complexity",
            "id": 565     
        },
        {
            "name": "Adapter pattern",
            "definition": "In software engineering, the adapter pattern is a software design pattern (also known as wrapper, an alternative naming shared with the decorator pattern) that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.\n\nAn example is an adapter that converts the interface of a Document Object Model of an XML document into a tree structure that can be displayed.\n\nThe adapter design pattern is one of the twenty-three well-known Gang of Four design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.\n\nThe adapter design pattern solves problems like:\n\n- How can a class be reused that does not have an interface that a client requires?\n- How can classes that have incompatible interfaces work together?\n-How can an alternative interface be provided for a class?",
            "url": "https://en.wikipedia.org/wiki/Adapter_pattern",
            "id": 566     
        },
        {
            "name": "Factory",
            "definition": "In object-oriented programming (OOP), a factory is an object for creating other objects; formally, it is a function or method that returns objects of a varying prototype or class from some method call, which is assumed to be ‘new’. More broadly, a subroutine that returns a ‘new’ object may be referred to as a ‘factory’, as in factory method or factory function. This is a basic concept in OOP, and forms the basis for a number of related software design patterns.",
            "url": "https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)",
            "id": 567     
        },
        {
            "name": "Time complexity",
            "definition": "In computer science, the time complexity is the computational complexity that describes the amount of computer time it takes to run an algorithm. Time complexity is commonly estimated by counting the number of elementary operations performed by the algorithm, supposing that each elementary operation takes a fixed amount of time to perform. Thus, the amount of time taken and the number of elementary operations performed by the algorithm are taken to be related by a constant factor.",
            "url": "https://en.wikipedia.org/wiki/Time_complexity",
            "id": 568     
        },
        {
            "name": "Space complexity",
            "definition": "The space complexity of an algorithm or a computer program is the amount of memory space required to solve an instance of the computational problem as a function of characteristics of the input. It is the memory required by an algorithm until it executes completely. Similar to time complexity, space complexity is often expressed asymptotically in big O notation.",
            "url": "https://en.wikipedia.org/wiki/Space_complexity",
            "id": 569     
        },
        {
            "name": "Breadth-first search (BFS)",
            "definition": "Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.",
            "url": "https://en.wikipedia.org/wiki/Breadth-first_search",
            "id": 570     
        },
        {
            "name": "Depth-first search (DFS)",
            "definition": "Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. Extra memory, usually a stack, is needed to keep track of the nodes discovered so far along a specified branch which helps in backtracking of the graph.",
            "url": "https://en.wikipedia.org/wiki/Depth-first_search",
            "id": 571     
        },
        {
            "name": "Hardware overhang",
            "definition": "Hardware overhang is a situation where sufficient compute is available, but the algorithms are suboptimal. It commonly refers to instances where large quantities of computing hardware can be diverted to running powerful AI systems as soon as the software is developed.",
            "url": "https://www.lesswrong.com/posts/75dnjiD8kv2khe9eQ/measuring-hardware-overhang",
            "id": 572     
        },
        {
            "name": "Computing overhang",
            "definition": "Computing overhang refers to a situation where new algorithms can exploit existing computing power far more efficiently than before. This can happen if previously used algorithms have been suboptimal.",
            "url": "https://www.lesswrong.com/tag/computing-overhang",
            "id": 573     
        },
        {
            "name": "Instrumental convergence",
            "definition": "Instrumental convergence is the hypothetical tendency for most sufficiently intelligent beings (both human and non-human) to pursue similar sub-goals, even if their ultimate goals are quite different. More precisely, agents (beings with agency) may pursue instrumental goals—goals which are made in pursuit of some particular end, but are not the end goals themselves—without end, provided that their ultimate (intrinsic) goals may never be fully satisfied. Instrumental convergence posits that an intelligent agent with unbounded but apparently harmless goals can act in surprisingly harmful ways. For example, a computer with the sole, unconstrained goal of solving an incredibly difficult mathematics problem like the Riemann hypothesis could attempt to turn the entire Earth into one giant computer in an effort to increase its computational power so that it can succeed in its calculations.\n\nProposed basic AI drives include utility function or goal-content integrity, self-protection, freedom from interference, self-improvement, and non-satiable acquisition of additional resources.",
            "url": "https://en.wikipedia.org/wiki/Instrumental_convergence",
            "id": 574     
        },
        {
            "name": "Orthogonality thesis",
            "definition": "The Orthogonality Thesis states that an agent can have any combination of intelligence level and final goal, that is, its Utility Functions and General Intelligence can vary independently of each other. This is in contrast to the belief that, because of their intelligence, AIs will all converge to a common goal.",
            "url": "https://en.wikipedia.org/wiki/Existential_risk_from_artificial_general_intelligence#Orthogonality_thesis",
            "id": 575     
        },
        {
            "name": "Separation of concerns",
            "definition": "In computer science, separation of concerns is a design principle for separating a computer program into distinct sections. Each section addresses a separate concern, a set of information that affects the code of a computer program. A concern can be as general as ‘the details of the hardware for an application’, or as specific as ‘the name of which class to instantiate’. A program that embodies SoC well is called a modular program. Modularity, and hence separation of concerns, is achieved by encapsulating information inside a section of code that has a well-defined interface. Encapsulation is a means of information hiding. Layered designs in information systems are another embodiment of separation of concerns (e.g., presentation layer, business logic layer, data access layer, persistence layer).",
            "url": "https://en.wikipedia.org/wiki/Separation_of_concerns",
            "id": 576     
        },
        {
            "name": "Anonymous function",
            "definition": "In computer programming, an anonymous function (function literal, lambda abstraction, lambda function, lambda expression or block) is a function definition that is not bound to an identifier. Anonymous functions are often arguments being passed to higher-order functions or used for constructing the result of a higher-order function that needs to return a function. If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfill the same role for the function type as literals do for other data types.",
            "url": "https://en.wikipedia.org/wiki/Anonymous_function",
            "id": 577     
        },
        {
            "name": "Static application security testing (SAST)",
            "definition": "Static application security testing (SAST) allows developers to scan their source code for weak or insecure coding, identifying potential security issues that should be fixed. Each issue discovered has a severity level that can help developers prioritize remediation.\n\nWhen SAST is integrated into the SDLC or a CI/CD pipeline, teams can define quality gates that identify how many issues and what level of severity should cause the build to fail, or prevent a component from being promoted to next stages of the pipeline. Integration into developers’ integrated development environment (IDE) will allow developers to see code weaknesses as they write code, helping them build security in from the start.",
            "url": "https://en.wikipedia.org/wiki/Static_application_security_testing",
            "id": 578     
        },
        {
            "name": "Dynamic application security testing (DAST)",
            "definition": "Dynamic application security testing (DAST) tools can automatically perform security testing on running applications, testing for a variety of real threats without requiring access to source code. These tools typically test the HTTP and HTML interfaces of a web application. \n\nDAST is a black box testing method, which can identify application vulnerabilities from an attacker’s perspective, simulating common attack vectors recreating how an attacker may detect and exploit vulnerabilities. Because DAST is automated and easy to integrate with other DevOps tools, it is a great way to verify application security in testing or staging environments.",
            "url": "https://en.wikipedia.org/wiki/Dynamic_application_security_testing",
            "id": 579     
        },
        {
            "name": "Software composition analysis (SCA)",
            "definition": "Software composition analysis (SCA) is an automated process that identifies the open source software in a codebase. This analysis is performed to evaluate security, license compliance, and code quality.\n\nCompanies need to be aware of open source license limitations and obligations. Tracking these obligations manually became too arduous of a task—and it often overlooked code and its accompanying vulnerabilities. An automated solution, SCA, was developed, and from this initial use case, it expanded to analyze code security and quality.\n\nIn a modern DevOps or DevSecOps environment, SCA has galvanized the ‘shift left’ paradigm. Earlier and continuous SCA testing has enabled developers and security teams to drive productivity without compromising security and quality.",
            "url": "https://www.synopsys.com/glossary/what-is-software-composition-analysis.html",
            "id": 580     
        },
        {
            "name": "Binary Tree",
            "definition": "In computer science, a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.\n\nIn computing, binary trees are used in two very different ways:\n\n- First, as a means of accessing nodes based on some value or label associated with each node. Binary trees labelled this way are used to implement binary search trees and binary heaps, and are used for efficient searching and sorting. The designation of non-root nodes as left or right child even when there is only one child present matters in some of these applications, in particular, it is significant in binary search trees. However, the arrangement of particular nodes into the tree is not part of the conceptual information. For example, in a normal binary search tree the placement of nodes depends almost entirely on the order in which they were added, and can be re-arranged (for example by balancing) without changing the meaning.\n- Second, as a representation of data with a relevant bifurcating structure. In such cases, the particular arrangement of nodes under and/or to the left or right of other nodes is part of the information (that is, changing it would change the meaning). Common examples occur with Huffman coding and cladograms. The everyday division of documents into chapters, sections, paragraphs, and so on is an analogous example with n-ary rather than binary trees.",
            "url": "https://en.wikipedia.org/wiki/Binary_tree",
            "id": 581     
        },
        {
            "name": "Tree (data structure)",
            "definition": "In computer science, a tree is a widely used abstract data type that represents a hierarchical tree structure with a set of connected nodes. Each node in the tree can be connected to many children (depending on the type of tree), but must be connected to exactly one parent, except for the root node, which has no parent. These constraints mean there are no cycles or ‘loops’ (no node can be its own ancestor), and also that each child can be treated like the root node of its own subtree, making recursion a useful technique for tree traversal. In contrast to linear data structures, many trees cannot be represented by relationships between neighboring nodes in a single straight line.",
            "url": "https://en.wikipedia.org/wiki/Tree_(data_structure)",
            "id": 582     
        },
        {
            "name": "Information technology service management (ITSM)",
            "definition": "Information technology service management (ITSM) is the activities that are performed by an organization to design, build, deliver, operate and control information technology (IT) services offered to customers.\n\nDiffering from more technology-oriented IT management approaches like network management and IT systems management, IT service management is characterized by adopting a process approach towards management, focusing on customer needs and IT services for customers rather than IT systems, and stressing continual improvement.\n\nAs a discipline, ITSM has ties and common interests with other IT and general management approaches, information security management and software engineering. Consequently, IT service management frameworks have been influenced by other standards and adopted concepts from them.",
            "url": "https://en.wikipedia.org/wiki/IT_service_management",
            "id": 583     
        },
        {
            "name": "IP address management (IPAM)",
            "definition": "IP address management (IPAM) is a methodology implemented in computer software for planning and managing the assignment and use of IP addresses and closely related resources of a computer network. IPAM tools are increasingly important as new IPv6 networks are deployed with large address pools of 128-bit hexadecimal numbers and new subnetting techniques.",
            "url": "https://en.wikipedia.org/wiki/IP_address_management",
            "id": 584     
        },
        {
            "name": "OpenConfig",
            "definition": "OpenConfig is a vendor-neutral, model-driven network management technology designed by users. It defines and implements a common, vendor-independent software layer for managing network devices. OpenConfig operates as an open source project with contributions from network operators, equipment vendors, and the wider community. OpenConfig is led by an Operator Working Group consisting of network operators from multiple segments of the industry.",
            "url": "https://www.openconfig.net/",
            "id": 585     
        },
        {
            "name": "First-class function",
            "definition": "In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures. Some programming language theorists require support for anonymous functions (function literals) as well. In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type. The term was coined by Christopher Strachey in the context of ‘functions as first-class citizens’ in the mid-1960s.",
            "url": "https://en.wikipedia.org/wiki/First-class_function",
            "id": 586     
        },
        {
            "name": "Software-defined everything (SDE/SDx)",
            "definition": "Software-defined everything (SDE), sometimes referred to as SDx, is a broad term which refers to a group of various systems controlled by advanced software programs and constructed in a virtual, versus physical, hardware space. SDE is an advance in technology that allows virtualization of the entire technology stack compute, network, storage, and security layers. Software-Defined Everything aims to make information technology (IT) infrastructures more flexible and agile.\n\nSoftware-defined everything is a container term where the umbrella of SDE/Sdx includes Software Defined Networking (SDN), Software-Defined Storage (SDS) and Software-Defined Data Center (SDDC).",
            "url": "https://www.geeksforgeeks.org/umbrella-of-software-defined-everything-sdx-sde/",
            "id": 587     
        },
        {
            "name": "Product-family engineering (PFE)",
            "definition": "Product-family engineering (PFE), also known as product-line engineering, is based on the ideas of ‘domain engineering’ created by the Software Engineering Institute, and coined as a term by James Neighbors. Software product lines are quite common in our daily lives, but before a product family can be successfully established, an extensive process has to be followed. This process is known as product-family engineering.\n\nProduct-family engineering can be defined as a method that creates an underlying architecture of an organization's product platform. It provides an architecture that is based on commonality as well as planned variabilities. The various product variants can be derived from the basic product family, which creates the opportunity to reuse and differentiate on products in the family. Product-family engineering is conceptually similar to the widespread use of vehicle platforms in the automotive industry.\n\nProduct-family engineering is a relatively new approach to the creation of new products. It focuses on the process of engineering new products in such a way that it is possible to reuse product components and apply variability with decreased costs and time. Product-family engineering is all about reusing components and structures as much as possible.",
            "url": "https://en.wikipedia.org/wiki/Product-family_engineering",
            "id": 588     
        },
        {
            "name": "Linked list",
            "definition": "In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.\n\nLinked lists are among the simplest and most common data structures. The principal benefit of a linked list over a conventional array is that the list elements can be easily inserted or removed without reallocation or reorganization of the entire structure because the data items need not be stored contiguously in memory or on disk, while restructuring an array at run-time is a much more expensive operation.\n\nOn the other hand, since simple linked lists by themselves do not allow random access to the data or any form of efficient indexing, many basic operations—such as obtaining the last node of the list, finding a node that contains a given datum, or locating the place where a new node should be inserted—may require iterating through most or all of the list elements.",
            "url": "https://en.wikipedia.org/wiki/Linked_list",
            "id": 589     
        },
        {
            "name": "Network management software",
            "definition": "Network management software was developed to help reduce the burden of managing the growing complexity of computer networks and addresses the issues of network faults, performance bottlenecks, compliance issues, etc. Some advanced network management software may rectify network problems automatically and may also help with tasks involved in provisioning new networks, such as installing and configuring new network nodes, etc. They may also help with maintenance of existing networks like upgrading software on existing network devices, creating new virtual networks, etc.\n\nFunctions of network management software include provisioning, mapping, monitoring, configuration management, regulatory compliance, change control, software asset management and cybersecurity.",
            "url": "https://en.wikipedia.org/wiki/Network_management_software",
            "id": 590     
        },
        {
            "name": "Service-oriented modeling",
            "definition": "Service-oriented modeling is the discipline of modeling business and software systems, for the purpose of designing and specifying service-oriented business systems within a variety of architectural styles and paradigms, such as application architecture, service-oriented architecture, microservices, and cloud computing.\n\nAny service-oriented modeling method typically includes a modeling language that can be employed by both the ‘problem domain organization’ (the business), and ‘solution domain organization’ (the information technology department), whose unique perspectives typically influence the service development life-cycle strategy and the projects implemented using that strategy.\n\nService-oriented modeling typically strives to create models that provide a comprehensive view of the analysis, design, and architecture of all software entities in an organization, which can be understood by individuals with diverse levels of business and technical understanding. Service-oriented modeling typically encourages viewing software entities as ‘assets’ (service-oriented assets), and refers to these assets collectively as ‘services’. A key service design concern is to find the right service granularity both on the business (domain) level and on a technical (interface contract) level.\n\nPopular approaches to service-oriented modeling include service-oriented design and development methodology (SDDM), service-oriented modeling and architecture (SOMA) and service-oriented modeling framework (SOMF).",
            "url": "https://en.wikipedia.org/wiki/Service-oriented_modeling",
            "id": 591     
        },
        {
            "name": "Modeling language",
            "definition": "A modeling language is any artificial language that can be used to express information or knowledge or systems in a structure that is defined by a consistent set of rules. The rules are used for interpretation of the meaning of components in the structure.\n\nA modeling language can be graphical or textual. Graphical modeling languages use a diagram technique with named symbols that represent concepts and lines that connect the symbols and represent relationships and various other graphical notation to represent constraints. Textual modeling languages may use standardized keywords accompanied by parameters or natural language terms and phrases to make computer-interpretable expressions.\n\nVarious kinds of modeling languages are applied in different disciplines, including computer science, information management, business process modeling, software engineering, and systems engineering. Modeling languages can be used to specify system requirements, structures and behaviors and are intended to be used to precisely specify systems so that stakeholders (e.g., customers, operators, analysts, designers) can better understand the system being modeled.\n\nSome popular modeling languages are Object-Role Modeling (ORM), Unified Modeling Language (UML) and Java Modeling Language (JML).",
            "url": "https://en.wikipedia.org/wiki/Modeling_language",
            "id": 592     
        },
        {
            "name": "Theory of constraints (TOC)",
            "definition": "The theory of constraints (TOC) is a management paradigm that views any manageable system as being limited in achieving more of its goals by a very small number of constraints. There is always at least one constraint, and TOC uses a focusing process to identify the constraint and restructure the rest of the organization around it. TOC adopts the common idiom ‘a chain is no stronger than its weakest link’. That means that organizations and processes are vulnerable because the weakest person or part can always damage or break them, or at least adversely affect the outcome.",
            "url": "https://en.wikipedia.org/wiki/Theory_of_constraints",
            "id": 593     
        },
        {
            "name": "DevSecOps",
            "definition": "DevSecOps stands for development, security and operations. It is an approach to culture, automation and platform design that integrates security as a shared responsibility throughout the entire IT lifecycle.\n\nIn the collaborative framework of DevOps, security is a shared responsibility integrated from end to end. It’s a mindset that is so important, it led some to coin the term ‘DevSecOps’ to emphasize the need to build a security foundation into DevOps initiatives.\n\nDevSecOps means thinking about application and infrastructure security from the start. It also means automating some security gates to keep the DevOps workflow from slowing down. Selecting the right tools to continuously integrate security, like agreeing on an integrated development environment (IDE) with security features, can help meet these goals. However, effective DevOps security requires more than new tools—it builds on the cultural changes of DevOps to integrate the work of security teams sooner rather than later.",
            "url": "https://www.redhat.com/en/topics/devops/what-is-devsecops",
            "id": 594     
        },
        {
            "name": "Scalar",
            "definition": "A scalar data type, or just scalar, is any non-composite value. Generally, all basic primitive data types are considered scalar, including boolean data type (bool), numeric types (int, the floating point types float and double) and character types (char and string). A variable (that is, a named location containing a scalar data type) is sometimes referred to as a ‘scalar’. Scalar processors are a class of computer processors that process only one data item at a time.",
            "url": "https://en.wikipedia.org/wiki/Scalar_processor#Scalar_data_type",
            "id": 595     
        },
        {
            "name": "Critical control point (CCP)",
            "definition": "A critical control point (CCP) is the point where the failure of Standard Operation Procedure (SOP) could cause harm to customers and to the business, or even loss of the business itself. It is a point, step or procedure at which controls can be applied and a safety hazard can be prevented, eliminated or reduced to acceptable (critical) levels.\n\nIt is now possible to apply algorithms to CCPs rather than just rely on individual parameters or combinations. Artificial intelligence and machine learning are also coming down the line allowing much greater understanding and ‘line of sight’ for failure prediction.",
            "url": "https://www.riskedge.com.au/have-we-been-getting-critical-control-points-all-wrongits-time-to-rethink-like-a-coder/",
            "id": 596     
        },
        {
            "name": "Internet of behaviors (IoB)",
            "definition": "The Internet of behaviors (IoB) can be defined as the collection and use of data to understand and drive behaviors. It is an area of research and development (R&D) that seeks to understand how, when and why humans use technology to make decisions. IoB combines three fields of study: behavioral science, edge analytics and the Internet of Things (IoT).\n\nIoB platforms are designed to gather, aggregate and analyze data generated from a wide variety of sources, including household digital devices, wearable computers and human online activities. The data is then analyzed in terms of behavioral psychology to look for patterns that can be used by marketing and sales teams to influence future consumer behavior.\n\nThe concept of IoB can be thought of in two high-level stages:\n\n1. Measuring: Harvesting and Understanding\n2. Influencing: Driving Behavior\n\nAn important goal of the IoB is to help marketers understand and monetize the massive amount of data produced by network nodes in the Internet of Things.\n\nThe collection of behavioral events data can be problematic. The IoB raises concerns about how businesses gather, navigate, and use data, particularly as more of it is collected. Whatever perspectives are on IoT and IoB, experts predict that they will continue to grow and influence in the near future.",
            "url": "https://www.rackspace.com/solve/internet-behavior-what-it",
            "id": 597     
        },
        {
            "name": "Protobuf",
            "definition": "Protocol Buffers (Protobuf) is a free and open-source cross-platform data format used to serialize structured data. It is useful in developing programs to communicate with each other over a network or for storing data. The method involves an interface description language that describes the structure of some data and a program that generates source code from that description for generating or parsing a stream of bytes that represents the structured data.\n\nGoogle developed Protocol Buffers for internal use and provided a code generator for multiple languages under an open-source license. The design goals for Protocol Buffers emphasized simplicity and performance. In particular, it was designed to be smaller and faster than XML. Protocol Buffers are widely used at Google for storing and interchanging all kinds of structured information. The method serves as a basis for a custom remote procedure call (RPC) system that is used for nearly all inter-machine communication at Google.\n\nProtocol Buffers are similar to the Apache Thrift (used by Facebook, Evernote), Ion (created by Amazon), or Microsoft Bond protocols, offering as well a concrete RPC protocol stack to use for defined services called gRPC.",
            "url": "https://en.wikipedia.org/wiki/Protocol_Buffers",
            "id": 598     
        },
        {
            "name": "gNMI",
            "definition": "gNMI (gRPC Network Management Interface) is gRPC network management protocol developed by Google. gNMI provides the mechanism to install, manipulate, and delete the configuration of network devices, and also to view operational data. It defines the gRPC service name, RPCs and messages. The content provided through gNMI can be modeled using YANG.\n\ngRPC is a remote procedure call developed by Google for low-latency, scalable distributions with mobile clients communicating to a cloud server. gRPC carries gNMI, and provides the means to formulate and transmit data and operation requests.\n\nWhen a failure occurs, the gNMI broker (GNMIB) will indicate an operational change of state from up to down, and all RPCs will return a service unavailable message until the database is up and running. Upon recovery, the GNMIB will indicate a change of operation state from down to up, and resume normal handling of RPCs.",
            "url": "https://datatracker.ietf.org/meeting/101/materials/slides-101-netconf-grpc-network-management-interface-gnmi-00",
            "id": 599     
        },
        {
            "name": "gRPC",
            "definition": "gRPC (a recursive acronym for gRPC Remote Procedure Calls) is a cross-platform open source high performance Remote Procedure Call (RPC) framework. gRPC was initially created by Google, which has used a single general-purpose RPC infrastructure called Stubby to connect the large number of microservices running within and across its data centers for over a decade[when?]. In March 2015, Google decided to build the next version of Stubby and make it open source. The result was gRPC, which is now used in many organizations outside of Google to power use cases from microservices to the ‘last mile’ of computing (mobile, web, and Internet of Things).\n\ngRPC uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. It generates cross-platform client and server bindings for many languages. Most common usage scenarios include connecting services in a microservices style architecture, or connecting mobile device clients to backend services.",
            "url": "https://en.wikipedia.org/wiki/GRPC",
            "id": 600     
        },
        {
            "name": "Network slicing",
            "definition": "Network slicing is a form of virtual network architecture using the same principles behind software defined networking (SDN) and network functions virtualization (NFV) in fixed networks. SDN and NFV are now being commercially deployed to deliver greater network flexibility by allowing traditional network architectures to be partitioned into virtual elements that can be linked (also through software).\n\nNetwork slicing allows multiple virtual networks to be created on top of a common shared physical infrastructure. The virtual networks are then customized to meet the specific needs of applications, services, devices, customers or operators.",
            "url": "https://en.wikipedia.org/wiki/5G_network_slicing",
            "id": 601    
        },
        {
            "name": "eMBB, URLLC and mMTC",
            "definition": "Enhanced Mobile Broadband (eMBB), Ultra Reliable Low Latency Communications (URLLC) and Massive Machine Type Communications (mMTC) are the three main application areas for the enhanced capabilities of 5G.\n\nEnhanced Mobile Broadband (eMBB) uses 5G as a progression from 4G LTE mobile broadband services, with faster connections, higher throughput, and more capacity. This will benefit areas of higher traffic such as stadiums, cities, and concert venues.\n\nUltra-Reliable Low-Latency Communications (URLLC) refer to using the network for mission critical applications that require uninterrupted and robust data exchange. The short-packet data transmission is used to meet both reliability and latency requirements of the wireless communication networks.\n\nMassive Machine-Type Communications (mMTC) would be used to connect to a large number of devices. 5G technology will connect some of the 50 billion connected IoT devices.\n\nOnly eMBB is deployed as of 2020; URLLC and mMTC are several years away in most locations.",
            "url": "https://en.wikipedia.org/wiki/5G#Application_areas",
            "id": 602     
        },
        {
            "name": "MPLS Traffic Engineering (MPLS-TE)",
            "definition": "MPLS Traffic Engineering (MPLS-TE) allows the MPLS-enabled network to replicate and expand upon the TE capabilities of Layer 2 ATM and Frame Relay networks. MPLS uses the reachability information provided by Layer 3 routing protocols and operates like a Layer 2 ATM network. With MPLS, TE capabilities are integrated into Layer 3, which can be implemented for efficient bandwidth utilization between routers in the SP network.\n\nMPLS-TE works by learning about the topology and resources available in a network. It then maps the traffic flows to a particular path based on the resources that the traffic flow requires and the available resources. MPLS-TE builds unidirectional tunnels from a source to the destination in the form of LSPs, which is then used for forwarding traffic. The point where the tunnel begins is called tunnel headend or tunnel source, and the node where the tunnel ends is called ‘tunnel tailend’ or ‘tunnel destination’.\n\nThe main advantage of implementing MPLS-TE is that it provides a combination of ATM's TE capabilities along with the class of service (CoS) differentiation of IP. In MPLS-TE, the headend router in the network controls the path taken by traffic to any particular destination in the network. The requirement to implement a full mesh of virtual circuits (VCs), as in ATM, does not exist when implementing MPLS-TE.",
            "url": "https://community.cisco.com/t5/networking-knowledge-base/how-mpls-traffic-engineering-works/ta-p/3128593",
            "id": 603     
        },
        {
            "name": "Abstraction and Control of Traffic-Engineered Networks (ACTN)",
            "definition": "Abstraction and Control of Traffic-Engineered Networks (ACTN) in an IETF standard architecture enabling virtual network operations to control and manage large-scale multi-domain, multilayer and multi-vendor TE networks, so as to facilitate network programmability, automation, efficient resource sharing. ACTN architecture, together with 3GPP 5G architecture addresses service assurance and performance guarantee for end-to-end 5G backhaul transport networks.\n\nThe ACTN initiative represents a set of well-defined use cases developed from the input of network operators and service providers, international academic researchers, and vendors. The ACTN framework and its ongoing solution development addresses gaps between technology layers that could limit resource abstraction for multitechnology and multivendor transport networks.",
            "url": "https://www.ietfjournal.org/actn-from-standard-to-interop/",
            "id": 604     
        },
        {
            "name": "Distributed Overlay Virtual Ethernet (DOVE)",
            "definition": "Distributed Overlay Virtual Ethernet (DOVE) is a tunneling and virtualization technology for computer networks, created and backed by IBM. DOVE allows creation of network virtualization layers for deploying, controlling, and managing multiple independent and isolated network applications over a shared physical network infrastructure.\n\nPrimary advantages of DOVE include the following:\n\n1. No dependency on the underlying physical network and protocols\n2. Use of the existing IP network infrastructure\n3. No addresses of virtual machines are present in Ethernet switches, resulting in smaller MAC tables and less complex STP layouts\n4. No limitations related to the Virtual LAN (VLAN) technology, resulting in more than 16 million possible separate networks, compared to the VLAN's limit of 4,000\n5. No dependency on the IP multicast traffic",
            "url": "https://en.wikipedia.org/wiki/Distributed_Overlay_Virtual_Ethernet",
            "id": 605     
        },
        {
            "name": "Cisco ACI (Application Centric Infrastructure)",
            "definition": "Cisco Application Centric Infrastructure (ACI) is a software-defined networking (SDN) solution designed for data centers. Cisco ACI allows network infrastructure to be defined based upon network policies – simplifying, optimizing, and accelerating the application deployment lifecycle. To make this possible Cisco has created the ACI Fabric OS, which is run by all systems within the ACI network. This shared OS makes it possible for the various switches within the ACI network to translate policies into infrastructure designs.\n\nA Cisco ACI environment is built with two main components:\n\n- Cisco Application Policy Infrastructure Controller (APIC): APIC is the SDN controller for Cisco ACI. It creates the policies that define the data center’s network infrastructure.\n- Nexus 9000 Switches: Nexus 9000 switches use the ACI Fabric OS to communicate with APIC and create infrastructure based on policies. They can be either Spine (distribution) or Leaf (access) switches.\n\nAll endpoints, including APICs, connect to the network via Leaf switches. These Leaf switches are connected together using Spine switches in the backend. Using these components, ACI can be deployed under a variety of different models. This includes support for on-site, cloud-based (including public, private, and hybrid clouds), and SD-WAN edge environments. This enables organizations to use policy-based network management throughout their corporate WANs.",
            "url": "https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/solution-overview-c22-741487.html",
            "id": 606     
        },
        {
            "name": "Underlay network vs. Overlay network",
            "definition": "An Underlay network is the physical network responsible for the delivery of packets like DWDM, L2, L3, MPLS, or internet, etc. while an Overlay is a logical network that uses network virtualization to built connectivity on top of physical infrastructure using tunneling encapsulations such as VXLAN, GRE, IPSec.\n\nTraditional networks can be limited by an underlay which is hardware-specific and too complex for the changes needed for proper security, load balancing and transport independence, much less the network slicing and multi-path forwarding required of modern solutions. Overlays, which are software-based virtual links on top of the physical network, solve this issue by making configuration changing much easier and, thus, faster. Underlays are the pipe on which overlays run and the intelligence is all in the overlay.",
            "url": "https://telcocloudbridge.com/blog/overlay-vs-underlay-networks/#:~:text=An%20Underlay%20network%20is%20the,as%20VXLAN%2C%20GRE%2C%20IPSec.",
            "id": 607     
        },
        {
            "name": "Segment routing",
            "definition": "Segment routing is a method of forwarding packets on the network based on the source routing paradigm. The source chooses a path and encodes it in the packet header as an ordered list of segments. Segments are an identifier for any type of instruction. For example, topology segments identify the next hop toward a destination. Each segment is identified by the segment ID (SID) consisting of a flat unsigned 20-bit integer. Segment routing works either on top of a MPLS network or on an IPv6 network.",
            "url": "https://www.packetcoders.io/what-is-segment-routing/",
            "id": 608     
        },
        {
            "name": "Segment Routing over IPv6 (SRv6)",
            "definition": "Segment Routing over IPv6 (SRv6) simplifies the network by eliminating MPLS altogether and by relying on the native IPv6 header and header extension to provide the same services and flexibility as SR-MPLS, directly over the IPv6 data plane. SRv6 takes advantage of IPv6 Extension Headers by inserting Segment Routing headers into IPv6 packets, which facilitates infrastructure programming.\n\nSRv6 provides advanced traffic engineering capabilities, turning the network into a multi-service infrastructure. New Flexible Algorithm capabilities make multiple optimizations of the same physical network infrastructure along various dimensions possible (e.g., one can be optimized for low-latency vs. another one for bandwidth, or one can offer disjoint paths via two distinct planes.)\n\nSRv6 TI-LFA (Topology Independent Loop Free Alternate) guarantees under 50ms protection against any kind of network failures and brings with 100% topology coverage, simplicity and path optimality.",
            "url": "https://events-cisco.webex.com/recordingservice/sites/events-cisco/recording/531d7bd2c0fa4dcda22eb0ba6a750304/playback?token=QUhTSwAAAAUs-SLeyM3WMCI4Z8CQKiP9O9RHr3ZK5bT6WrsP3BrKshYykwSuswJQMDdMTYM_vaplZPVA-sm4BqyViKSTPZ2Fd-VCeRP55oswcWEc4tRydS3IjRibvfMpLWovSXXRwfNBUfosY9oil_hvQ2xMJ_YJJ-GbADorQxpejdZtRLJbfxd9cWXm-JAqItpUmvjlWLeI4Hc-gKPH4NZR_UbNt-hG0",
            "id": 609     
        },
        {
            "name": "Source routing",
            "definition": "In computer networking, source routing, also called path addressing, allows a sender of a packet to partially or completely specify the route the packet takes through the network. In contrast, in conventional routing, routers in the network determine the path incrementally based on the packet's destination. Another routing alternative, label switching, is used in connection-oriented networks such as X.25, Frame Relay, Asynchronous Transfer Mode and Multiprotocol Label Switching.\n\nSource routing allows easier troubleshooting, improved traceroute, and enables a node to discover all the possible routes to a host. It does not allow a source to directly manage network performance by forcing packets to travel over one path to prevent congestion on another.",
            "url": "https://en.wikipedia.org/wiki/Source_routing",
            "id": 610     
        },
        {
            "name": "Deployment vs. Provisioning",
            "definition": "Deployment is the ‘process of putting a new application, or new version of an application, onto a prepared application server’ while provisioning is ‘getting computers or virtual hosts to use, and installing needed libraries or services on them’. A key distinction is that ‘deployment’ does not, as a rule, include ‘provisioning’.",
            "url": "https://codefol.io/posts/deployment-versus-provisioning-versus-orchestration/",
            "id": 611     
        },
        {
            "name": "Interior gateway protocol vs. Exterior gateway protocol",
            "definition": "An interior gateway protocol (IGP) or Interior routing protocol is a type of routing protocol used for exchanging routing table information between gateways (commonly routers) within an autonomous system (for example, a system of corporate local area networks). This routing information can then be used to route network-layer protocols like IP. Interior gateway protocols can be divided into two categories: distance-vector routing protocols and link-state routing protocols. Specific examples of IGPs include Open Shortest Path First (OSPF), Routing Information Protocol (RIP), Intermediate System to Intermediate System (IS-IS) and Enhanced Interior Gateway Routing Protocol (EIGRP).\n\nBy contrast, an exterior gateway protocol is an IP routing protocol used to exchange routing information between autonomous systems. This exchange is crucial for communications across the Internet. Notable exterior gateway protocols include Exterior Gateway Protocol (EGP), now obsolete, and Border Gateway Protocol (BGP).",
            "url": "https://en.wikipedia.org/wiki/Interior_gateway_protocol",
            "id": 612     
        },
        {
            "name": "Equal-cost multi-path routing (ECMP)",
            "definition": "Equal-cost multi-path routing (ECMP) is a routing strategy where packet forwarding to a single destination can occur over multiple best paths with equal routing priority. Multi-path routing can be used in conjunction with most routing protocols because it is a per-hop local decision made independently at each router. It can substantially increase bandwidth by load-balancing traffic over multiple paths; however, there may be significant problems in deploying it in practice.\n\nLoad balancing by per-packet multipath routing was generally disfavored due to the impact of rapidly changing latency, packet reordering and maximum transmission unit (MTU) differences within a network flow, which could disrupt the operation of many Internet protocols, most notably TCP and path MTU discovery. RFC 2992 analyzed one particular multipath routing strategy involving the assignment of flows through hashing flow-related data in the packet header. This solution is designed to avoid these problems by sending all packets from any particular network flow through the same path while balancing multiple flows over multiple paths in general.",
            "url": "https://www.juniper.net/documentation/us/en/software/junos/flow-packet-processing/topics/topic-map/security-ecmp-flow-based-forwarding.html",
            "id": 613     
        },
        {
            "name": "Processor affinity",
            "definition": "Processor affinity, or CPU pinning or ‘cache affinity’, enables the binding and unbinding of a process or a thread to a central processing unit (CPU) or a range of CPUs, so that the process or thread will execute only on the designated CPU or CPUs rather than any CPU. This can be viewed as a modification of the native central queue scheduling algorithm in a symmetric multiprocessing operating system. Each item in the queue has a tag indicating its kin processor. At the time of resource allocation, each task is allocated to its kin processor in preference to others.",
            "url": "https://en.wikipedia.org/wiki/Processor_affinity",
            "id": 614     
        },
        {
            "name": "Eastbound/Westbound interfaces",
            "definition": "Eastbound and Westbound interfaces, often in the form of APIs, are used by systems to integrate with other systems for exchange of information or to work together on common workflows.\n\nCisco DNA Center defines an Eastbound interface (outbound) to facilitate other systems subscribing to event notifications sent by a push mechanism and RESTful API known as a webhook. In contrast, it defines a Westbound interface (inbound/integrative) exposes a RESTful API, called the Integration API, that allows ITTSM, IPAM, reporting and analytics systems to integrate with DNA Center.",
            "url": "https://blogs.cisco.com/networking/with-apis-cisco-dna-center-can-improve-your-competitive-advantage",
            "id": 615     
        },
        {
            "name": "Internal Developer Platform (IDP)",
            "definition": "An Internal Developer Platform (IDP) is built by a platform team to build golden paths and enable developer self-service. An IDP consists of many different techs and tools, glued together in a way that lowers cognitive load on developers without abstracting away context and underlying technologies. Following best practices, platform teams treat their platform as a product and build it based on user research, maintain and continuously improve it.\n\nInternal Developer Platforms (IDPs) are configured by Ops teams and used by developers. Ops teams specify what resources start up with what environment or at what request. They also set base-line templates for application configurations and govern permissions. This helps them to automate recurring tasks such as spinning up environments and resources and makes their setup easier to maintain by enforcing standards. Developer teams gain autonomy by changing configurations, deploying, spinning up fully provisioned environments, and rollback. IDPs can be built or bought.",
            "url": "https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/",
            "id": 616     
        },
        {
            "name": "Platform engineering",
            "definition": "Platform engineering is the discipline of designing and building toolchains and workflows that enable self-service capabilities for software engineering organizations in the cloud-native era. Platform engineers provide an integrated product most often referred to as an Internal Developer Platform (IDP) covering the operational necessities of the entire lifecycle of an application.",
            "url": "https://platformengineering.org/blog/what-is-platform-engineering",
            "id": 617     
        },
        {
            "name": "Jinja",
            "definition": "Jinja is a web template engine for the Python programming language. It is similar to the Django template engine but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as source code.\n\nThe Jinja template engine allows customization of tags, filters, tests and globals. Also, unlike the Django template engine, Jinja allows the template designer to call functions with arguments on objects. Jinja is Flask's default template engine and it is also used by Ansible, Trac and Salt.\n\nSome of the features of Jinja are:\n\nsandboxed execution\nautomatic HTML escaping to prevent cross-site scripting (XSS) attacks\ntemplate inheritance\ncompiles down to the optimal Python code just-in-time\noptional ahead-of-time template compilation\neasy to debug (for example, line numbers of exceptions directly point to the correct line in the template)\nconfigurable syntax\neasy-to-use filter system similar to the Unix pipeline.",
            "url": "https://en.wikipedia.org/wiki/Jinja_(template_engine)",
            "id": 618     
        },
        {
            "name": "Common Information Model (CIM)",
            "definition": "The Common Information Model (CIM) is an open standard that defines how managed elements in an IT environment are represented as a common set of objects and relationships between them.\n\nThe Distributed Management Task Force maintains the CIM to allow consistent management of these managed elements, independent of their manufacturer or provider.\n\nOne way to describe CIM is to say that it allows multiple parties to exchange management information about these managed elements. However, this falls short in expressing that CIM not only represents these managed elements and the management information, but also provides means to actively control and manage these elements. By using a common model of information, management software can be written once and work with many implementations of the common model without complex and costly conversion operations or loss of information.\n\nThe CIM standard includes the CIM Infrastructure Specification and the CIM Schema.",
            "url": "https://en.wikipedia.org/wiki/Common_Information_Model_(computing)",
            "id": 619     
        },
        {
            "name": "Managed object (MO)",
            "definition": "In telecommunication network, a managed object (MO) is an abstract representation of network resources that are managed. With ‘representation’, it is meant not only the actual device that is managed, but also the device driver, that communicates with the device. An example of a printer as a managed object is the window that shows information about the printer, such as the location, printer status, printing progress, paper choice, and printing margins.\n\nThe database, where all managed objects are stored, is called Management Information Base. A managed object is ‘dynamic’ and communicates with other network resources that are managed. A managed object may represent a physical entity, a network service, or an abstraction of a resource that exists independently of its use in management. A managed object model is a set of objects that together form a blueprint describing the managed objects you use in your application.",
            "url": "https://cobra.readthedocs.io/en/latest/api-ref/mo.html",
            "id": 620     
        },
        {
            "name": "Management information base (MIB",
            "definition": "A management information base (MIB) is a database used for managing the entities in a communication network. Most often associated with the Simple Network Management Protocol (SNMP), the term is also used more generically in contexts such as in OSI/ISO Network management model. While intended to refer to the complete collection of management information available on an entity, it is often used to refer to a particular subset, more correctly referred to as MIB-module.\n\nThe database is hierarchical (tree-structured) and each entry is addressed through an object identifier (OID). The software that performs the parsing is a MIB compiler.",
            "url": "https://en.wikipedia.org/wiki/Management_information_base",
            "id": 621     
        },
        {
            "name": "Database engine",
            "definition": "A database engine (or storage engine) is the underlying software component that a database management system (DBMS) uses to create, read, update and delete (CRUD) data from a database. Most database management systems include their own application programming interface (API) that allows the user to interact with their underlying engine without going through the user interface of the DBMS.\n\nThe term ‘database engine’ is frequently used interchangeably with ‘database server’ or ‘database management system’. A ‘database instance’ refers to the processes and memory structures of the running database engine.",
            "url": "https://en.wikipedia.org/wiki/Database_engine",
            "id": 622     
        },
        {
            "name": "Software Image Management (SWIM)",
            "definition": "Software Image Management (SWIM) is the management of software upgrades and control over the consistency of image versions across a network. Cisco DNA Center provides a SWIM solution which stores the unique software images according to image type and version for the devices in your network. It allows to view, import, and delete software images and also push software images to the devices in your network. Software upgrade can also be scheduled for later date and time.",
            "url": "https://www.youtube.com/watch?v=PuTSB8S5An0",
            "id": 623     
        },
        {
            "name": "Free Range Routing (FRR)",
            "definition": "Free Range Routing or FRRouting or FRR is a network routing software suite running on Unix-like platforms, particularly Linux, Solaris, OpenBSD, FreeBSD and NetBSD. It was created as a fork from Quagga in 2017, with a current, stable version as of August, 2022. FRRouting is distributed under the terms of the GNU General Public License v2 (GPL2).\n\nFRR provides implementations of the following protocols:\n\nOpen Shortest Path First (OSPF)\nRouting Information Protocol (RIP)\nBorder Gateway Protocol (BGP)\nIS-IS\nLabel Distribution Protocol (LDP)\nProtocol Independent Multicast (PIM)\nBabel\nBidirectional Forwarding Detection (BFD)\nEthernet VPN (EVPN)\n\nIt also provides alpha implementations of:\n\nNext Hop Resolution Protocol (NHRP)\nEnhanced Interior Gateway Routing Protocol (EIGRP)",
            "url": "https://en.wikipedia.org/wiki/FRRouting",
            "id": 624     
        },
        {
            "name": "Ethernet Virtual Private Network (EVPN)",
            "definition": "Ethernet VPN (EVPN) is a technology for carrying layer 2 Ethernet traffic as a virtual private network using wide area network protocols. EVPN technologies include Ethernet over MPLS and Ethernet over VXLAN.\n\nAn EVPN enables you to connect dispersed customer sites using a Layer 2 virtual bridge. As with other types of VPNs, an EVPN consists of customer edge (CE) devices (host, router, or switch) connected to provider edge (PE) routers.",
            "url": "https://blogs.cisco.com/sp/ethernet-vpn-whats-the-big-deal-about-it",
            "id": 625     
        },
        {
            "name": "Provider edge (PE) router vs. Customer edge (CE) Router",
            "definition": "The provider edge (PE) router is located at the provider network, usually either at its core or on the edge of the Multiprotocol Label Switching (MPLS) cloud. The PE router provides connectivity from the MPLS cloud to the Customer network. The customer edge (CE) router is located on the customer premises and provides connectivity to the interior of the customer network and to the MPLS cloud.\n\nThe CE router peers with the PE and exchanges routes with the corresponding virtual routing and forwarding (VRF) inside the PE. The routing protocol used could be static or dynamic (an interior gateway protocol like OSPF or an exterior gateway protocol like BGP).",
            "url": "https://docs.oracle.com/cd/E35292_01/doc.72/e47715/con_vpn.htm#autoId3",
            "id": 626     
        },
        {
            "name": "Golden image",
            "definition": "A golden image is a template for a virtual machine, virtual desktop, server or hard disk drive. Golden images are also known as ghost images, clones, master images or base images.\n\nTo create a golden image, an administrator first sets up the computing environment with the exact specifications needed and then saves the disk image as a pattern for future copies. Using golden images can save time and ensure consistency by eliminating the need for repetitive configuration changes and performance tweaks.\n\nThis approach can be compared with automated replication, which requires a configuration management tool such as Puppet to build new images on demand.\n\nIn an automated provisioning environment, a collection of golden images might be referred to as a golden repository or golden image library.",
            "url": "https://www.redhat.com/en/topics/linux/what-is-a-golden-image",
            "id": 627
        },
        {
            "name": "High-performance computing (HPC)",
            "definition": "High-performance computing (HPC) uses supercomputers and computer clusters to solve advanced computation problems.\n\nHPC integrates systems administration (including network and security knowledge) and parallel programming into a multidisciplinary field that combines digital electronics, computer architecture, system software, programming languages, algorithms and computational techniques. HPC technologies are the tools and systems used to implement and create high performance computing systems.\n\nRecently, HPC systems have shifted from supercomputing to computing clusters and grids. Because of the need of networking in clusters and grids, High Performance Computing Technologies are being promoted by the use of a collapsed network backbone, because the collapsed backbone architecture is simple to troubleshoot and upgrades can be applied to a single router as opposed to multiple ones.",
            "url": "https://en.wikipedia.org/wiki/High-performance_computing",
            "id": 628
        },
        {
            "name": "Heisenbug",
            "definition": "In computer programming jargon, a heisenbug is a software bug that seems to disappear or alter its behavior when one attempts to study it. The term is a pun on the name of Werner Heisenberg, the physicist who first asserted the observer effect of quantum mechanics, which states that the act of observing a system inevitably alters its state. In electronics, the traditional term is probe effect, where attaching a test probe to a device changes its behavior.\n\nHeisenbugs occur because common attempts to debug a program, such as inserting output statements or running it with a debugger, usually have the side-effect of altering the behavior of the program in subtle ways, such as changing the memory addresses of variables and the timing of its execution.",
            "url": "https://en.wikipedia.org/wiki/Heisenbug#cite_note-jarhei-1",
            "id": 629
        },
        {
            "name": "Dvorak vs. QWERTY",
            "definition": "Dvorak is a keyboard layout for English patented in 1936 by August Dvorak and his brother-in-law, William Dealey, as a faster and more ergonomic alternative to the QWERTY layout (the de facto standard keyboard layout). Dvorak proponents claim that it requires less finger motion and as a result reduces errors, increases typing speed, reduces repetitive strain injuries, or is simply more comfortable than QWERTY.\n\nDvorak has failed to replace QWERTY as the most common keyboard layout, with the most oft pointed to reason being QWERTY was popularized 60 years prior to Dvorak's creation and Dvorak's advantages are debated and relatively minuscule. However, most major modern operating systems (such as Windows, macOS, Linux, iOS, Android, ChromeOS, and BSD) allow a user to switch to the Dvorak layout. The layout can be chosen for use with any hardware keyboard, regardless of printed characters on the keyboard.",
            "url": "https://www.youtube.com/watch?v=tIJNusYZXMA",
            "id": 630
        },
        {
            "name": "Conway's law",
            "definition": "Conway's law is an adage that states organizations design systems that mirror their own communication structure. It is named after the computer programmer Melvin Conway, who introduced the idea in 1967. His original wording was:\n\n’Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.’\n\n— Melvin E. Conway\n\nThe law is based on the reasoning that in order for a product to function, the authors and designers of its component parts must communicate with each other in order to ensure compatibility between the components. Therefore, the technical structure of a system will reflect the social boundaries of the organizations that produced it, across which communication is more difficult.\n\nIn colloquial terms, it means complex products end up 'shaped like' the organizational structure they are designed in or designed for. The law is applied primarily in the field of software architecture, though Conway directed it more broadly and its assumptions and conclusions apply to most technical fields.",
            "url": "https://en.wikipedia.org/wiki/Conway%27s_law",
            "id": 631
        },
        {
            "name": "Programming kata",
            "definition": "Kata, a term borrowed from the Japanese word for ‘form’, is a term used by some programmers in the Software Craftsmanship movement. Computer programmers who call themselves ‘Software Craftsmen’ will write 'Kata' - small snippets of code that they write in one sitting, sometimes repeatedly, often daily, in order to build muscle memory and practise their craft.\n\nIn 1999, the term was used by Dave Thomas, co-author of the book The Pragmatic Programmer. The concept was implemented by Laurent Bossavit and Emmanuel Gaillot who talked about it at XP2005 in Sheffield (UK). Following this conference, Robert C. Martin described the concept and initial usages in his article ‘The Programming Dojo’.",
            "url": "",
            "id": 632
        },
        {
            "name": "Chaos Monkey",
            "definition": "Chaos Monkey is a chaos engineering tool invented in 2011 by Netflix to test the resilience of its IT infrastructure. It works by intentionally and randomly terminating instances in production to ensure that engineers implement their services to be resilient to instance failures. Chaos Monkey is now part of a larger suite of tools called the Simian Army designed to simulate and test responses to various system failures and edge cases.",
            "url": "https://en.wikipedia.org/wiki/Chaos_engineering#Chaos_Monkey",
            "id": 633
        },
        {
            "name": "Antifragility",
            "definition": "Antifragility is a property of systems in which they increase in capability to thrive as a result of stressors, shocks, volatility, noise, mistakes, faults, attacks, or failures. The concept was developed by Nassim Nicholas Taleb in his book, Antifragile, and in technical papers. As Taleb explains in his book, antifragility is fundamentally different from the concepts of resiliency (i.e. the ability to recover from failure) and robustness (that is, the ability to resist failure).\n\nThe concept has been applied in risk analysis, physics, molecular biology, transportation planning, engineering, aerospace (NASA), and computer science.\n\nIn computer science, there is a structured proposal for an ‘Antifragile Software Manifesto’, to react to traditional system designs. The major idea is to develop antifragility by design, building a system which improves from environment's input.",
            "url": "https://en.wikipedia.org/wiki/Antifragility",
            "id": 634
        },
        {
            "name": "Source Code Management (SCM)",
            "definition": "Source code management (SCM) is used to track modifications to a source code repository. SCM tracks a running history of changes to a code base and helps resolve conflicts when merging updates from multiple contributors. It helps your development team collaborate and maximize productivity, sparking faster delivery and increased visibility. SCM is also synonymous with 'version control' and is often handled by a Source Code Manager (SCM) or Source Code Control System (SCCS).",
            "url": "https://en.wikipedia.org/wiki/Source_Code_Control_System",
            "id": 627     
        },
        {
            "name": "Recovery as a service (RaaS)",
            "definition": "Recovery as a service (RaaS), sometimes referred to as disaster recovery as a service (DRaaS), is a category of cloud computing used for protecting an application or data from a natural or human disaster or service disruption at one location by enabling a full recovery in the cloud.\nRaaS differs from cloud-based backup services by protecting data and providing standby computing capacity on demand to facilitate more rapid application recovery. RaaS capacity is delivered in a cloud-computing model so recovery resources are only paid for when they are used, making it more efficient than a traditional disaster recovery warm site or hot site where the recovery resources must be running at all times.",
            "url": "https://en.wikipedia.org/wiki/Recovery_as_a_service",
            "id": 628     
        },
        {
            "name": "Flow-based programming",
            "definition": "In computer programming, flow-based programming (FBP) is a programming paradigm that defines applications as networks of ‘black box’ processes, which exchange data across predefined connections by message passing, where the connections are specified externally to the processes. These black box processes can be reconnected endlessly to form different applications without having to be changed internally. FBP is thus naturally component-oriented.\nFBP is a particular form of dataflow programming based on bounded buffers, information packets with defined lifetimes, named ports, and separate definition of connections.",
            "url": "https://en.wikipedia.org/wiki/Flow-based_programming",
            "id": 629     
        },
        {
            "name": "Programmatic vs. Declarative transaction management",
            "definition": "In Java programming, you can approach coding transactions in two basic ways: programmatically or declaratively. When possible, declarative transactions are a better choice since they allow the container to manage the transaction for you, and this saves you from having to put transaction management calls into your application code.\nProgrammatic transaction management means you have transaction management code surrounding your business code. Programmatic transaction management is usually a good idea only if you have a small number of transactional operations.\nDeclarative transaction management involves separating transaction management from the business logic. If your application has numerous transactional operations, declarative transaction management is usually worthwhile. ",
            "url": "https://www.oreilly.com/library/view/java-enterprise-in/0596101422/ch16s02.html",
            "id": 630     
        },
        {
            "name": "Dependency hell",
            "definition": "Dependency hell is a colloquial term for the frustration of some software users who have installed software packages which have dependencies on specific versions of other software packages.\nThe dependency issue arises when several packages have dependencies on the same shared packages or libraries, but they depend on different and incompatible versions of the shared packages. If the shared package or library can only be installed in a single version, the user may need to address the problem by obtaining newer or older versions of the dependent packages. This, in turn, may break other dependencies and push the problem to another set of packages.",
            "url": "https://en.wikipedia.org/wiki/Dependency_hell",
            "id": 631     
        },
        {
            "name": "Onshore vs. Offshore vs. Nearshore",
            "definition": "In the outsourcing of labor, the following terms indicate where resources, including personnel, are located.\n\n- Onshore signifies the resource are located within the same country.\n- Offshore indicates that the resources are in another country with a different time zone.\n- Nearshore refers to resources in a neighboring country, which is a short distance away.",
            "url": "https://en.wikipedia.org/wiki/Outsourcing",
            "id": 632     
        },
        {
            "name": "Homeshoring",
            "definition": "Homeshoring (also known as Homesourcing) is a form of IT-enabled ‘transfer of service industry employment from offices to home-based ... with appropriate telephone and Internet facilities’. These remote work positions may be customer-facing or back office and the workers may be employees or independent contractors.",
            "url": "https://en.wikipedia.org/wiki/Remote_work",
            "id": 633     
        },
        {
            "name": "Dynamic Multipoint Virtual Private Network (DMVPN)",
            "definition": "Dynamic Multipoint Virtual Private Network (DMVPN) is a dynamic tunneling form of a virtual private network (VPN) supported on Cisco IOS-based routers, and Huawei AR G3 routers, and on Unix-like operating systems.\nDMVPN provides the capability for creating a dynamic-mesh VPN network without having to pre-configure (static) all possible tunnel end-point peers, including IPsec (Internet Protocol Security) and ISAKMP (Internet Security Association and Key Management Protocol) peers.\nAs with GRE tunnels, DMVPN allows for several encryption schemes (including none) for the encryption of data traversing the tunnels. For security reasons Cisco recommend that customers use AES.",
            "url": "https://en.wikipedia.org/wiki/Dynamic_Multipoint_Virtual_Private_Network",
            "id": 634     
        },
        {
            "name": "Greenfield vs. Brownfield",
            "definition": "In general terms, a greenfield project is a brand new one, developed from scratch, and not based on any existing systems, code or infrastructure, unlike a brownfield one, which is built upon already existing projects, code or other resources.\nIn software development, brownfield development describes problem spaces needing the development and deployment of new software systems within the immediate presence of existing (legacy) software applications/services. This implies that any new software architecture must take into account and coexist with live software already in production. A brownfield project usually refers to a major upgrade, or a redevelopment of an existing live application where there are issues like backwards compatibility to existing file formats, interfaces, modules, etc. On the other hand, greenfield development lacks any constraints imposed by prior work.",
            "url": "https://www.moogsoft.com/blog/aiops/brownfield-greenfield-ops/",
            "id": 635     
        },
        {
            "name": "Decentralized application",
            "definition": "A decentralised application (DApp, dApp, Dapp, or dapp) is an application that can operate autonomously, typically through the use of smart contracts, that run on a decentralized computing, blockchain or other distributed ledger system. Like traditional applications, DApps provide some function or utility to its users. However, unlike traditional applications, DApps operate without human intervention and are not owned by any one entity, rather DApps distribute tokens that represent ownership. These tokens are distributed according to a programmed algorithm to the users of the system, diluting ownership and control of the DApp. Without any one entity controlling the system, the application is therefore decentralised.",
            "url": "https://en.wikipedia.org/wiki/Decentralized_application",
            "id": 636     
        },
        {
            "name": "Dry run",
            "definition": "A dry run (or practice run) is a software testing process where the effects of a possible failure are intentionally mitigated. For example, an aerospace company may conduct a ‘dry run’ test of a jet's new pilot ejection seat while the jet is parked on the ground, rather than while it is in flight. The term dry run appears to have originated from fire departments in the U.S. In order to practice, they would carry out dispatches of the fire brigade where water was not pumped. A run with real fire and water was referred to as a wet run. ",
            "url": "https://www.bbc.co.uk/bitesize/guides/zg4j7ty/revision/3",
            "id": 637     
        },
        {
            "name": "Trace table",
            "definition": "A trace table is a technique used to test algorithms in order to make sure that no logical errors occur while the calculations are being processed. They can also be useful for debugging applications, helping the programmer to easily detect what error is occurring, and why it may be occurring.",
            "url": "https://www.bbc.co.uk/bitesize/guides/zg4j7ty/revision/4",
            "id": 638     
        },
        {
            "name": "Dereference",
            "definition": "In computer programming, to dereference is to go to an address before performing the operation. For example, in C programming, a dereferenced variable is a pointer to the variable, not the variable itself. An example is found in the tar archiving program. The dereference switch causes files referenced by symbolic links to be archived rather than the symbolic link itself. ",
            "url": "https://en.wikipedia.org/wiki/Dereference_operator",
            "id": 639     
        },
        {
            "name": "Kanban",
            "definition": "Kanban (Japanese, meaning signboard or billboard) is a lean method to manage and improve work across human systems. This approach aims to manage work by balancing demands with available capacity, and by improving the handling of system-level bottlenecks.\nWork items are visualized to give participants a view of progress and process, from start to finish—usually via a kanban board. Work is pulled as capacity permits, rather than work being pushed into the process when requested.\nIn knowledge work and in software development, the aim is to provide a visual process management system which aids decision-making about what, when, and how much to produce.",
            "url": "https://en.wikipedia.org/wiki/Kanban_(development)",
            "id": 640     
        },
        {
            "name": "Salt",
            "definition": "In cryptography, a salt is random data that is used as an additional input to a one-way function that hashes data, a  or passphrase. Salts are used to safeguard passwords in storage. Historically, only the output from an invocation of a cryptographic hash function on the password was stored on a system, but, over time, additional safeguards were developed to protect against duplicate or common passwords being identifiable (as their hashes are identical). Salting is one such protection.\nA new salt is randomly generated for each password. Typically, the salt and the password (or its version after key stretching) are concatenated and fed to a cryptographic hash function, and the output hash value (but not the original password) is stored with the salt in a database. Hashing allows later authentication without keeping and therefore risking exposure of the plaintext password if the authentication data store is compromised. Salts don't need to be encrypted or stored separately from the hashed password itself, because even if an attacker has access to the database with the hash values and the salts, the correct use of said salts will hinder common attacks.",
            "url": "https://en.wikipedia.org/wiki/Salt_(cryptography)",
            "id": 641     
        },
        {
            "name": "Feedback vs. Feed forward",
            "definition": "A feedback control system is a control system where the output depends on the generated feedback signal. Feedback control system is responsible for processing the feedback signals which further act as an input to the system. The loop in a feedback control system is a closed loop. It focuses on the output of the system and variables are adjusted on the basis of errors.\n\nA feed forward control system is a system which passes the signal to some external load. It directly measures and rejects the disturbances before they affect the controlled variable. The loop in a feed forward control system is an open loop. It focuses on the input of the system and variables are adjusted on the basis of knowledge.",
            "url": "https://en.wikipedia.org/wiki/Feed_forward_(control)",
            "id": 642     
        },
        {
            "name": "ChatOps",
            "definition": "Chat Operations (ChatOps) is the use of chat clients and real-time chat tools to facilitate software development and operations. Also known as ‘conversation-driven collaboration’ or ‘conversation-driven DevOps’, ChatOps is designed for fast and simple instant messaging between development team members. Throughout the ChatOps experience, a chatbot accepts plain-English commands and initiates actions with background apps (via API) to optimize IT operations (ITOps) and development operations (DevOps).\n\nThe ChatOps flow connects the work needed, the work happening, and the work done in a persistent location staffed by the people, bots and related tools. The transparency tightens the feedback loop, improves information sharing, and enhances team collaboration.",
            "url": "https://www.ibm.com/cloud/blog/benefits-of-chatops",
            "id": 643     
        },
        {
            "name": "CALMS",
            "definition": "CALMS (Culture, Automation, Lean, Measurement, and Sharing) is a framework that assesses a company's ability to adopt DevOps processes, as well as a way of measuring success during a DevOps transformation. The acronym was coined by Jez Humble, co-author of ‘The DevOps Handbook’. The CALMS framework covers all stakeholders within DevOps, including business, IT operations, QA, InfoSec and development teams, and how they collectively deliver, deploy and integrate automated processes that make business sense.",
            "url": "https://www.atlassian.com/devops/frameworks/calms-framework",
            "id": 644     
        },
        {
            "name": "DevOps Wall of Confusion",
            "definition": "The ‘Wall of Confusion’ is a DevOps term popularized by Andrew Clay Schafer and Lee Thompson. It refers to the phenomena where one group in a value stream approaches their job as complete when they’ve passed it onto the next group. The canonical example is when developers throw their code ‘over the wall’ to their ops colleagues and ignore what must be done to get the software they’ve written into a deployable state. This often causes the ops team to struggle with getting the software deployed, leading to significant delays in releases and raising the risk of defects and other problems.\n\nThis phenomenon is not limited to development and IT operations, but the result is almost always the same: waste in our workflows, including overhead in communication, defects being passed downstream resulting in back-flow, context-switching due to excessive cognitive load, and over-engineered solutions. This can call be mitigated through the breaking down of organizational silos, the use of boundary objects to ensure collaboration and the implementation of shift left, parallel work streams.",
            "url": "https://levelup.gitconnected.com/the-wall-of-confusion-623057a4dd26",
            "id": 645     
        },
        {
            "name": "Big bang adoption",
            "definition": "Big bang adoption or direct changeover is when a new system is adopted instantly, with no transition period between the old and new systems.\n\nWhen a new system needs to be implemented in an organization, there are three different ways to adopt this new system: the big bang adoption, phased adoption and parallel adoption. In case of parallel adoption the old and the new system are running parallel, so all the users can get used to the new system, and meanwhile do their work using the old system. Phased adoption means that the adoption will happen in several phases, so after each phase the system is a little nearer to be fully adopted. With the big bang adoption, the switch between using the old system and using the new system happens at one single date, the so-called instant changeover of the system. Everybody starts to use the new system at the same date and the old system will not be used anymore from that moment on.\n\nThe advantage of a big bang adoption is that the new system does not need to be compatible or connected with any old systems it is replacing. This significantly simplifies the design of the new system, especially in an organization that is running on multiple incompatible systems. However, the big bang adoption type is riskier than other adoption types because there are fewer learning opportunities incorporated in the approach, so more preparation is needed to get to the big bang. This preparation will be described below, illustrated by the process-data model of the big bang adoption.",
            "url": "https://en.wikipedia.org/wiki/Big_bang_adoption",
            "id": 646     
        },
        {
            "name": "Root cause analysis (RCA)",
            "definition": "In science and engineering, root cause analysis (RCA) is a method of problem solving used for identifying the root causes of faults or problems. It is widely used in IT operations, manufacturing, telecommunications, industrial process control, accident analysis (e.g., in aviation, rail transport, or nuclear plants), medicine (for medical diagnosis), healthcare industry (e.g., for epidemiology), etc. Root cause analysis is a form of deductive inference since it requires an understanding of the underlying causal mechanisms of the potential root causes and the problem.\n\nRCA can be decomposed into four steps: 1. Identify and describe the problem clearly. 2. Establish a timeline from the normal situation until the problem occurs. 3. Distinguish between the root cause and other causal factors (e.g., using event correlation). 4. Establish a causal graph between the root cause and the problem.",
            "url": "https://en.wikipedia.org/wiki/Root_cause_analysis",
            "id": 647     
        },
        {
            "name": "Muxponder",
            "definition": "In optical fiber communications, a muxponder is the element that sends and receives the optical signal on a fiber in much the same way as a transponder except that the muxponder has the additional functionality of multiplexing multiple sub-rate client interfaces onto the line interface.",
            "url": "https://www.cisco.com/c/en/us/products/collateral/optical-networking/ons-15500-series/product_data_sheet0900aecd801d2889.html",
            "id": 648     
        },
        {
            "name": "Lindy effect",
            "definition": "The Lindy effect (also known as Lindy's Law) is a theorized phenomenon by which the future life expectancy of some non-perishable things, like a technology or an idea, is proportional to their current age. Thus, the Lindy effect proposes the longer a period something has survived to exist or be used in the present, the longer its remaining life expectancy. Longevity implies a resistance to change, obsolescence or competition, and greater odds of continued existence into the future. Where the Lindy effect applies, mortality rate decreases with time. Mathematically, the Lindy effect corresponds to lifetimes following a Pareto probability distribution.\n\nThe concept is named after Lindy's delicatessen in New York City, where the concept was informally theorized by comedians. The Lindy effect has subsequently been theorized by mathematicians and statisticians. Nassim Nicholas Taleb has expressed the Lindy effect in terms of ‘distance from an absorbing barrier’.",
            "url": "https://en.wikipedia.org/wiki/Lindy_effect",
            "id": 649     
        },
        {
            "name": "Automagically",
            "definition": "Automatic, but with an apparent element of magic. Commonly referring to complex technical processes hidden from the view of users or operators, resulting in technology that ‘just works’.",
            "url": "https://www.techopedia.com/definition/14261/automagically",
            "id": 650     
        },
        {
            "name": "Foot gun",
            "definition": "Any feature whose addition to a product results in the user ‘shooting themselves in the foot’. A footgun is designed in such a way as to be extremely likely to cause problems. Use of this word puts blame on the design, not on users.",
            "url": "https://swizec.com/blog/dry-is-a-footgun-remember-to-yagni/",
            "id": 651     
        },
        {
            "name": "LLVM",
            "definition": "LLVM is a set of compiler and toolchain technologies that can be used to develop a front end for any programming language and a back end for any instruction set architecture. LLVM is designed around a language-independent intermediate representation (IR) that serves as a portable, high-level assembly language that can be optimized with a variety of transformations over multiple passes.\n\nLLVM is written in C++ and is designed for compile-time, link-time, run-time, and ‘idle-time’ optimization. Originally implemented for C and C++, the language-agnostic design of LLVM has since spawned a wide variety of front ends: languages with compilers that use LLVM (or which do not directly use LLVM but can generate compiled programs as LLVM IR) include ActionScript, Ada, C#, Common Lisp, PicoLisp, Crystal, CUDA, D, Delphi, Dylan, Forth,[9] Fortran, Free Basic, Free Pascal, Graphical G, Halide, Haskell, Java bytecode, Julia, Kotlin, Lua, Objective-C, OpenCL, PostgreSQL's SQL and PLpgSQL, Ruby, Rust, Scala, Swift, XC, Xojo and Zig.",
            "url": "https://en.wikipedia.org/wiki/LLVM",
            "id": 652     
        },
        {
            "name": "Homoiconicity",
            "definition": "In computer programming, homoiconicity (from the Greek words homo- meaning ‘the same’ and icon meaning ‘representation’) is a property of some programming languages. A language is homoiconic if a program written in it can be manipulated as data using the language, and thus the program's internal representation can be inferred just by reading the program itself. This property is often summarized by saying that the language treats ‘code as data’.",
            "url": "https://en.wikipedia.org/wiki/Homoiconicity",
            "id": 653     
        },
        {
            "name": "Metaprogramming",
            "definition": "Metaprogramming is a programming technique in which computer programs have the ability to treat other programs as their data. It means that a program can be designed to read, generate, analyze or transform other programs, and even modify itself while running. In some cases, this allows programmers to minimize the number of lines of code to express a solution, in turn reducing development time. It also allows programs a greater flexibility to efficiently handle new situations without recompilation.",
            "url": "https://en.wikipedia.org/wiki/Metaprogramming",
            "id": 654     
        },
        {
            "name": "Weighted random early detection (WRED)",
            "definition": "Weighted random early detection (WRED) is a queueing discipline for a network scheduler suited for congestion avoidance. It is an extension to random early detection (RED) where a single queue may have several different sets of queue thresholds. Each threshold set is associated to a particular traffic class.\n\nFor example, a queue may have lower thresholds for lower priority packet. A queue buildup will cause the lower priority packets to be dropped, hence protecting the higher priority packets in the same queue. In this way quality of service prioritization is made possible for important packets from a pool of packets using the same buffer. It is more likely that standard traffic will be dropped instead of higher prioritized traffic.\n\nOn Cisco switches WRED is restricted to TCP/IP traffic. Only this kind of traffic indicates congestion to the sender to enable a reduction of the transmission rate. Non-IP traffic will be dropped more often than TCP/IP traffic because it is treated with the lowest possible precedence.",
            "url": "https://en.wikipedia.org/wiki/Weighted_random_early_detection",
            "id": 655     
        },
        {
            "name": "Tabula rasa",
            "definition": "Tabula rasa is a Latin phrase often translated as ‘clean slate’ in English and originates from the Roman tabula, a wax-covered tablet used for notes, which was blanked (rasa) by heating the wax and then smoothing it. This roughly equates to the English term ‘blank slate’ (or, more literally, ‘erased slate’) which refers to the emptiness of a slate prior to it being written on with chalk. Both may be renewed repeatedly, by melting the wax of the tablet or by erasing the chalk on the slate.\n\nIn artificial intelligence, tabula rasa refers to the development of autonomous agents with a mechanism to reason and plan toward their goal, but no ‘built-in’ knowledge-base of their environment. Thus, they truly are a blank slate. AlphaZero achieved superhuman performance in various board games using self-play and tabula rasa reinforcement learning, meaning it had no access to human games or hard-coded human knowledge about either game, only being given the rules of the games.",
            "url": "https://en.wikipedia.org/wiki/Tabula_rasa",
            "id": 656     
        },
        {
            "name": "NAT64",
            "definition": "NAT64 is an IPv6 transition mechanism that facilitates communication between IPv6 and IPv4 hosts by using a form of network address translation (NAT). The NAT64 gateway is a translator between IPv4 and IPv6 protocols, for which function it needs at least one IPv4 address and an IPv6 network segment comprising a 32-bit address space. The ‘well-known prefix’ reserved for this service is 64:ff9b::/96.\n\nAn IPv6 client embeds the IPv4 address it wishes to communicate with using the host part of the IPv6 network segment, resulting in an IPv4-embedded IPv6 addresses (hence the 32-bit address space in the IPv6 network segment), and sends packets to the resulting address. The NAT64 gateway creates a mapping between the IPv6 and the IPv4 addresses, which may be manually configured or determined automatically.",
            "url": "https://en.wikipedia.org/wiki/NAT64",
            "id": 657     
        },
        {
            "name": "Y2K38",
            "definition": "The year 2038 problem (also known as Y2038, Y2K38, or the Epochalypse) is a time formatting bug in computer systems with representing times after 03:14:07 UTC on 19 January 2038.\n\nThe problem exists in systems which measure Unix time – the number of seconds elapsed since the Unix epoch (00:00:00 UTC on 1 January 1970) – and store it in a signed 32-bit integer. The data type is only capable of representing integers between −(2^31) and 2^31 -1, meaning the latest time that can be properly encoded is 2^31 − 1 seconds after epoch (03:14:07 UTC on 19 January 2038). Attempting to increment to the following second (03:14:08) will cause the integer to overflow, setting its value to −(2^31) which systems will interpret as 2^31 seconds before epoch (20:45:52 UTC on 13 December 1901). The problem is similar in nature to the year 2000 problem.\n\nComputer systems that use time for critical computations may encounter fatal errors if the Y2038 problem is not addressed. Some applications that use future dates have already encountered the bug. The most vulnerable systems are those which are infrequently or never updated, such as legacy and embedded systems. There is no universal solution to the problem, though many modern systems have been upgraded to measure Unix time with signed 64-bit integers which will not overflow for 292 billion years, which is approximately 21 times the estimated age of the universe.",
            "url": "https://en.wikipedia.org/wiki/Year_2038_problem",
            "id": 658     
        },
        {
            "name": "Clos network",
            "definition": "In the field of telecommunications, a Clos network is a kind of multistage circuit-switching network which represents a theoretical idealization of practical, multistage switching systems. It was invented by Edson Erwin in 1938 and first formalized by Charles Clos in 1952.\n\nWhen the Clos network was first devised, the number of crosspoints was a good approximation of the total cost of the switching system. While this was important for electromechanical crossbars, it became less relevant with the advent of VLSI, wherein the interconnects could be implemented either directly in silicon, or within a relatively small cluster of boards. Upon the advent of complex data centers, with huge interconnect structures, each based on optical fiber links, Clos networks regained importance. A subtype of Clos network, the Beneš network, has also found recent application in machine learning.",
            "url": "https://en.wikipedia.org/wiki/Clos_network",
            "id": 659     
        },
        {
            "name": "Very large-scale integration (VLSI)",
            "definition": "Very large-scale integration (VLSI) is the process of creating an integrated circuit (IC) by combining millions or billions of MOS transistors onto a single chip. VLSI began in the 1970s when MOS integrated circuit (Metal Oxide Semiconductor) chips were developed and then widely adopted, enabling complex semiconductor and telecommunication technologies. The microprocessor and memory chips are VLSI devices.\n\nBefore the introduction of VLSI technology, most ICs had a limited set of functions they could perform. An electronic circuit might consist of a CPU, ROM, RAM and other glue logic. VLSI enables IC designers to add all of these into one chip.",
            "url": "https://en.wikipedia.org/wiki/Very_Large_Scale_Integration",
            "id": 660     
        },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 661     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 662     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 663     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 664     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 665     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 666     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 667     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 668     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 669     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 670    
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 6     
        # },

    ]

    # Note -- if you want to run this app in GitHub only, remove all lines regarding variables 'used_list' and 'items'

    # select a candidate word from word list
    candidate_word = random.choice(word_list)
    # query db for current used word list
    used_list_search = db.search(User.used.exists())
    used_list = used_list_search[0]["used"]
    # if length of word list and length of used list is equal, erase used list and start over
    if len(used_list) == len(word_list):
        used_list = []
    # if random choice is already in used list, choose again
    while candidate_word["id"] in used_list:
        candidate_word = random.choice(word_list)
    # solidify choice
    word = candidate_word
    # add new choice to used list and to db
    # remove these three lines to test without writing to db
    # used_list.append(word["id"])
    # items = {'used':used_list}
    # db.update(items)

    return word
