import random


##                        ATTENTION DEVELOPERS!!
##     Hi, please add new definitions to the end of the list. 
##     A Wikipedia entry is the default url unless it is lacking, absent or clearly outdone.



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
            "definition": "The ability of a system to efficiently handle a growing or shrinking workload by providing it with more or less resources. Scaling horizontally (out/in) means adding more nodes to (or removing nodes from) a system while scaling vertically (up/down) means adding resources to (or removing resources from) a single node.\n\n Scalability is the ability of the system to accommodate larger loads just by adding resources either making hardware stronger (scale up) or adding additional nodes (scale out). Elasticity is the ability to fit the resources needed to cope with loads dynamically usually in relation to scale out.",
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
            "definition": "Runtime is the period of time when a program is running. It begins when a program is opened (or executed) and ends with the program is quit or closed. Runtime is a technical term, used most often in software development. It is commonly seen in the context of a 'runtime error',  which is an error that occurs while a program is running. \n\n The term 'runtime error' is used to distinguish from other types of errors, such as syntax errors and compilation errors, which occur before a program is run.",
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
            "definition": "An approach to software engineering which takes advantage of innovations in cloud computing to build and run scalable apps via the cloud’s resources and technologies such as containers, microservices, serverless functions and immutable infrastructure. \n\n The result is loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers the granular control to make major changes frequently with relative safety and ease. Cloud native systems are container packaged, dynamically merged and microservices oriented.",
            "url": "https://en.wikipedia.org/wiki/Cloud_native_computing",
            "id": 16       
        },       
        {
            "name": "Containerization",
            "definition": "Containerization, or OS-level virtualization, is an operating system (OS) paradigm in which the kernel allows the existence of multiple isolated user space instances, called containers (LXC, Solaris containers, Docker, Podman), zones (Solaris containers), virtual private servers (OpenVZ), partitions, virtual environments (VEs), virtual kernels (DragonFly BSD), or jails (FreeBSD jail or chroot jail) Such instances may look like real computers from the point of view of programs running in them. \n\n A computer program running on an ordinary operating system can see all resources (connected devices, files and folders, network shares, CPU power, quantifiable hardware capabilities) of that computer. However, programs running inside of a container can only see the container's contents and devices assigned to the container.",
            "url": "https://en.wikipedia.org/wiki/OS-level_virtualization",
            "id": 17       
        },       
        {
            "name": "DevSecOps",
            "definition": "DevSecOps is the augmentation of DevOps to allow for security practices to be integrated into the DevOps approach, resulting in the merger of development, operational and security responsibilities. Security practices and testing are performed earlier in the development lifecycle, hence the term ‘shift left’ can be used. \n \n DevSecOps empowers the developer by breaking down team silos and promoting the creation of secure, automated workflows and policy enforcement which provide the developer with timely and accurate information on how to move the project forward.",
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
            "definition": "A computer infrastructure (VMs, containers, network appliances, etc.) that can’t be altered once it’s deployed, which makes it easier to prevent and mitigate security vulnerabilities. This is often enforced via an automated process that overwrites unauthorized changes or through a system that won’t allow changes in the first place. \n \n Containers are an excellent example of immutable infrastructure because persistent changes to containers can only be made by creating a new version of the container or recreating the existing container from its image.",
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
            "definition": "Kubernetes (K8s) is an open-source tool for infrastructure automation. It’s like a data center operating system that manages applications running across a distributed system (just like the OS on your laptop that manages your apps). Kubernetes schedules containers across nodes in a cluster. \n \n It defines infrastructure building blocks, called ‘primitives’ (exmples include app instances, load balancers, and persistent storage) which collectively provide mechanisms that deploy, maintain, and scale applications based on CPU, memory or custom metrics. \n\n Amazon, Google, IBM, Microsoft, Oracle, Red Hat, SUSE and VMware offer Kubernetes-based platforms or infrastructure as a service (IaaS) that deploy Kubernetes.",
            "url": "https://en.wikipedia.org/wiki/Kubernetes",
            "id": 23       
        },       
        {
            "name": "Cloud enabler",
            "definition": "A technology or manufacturer that serves as an organization’s backbone for all of its cloud computing products and services. It is a broad term for technology vendors and solutions that let a company build, deploy, integrate, and deliver cloud computing solutions. \n \n Cloud enablers for infrastructure as a strive, for example, include high-capacity networks, low-cost computing, low cost storage devices, the widespread adoption of hardware virtualization and service-oriented architecture.",
            "url": "https://www.techslang.com/definition/what-is-a-cloud-enabler/",
            "id": 24       
        },       
        {
            "name": "Elasticity",
            "definition": "In cloud computing, elasticity is defined as 'the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible.\n \n Scalability is the ability of the system to accommodate larger loads just by adding resources either making hardware stronger (scale up) or adding additional nodes (scale out). Elasticity is the ability to fit the resources needed to cope with loads dynamically usually in relation to scale out.'",
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
            "definition": "Function as a Service (FaaS) is a type of serverless cloud computing service where code is executed in response to events or triggers but without the need for maintaining the complex infrastructure typically associated with building and launching applications. \n \n Building an application following this model is one way of achieving a 'serverless' architecture, and is typically used when building microservices applications. With FaaS, users manage only functions and data while the cloud provider manages the application. \n \n This allows developers to get the functions they need without paying for services when code isn’t running. Some popular FaaS examples include: Amazon’s AWS Lambda, Google Cloud Functions and Microsoft Azure Functions.",
            "url": "https://en.wikipedia.org/wiki/Function_as_a_service",
            "id": 27       
        },       
        {
            "name": "Bare-metal server",
            "definition": "a physical computer server that is used by one consumer, or tenant, only.[1] Each server offered for rental is a distinct physical piece of hardware that is a functional server on its own. They are not virtual servers running in multiple pieces of shared hardware.",
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
            "definition": "The ability of software to be used in different environments, which helps to avoid being locked-in to certain operating environments, such as operating systems, cloud providers or vendors. Portable software works in different operating environments without needing major reconfiguration. When software with the same functionality is produced for several computing platforms, portability is the key issue for development cost reduction. \n\n In software engineering, ‘porting’ is the process of adapting software for the purpose of achieving some form of execution in a computing environment that is different from the one that a given program (meant for such execution) was originally designed for (e.g., different CPU, operating system, or third party library). The term is also used when software/hardware is changed to make them usable in different environments.",
            "url": "https://en.wikipedia.org/wiki/Software_portability",
            "id": 33     
        },  
        {
            "name": "Serverless",
            "definition": "A cloud computing and cloud native model in which the cloud provider allocates machine resources on demand, taking care of the servers on behalf of their customers. In this way, developers can build and run applications without having to manage servers. Although, ‘Serverless’ is a misnomer in the sense that servers are still used by cloud service providers to execute code for developers. However, developers of serverless applications are not concerned with capacity planning, configuration, management, maintenance, fault tolerance, or scaling of containers, VMs, or physical servers. \n\n Serverless computing does not hold resources in volatile memory; computing is rather done in short bursts with the results persisted to storage. When an app is not in use, there are no computing resources allocated to the app. And pricing is based on the actual amount of resources consumed by an application.",
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
            "definition": "Site reliability engineering (SRE) is a set of principles and practices which incorporates aspects of software engineering and applies them to infrastructure and operations problems.The main goals are to create scalable and highly reliable software systems. Site reliability engineering is closely related to DevOps, a set of practices that combine software development and IT operations, and SRE has also been described as a specific implementation of DevOps. However, while DevOps is focused on getting code to production, SRE ensures that the code running in production works properly.",
            "url": "https://en.wikipedia.org/wiki/Site_reliability_engineering",
            "id": 37     
        },  
        {
            "name": "Stateful vs. Stateless",
            "definition": "A stateless process or application can be understood in isolation. There is no stored knowledge of or reference to past transactions. Each transaction is made as if from scratch for the first time. Stateless applications provide one service or function and use content delivery network (CDN), web, or print servers to process these short-term requests. \n\n Stateful applications and processes, however, are those that can be returned to again and again, like online banking or email. They’re performed with the context of previous transactions and the current transaction may be affected by what happened during previous transactions. For these reasons, stateful apps use the same servers each time they process a request from a user.  \n\n If a stateful transaction is interrupted, the context and history have been stored so you can more or less pick up where you left off. Stateful apps track things like window location, setting preferences, and recent activity. You can think of stateful transactions as an ongoing periodic conversation with the same person. /n/n The majority of applications we use day to day are stateful, but as technology advances, microservices and containers make it easier to build and deploy applications in the cloud.",
            "url": "https://www.redhat.com/en/topics/cloud-native-apps/stateful-vs-stateless",
            "id": 38     
        },  
            {
            "name": "Version control",
            "definition": "Version control (also known as revision control, source control, or source code management) is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management. \n\n Version control systems are most commonly run as stand-alone applications, but revision control is also embedded in various types of software, such as word processors and spreadsheets, collaborative web docs, and content management systems, e.g., Wikipedia's page history. Revision control enables reverting a document to a previous revision, which is critical for allowing editors to track each other's edits, correct mistakes, and defend against vandalism and spamming in wikis. Git is the most popular version control software but there are many competitors.",
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
            "definition": "A software testing technique that repeatedly applies inputs on a module to ensure it is functioning correctly and that there are no bugs. Gorilla testing is a manual testing procedure and is performed on selected modules of the software system with selected test cases. \n\n The main objective is to test specific modules heavily and find any faults in their implementation. Since the tester manually applies the same test case repeatedly, it is also known as Torture Testing, Fault Tolerance Testing, or Frustrating Testing.",
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
            "definition": "A software application that offers features for Cisco contact center agents and supervisors in UCCE, PCCE and UCCX. It provides a web interface for agents and supervisors to login, change their state and receive calls. It also has some integration options with other platforms to display data and offer other features. \n\n Cisco Finesse is a service that runs inside Cisco UCCX or as a separate virtual server in Cisco UCCE and PCCE. It offers call center agent functionality which includes managing agent's phone, answering incoming calls, making calls and other call control features. \n\n Cisco Finesse is like a remote control, as it helps agents to control their Cisco phone remotely. They can answer a call, make a call, transfer an existing call without touching their Cisco IP Phone or Jabber Phone. However, it is actually the Cisco phone which offers all the telephony functionality for the call center agent. Cisco Finesse also helps agents to set their availability for taking calls from the queue.",
            "url": "https://developer.cisco.com/docs/finesse/#!finesse-overview/what-is-finesse",
            "id": 43     
        },  
        {
            "name": "Cisco JTAPI",
            "definition": "JTAPI serves as a programming interface standard developed by Sun Microsystems for use with Java-based computer–telephony applications. You use Cisco JTAPI to develop applications that \n\n a) Control and observe Cisco Unified Communications Manager (CUCM) phones and \n b) route calls by using Computer–Telephony Integration (CTI) ports and route points (virtual devices). \n\n Cisco Unified JTAPI gets used in a contact center to monitor device status and to issue routing instructions to send calls to the right place at the right time, to start and stop recording instructions while retrieving call statistics for analysis; and to screen-pop calls into CRM applications, automated scripting, and remote call control. \n\n Cisco Unified JTAPI, used in an enterprise environment, combines user availability, location, and preferences for a uniquely tailored environment for presence-based routing. For example, in a financial environment, market data, business logic, and call control combine in a browser-based application to enable brokers and analysts to respond to rapid changes in the global financial markets. \n\n In a healthcare environment, call control, doctor/patient lookup, and emergency response team paging combine in a browser-based console. Further, in a hospitality environment, caller data gets linked with POS systems to automate room or restaurant reservations, dispatch taxis, and schedule wakeup calls.",
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
            "definition": "Hashing is a widely used concept within the IT world. It’s a multi-purpose technique used to generate a value based on a string that is computed through a mathematical function. The mathematical function used is called the hashing algorithm, and the value computed is called the hash value. A hash value is used because as long as you provide the same input string to a hashing algorithm, it will always generate exactly the same output hash value. \n\n We can then use the computed hash value instead of the original string for simplicity. In networks, we run a lot of data through a hashing algorithm to scramble data before we transmit it (encrypt it). But the same technique can also be used to choose a physical link to use when they’re bundled into a logical interface.",
            "url": "https://en.wikipedia.org/wiki/Hash_function",
            "id": 47     
        },         
        {
            "name": "Bandwidth, Throughput and Goodput",
            "definition": "In computing, bandwidth is the maximum rate of data transfer across a given path. \n\n Throughput is all the bits that you can actually, physically transfer through your network, which can fall short of the bandwidth ideal. This includes all the needed headers and everything that is transported across your network. \n\n To determine goodput, take all your throughput data and strip all the headers and all the application layer overheads; what’s left is the data that you can use: goodput. \n\n Bandwidth > Throughput > Goodput",
            "url": "https://en.wikipedia.org/wiki/Goodput",
            "id": 48     
        },         
        {
            "name": "Trunking",
            "definition": "In telecommunications, trunking is a technology for providing network access to multiple clients simultaneously by sharing a set of circuits, carriers, channels, or frequencies, instead of providing individual circuits or channels for each client. This is reminiscent to the structure of a tree with one trunk and many branches. \n\n In computer networking, port trunking is the use of multiple concurrent network connections to aggregate the link speed of each participating port and cable, also called link aggregation. Such high-bandwidth link groups may be used to interconnect switches or to connect high-performance servers to a network. \n\n In the context of Ethernet VLANs, Cisco uses the term Ethernet trunking to mean carrying multiple VLANs through a single network link through the use of a trunking protocol. To allow for multiple VLANs on one link, frames from individual VLANs must be identified. The most common and preferred method, IEEE 802.1Q adds a tag to the Ethernet frame, labeling it as belonging to a certain VLAN. Since 802.1Q is an open standard, it is the only option in an environment with multiple-vendor equipment.",
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
            "definition": "In packet-switched computer networks, a jumbogram is an internet-layer packet exceeding the standard maximum transmission unit (MTU) of the underlying network technology. While IPv4 has no facilities to exceed its theoretical IP MTU limit, the designers of IPv6 have provided a protocol extension to permit packets of larger size. An optional feature of IPv6, the jumbo payload option, allows the exchange of packets with payloads of up to one byte less than 4 GiB (232 − 1 = 4,294,967,295 bytes), by making use of a 32-bit length field. \n\n In contrast, large packets (more than 1500 bytes of payload, the limit set by the IEEE 802.3 standard) for link-layer technologies are referred to as jumbo frames. Commonly, jumbo frames can carry up to 9000 bytes of payload, but smaller and larger variations exist and some care must be taken using the term. Many Gigabit Ethernet switches and Gigabit Ethernet network interface controllers and some Fast Ethernet switches and Fast Ethernet network interface cards can support jumbo frames.",
            "url": "https://en.wikipedia.org/wiki/Jumbo_frame",
            "id": 53     
        },        
        {
            "name": "Information Technology Infrastructure Library (ITIL)",
            "definition": "Information Technology Infrastructure Library (ITIL) is a library and set of detailed practices for IT activities such as IT service management (ITSM) and IT asset management (ITAM) that focus on aligning IT services with the needs of business. \n\n ITIL describes processes, procedures, tasks, and checklists which are neither organization-specific nor technology-specific, but can be applied by an organization toward strategy, delivering value, and maintaining a minimum level of competency. It allows the organization to establish a baseline from which it can plan, implement, and measure. It is used to demonstrate compliance and to measure improvement.",
            "url": "https://en.wikipedia.org/wiki/ITIL",
            "id": 54     
        },          
        {
            "name": "Big data",
            "definition": "A tech term that describes large volumes of data in a structured, semi-structured, and unstructured form that can be leveraged for gleaning valuable business insights using machine learning and advanced analytics techniques. Big Data is characterized by the four V’s – Volume of the data, Variety of the data, Veracity, i.e. trustworthiness of the data, and Velocity. \n\n Big data also refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. Data with many fields (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.",
            "url": "https://en.wikipedia.org/wiki/Big_data",
            "id": 55     
        },          
        {
            "name": "Colo (Colocation Centre)",
            "definition": "A colocation center (also spelled co-location, or colo) or 'carrier hotel', is a type of data centre where equipment, space, and bandwidth are available for rental to retail customers. Colocation facilities provide space, power, cooling, and physical security for the server, storage, and networking equipment of other firms and also connect them to a variety of telecommunications and network service providers with a minimum of cost and complexity.",
            "url": "https://en.wikipedia.org/wiki/Colocation_centre",
            "id": 56     
        },          
        {
            "name": "Data migration",
            "definition": "The process of moving data, applications, or business elements between multiple formats, storage systems, warehouses, and servers. ",
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
            "definition": "A hypervisor (or virtual machine monitor, VMM, virtualizer) is software that allows multiple operating systems to share a single hardware host system. A hypervisor is similar to an emulator; it is computer software, firmware or hardware that creates and runs virtual machines. A computer on which a hypervisor runs one or more virtual machines is called a host machine, and each virtual machine is called a guest machine. The hypervisor presents the guest operating systems with a virtual operating platform and manages the execution of the guest operating systems. \n\n Multiple instances of a variety of operating systems may share the virtualized hardware resources: for example, Linux, Windows, and macOS instances can all run on a single physical x86 machine. This contrasts with operating-system–level virtualization, where all instances (usually called containers) must share a single kernel, though the guest operating systems can differ in user space, such as different Linux distributions with the same kernel.",
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
            "definition": "YAML is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted. YAML targets many of the same communications applications as Extensible Markup Language (XML) but has a minimal syntax. It uses both Python-style indentation to indicate nesting, and a more compact format that uses [...] for lists and {...} for maps, thus JSON files are valid as of YAML 1.2. \n\n The official recommended filename extension for YAML files has been .yaml since 2006. Support for reading and writing YAML is available for many programming languages. Some source-code editors such as Vim, Emacs, and various integrated development environments have features that make editing YAML easier, such as folding up nested structures or automatically highlighting syntax errors.",
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
            "definition": "Network neutrality, most commonly called net neutrality, is the principle that Internet service providers (ISPs) must treat all Internet communications equally, and not charge users different rates based on content, website, platform, application, type of equipment, source address, destination address, or method of communication. \n\n With net neutrality, ISPs may not intentionally block, slow down, or charge money for specific online content. Without net neutrality, ISPs may prioritize certain types of traffic, meter others, or potentially block traffic from specific services, while charging consumers for various tiers of service.",
            "url": "https://en.wikipedia.org/wiki/Net_neutrality",
            "id": 65      
        },           
        {
            "name": "Non-fungible token (NFT)",
            "definition": "A non-fungible token (NFT) is a unique, non-interchangeable unit of data stored on a blockchain, a form of digital ledger, that can be sold and traded. Types of NFT data units may be associated with digital files such as photos, videos, and audio. Because each token is uniquely identifiable, NFTs differ from blockchain cryptocurrencies, such as Bitcoin. \n\n NFT ledgers claim to provide a public certificate of authenticity or proof of ownership, but the legal rights conveyed by an NFT can be uncertain. NFTs do not restrict the sharing or copying of the underlying digital files, do not necessarily convey the copyright of the digital files, and do not prevent the creation of NFTs with identical associated files.",
            "url": "Non-fungible token",
            "id": 66     
        },         
        {
            "name": "Metaverse",
            "definition": "A metaverse is a network of 3D virtual worlds focused on social connection. In futurism and science fiction, it is often described as a hypothetical iteration of the Internet as a single, universal virtual world that is facilitated by the use of virtual and augmented reality headsets. \n\n The term ‘metaverse’ has its origins in the 1992 science fiction novel Snow Crash as a portmanteau of ‘meta’ and ‘universe.’ Various metaverses have been developed for popular use such as virtual world platforms like Second Life. Some metaverse iterations involve integration between virtual and physical spaces and virtual economies. Demand for increased immersion means metaverse development is often linked to advancing virtual reality technology.",
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
            "name": "Wantrepreneur",
            "definition": "Someone who would like to start a business and thinks and talks about doing so, but never gets started.",
            "url": "https://www.entrepreneur.com/article/242451",
            "id": 71     
        },          
        {
            "name": "Robotic process automation",
            "definition": "Robotic process automation (RPA) is a form of business process automation technology based on metaphorical software robots (bots) or on artificial intelligence (AI)/digital workers. It is sometimes referred to as software robotics (not to be confused with robot software). \n\n In traditional workflow automation tools, a software developer produces a list of actions to automate a task and interface to the back end system using internal application programming interfaces (APIs) or dedicated scripting language. In contrast, RPA systems develop the action list by watching the user perform that task in the application's graphical user interface (GUI), and then perform the automation by repeating those tasks directly in the GUI. This can lower the barrier to the use of automation in products that might not otherwise feature APIs for this purpose. \n\n RPA tools have strong technical similarities to graphical user interface testing tools. These tools also automate interactions with the GUI, and often do so by repeating a set of demonstration actions performed by a user. RPA tools differ from such systems in that they allow data to be handled in and between multiple applications, for instance, receiving email containing an invoice, extracting the data, and then typing that into a bookkeeping system.",
            "url": "https://en.wikipedia.org/wiki/Robotic_process_automation",
            "id": 72     
        },           
        {
            "name": "Neural networks",
            "definition": "Artificial neural networks (ANNs), usually simply called neural networks (NNs), are computing systems inspired by the biological neural networks that constitute animal brains. \n\n A neural network is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain. Each connection, like the synapses in a biological brain, can transmit a signal to other neurons. An artificial neuron receives a signal then processes it and can signal neurons connected to it.",
            "url": "https://en.wikipedia.org/wiki/Artificial_neural_network",
            "id": 73      
        },           
        {
            "name": "Hyperautomation",
            "definition": "Hyperautomation is the application of advanced technologies like RPA, artificial intelligence, machine learning (ML) and process mining to augment workers and automate processes in ways that are significantly more impactful than traditional automation capabilities. Hyperautomation is the combination of automation tools and technologies to deliver work.",
            "url": "https://en.wikipedia.org/wiki/Robotic_process_automation#Hyperautomation",
            "id": 74     
        },          
        {
            "name": "Full-stack observability",
            "definition": "Full-stack observability is the ability to understand at any time what is happening across a technology stack. By collecting, correlating, and aggregating all telemetry in the components, it provides insight into the behavior, performance, and health of a system. Through full-stack observability, teams can deeply understand the dependencies across domains and system topology. \n\n Contrary to traditional monitoring systems, full-stack observability enables IT teams to proactively react, predict, and prevent problems using artificial intelligence and machine learning, which is all but a requirement considering that the amount of data collected would be nearly impossible otherwise. Presenting this data in the form of unified analytics and dashboards can give the observer a complete picture into the health of the system, for example, where issues occurred and solutions were introduced.",
            "url": "https://www.appdynamics.com/topics/what-is-full-stack-observability",
            "id": 75     
        },         
        {
            "name": "Extended reality (XR)",
            "definition": "Extended reality (XR) is a term referring to all real-and-virtual combined environments and human-machine interactions generated by computer technology and wearables. E.g. It includes representative forms such as augmented reality (AR), mixed reality (MR) and virtual reality (VR) and the areas interpolated among them. The levels of virtuality range from partially sensory inputs to immersive virtuality, also called VR. \n\n XR is a superset which includes the entire spectrum from ‘the complete real’ to ‘the complete virtual’ in the concept of reality–virtuality continuum introduced by Paul Milgram. Still, its connotation lies in the extension of human experiences especially relating to the senses of existence (represented by VR) and the acquisition of cognition (represented by AR). With the continuous development in human–computer interactions, this connotation is still evolving. \n\n XR is a rapid growing field being applied in a wide range of ways, such as entertainment, marketing, real-estate, training and remote work.",
            "url": "https://en.wikipedia.org/wiki/Extended_reality",
            "id": 76      
        },          
        {
            "name": "5G",
            "definition": "In telecommunications, 5G is the fifth-generation technology standard for broadband cellular networks, which cellular phone companies began deploying worldwide in 2019, and is the planned successor to the 4G networks which provide connectivity to most current cellphones. 5G networks are predicted to have more than 1.7 billion subscribers worldwide by 2025, according to the GSM Association. \n\n Like its predecessors, 5G networks are cellular networks, in which the service area is divided into small geographical areas called cells. All 5G wireless devices in a cell are connected to the Internet and telephone network by radio waves through a local antenna in the cell. The new networks is that they will have greater bandwidth, giving higher download speeds, eventually up to 10 gigabits per second (Gbit/s). \n\n In addition to 5G being faster than existing networks, 5G has higher bandwidth and can thus connect more different devices, improving the quality of Internet services in crowded areas. Due to the increased bandwidth, it is expected the networks will increasingly be used as general internet service providers (ISPs) for laptops and desktop computers, competing with existing ISPs such as cable internet, and also will make possible new applications in internet-of-things (IoT) and machine-to-machine areas. Cellphones with 4G capability alone are not able to use the new networks, which require 5G-enabled wireless devices.",
            "url": "https://en.wikipedia.org/wiki/5G",
            "id": 77     
        },          
        {
            "name": "Voice-user interface (VUI)",
            "definition": "A voice-user interface (VUI) makes spoken human interaction with computers possible, using speech recognition to understand spoken commands and answer questions, and typically text to speech to play a reply. A voice command device (VCD) is a device controlled with a voice user interface. \n\n Voice user interfaces have been added to automobiles, home automation systems, computer operating systems, home appliances like washing machines and microwave ovens, and television remote controls. They are the primary way of interacting with virtual assistants on smartphones and smart speakers.",
            "url": "https://en.wikipedia.org/wiki/Voice_user_interface",
            "id": 78     
        },          
        {
            "name": "Web3",
            "definition": "Web3 (also known as Web 3.0 and sometimes stylized as web3) is an idea for a new iteration of the World Wide Web based on blockchain technology, which incorporates concepts such as decentralization and token-based economics. Some technologists and journalists have contrasted it with Web 2.0, wherein they say data and content are centralized in a small group of companies sometimes referred to as ‘Big Tech’. \n\n The term ‘Web3’ was coined in 2014 by Ethereum co-founder Gavin Wood, and the idea gained interest in 2021 from cryptocurrency enthusiasts, large technology companies, and venture capital firms. Some experts argue that web3 will provide increased data security, scalability, and privacy for users and combat the influence of large technology companies. Others have raised concerns about a decentralized web, citing the potential for low moderation and the proliferation of harmful content, the centralization of wealth to a small group of investors and individuals, or a loss of privacy due to more expansive data collection.",
            "url": "https://en.wikipedia.org/wiki/Web3",
            "id": 79     
        },          
        {
            "name": "Multiexperience (MX)",
            "definition": "An experience composed by several modes (touch, voice, and gesture, for example), devices, and applications with which users interact through digital itineraries with different points of contact. The development of a multi-experience involves the creation of applications that are suitable to its purpose, basing on the specific categories of the point of contact, while guaranteeing a consistent user experience on various mobile, wearable, conversational and immersive (AR / VR) devices. \n\n These devices currently support pressure detectors, luminosity, proximity, sound, inclination, movement, and orientation sensors that facilitate obtaining and integrating real data, as well as providing timely feedback. Multiexperience may embody the biggest UX challenge since the birth of the smartphone, as UI/UX Designers must move beyond the limitations of a GUI-only interface while taking into account the world as it will be experienced by users in the future.",
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
            "definition": "Data mining is a process of extracting and discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.  Data mining is an interdisciplinary subfield of computer science and statistics with an overall goal of extracting information (with intelligent methods) from a data set and transforming the information into a comprehensible structure for further use. \n\n The term ‘data mining’ is a misnomer, because the goal is the extraction of patterns and knowledge from large amounts of data, not the extraction (mining) of data itself. It also is a buzzword and is frequently applied to any form of large-scale data or information processing (collection, extraction, warehousing, analysis, and statistics) as well as any application of computer decision support system, including artificial intelligence (e.g., machine learning) and business intelligence.",
            "url": "https://en.wikipedia.org/wiki/Data_mining",
            "id": 82     
        },          
        {
            "name": "Machine learning operations (MLOps)",
            "definition": "MLOps or ML Ops is a set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently. The word is a compound of ‘machine learning’ and the continuous development practice of DevOps in the software field. Machine learning models are tested and developed in isolated experimental systems. When an algorithm is ready to be launched, MLOps is practiced between Data Scientists, DevOps, and Machine Learning engineers to transition the algorithm to production systems. \n\n Similar to DevOps or DataOps approaches, MLOps seeks to increase automation and improve the quality of production models, while also focusing on business and regulatory requirements. While MLOps started as a set of best practices, it is slowly evolving into an independent approach to ML lifecycle management. \n\n MLOps applies to the entire lifecycle - from integrating with model generation (software development lifecycle, continuous integration/continuous delivery), orchestration, and deployment, to health, diagnostics, governance, and business metrics. According to Gartner, MLOps is a subset of ModelOps. MLOps is focused on the operationalization of ML models, while ModelOps covers the operationalization of all types of AI models.",
            "url": "https://en.wikipedia.org/wiki/MLOps",
            "id": 83     
        },          
        {
            "name": "Internet of things (IoT)",
            "definition": "The Internet of things (IoT) describes physical objects (or groups of such objects) with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks. Internet of things has been considered a misnomer because devices do not need to be connected to the public internet, they only need to be connected to a network and be individually addressable. \n\n The field of IoT has evolved due to the convergence of multiple technologies, including ubiquitous computing, commodity sensors, increasingly powerful embedded systems, and machine learning. Traditional fields of embedded systems, wireless sensor networks, control systems, automation (including home and building automation), independently and collectively enable the Internet of things. In the consumer market, IoT technology is most synonymous with products pertaining to the concept of the ‘smart home’, including devices and appliances (such as lighting fixtures, thermostats, home security systems, cameras, and other home appliances) that support one or more common ecosystems, and can be controlled via devices associated with that ecosystem, such as smartphones and smart speakers. IoT is also used in healthcare systems.",
            "url": "https://en.wikipedia.org/wiki/Internet_of_things",
            "id": 84     
        },          
        {
            "name": "Machine learning (ML)",
            "definition": "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks. \n\n A subset of machine learning is closely related to computational statistics, which focuses on making predictions using computers; but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a related field of study, focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning use data and neural networks in a way that mimics the working of a biological brain. In its application across business problems, machine learning is also referred to as predictive analytics.",
            "url": "https://en.wikipedia.org/wiki/Machine_learning",
            "id": 85     
        },           
        {
            "name": "Always On VPN (AOVPN)",
            "definition": "Microsoft’s Always On VPN is the revamp of DirectAccess remote access technology seeking to overcome the limitations of DirectAccess and achieve much wider adoption. With the new Always On VPN technology, Microsoft is looking to achieve a single solution of remote access that supports a wide array of clients. Like DirectAccess, the VPN connection is ‘Always On’ meaning there is no user input required unless multi-factor authentication is enabled. As soon as a client is connected to the Internet, the VPN connection is established. \n\n AOVPN’s range of supported clients, unlike DirectAccess, includes more than simply domain-joined clients: Domain-joined, Non Domain-joined, Azure AD-joined devices, BYOD. Microsoft’s AOVPN applies to to the Microsoft Windows Server and Windows operating systems. Such as Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2 and Windows 10.",
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
            "definition": "In computing, an attribute is a specification that defines a property of an object, element, or file. It may also refer to or set the specific value for a given instance of such. For clarity, attributes should more correctly be considered metadata. \n\n An attribute is frequently and generally a property of a property. However, in actual usage, the term attribute can and is often treated as equivalent to a property depending on the technology being discussed. An attribute of an object usually consists of a name and a value; of an element, a type or class name; of a file, a name and extension.",
            "url": "https://en.wikipedia.org/wiki/Attribute_(computing)",
            "id": 88     
        },        
        {
            "name": "Frontend and backend",
            "definition": "In software engineering, the terms frontend and backend (or sometimes referred to as back end or back-end) refer to the separation of concerns between the presentation layer (frontend), and the data access layer (backend) of a piece of software, or the physical infrastructure or hardware. \n\n In the client–server model, the client is usually considered the frontend and the server is usually considered the backend, even when some presentation work is actually done on the server itself.",
            "url": "https://en.wikipedia.org/wiki/Frontend_and_backend",
            "id": 89     
        },        
        {
            "name": "Cache",
            "definition": "In computing, a cache is a hardware or software component that stores data so that future requests for that data can be served faster; the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere. \n\n A cache hit occurs when the requested data can be found in a cache, while a cache miss occurs when it cannot. Cache hits are served by reading data from the cache, which is faster than recomputing a result or reading from a slower data store; thus, the more requests that can be served from the cache, the faster the system performs.",
            "url": "https://en.wikipedia.org/wiki/Cache_(computing)",
            "id": 90     
        },        
        {
            "name": "Content management system (CMS)",
            "definition": "Computer software used to manage the creation and modification of digital content (content management). Features of CMS may include: \n\n \n\n - Format management facilitates turning scanned paper documents and legacy electronic documents into HTML or PDF documents. \n - Publishing functionality allows individuals to use a template or a set of templates approved by the organization, as well as wizards and other tools to create or modify content. \n - Revision features allow content to be updated and edited after initial publication. Revision control also tracks any changes made to files by individuals. \n\n A CMS typically has two major components: a content management application (CMA), as the front-end user interface that allows a user, even with limited expertise, to add, modify, and remove content from a website without the intervention of a webmaster; and a content delivery application (CDA), that compiles the content and updates the website.",
            "url": "https://en.wikipedia.org/wiki/Content_management_system",
            "id": 91     
        },  
        {
            "name": "Web crawler",
            "definition": "A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering). \n\n Web search engines and some other websites use Web crawling or spidering software to update their web content or indices of other sites' web content. Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently. \n\n Crawlers consume resources on visited systems and often visit sites unprompted. Issues of schedule, load, and 'politeness' come into play when large collections of pages are accessed. Mechanisms exist for public sites not wishing to be crawled to make this known to the crawling agent. For example, including a robots.txt file can request bots to index only parts of a website, or nothing at all.",
            "url": "https://en.wikipedia.org/wiki/Web_crawler",
            "id": 92     
        },        
        {
            "name": "Customer relationship management (CRM)",
            "definition": "Customer relationship management (CRM) is a process in which a business or other organization administers its interactions with customers, typically using data analysis to study large amounts of information. \n\n CRM systems compile data from a range of different communication channels, including a company's website, telephone, email, live chat, marketing materials and more recently, social media. They allow businesses to learn more about their target audiences and how to best cater for their needs, thus retaining customers and driving sales growth. \n\n CRM may be used with past, present or potential customers. The concepts, procedures, and rules that a corporation follows when communicating with its consumers are referred to as CRM.",
            "url": "https://en.wikipedia.org/wiki/Customer_relationship_management",
            "id": 93     
        },        
        {
            "name": "CSS (Cascading Style Sheets)",
            "definition": "Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript. \n\n CSS is designed to enable the separation of presentation and content, including layout, colors, and fonts. This separation can improve content accessibility; provide more flexibility and control in the specification of presentation characteristics; enable multiple web pages to share formatting by specifying the relevant CSS in a separate .css file, which reduces complexity and repetition in the structural content; and enable the .css file to be cached to improve the page load speed between the pages that share the file and its formatting.",
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
            "definition": "The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript. Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document. \n\n HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags but use them to interpret the content of the page. \n\n HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997. A form of HTML, known as HTML5, is used to display video and audio, primarily using the <canvas> element, in collaboration with javascript.",
            "url": "https://en.wikipedia.org/wiki/HTML",
            "id": 97     
        },        
        {
            "name": "Meta element",
            "definition": "Meta elements are tags used in HTML and XHTML documents to provide structured metadata about a Web page. They are part of a web page's head section. Multiple Meta elements with different attributes can be used on the same page. Meta elements can be used to specify page description, keywords and any other metadata not provided through the other head elements and attributes. The meta element has two uses: either to emulate the use of an HTTP response header field, or to embed additional metadata within the HTML document. e.g. \n\n <meta name='generator' content='MediaWiki 1.39.0-wmf.7'> \n <meta name='referrer' content='origin-when-cross-origin'>",
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
            "definition": "Commercial off-the-shelf or commercially available off-the-shelf (COTS) products are packaged or canned (ready-made) hardware or software, which are adapted aftermarket to the needs of the purchasing organization, rather than the commissioning of custom-made, or bespoke, solutions. A related term, Mil-COTS, refers to COTS products for use by the U.S. military. \n\n In the context of the U.S. government, the Federal Acquisition Regulation (FAR) has defined ‘COTS’ as a formal term for commercial items, including services, available in the commercial marketplace that can be bought and used under government contract. For example, Microsoft is a COTS software provider. COTS purchases are alternatives to custom software or one-off developments – government-funded developments or otherwise. \n\n Although COTS products can be used out of the box, in practice the COTS product must be configured to achieve the needs of the business and integrated to existing organizational systems. Extending the functionality of COTS products via custom development is also an option, however this decision should be carefully considered due to the long term support and maintenance implications. Such customized functionality is not supported by the COTS vendor, so brings its own sets of issues when upgrading the COTS product. \n\n The use of COTS has been mandated across many government and business programs, as such products may offer significant savings in procurement, development, and maintenance. In the 1990s, many regarded COTS as extremely effective in reducing the time and cost of software development.  COTS software came with many not-so-obvious tradeoffs— a reduction in initial cost and development time over an increase in software component-integration work, dependency on the vendor, security issues and incompatibilities from future changes.",
            "url": "https://en.wikipedia.org/wiki/Commercial_off-the-shelf",
            "id": 100     
        },        
        {
            "name": "Responsive design",
            "definition": "Responsive web design (RWD) or responsive design is an approach to web design that aims to make web pages render well on a variety of devices and window or screen sizes from minimum to maximum display size to ensure usability and satisfaction. \n\n A responsive design adapts the web-page layout to the viewing environment by using techniques such as fluid proportion-based grids, flexible images, and CSS3 media queries, an extension of the @media rule, in the following ways: \n\n\n 1. The fluid grid concept calls for page element sizing to be in relative units like percentages, rather than absolute units like pixels or points. \n 2. Flexible images are also sized in relative units, so as to prevent them from displaying outside their containing element. \n 3. Media queries allow the page to use different CSS style rules based on characteristics of the device the site is being displayed on, e.g. width of the rendering surface (browser window width or a physical display size). \n 4. Responsive layouts automatically adjust and adapt to any device screen size, whether it is a desktop, a laptop, a tablet, or a mobile phone. \n\n\n Responsive web design became more important as users of mobile devices came to account for the majority of web site visitors",
            "url": "https://en.wikipedia.org/wiki/Responsive_web_design",
            "id": 101     
        },        
        {
            "name": "UI vs. UX",
            "definition": "A user interface (UI) is a place where interactions between humans and machines occur. It allows users to effectively operate a machine to complete a task or achieve a specific goal, like making a purchase or downloading an app. The three most common UIs are the command line interface, graphic user interface, and voice-enabled user interface. Essential properties of a well-designed UI include clarity, familiarity, consistency, forgiveness and efficiency. The primary interface design techniques are prototyping and simulation. \n\n User experience (UX) is the experience that a person has as they interact with a product. The term was coined by Don Norman back in the 90s when he worked at Apple. Don Norman says that ‘’User experience’ encompasses all aspects of the end-users interaction with the company, its services, and its products.’ UX designers incorporate the ideas of user persona and user journey into their research and design. These understandings help them to propose design solutions that works the best for their users. \n\n The meanings of UX and UI imply that they are related design disciplines, yet they are very different in nature. The UI design is more concerned with the visual properties of design as well as the overall feel it conveys (i.e., is it aesthetically pleasing?). UX design is more analytical; It’s rooted in cognitive behavior and human psychology.",
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
            "definition": "Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: the presentation tier, or user interface; the application tier, where data is processed; and the data tier, where the data associated with the application is stored and managed. \n\n The chief benefit of three-tier architecture is that because each tier runs on its own infrastructure, each tier can be developed simultaneously by a separate development team, and can be updated or scaled as needed without impacting the other tiers. Three-tier architecture is the predominant software architecture for traditional client-server applications. \n\n A 3-tier application is a program that is organized into three major parts: the workstation or presentation interface; the business logic; and the database and related programming. Each of these is distributed to one or more separate places on a network.",
            "url": "https://www.ibm.com/cloud/learn/three-tier-architecture",
            "id": 104     
        },        
        {
            "name": "Agile software development",
            "definition": "In software development, agile (sometimes written Agile) practices include requirements discovery and solutions improvement through the collaborative effort of self-organizing and cross-functional teams with their customer(s)/end user(s), adaptive planning, evolutionary development, early delivery, continual improvement, and flexible responses to changes in requirements, capacity, and understanding of the problems to be solved. \n\n Popularized in the 2001 Manifesto for Agile Software Development, these values and principles were derived from and underpin a broad range of software development frameworks, including Scrum and Kanban.",
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
            "definition": "An anti-pattern in software engineering, project management, and business processes is a common response to a recurring problem that is usually ineffective and risks being highly counterproductive. The term, coined in 1995 by computer programmer Andrew Koenig, was inspired by the book Design Patterns (which highlights a number of design patterns in software development that its authors considered to be highly reliable and effective) and first published in his article in the Journal of Object-Oriented Programming. A further paper in 1996 presented by Michael Ackroyd at the Object World West Conference also documented anti-patterns. \n\n It was, however, the 1998 book AntiPatterns that both popularized the idea and extended its scope beyond the field of software design to include software architecture and project management. Other authors have extended it further since to encompass environmental/organizational/cultural anti-patterns.",
            "url": "https://en.wikipedia.org/wiki/Anti-pattern",
            "id": 107     
        },        
        {
            "name": "Aspect-Oriented Programming (AOP)",
            "definition": "Aspect-Oriented Programming (AOP). Nearly all programming paradigms support some level of grouping and encapsulation of concerns into separate, independent entities. Aspect-oriented programming entails breaking down program logic into distinct parts (so-called concerns, which are cohesive areas of functionality). AOP aims to increase modularity by allowing the separation of cross-cutting concerns. \n\n  Systems are composed of several components, each responsible for a specific piece of functionality. But often these components also carry additional responsibilities beyond their core functionality. System services such as logging, transaction management, and security often find their way into components whose core responsibilities is something else. These system services are commonly referred to as cross-cutting concerns because they tend to cut across multiple components in a system. Logging exemplifies a crosscutting concern because a logging strategy necessarily affects every logged part of the system. Logging thereby crosscuts all logged classes and methods.  \n\n Aspect-oriented programming allows for the creation of relationships between different classes. These relationships are arbitrary, but can be used to encapsulate the housekeeping code needed to create compatibility between two classes. \n\n AOP is a technique for building common, reusable routines that can be applied applicationwide. During development this facilitates separation of core application logic and common, repeatable tasks (input validation, logging, error handling, etc.). At runtime, you can use AOP to hot-patch applications that are vulnerable to SQL injection, or embed intrusion detection and audit logging capabilities directly into an application without modifying the underlying source code.",
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
            "definition": "Data modeling in software engineering is the process of creating a data model for an information system by applying certain formal techniques. Data modeling is a process used to define and analyze data requirements needed to support the business processes within the scope of corresponding information systems in organizations. Therefore, the process of data modeling involves professional data modelers working closely with business stakeholders, as well as potential users of the information system. \n\n Data modeling techniques and methodologies are used to model data in a standard, consistent, predictable manner in order to manage it as a resource. The use of data modeling standards is strongly recommended for all projects requiring a standard means of defining and analyzing data within an organization, e.g., using data modeling: \n\n - to assist business analysts, programmers, testers, manual writers, IT package selectors, engineers, managers, related organizations and clients to understand and use an agreed upon semi-formal model that encompasses the concepts of the organization and how they relate to one another \n - to manage data as a resource \n - to integrate information systems \n - to design databases/data warehouses (aka data repositories) \n\n Data modeling may be performed during various types of projects and in multiple phases of projects. Data models are progressive; there is no such thing as the final data model for a business or application. Instead a data model should be considered a living document that will change in response to a changing business. The data models should ideally be stored in a repository so that they can be retrieved, expanded, and edited over time.",
            "url": "https://en.wikipedia.org/wiki/Data_modeling",
            "id": 110     
        },        
        {
            "name": "Driver",
            "definition": "In computing, a device driver is a computer program that operates or controls a particular type of device that is attached to a computer or automaton.[1] A driver provides a software interface to hardware devices, enabling operating systems and other computer programs to access hardware functions without needing to know precise details about the hardware being used. \n\n A driver communicates with the device through the computer bus or communications subsystem to which the hardware connects. When a calling program invokes a routine in the driver, the driver issues commands to the device (drives it). Once the device sends data back to the driver, the driver may invoke routines in the original calling program. \n\n Drivers are hardware dependent and operating-system-specific. They usually provide the interrupt handling required for any necessary asynchronous time-dependent hardware interface. \n\n Previously, we have been describing a hardware device driver. Now, a driver in software provides a programming interface to control and manage specific lower level interfaces that are often linked to a specific type of hardware, or other low-level service. In the case of hardware, the specific subclass of drivers controlling physical or virtual hardware devices are known as device drivers. E.g., a client library for connecting to a database is often known as a driver, for example the MySQL native driver for PHP.",
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
            "name": "Ergonomics",
            "definition": "The science of refining the design of products to optimize them for human use. Human characteristics, such as height, weight, and proportions are considered, as well as information about human hearing, sight, temperature preferences, and so on.",
            "url": "https://en.wikipedia.org/wiki/Human_factors_and_ergonomics",
            "id": 108     
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
            "definition": "A software development methodology intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development, it advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted. \n\n Other elements of extreme programming include: programming in pairs or doing extensive code review, unit testing of all code, not programming features until they are actually needed, a flat management structure, code simplicity and clarity, expecting changes in the customer's requirements as time passes and the problem is better understood, and frequent communication with the customer and among programmers.",
            "url": "https://en.wikipedia.org/wiki/Extreme_programming",
            "id": 115     
        },        
        {
            "name": "Feature creep",
            "definition": "Feature creep is the excessive ongoing expansion or addition of new features in a product, especially in computer software, video games and consumer and business electronics. These extra features go beyond the basic function of the product and can result in software bloat and over-complication, rather than simple design. The definition of what qualifies as 'feature creep' does vary among end users, where what is perceived as such by some users may be considered practical functionality by others. \n\n The most common cause of feature creep is the desire to provide the consumer with a more useful or desirable product, in order to increase sales or distribution. However, once the product reaches the point at which it does everything that it is designed to do, the manufacturer is left with the choice between adding functions some users might consider unneeded (sometimes at the cost of efficiency), and sticking with the old version (at the cost of a perceived lack of improvement). \n\n Another major cause of feature creep might be a compromise from a committee which decides to implement multiple, different viewpoints or use cases in the same product. Then, as more features are added to support each approach, it might be necessary to have cross-conversion features between the multiple paradigms, further complicating the total features.",
            "url": "https://en.wikipedia.org/wiki/Feature_creep",
            "id": 116     
        },        
        {
            "name": "Functional specification",
            "definition": "A functional specification (also, functional spec, specs, functional specifications document (FSD), functional requirements specification) in systems engineering and software development is a document that specifies the functions that a system or component must perform (often part of a requirements specification).\n\n The documentation typically describes what is needed by the system user as well as requested properties of inputs and outputs (e.g. of the software system). A functional specification is the more technical response to a matching requirements document, e.g. the Product Requirements Document ‘PRD’. Thus it picks up the results of the requirements analysis stage. On more complex systems multiple levels of functional specifications will typically nest to each other, e.g. on the system level, on the module level and on the level of technical details.",
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
            "definition": "Generic programming is a style of computer programming in which algorithms are written in terms of types to-be-specified-later that are then instantiated when needed for specific types provided as parameters. This approach, pioneered by the ML programming language in 1973, permits writing common functions or types that differ only in the set of types on which they operate when used, thus reducing duplication. Such software entities are known as generics in Ada, C#, Delphi, Eiffel, F#, Java, Nim, Python, Go, Rust, Swift, TypeScript and Visual Basic .NET. They are known as parametric polymorphism in ML, Scala, Julia, and Haskell (the Haskell community also uses the term 'generic' for a related but somewhat different concept); templates in C++ and D; and parameterized types in the influential 1994 book Design Patterns. \n\n The term 'generic programming' was originally coined by David Musser and Alexander Stepanov in a more specific sense than the above, to describe a programming paradigm whereby fundamental requirements on types are abstracted from across concrete examples of algorithms and data structures and formalized as concepts, with generic functions implemented in terms of these concepts, typically using language genericity mechanisms as described above.",
            "url": "https://en.wikipedia.org/wiki/Generic_programming",
            "id": 120     
        },        
        {
            "name": "Gold code",
            "definition": "Program source code that is ready for commercial distribution. Gold code is the final form of software code before the software's commercial release. A software usually undergoes several development phases before it becomes gold code. First, software functions are individually developed and tested with each newly added function. Then, a graphical user interface is added so that users can perform functions via several means, including buttons, task bars and keyboard shortcuts. Finally, a team tests different function sequences to ensure there are no hidden bugs. \n\n When a vendor says its product ‘has gone gold’, it means the source code has been compiled into an executable program ready for sale. The next steps are to turn it into an installable product and create a CD or DVD ‘golden master’ (GM) for the disc manufacturer or into a file for Web downloads.",
            "url": "https://www.techopedia.com/definition/16387/gold-code",
            "id": 121     
        },        
        {
            "name": "Patch vs Hotfix vs Coldfix vs Bugfix",
            "definition": "Patch vs Hotfix vs Coldfix vs Bugfix. Patches are often temporary fixes between full releases of software packages. Patches are used to correct both large and small issues that may or may not require fixing a software bug, installing new drivers, addressing new security vulnerabilities, addressing software stability issues or upgrading the software. Generally, patches are automatic updates that self-install packages in various sizes and are delivered on a set schedule. They can be included in the product’s new version release with additional updates and fixes. \n\n Hotfixes can also solve many of the same issues as a patch, but it is applied to a ‘hot’ system—a live system—to fix an issue immediately and without creating system downtimes or outages. Normally, you’ll create a hotfix quickly, as an urgent measure against issues that need to be fixed immediately and outside of your normal development flow. Unlike patches, hotfixes address very specific issues like adding a new feature, bug, or security fix or changing database schema. Importantly, hotfixes are not always publicly released, in contrast to patches. \n\n Where a hotfix is executed quickly without restarting any systems or hardware, a coldfix is just the opposite. Implementing a coldfix requires users to log out of the software while entire systems need to be rebooted for fixes to go into effect. They’re normally announced several days ahead of time to give users advanced notice the service will be unavailable while the fix is completed. Notices generally include estimated times the service will be back online. \n\n A bugfix sounds a lot like a hotfix, but the difference lies in the timing and execution of the correction. Bugfixes generally describe issues that are found and resolved during production or testing phases or even after deployment as part of the normal release cycle of a product. Hotfixes are applied only after the product has been released and is live. Implementing a bugfix, also known as a program temporary fix (PTF), can be as simple as adding missing parentheses in a piece of code. But the fix can become quite challenging if the symptoms don’t clearly point to a cause. Once you’ve uncovered the root cause and issued a bug fix, it’s not uncommon for your programmers to find that one bugfix can actually introduce a new bug.",
            "url": "https://www.bmc.com/blogs/patch-hotfix-coldfix-bugfix/",
            "id": 122     
        },        
        {
            "name": "Integrated development environment (IDE)",
            "definition": "An Integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. Some IDEs, such as NetBeans and Eclipse, contain the necessary compiler, interpreter, or both; others, such as SharpDevelop and Lazarus, do not. \n\n The boundary between an IDE and other parts of the broader software development environment is not well-defined; sometimes a version control system or various tools to simplify the construction of a graphical user interface (GUI) are integrated. Many modern IDEs also have a class browser, an object browser, and a class hierarchy diagram for use in object-oriented software development.",
            "url": "https://en.wikipedia.org/wiki/Integrated_development_environment",
            "id": 123     
        },        
        {
            "name": "Independent software vendor (ISV)",
            "definition": "An independent software vendor, or ISV, is an individual or organization that develops, markets, and sells software solutions that run on one or more computer hardware providers like Macintosh, operating systems like iOS, or cloud platforms like Amazon Web Services. \n\n Computer hardware providers, operating systems, and cloud platforms will all test independent software vendors who want to offer their software solutions on their marketplace. But they’ll only allow, or ISV certify, the independent software vendors who can offer the most relevant and best software solutions on their marketplaces. \n\n For example, Microsoft, a company that develops computer hardware (Xbox), operating systems (Windows), and a cloud platform (Azure), offers silver and gold ISV certifications to independent software vendors whose products can pass their rigorous quality tests and prove they can offer the top software solutions to Microsoft’s customers on each of their marketplaces.",
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
            "definition": "Lean software development is a translation of lean manufacturing principles and practices to the software development domain. Adapted from the Toyota Production System, it is emerging with the support of a pro-lean subculture within the agile community. Lean offers a solid conceptual framework, values and principles, as well as good practices, derived from experience, that support agile organizations. \n\n Lean development can be summarized by seven principles, very close in concept to lean manufacturing principles: \n 1. Eliminate waste \n 2. Amplify learning \n 3. Decide as late as possible \n 4. Deliver as fast as possible \n 5. Empower the team \n 6. Build integrity in \n 7. Optimize the whole \n",
            "url": "https://en.wikipedia.org/wiki/Lean_software_development",
            "id": 128      
        }, 
        {
            "name": "Legacy system",
            "definition": "In computing, a legacy system is an old method, technology, computer system, or application program, ‘of, relating to, or being a previous or outdated computer system,’ yet still in use. Often referencing a system as ‘legacy’ means that it paved the way for the standards that would follow it. This can also imply that the system is out of date or in need of replacement. \n\n Legacy code is old computer source code. It could simply refer to an organization's existing code base which has been written over many years, or it could imply a codebase that is in some respect obsolete or supporting something obsolete. Long-lived code is susceptible to software rot, where changes to the runtime environment, or surrounding software or hardware may require maintenance or emulation of some kind to keep working. Legacy code may be present to support legacy hardware, a separate legacy system, or a legacy customer using an old feature or software version.",
            "url": "https://en.wikipedia.org/wiki/Legacy_system",
            "id": 129      
        }, 
        {
            "name": "Object-oriented programming (OOP)",
            "definition": "Object-oriented programming (OOP) is a programming paradigm based on the concept of ‘objects’, which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). \n\n A feature of objects is that an object's own procedures can access and often modify the data fields of itself (objects have a notion of this or self). In OOP, computer programs are designed by making them out of objects that interact with one another. OOP languages are diverse, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types. \n\n Many of the most widely used programming languages (such as C++, Java, Python, etc.) are multi-paradigm and they support object-oriented programming to a greater or lesser degree, typically in combination with imperative, procedural programming. Significant object-oriented languages include: Java, C++, C#, Python, R, PHP, Visual Basic.NET, JavaScript, Ruby, Perl, SIMSCRIPT, Object Pascal, Objective-C, Dart, Swift, Scala, Kotlin, Common Lisp, MATLAB, and Smalltalk.",
            "url": "https://en.wikipedia.org/wiki/Object-oriented_programming",
            "id": 130      
        },   
        {
            "name": "Pasta theory of programming",
            "definition": "Pasta theory of programming. The idea that various programming structures can be likened to the structures of well-known pasta dishes: \n\n Unstructured procedural programming is called spaghetti code. Spaghetti code is often considered a pejorative phrase for unstructured and difficult-to-maintain source code. In this sense, spaghetti code can be caused by several factors, such as volatile project requirements, lack of programming style rules, and software engineers with insufficient ability or experience. \n\n Lasagna code refers to structured programming code whose layers are so complicated and intertwined that making a change in one layer would necessitate changes in all other layers. \n\n Ravioli code is a term specific to object-oriented programming. It describes code that comprises well-structured classes that are easy to understand in isolation, but difficult to understand as a whole.",
            "url": "https://en.wikipedia.org/wiki/Spaghetti_code",
            "id": 131      
        },     
        {
            "name": "Polymorphism",
            "definition": "Polymorphism is an object-oriented programming concept that refers to the ability of a variable, function or object to take on multiple forms. A language that features polymorphism allows developers to program in the general rather than program in the specific. \n\n In a programming language that exhibits polymorphism, objects of classes belonging to the same hierarchical tree (inherited from a common base class) may possess functions bearing the same name, but each having different behaviors. \n\n In effect, polymorphism cuts down the work of the developer because he can now create a sort of general class with all the attributes and behaviors that he envisions for it. When the time comes for the developer to create more specific subclasses with certain unique attributes and behaviors, the developer can simply alter code in the specific portions where the behaviors differ. All other portions of the code can be left as is. \n\nTo know whether an object is polymorphic, you can perform a simple test. If the object successfully passes multiple is-a or instanceof tests, it’s polymorphic.",
            "url": "https://en.wikipedia.org/wiki/Polymorphism_(computer_science)",
            "id": 132      
        }, 
        {
            "name": "Duck typing",
            "definition": "Duck typing in computer programming is an application of the duck test—‘If it walks like a duck and it quacks like a duck, then it must be a duck’—to determine whether an object can be used for a particular purpose. With nominative typing, an object is of a given type if it is declared to be (or if a type's association with the object is inferred through mechanisms such as object inheritance). \n\n In duck typing, an object is of a given type if it has all methods and properties required by that type. Duck typing can be viewed as a usage-based structural equivalence between a given object and the requirements of a type.",
            "url": "https://en.wikipedia.org/wiki/Duck_typing",
            "id": 133      
        }, 
        {
            "name": "Pseudocode",
            "definition": "In computer science, pseudocode is a plain language description of the steps in an algorithm or another system. Pseudocode often uses structural conventions of a normal programming language, but is intended for human reading rather than machine reading. It typically omits details that are essential for machine understanding of the algorithm, such as variable declarations and language-specific code. \n\n  The purpose of using pseudocode is that it is easier for people to understand than conventional programming language code, and that it is an efficient and environment-independent description of the key principles of an algorithm. It is commonly used in textbooks and scientific publications to document algorithms and in planning of software and other algorithms. \n\n No broad standard for pseudocode syntax exists, as a program in pseudocode is not an executable program; however, certain limited standards exist (such as for academic assessment). Pseudocode resembles skeleton programs, which can be compiled without errors. Flowcharts, drakon-charts and Unified Modelling Language (UML) charts can be thought of as a graphical alternative to pseudocode, but need more space on paper. Languages such as HAGGIS bridge the gap between pseudocode and code written in programming languages.",
            "url": "https://en.wikipedia.org/wiki/Pseudocode",
            "id": 134      
        }, 
        {
            "name": "Rapid application development (RAD",
            "definition": "Rapid application development (RAD), also called rapid application building (RAB), is both a general term for adaptive software development approaches, and the name for James Martin's method of rapid development. In general, RAD approaches to software development put less emphasis on planning and more emphasis on an adaptive process. Prototypes are often used in addition to or sometimes even instead of design specifications. \n\n RAD is especially well suited for (although not limited to) developing software that is driven by user interface requirements. Graphical user interface builders are often called rapid application development tools. Other approaches to rapid development include the adaptive, agile, spiral, and unified models.",
            "url": "https://en.wikipedia.org/wiki/Rapid_application_development",
            "id": 135      
        }, 
        {
            "name": "Iterative and incremental development",
            "definition": "Iterative and incremental development is any combination of both iterative design or iterative method and incremental build model for development. Usage of the term began in software development, with a long-standing combination of the two terms iterative and incremental having been widely suggested for large development efforts. For example, the 1985 DOD-STD-2167 mentions (in section 4.1.2): ‘During software development, more than one iteration of the software development cycle may be in progress at the same time.’ and 'This process may be described as an evolutionary acquisition or incremental build approach.' In software, the relationship between iterations and increments is determined by the overall software development process. \n\n The basic idea behind this method is to develop a system through repeated cycles (iterative) and in smaller portions at a time (incremental), allowing software developers to take advantage of what was learned during development of earlier parts or versions of the system. Learning comes from both the development and use of the system, where possible key steps in the process start with a simple implementation of a subset of the software requirements and iteratively enhance the evolving versions until the full system is implemented. At each iteration, design modifications are made and new functional capabilities are added, incrementally.",
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
            "definition": "In computer programming and software design, code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality. Potential advantages of refactoring may include improved code readability and reduced complexity; these can improve the source code's maintainability and create a simpler, cleaner, or more expressive internal architecture or object model to improve extensibility. Another potential goal for refactoring is improved performance; software engineers face an ongoing challenge to write programs that perform faster or use less memory. \n\n Typically, refactoring applies a series of standardised basic micro-refactorings, each of which is (usually) a tiny change in a computer program's source code that either preserves the behaviour of the software, or at least does not modify its conformance to functional requirements. Many development environments provide automated support for performing the mechanical aspects of these basic refactorings. If done well, code refactoring may help software developers discover and fix hidden or dormant bugs or vulnerabilities in the system by simplifying the underlying logic and eliminating unnecessary levels of complexity. If done poorly, it may fail the requirement that external functionality not be changed, and may thus introduce new bugs.",
            "url": "https://en.wikipedia.org/wiki/Code_refactoring",
            "id": 138     
        }, 
        {
            "name": "Rewrite",
            "definition": "A rewrite in computer programming is the act or result of re-implementing a large portion of existing functionality without re-use of its source code. When the rewrite is not using existing code at all, it is common to speak of a rewrite from scratch. \n\n A piece of software is typically rewritten when one or more of the following apply: \n\n - its source code is not available or is only available under an incompatible license \n - its code cannot be adapted to a new target platform \n - its existing code has become too difficult to handle and extend \n - the task of debugging it seems too complicated \n - the programmer finds it difficult to understand its source code \n - developers learn new techniques or wish to do a big feature overhaul which requires much change \n - developers learn that new codes written may extend content options that can fix or overwrite previous problems \n - the programming language of the source code has to be changed \n\n Several software engineers, such as Joel Spolsky have warned against total rewrites, especially under schedule constraints or competitive pressures. While developers may initially welcome the chance to correct historical design mistakes, a rewrite also discards those parts of the design that work as required. A rewrite commits the development team to deliver not just new features, but all those that exist in the previous code, while potentially introducing new bugs or regressions of previously fixed bugs. A rewrite also interferes with the tracking of unfixed bugs in the old version. \n\n The incremental rewrite is an alternative approach, in which developers gradually replace the existing code with calls into a new implementation, expanding that implementation until it fully replaces the old one. This approach avoids a broad loss of functionality during the rewrite. Cleanroom software engineering is another approach, which requires the team to work from an exhaustive written specification of the software's functionality, without access to its code.",
            "url": "https://en.wikipedia.org/wiki/Rewrite_(programming)",
            "id": 139      
        }, 
        {
            "name": "Regression testing",
            "definition": "Regression testing (rarely, non-regression testing) is re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change. If not, that would be called a regression. \n\n Changes that may require regression testing include bug fixes, software enhancements, configuration changes, and even substitution of electronic components. As regression test suites tend to grow with each found defect, test automation is frequently involved. Sometimes a change impact analysis is performed to determine an appropriate subset of tests (non-regression analysis).",
            "url": "https://en.wikipedia.org/wiki/Regression_testing",
            "id": 140      
        },     
        {
            "name": "Software development kit (SDK)",
            "definition": "A software development kit (SDK) is a collection of software development tools in one installable package. They facilitate the creation of applications by having a compiler, debugger and sometimes a software framework. They are normally specific to a hardware platform and operating system combination. To create applications with advanced functionalities such as advertisements, push notifications, etc; most application software developers use specific software development kits. \n\n Some SDKs are required for developing a platform-specific app. For example, the development of an Android app on the Java platform requires a Java Development Kit. For iOS applications (apps) the iOS SDK is required. For Universal Windows Platform the .NET Framework SDK might be used. There are also SDKs that add additional features and can be installed in apps to provide analytics, data about application activity, and monetization options. \n\n An SDK can take the form of application programming interfaces (APIs) in the form of on-device libraries of reusable functions used to interface to a particular programming language, or it may be as complex as hardware-specific tools that can communicate with a particular embedded system. Common tools include debugging facilities and other utilities, often presented in an integrated development environment (IDE). SDKs may include sample software and/or technical notes along with documentation, and tutorials to help clarify points made by the primary reference material. \n\n SDKs often include licenses that make them unsuitable for building software intended to be developed under an incompatible license. For example, a proprietary SDK is generally incompatible with free software development, while a GPL-licensed SDK could be incompatible with proprietary software development, for legal reasons. However, SDKs built under the GNU Lesser General Public License (LGPL) are typically usable for proprietary development. In cases where the underlying technology is new, SDKs may include hardware.",
            "url": "https://en.wikipedia.org/wiki/Software_development_kit",
            "id": 141      
        }, 
        {
            "name": "Service pack",
            "definition": "In computing, a service pack comprises a collection of updates, fixes, or enhancements to a software program delivered in the form of a single installable package. Companies often release a service pack when the number of individual patches to a given program reaches a certain (arbitrary) limit, or the software release has shown to be stabilized with a limited number of remaining issues based on users' feedback and bug reports. \n\n In large software applications such as office suites, operating systems, database software, or network management, it is not uncommon to have a service pack issued within the first year or two of a product's release. Installing a service pack is easier and less error-prone than installing many individual patches, even more so when updating multiple computers over a network, where service packs are common. \n\n Service packs are usually numbered, and thus shortly referred to as SP1, SP2, SP3 etc. They may also bring, besides bug fixes, entirely new features, as is the case of SP2 of Windows XP (e.g. Windows Security Center), or SP3 and SP4 of the heavily database dependent Trainz 2009: World Builder Edition.",
            "url": "https://en.wikipedia.org/wiki/Service_pack",
            "id": 142      
        }, 
        {
            "name": "Shotgun debugging",
            "definition": "Shotgun debugging can be defined as a process of making relatively un-directed changes to software in the hope that a bug will be perturbed out of existence. It can also mean using the approach of trying several possible solutions of hardware or software problem at the same time, in the hope that one of the solutions (typically source code modifications) will work. \n\n Shotgun debugging has a relatively low success rate and can be very time-consuming, except when used as an attempt to work around programming language features that one may be using improperly. When combined with domain expertise and a strong intuition for the underlying codebase, it can be a good starting point to gut-solve a buggy piece of code a few times before formally researching the corresponding error message. When used in this way, it may be a valuable technique that is faster than browsing through the Internet searching a particular error message every time. \n\n Shotgun debugging can occur when working with multi-threaded applications. Attempting to debug a race condition by adding debugging code to the application is likely to change the speed of one thread in relation to another and could cause the problem to disappear. This is known as a Heisenbug. Although apparently a solution to the problem, it is a fix by pure chance and anything else that changes the behavior of the threads could cause it to resurface — for example on a computer with a different scheduler. Code added to any part of the program could easily revert the effect of the ‘fix’.",
            "url": "https://en.wikipedia.org/wiki/Shotgun_debugging",
            "id": 143      
        }, 
        {
            "name": "Programming by permutation",
            "definition": "Programming by permutation, sometimes called ‘programming by accident’ or ‘shotgunning’, is an approach to software development wherein a programming problem is solved by iteratively making small changes (permutations) and testing each change to see if it behaves as desired. This approach sometimes seems attractive when the programmer does not fully understand the code and believes that one or more small modifications may result in code that is correct. \n\n Programming by permutation gives little or no assurance about the quality of the code produced—it is the polar opposite of formal verification. Programmers are often compelled to program by permutation when an API is insufficiently documented. This lack of clarity drives others to copy and paste from reference code which is assumed to be correct, but was itself written as a result of programming by permutation. In some cases where the programmer can logically explain that exactly one out of a small set of variations must work, programming by permutation leads to correct code (which then can be verified) and makes it unnecessary to think about the other (wrong) variations.",
            "url": "https://en.wikipedia.org/wiki/Programming_by_permutation",
            "id": 144      
        },   
        {
            "name": "Sanity testing",
            "definition": "In software development, a sanity test (a form of software testing which offers ‘quick, broad, and shallow testing’) evaluates the result of a subset of application functionality to determine whether it is possible and reasonable to proceed with further testing of the entire application. Sanity tests may sometimes be used interchangeably with smoke tests insofar as both terms denote tests which determine whether it is possible and reasonable to continue testing further. \n\n On the other hand, a distinction is sometimes made that a smoke test is a non-exhaustive test that ascertains whether the most crucial functions of a program work before proceeding with further testing whereas a sanity test refers to whether specific functionality such as a particular bug fix works as expected without testing the wider functionality of the software. In other words, a sanity test determines whether the intended result of a code change works correctly while a smoke test ensures that nothing else important was broken in the process. Sanity testing and smoke testing avoid wasting time and effort by quickly determining whether an application is too flawed to merit more rigorous QA testing, but needs more developer debugging. \n\n Groups of sanity tests are often bundled together for automated unit testing of functions, libraries, or applications prior to merging development code into a testing or trunk version control branch, for automated building, or for continuous integration and continuous deployment.",
            "url": "https://en.wikipedia.org/wiki/Sanity_check#Software_development",
            "id": 145      
        },     
        {
            "name": "Smoke testing",
            "definition": "In computer programming and software testing, smoke testing (also confidence testing, sanity testing, build verification test (BVT) and build acceptance test) is preliminary testing to reveal simple failures severe enough to, for example, reject a prospective software release. Smoke tests are a subset of test cases that cover the most important functionality of a component or system, used to aid assessment of whether main functions of the software appear to work correctly. \n\n When used to determine if a computer program should be subjected to further, more fine-grained testing, a smoke test may be called an intake test. Alternatively, it is a set of tests run on each new build of a product to verify that the build is testable before the build is released into the hands of the test team. \n\n Smoke tests frequently run quickly, giving benefits of faster feedback, rather than running more extensive test suites, which would naturally take much longer. A daily build and smoke test is among industry best practices. Smoke testing is also done by testers before accepting a build for further testing. Microsoft claims that after code reviews, ‘smoke testing is the most cost-effective method for identifying and fixing defects in software’. \n\n One can perform smoke tests either manually or using an automated tool. In the case of automated tools, the process that generates the build will often initiate the testing. Smoke tests can be functional tests or unit tests. Functional tests exercise the complete program with various inputs. Unit tests exercise individual functions, subroutines, or object methods. Functional tests may comprise a scripted series of program inputs, possibly even with an automated mechanism for controlling mouse movements. Unit tests can be implemented either as separate functions within the code itself, or else as a driver layer that links to the code without altering the code being tested.",
            "url": "https://en.wikipedia.org/wiki/Smoke_testing_(software)",
            "id": 146      
        }, 
        {
            "name": "Synchronize and stabilize",
            "definition": "Synchronize-and-stabilize is a software life cycle development model. It allows the teams to work efficiently in parallel on different individual application modules. This is done while frequently synchronizing the work as individual’s and as members of parallel teams and periodically stabilizing and/or debugging the code through out the development process. \n\n This model has several advantages over the classic waterfall model, which follows a sequential method. It has proven to be a more flexible model when compared to other life cycle development models. The distinguishing feature of the synchronize and stabilize model is allowing changes and modifications at any point in the software development process.",
            "url": "https://www.techopedia.com/definition/26121/synchronize-and-stabilize",
            "id": 147      
        }, 
        {
            "name": "Total cost of ownership (TCO)",
            "definition": "Total cost of ownership (TCO) is a financial estimate intended to help buyers and owners determine the direct and indirect costs of a product or service. It is a management accounting concept that can be used in full cost accounting or even ecological economics where it includes social costs. TCO is applied to the analysis of information technology products, seeking to quantify the financial impact of deploying a product over its life cycle. This includes software and hardware as well as training, warranties, licenses, migration expenses, risks, testing costs, backup and recovery, decommissioning and much more. \n\n A TCO analysis includes total cost of acquisition and operating costs, as well as costs related to replacement or upgrades at the end of the life cycle. A TCO analysis is used to gauge the viability of any capital investment. An enterprise may use it as a product/process comparison tool. It is also used by credit markets and financing agencies. TCO directly relates to an enterprise's asset and/or related systems total costs across all projects and processes, thus giving a picture of the profitability over time.",
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
            "definition": "In software engineering, rubber duck debugging is a method of debugging code by articulating a problem in spoken or written natural language. The name is a reference to a story in the book The Pragmatic Programmer in which a programmer would carry around a rubber duck and debug their code by forcing themselves to explain it, line-by-line, to the duck. Many other terms exist for this technique, often involving different (usually) inanimate objects, or pets such as a dog or a cat. \n\n .Many programmers have had the experience of explaining a problem to someone else, possibly even to someone who knows nothing about programming, and then hitting upon the solution in the process of explaining the problem. In describing what the code is supposed to do and observing what it actually does, any incongruity between these two becomes apparent. More generally, teaching a subject forces its evaluation from different perspectives and can provide a deeper understanding. By using an inanimate object, the programmer can try to accomplish this without having to interrupt anyone else. This approach has been taught in computer science and software engineering courses.",
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
            "definition": "Data anonymization is a type of information sanitization whose intent is privacy protection. It is the process of removing personally identifiable information from data sets, so that the people whom the data describe remain anonymous. \n\n Data anonymization has been defined as a ‘process by which personal data is altered in such a way that a data subject can no longer be identified directly or indirectly, either by the data controller alone or in collaboration with any other party.’ Data anonymization may enable the transfer of information across a boundary, such as between two departments within an agency or between two agencies, while reducing the risk of unintended disclosure, and in certain environments in a manner that enables evaluation and analytics post-anonymization.",
            "url": "",
            "id": 153      
        }, 
        {
            "name": "Bot",
            "definition": "An Internet bot, web robot, robot or simply bot, is a software application that runs automated tasks (scripts) over the Internet, usually with the intent to emulate human activity on the Internet, such as messaging, on a large scale. An Internet bot plays the client role in a client–server model whereas the server role is usually played by web servers. Internet bots are able to perform tasks, that are simple and repetitive, much faster than a person could ever do. The most extensive use of bots is for web crawling, in which an automated script fetches, analyzes and files information from web servers. More than half of all web traffic is generated by bots. \n\n Efforts by web servers to restrict bots vary. Some servers have a robots.txt file that contains the rules governing bot behavior on that server. Any bot that does not follow the rules could, in theory, be denied access to or removed from, the affected website. If the posted text file has no associated program/software/app, then adhering to the rules is entirely voluntary. There would be no way to enforce the rules or to ensure that a bot's creator or implementer reads or acknowledges the robots.txt file. Some bots are ‘good’ – e.g. search engine spiders – while others are used to launch malicious attacks on, for example, political campaigns.",
            "url": "https://en.wikipedia.org/wiki/Internet_bot",
            "id": 154      
        },   
        {
            "name": "Botnet",
            "definition": "A botnet is a number of Internet-connected devices, each of which runs one or more bots. Botnets can be used to perform Distributed Denial-of-Service (DDoS) attacks, steal data, send spam, and allow the attacker to access the device and its connection. The owner can control the botnet using command and control (C&C) software. The word ‘botnet’ is a portmanteau of the words ‘robot’ and ‘network’. The term is usually used with a negative or malicious connotation. \n\n A botnet is a logical collection of Internet-connected devices, such as computers, smartphones or Internet of things (IoT) devices whose security have been breached and control ceded to a third party. Each compromised device, known as a ‘bot’, is created when a device is penetrated by software from a malware (malicious software) distribution. \n\n The controller of a botnet is able to direct the activities of these compromised computers through communication channels formed by standards-based network protocols, such as IRC and Hypertext Transfer Protocol (HTTP). Botnets are increasingly rented out by cyber criminals as commodities for a variety of purposes",
            "url": "https://en.wikipedia.org/wiki/Botnet",
            "id": 155      
        },     
        {
            "name": "Buffer overflow",
            "definition": "In information security and programming, a buffer overflow, or buffer overrun, is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory locations. \n\n Buffers are areas of memory set aside to hold data, often while moving it from one section of a program to another, or between programs. Buffer overflows can often be triggered by malformed inputs; if one assumes all inputs will be smaller than a certain size and the buffer is created to be that size, then an anomalous transaction that produces more data could cause it to write past the end of the buffer. If this overwrites adjacent data or executable code, this may result in erratic program behavior, including memory access errors, incorrect results, and crashes. \n\n Exploiting the behavior of a buffer overflow is a well-known security exploit. On many systems, the memory layout of a program, or the system as a whole, is well defined. By sending in data designed to cause a buffer overflow, it is possible to write into areas known to hold executable code and replace it with malicious code, or to selectively overwrite data pertaining to the program's state, therefore causing behavior that was not intended by the original programmer. Buffers are widespread in operating system (OS) code, so it is possible to make attacks that perform privilege escalation and gain unlimited access to the computer's resources. The famed Morris worm in 1988 used this as one of its attack techniques.",
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
            "definition": "OAuth (Open Authorization) is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites but without giving them the passwords. Generally, OAuth provides clients a ‘secure delegated access’ to server resources on behalf of a resource owner. It specifies a process for resource owners to authorize third-party access to their server resources without providing credentials. \n\n Designed specifically to work with Hypertext Transfer Protocol (HTTP), OAuth essentially allows access tokens to be issued to third-party clients by an authorization server, with the approval of the resource owner. The third party then uses the access token to access the protected resources hosted by the resource server. In particular, OAuth 2.0 provides specific authorization flows for web applications, desktop applications, mobile phones, and smart devices.",
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
            "definition": "In internet slang, a troll is a person who posts inflammatory, insincere, digressive, extraneous, or off-topic messages in an online community (such as social media (Twitter, Facebook, Instagram, etc.), a newsgroup, forum, chat room, online video game, or blog), with the intent of provoking readers into displaying emotional responses, or manipulating others' perception. This is typically for the troll's amusement, or to achieve a specific result such as disrupting a rival's online activities or manipulating a political process. Even so, Internet trolling can also be defined as purposefully causing confusion or harm to other users online, for no reason at all. \n\n Application of the term troll is subjective. At times the word is incorrectly used to refer to anyone with controversial, or differing, opinions. Some readers may characterize a post as trolling, while others may regard the same post as a legitimate contribution to the discussion, even if controversial. More potent acts of trolling are blatant harassment or off-topic banter. The advice to ignore rather than engage with a troll is sometimes phrased as ‘Please don't feed the trolls.’",
            "url": "https://en.wikipedia.org/wiki/Internet_troll",
            "id": 160      
        }, 
        {
            "name": "Composite pattern",
            "definition": "In software engineering, the composite pattern is a partitioning design pattern. The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. The intent of a composite is to 'compose' objects into tree structures to represent part-whole hierarchies. Implementing the composite pattern lets clients treat individual objects and compositions uniformly. \n\n The Composite design pattern is one of the twenty-three well-known GoF design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.",
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
            "name": "This changes everything",
            "definition": "Nothing has changed. Pure marketing. Outside of Silicon Valley this can mean curing cancer, eliminating Malaria and solving world hunger but within SV it means a bigger iPhone, an iPhone the size of a tablet or an iPhone strapped to your wrist. Synonyms include ‘This changes everything. Again’ and ‘Changing the world’.",
            "url": "https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/media/this-changes-everything.jpeg?raw=true",
            "id": 163      
        }, 
        {
            "name": "Code ninja",
            "definition": "Code ninjas, also referred to as ninja developers, don’t limit themselves to just one programming language or one technology stack; they are ‘developer polyglots.’ The ninja is an expert in a particular programming language, but is comfortable using any other language. They know how to navigate the various stacks in order to solve whatever technical challenge they come across. Organizations seek the most talented professionals for the lowest possible salary, but the type of knowledge a code ninja possesses comes with a steep price tag. That’s because they’re essentially full stack developers who can work within various technology stacks – a skillset that is in increasing demand and very well-compensated! Though the code ninja has broad knowledge rather than deep expertise in one or two areas, gaining knowledge across the aforementioned skill-sets takes years devotion. There is no such thing as a junior or semi-senior code ninja; you either are one, or you aren’t...yet.’ \n\n 'Code ninja’ can also be a euphemism used by recruiters who don't actually know what specifically they want in a software engineer, just someone who can pretty much do everything and anything that's handed to them.",
            "url": "https://www.codeninjas.com/",
            "id": 164      
        }, 
        {
            "name": "Brogrammer",
            "definition": "‘Brogrammer’, a portmanteau of bro and programmer, is a slang term for a computer programmer who engages in stereotypically male-oriented activities and macho behavior. It is often used pejoratively, but some programmers self-describe themselves as a brogrammer positively as a word for ‘sociable or outgoing programmer’, and it also tends to represent a subculture within the greater tech industry. Brogrammer culture has been said to have created an entry barrier based on adherence to the image presented by its participants, rather than ability. It can be viewed as antithetical to geek culture, which emphasizes ability and passion for field over image.",
            "url": "https://en.wikipedia.org/wiki/Brogrammer",
            "id": 165      
        }, 
        {
            "name": "Vanity metrics",
            "definition": "Vanity metrics are metrics that make you look good to others but do not help you understand your own performance in a way that informs future strategies. These metrics are exciting to point to if you want to appear to be improving, but they often aren’t actionable and aren’t related to anything you can control or repeat in a meaningful way. Vanity metrics are most often contrasted against actionable metrics, which is data that helps you make decisions and helps your business reach its goals or grow. \n\n It is important to mention: Any metric can be a vanity metric. There just happen to be some telltale signs. They are hollow metrics that look nice on the surface but hold little substance. For example, 10,000 total registered accounts might seem impressive, but that number loses face quickly if there are only 100 active monthly users.",
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
            "definition": "Bootstrapping is a self-starting process that is supposed to proceed without external input. For various definitions, click 'Learn More', below.",
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
            "definition": "Digital nomads are people who conduct their life in a nomadic manner while engaging in remote work using digital telecommunications technology. Such people generally have minimal material possessions and work remotely in temporary housing, hotels, cafes, public libraries, co-working spaces, or recreational vehicles, using Wi-Fi, smartphones or mobile hotspots to access the Internet. \n\n Some digital nomads are perpetual travelers, while others are only nomadic for a short period of time. While some nomads travel through various countries, others focus on one area. Some may engage in vandwelling. In 2020, a research study found that 10.9 million American workers described themselves as digital nomads, an increase of 49% from 2019. Digital nomads are often younger remote workers, backpackers, retired or semi-retired persons, snowbirds, and/or entrepreneurs.",
            "url": "https://en.wikipedia.org/wiki/Digital_nomad",
            "id": 172      
        }, 
        {
            "name": "Mechatronics",
            "definition": "Mechatronics, also called mechatronics engineering, is an interdisciplinary branch of engineering that focuses on the integration of mechanical, electronic and electrical engineering systems, and also includes a combination of robotics, electronics, computer science, telecommunications, systems, control, and product engineering. \n\n As technology advances over time, various subfields of engineering have succeeded in both adapting and multiplying. The intention of mechatronics is to produce a design solution that unifies each of these various subfields. Originally, the field of mechatronics was intended to be nothing more than a combination of mechanics and electronics, hence the name being a portmanteau of mechanics and electronics; however, as the complexity of technical systems continued to evolve, the definition had been broadened to include more technical areas. \n\n The word mechatronics originated in Japanese-English and was created by Tetsuro Mori, an engineer of Yaskawa Electric Corporation. The word mechatronics was registered as trademark by the company in Japan with the registration number of ’46-32714’ in 1971. The company later released the right to use the word to the public, and the word began being used globally. Currently the word is translated into many languages and is considered an essential term for advanced automated industry. Many people treat mechatronics as a modern buzzword synonymous with automation, robotics and electromechanical engineering.",
            "url": "https://en.wikipedia.org/wiki/Mechatronics",
            "id": 173      
        }, 
        {
            "name": "Growth hacking",
            "definition": "Growth hacking is a subfield of marketing focused on the rapid growth of a company. It is referred to as both a process and a set of cross-disciplinary (digital) skills. The goal is to regularly conduct A/B testing that will lead to improving the customer journey, and replicate and scale the ideas that work and modify or abandon the ones that don't before investing a lot of resources. It started in relation to early-stage startups that need rapid growth within short time on tight budgets, and also reached bigger corporate companies. \n\n A growth hacking team is made up of marketers, developers, engineers and product managers that specifically focus on building and engaging the user base of a business. Growth hacking is not just a process for marketers. It can be applied to product development and to the continuous improvement of products as well as to growing an existing customer base. As such, it’s equally useful to everyone from product developers, to engineers, to designers, to salespeople and to managers.",
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
            "definition": "In computing, input/output (I/O, or informally io or IO) is the communication between an information processing system, such as a computer, and the outside world, possibly a human or another information processing system. Inputs are the signals or data received by the system and outputs are the signals or data sent from it. The term can also be used as part of an action; to ‘perform I/O’ is to perform an input or output operation. \n\n I/O devices are the pieces of hardware used by a human (or other system) to communicate with a computer. For instance, a keyboard or computer mouse is an input device for a computer, while monitors and printers are output devices. Devices for communication between computers, such as modems and network cards, typically perform both input and output operations.",
            "url": "https://en.wikipedia.org/wiki/Input/output",
            "id": 177      
        }, 
        {
            "name": "Dogfooding",
            "definition": "Eating your own dog food or “dogfooding” is the practice of using one's own products or services. This can be a way for an organization to test its products in real-world usage using product management techniques. Hence dogfooding can act as quality control, and eventually a kind of testimonial advertising. Once in the market, dogfooding can demonstrate developers' confidence in their own products.",
            "url": "https://en.wikipedia.org/wiki/Eating_your_own_dog_food",
            "id": 178      
        }, 
        {
            "name": "SWOT analysis",
            "definition": "SWOT analysis (or SWOT matrix) is a strategic planning and strategic management technique used to help a person or organization identify strengths, weaknesses, opportunities, and threats related to business competition or project planning. It is sometimes called situational assessment or situational analysis. Additional acronyms using the same components include TOWS and WOTS-UP. \n\n This technique is designed for use in the preliminary stages of decision-making processes and can be used as a tool for evaluation of the strategic position of organizations of many kinds (for-profit enterprises, local and national governments, NGOs, etc.). It is intended to identify the internal and external factors that are favorable and unfavorable to achieving the objectives of the venture or project. Users of a SWOT analysis often ask and answer questions to generate meaningful information for each category to make the tool useful and identify their competitive advantage. SWOT has been described as a tried-and-true tool of strategic analysis, but has also been criticized for its limitations, and alternatives have been developed.",
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
            "definition": "Pair programming is an agile software development technique in which two programmers work together at one workstation. One, the driver, writes code while the other, the observer or navigator, reviews each line of code as it is typed in. The two programmers switch roles frequently. \n\n While reviewing, the observer also considers the ‘strategic’ direction of the work, coming up with ideas for improvements and likely future problems to address. This is intended to free the driver to focus all of their attention on the ‘tactical’ aspects of completing the current task, using the observer as a safety net and guide.",
            "url": "https://en.wikipedia.org/wiki/Pair_programming",
            "id": 183      
        }, 
        {
            "name": "AWK",
            "definition": "AWK (awk) is a domain-specific language designed for text processing and typically used as a data extraction and reporting tool. Like sed and grep, it is a filter, and is a standard feature of most Unix-like operating systems. \n\n AWK was created at Bell Labs in the 1970s, and its name is derived from the surnames of its authors: Alfred Aho, Peter Weinberger, and Brian Kernighan. The acronym is pronounced the same as the bird auk, which is on the cover of The AWK Programming Language. When written in all lowercase letters, as awk, it refers to the Unix or Plan 9 program that runs scripts written in the AWK programming language.",
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
            "definition": "A pipe is an inter-process communication mechanism originating in Unix, which directs the output (standard out and, optionally, standard error) of one process to the input (standard in) of another. In this way, a series of commands can be ‘piped’ together, giving users the ability to quickly perform complex multi-stage processing from the command line or as part of a Unix shell script (‘bash file’). In most Unix shells (command interpreters), this is represented by the vertical bar character, | \n\n  For example: \n\n command1 | command2 | command3",
            "url": "https://en.wikipedia.org/wiki/Pipeline_(Unix)",
            "id": 186      
        }, 
        {
            "name": "Technical debt",
            "definition": "In software development, technical debt (also known as design debt or code debt) is the implied cost of additional rework caused by choosing an easy (limited) solution now instead of using a better approach that would take longer. \n\n Analogous with monetary debt, if technical debt is not repaid, it can accumulate ‘interest’, making it harder to implement changes. Unaddressed technical debt increases software entropy and cost of further rework. Similarly to monetary debt, technical debt is not necessarily a bad thing, and sometimes (e.g. as a proof-of-concept) is required to move projects forward. On the other hand, some experts claim that the ‘technical debt’ metaphor tends to minimize the ramifications, which results in insufficient prioritization of the necessary work to correct it. \n\n As a change is started on a codebase, there is often the need to make other coordinated changes in other parts of the codebase or documentation. Changes required that are not completed are considered debt, and until paid, will incur interest on top of interest, making it cumbersome to build a project. Although the term is used in software development primarily, it can also be applied to other professions.",
            "url": "https://en.wikipedia.org/wiki/Technical_debt",
            "id": 187      
        }, 
        {
            "name": "Application streaming",
            "definition": "Application streaming is a form of on-demand software distribution. In these scenarios, only essential portions of an application's code need to be installed on the computer: while the end user performs actions in the application, the necessary code and files are delivered over the network as and when they are required. \n\n Application streaming provides an extremely accurate metric of actual application usage, and rather than install the same applications on every client machine in the company, only the programs users actually want to run are delivered. As a result, licensing fees can often be reduced. \n\n Application streaming is a related concept to application virtualization, where applications are run directly from a virtual machine on a central server that is completely separate from the local system. By contrast, application streaming runs the program locally, but still involves the centralized storage of application code.",
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
            "definition": "An application service provider (ASP), also known as Apps on tap, is a business providing computer-based services to customers over a network; such as access to a particular software application (such as customer relationship management) using a standard protocol (such as HTTP). \n\n The need for ASPs has evolved from the increasing costs of specialized software that have far exceeded the price range of small to medium-sized businesses. As well, the growing complexities of software have led to huge costs in distributing the software to end-users. Through ASPs, the complexities and costs of such software can be cut down. In addition, the issues of upgrading have been eliminated from the end-firm by placing the onus on the ASP to maintain up-to-date services, 24 x 7 technical support, physical and electronic security and in-built support for business continuity and flexible working.",
            "url": "https://en.wikipedia.org/wiki/Application_service_provider",
            "id": 190      
        }, 
        {
            "name": "Augmented reality (AR)",
            "definition": "Augmented reality (AR) is an interactive experience of a real-world environment where the objects that reside in the real world are enhanced by computer-generated perceptual information, sometimes across multiple sensory modalities, including visual, auditory, haptic, somatosensory and olfactory. AR can be defined as a system that incorporates three basic features: a combination of real and virtual worlds, real-time interaction, and accurate 3D registration of virtual and real objects. \n\n The overlaid sensory information can be constructive (i.e. additive to the natural environment), or destructive (i.e. masking of the natural environment). This experience is seamlessly interwoven with the physical world such that it is perceived as an immersive aspect of the real environment. In this way, augmented reality alters one's ongoing perception of a real-world environment, whereas virtual reality completely replaces the user's real-world environment with a simulated one. Augmented reality is related to two largely synonymous terms: mixed reality and computer-mediated reality.",
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
            "definition": "Abandonware is a product, typically software, ignored by its owner and manufacturer, and for which no official support is available. \n\n Within an intellectual rights contextual background, abandonware is a software (or hardware) sub-case of the general concept of orphan works. Museums and various organizations dedicated to preserving this software continue to provide legal access. \n\n The term ‘abandonware’ is broad, and encompasses many types of old software. Definitions of ‘abandoned’ vary, but in general it is like any item that is abandoned – it is ignored by the owner, and as such product support and possibly copyright enforcement are also ‘abandoned’.",
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
            "definition": "A language that is generated from programming source code, but that cannot be directly executed by the CPU. Also called ‘bytecode’, ‘p-code’, ‘pseudocode’ or ‘pseudo language’, the intermediate language (IL) is platform independent. It can be run in any computer environment that has a runtime engine for the language. \n\n In order to execute the intermediate language program, it must be interpreted a line at a time into machine language when it is run or compiled entirely into machine language just before it is run or compiled entirely ahead of time and run when required. \n\n Visual Basic and Java are notable examples of programming languages that generate an intermediate language. Microsoft's .NET and Common Language Infrastructure (CLI), the ECMA standard version of .NET, also generate an intermediate language.",
            "url": "https://en.wikipedia.org/wiki/Intermediate_representation#Intermediate_language",
            "id": 195      
        },
        { 
            "name": "Cross-platform software",
            "definition": "",
            "url": "https://en.wikipedia.org/wiki/Cross-platform_software",
            "id": 196      
        }, 
        {
            "name": "Coding best practices",
            "definition": "Coding best practices are a set of informal rules that the software development community employs to help improve software quality.Many computer programs remain in use for long periods of time so any rules need to facilitate both initial development and subsequent maintenance and enhancement by people other than the original authors. \n\n There are a few best practices when it comes to learning how to code, and they center around these 7 concepts: \n\n 1. Variable naming conventions \n 2. Class and function naming conventions \n 3. Clear and concise comments \n 4. Indentations \n	 5. Portability \n 6. Reusability and scalability \n 7. Testing",
            "url": "https://en.wikipedia.org/wiki/Coding_best_practices",
            "id": 197      
        }, 
        {
            "name": "Best current practice (BCP)",
            "definition": "A Best Current Practice (BCP) is a de facto level of performance in engineering and information technology. It is more flexible than a standard, since techniques and tools are continually evolving. The Internet Engineering Task Force publishes Best Current Practice documents in a numbered document series. Each document in this series is paired with the currently valid Request for Comments (RFC) document. BCP was introduced in RFC-1818. \n\n BCPs are document guidelines, processes, methods, and other matters not suitable for standardization. The Internet standards process itself is defined in a series of BCPs, as is the formal organizational structure of the IETF, Internet Engineering Steering Group, Internet Architecture Board, and other groups involved in that process. \n\n IETF's separate Standard Track (STD) document series defines the fully standardized network protocols of the Internet, such as the Internet Protocol, the Transmission Control Protocol, and the Domain Name System. Each RFC number refers to a specific version of a document Standard Track, but the BCP number refers to the most recent revision of the document. Thus, citations often reference both the BCP number and the RFC number. Example citations for BCPs are: BCP 38, RFC 2827.",
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
            "definition": "Arduino is an open-source hardware and software company, project, and user community that designs and manufactures single-board microcontrollers and microcontroller kits for building digital devices. Its hardware products are licensed under a CC BY-SA license, while software is licensed under the GNU Lesser General Public License (LGPL) or the GNU General Public License (GPL), permitting the manufacture of Arduino boards and software distribution by anyone. Arduino boards are available commercially from the official website or through authorized distributors. \n\n Arduino board designs use a variety of microprocessors and controllers. The boards are equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards ('shields') or breadboards (for prototyping) and other circuits. The boards feature serial communications interfaces, including Universal Serial Bus (USB) on some models, which are also used for loading programs. The microcontrollers can be programmed using the C and C++ programming languages, using a standard API which is also known as the Arduino language, inspired by the Processing language and used with a modified version of the Processing IDE. In addition to using traditional compiler toolchains, the Arduino project provides an integrated development environment (IDE) and a command line tool developed in Go. \n\n The Arduino project began in 2005 as a tool for students at the Interaction Design Institute Ivrea, Italy, aiming to provide a low-cost and easy way for novices and professionals to create devices that interact with their environment using sensors and actuators. Common examples of such devices intended for beginner hobbyists include simple robots, thermostats and motion detectors. The name Arduino comes from a bar in Ivrea, Italy, where some of the founders of the project used to meet. The bar was named after Arduin of Ivrea, who was the margrave of the March of Ivrea and King of Italy from 1002 to 1014.",
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
            "definition": "A path is a string of characters used to uniquely identify a location in a directory structure. It is composed by following the directory tree hierarchy in which components, separated by a delimiting character, represent each directory. The delimiting character is most commonly the slash (‘/‘), the backslash character (‘\’), or colon (‘:’), though some operating systems may use a different delimiter. Paths are used extensively in computer science to represent the directory/file relationships common in modern operating systems and are essential in the construction of Uniform Resource Locators (URLs). Resources can be represented by either absolute or relative paths. \n\n An absolute or full path points to the same location in a file system, regardless of the current working directory. To do that, it must include the root directory. By contrast, a relative path starts from some given working directory, avoiding the need to provide the full absolute path. A filename can be considered as a relative path based at the current working directory. If the working directory is not the file's parent directory, a file not found error will result if the file is addressed by its name.",
            "url": "https://en.wikipedia.org/wiki/Path_(computing)",
            "id": 204      
        }, 
        {
            "name": "Garbage collection (GC)",
            "definition": "In computer science, garbage collection (GC) is a form of automatic memory management. The garbage collector attempts to reclaim memory which was allocated by the program, but is no longer referenced—also called garbage. Garbage collection was invented by American computer scientist John McCarthy around 1959 to simplify manual memory management in Lisp. \n\n Garbage collection relieves the programmer from performing manual memory management where the programmer specifies what objects to deallocate and return to the memory system and when to do so. Other similar techniques include stack allocation, region inference, memory ownership, and combinations of multiple techniques. Garbage collection may take a significant proportion of total processing time in a program and, as a result, can have significant influence on performance. \n\n Resources other than memory, such as network sockets, database handles, user interaction windows, file and device descriptors, are not typically handled by garbage collection. Methods for managing such resources, particularly destructors, may suffice to manage memory as well, leaving no need for GC. Some GC systems allow such other resources to be associated with a region of memory that, when collected, causes the work of reclaiming these resources.",
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
            "definition": "The most widely used microprocessors worldwide. Designed by ARM Holdings plc, Cambridge, England (www.arm.com), the company was founded in 1990 by Acorn Computers, Apple and VLSI Technology. The ARM brand originally stood for Acorn RISC Machine and later Advanced RISC Machine. \n\n In 2016, ARM was acquired by Japan-based Softbank, which agreed to sell the company to NVIDIA in 2020 for $40 billion, pending U.S. and U.K. approval. As of 2022, the deal is still pending due to U.S. antitrust concerns. \n\n Low Power Requirements - ARM chips are 32-bit and 64-bit RISC-based CPUs that are known for their low cost but primarily for their low power requirements. In some cases, an ARM-based smartphone using five watts of battery can perform as well or better than a CISC-based desktop computer requiring more than 100 watts. \n\n Manufactured under license from ARM by more than a dozen semiconductor companies, billions of ARM-based devices are made every year, including smartphones, tablets, e-book readers, TVs and myriad other consumer and industrial products. Apple surprised the industry in 2020 by using its new ARM-based chip in its laptop and desktop computers. \n\n Very often, multiple ARM processing cores make up the CPU in a system-on-chip (SoC). For example, Qualcomm's Snapdragon and NVIDIA's Tegra are ARM-based smartphone and tablet SoCs.",
            "url": "https://en.wikipedia.org/wiki/ARM_architecture_family",
            "id": 207      
        }, 
        {
            "name": "Array vs. List",
            "definition": "Array \n\n In computer science, an array type is a data type that represents a collection of elements (values or variables), each selected by one or more indices (identifying keys) that can be computed at run time during program execution. Such a collection is usually called an array variable, array value, or simply array. By analogy with the mathematical concepts vector and matrix, array types with one and two indices are often called vector type and matrix type, respectively. More generally, a multidimensional array type can be called a tensor type. \n\n List \n\n In computer science, a list or sequence is an abstract data type that represents a finite number of ordered values, where the same value may occur more than once. An instance of a list is a computer representation of the mathematical concept of a tuple or finite sequence; the (potentially) infinite analog of a list is a stream. Lists are a basic example of containers, as they contain other values. If the same value occurs multiple times, each occurrence is considered a distinct item. \n\n Similarities between Lists and Arrays \n\n They can look the same: [3,4,3,6,3]. Both are used for storing data. Both are mutable. Both can be indexed and iterated through. Both can be sliced \n\n Differences \n\n The main difference between these two data types is the operation you can perform on them. Arrays are specially optimized for arithmetic computations so if you’re going to perform similar operations you should consider using an array instead of a list. Lists are easier to modify while arrays are more difficult. In comparison to the list, an array has a more compact in-memory size. List memory allocation is dynamic and random, while array memory allocation is static and continuous. Also lists are containers for elements having differing data types (heterogeneous) but arrays are used as containers for elements of the same data type (homogeneous).",
            "url": "https://learnpython.com/blog/python-array-vs-list/",
            "id": 208      
        }, 
        {
            "name": "Artificial empathy (AE)",
            "definition": "Artificial empathy (AE) or computational empathy is the development of AI systems—such as companion robots or virtual agents—that can detect emotions and respond to them in an empathic way. \n\n Although such technology can be perceived as scary or threatening, it could also have a significant advantage over humans for roles in which emotional expression can be important, such as in the health care sector. For example, care-givers who perform emotional labor above and beyond the requirements of paid labor can experience chronic stress or burnout, and can become desensitized to patients. \n\n A broader definition of artificial empathy is ‘the ability of nonhuman models to predict a person's internal state (e.g., cognitive, affective, physical) given the signals (s)he emits (e.g., facial expression, voice, gesture) or to predict a person's reaction (including, but not limited to internal states) when he or she is exposed to a given set of stimuli (e.g., facial expression, voice, gesture, graphics, music, etc.)’.",
            "url": "https://en.wikipedia.org/wiki/Artificial_empathy",
            "id": 209      
        }, 
        {
            "name": "Service set",
            "definition": "In IEEE 802.11 wireless local area networking standards (including Wi-Fi), a service set is a group of wireless network devices which share a service set identifier (SSID)—typically the natural language label that users see as a network name. (For example, all of the devices that together form and use a Wi‑Fi network called Foo are a service set.) A service set forms a logical network of nodes operating with shared link-layer networking parameters; they form one logical network segment. A service set is either a basic service set (BSS) or an extended service set (ESS). \n\n Basic service set \n\n A basic service set is a subgroup, within a service set, of devices that share physical-layer medium access characteristics (e.g. radio frequency, modulation scheme, security settings) such that they are wirelessly networked. The basic service set is defined by a basic service set identifier (BSSID) shared by all devices within it. A basic service set should not be confused with the coverage area of an access point, known as the basic service area (BSA). \n\n An infrastructure BSS is created by an infrastructure device called an access point (AP) for other devices to join. The Wi‑Fi segments of common home and business networks are examples of this type. \n\n An independent BSS (IBSS), or ad hoc network, is created by peer devices among themselves without network infrastructure. A temporary network created by a cellular telephone to share its Internet access with other devices is a common example. \n\n A mesh basic service set (MBSS) forms a self-contained network of mesh stations that share a mesh profile. Each node may also be an access point hosting its own basic service set, for example using the mesh BSS to provide Internet access for local users. From the point of view of a wireless client, an IEEE 802.11s wireless mesh network appears as a conventional infrastructure mode topology, and is centrally configured as such. The formation of the mesh's BSS, as well as wireless traffic management (including path selection and forwarding) is negotiated between the nodes of the mesh infrastructure. The mesh's BSS is distinct from the networks (which may also be wireless) used by a mesh's redistribution points to communicate with one another. \n\n Extended service set \n\n An extended service set (ESS) is a wireless network, created by multiple access points, which appears to users as a single, seamless network, such as a network covering a home or office that is too large for reliable coverage by a single access point. It is a set of one or more infrastructure basic service sets on a common logical network segment (i.e. same IP subnet and VLAN). Key to the concept is that the participating basic service sets appear as a single network to the logical link control layer. \n\n Thus, from the perspective of the logical link control layer, stations within an ESS may communicate with one another, and mobile stations may move transparently from one participating basic service set to another (within the same ESS). Extended service sets make possible distribution services such as centralized authentication. From the perspective of the link layer, all stations within an ESS are all on the same link, and transfer from one BSS to another is transparent to logical link control.",
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
            "definition": "Public-key cryptography, or asymmetric cryptography, is a cryptographic system that uses pairs of keys. Each pair consists of a public key (which may be known to others) and a private key (which may not be known by anyone except the owner). The generation of such key pairs depends on cryptographic algorithms which are based on mathematical problems termed one-way functions. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security. \n\n In such a system, any person can encrypt a message using the intended receiver's public key, but that encrypted message can only be decrypted with the receiver's private key. This allows, for instance, a server program to generate a cryptographic key intended for a suitable symmetric-key cryptography, then to use a client's openly-shared public key to encrypt that newly generated symmetric key. The server can then send this encrypted symmetric key over an insecure channel to the client; only the client can decrypt it using the client's private key (which pairs with the public key used by the server to encrypt the message). With the client and server both having the same symmetric key, they can safely use symmetric key encryption (likely much faster) to communicate over otherwise-insecure channels. This scheme has the advantage of not having to manually pre-share symmetric keys (a fundamentally difficult problem) while gaining the higher data throughput advantage of symmetric-key cryptography. \n\n With public-key cryptography, robust authentication is also possible. A sender can combine a message with a private key to create a short digital signature on the message. Anyone with the sender's corresponding public key can combine that message with a claimed digital signature; if the signature matches the message, the origin of the message is verified (i.e., it must have been made by the owner of the corresponding private key).",
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
            "definition": "Active cooling is a heat-reducing mechanism that is typically implemented in electronic devices and indoor buildings to ensure proper heat transfer and circulation from within. Unlike its counterpart passive cooling, active cooling is entirely dependent on energy consumption in order to operate. It uses various mechanical systems that consume energy to dissipate heat. It is commonly implemented in systems that are unable to maintain their temperature through passive means. \n\n Active cooling systems are usually powered through the use of electricity or thermal energy but it's possible for some systems to be powered by solar energy or even hydroelectric energy. They need to be well-maintained and sustainable in order for them to perform its necessary tasks or the possibility of damages within objects could occur. Various applications of commercial active cooling systems include indoor air conditioners, computer fans, and heat pumps.",
            "url": "https://en.wikipedia.org/wiki/Computer_cooling",
            "id": 216      
        }, 
        {
            "name": "Passive cooling",
            "definition": "Passive cooling is a design approach that focuses on heat gain control and heat dissipation in order to lower the thermal temperature, with low or no energy consumption. This approach works either by preventing heat from entering the interior (heat gain prevention) or by removing heat from the structure (natural cooling). \n\n Passive heatsink cooling involves attaching a block of machined or extruded metal to the part that needs cooling. A thermal adhesive may be used. More commonly for a personal computer CPU, a clamp holds the heatsink directly over the chip, with a thermal grease or thermal pad spread between. This block has fins and ridges to increase its surface area. The heat conductivity of metal is much better than that of air, and it radiates heat better than the component that it is protecting (usually an integrated circuit or CPU). Fan-cooled aluminium heatsinks were originally the norm for desktop computers, but nowadays many heatsinks feature copper base-plates or are entirely made of copper.",
            "url": "https://en.wikipedia.org/wiki/Computer_cooling#Passive_cooling",
            "id": 217      
        }, 
        {
            "name": "Active Directory (AD)",
            "definition": "An advanced, hierarchical network directory service that comes with Windows servers and used for managing permissions and user access to network resources. Introduced in Windows 2000, Active Directory is a domain-based network that is structured like the Internet's Domain Naming System (DNS). Using the LDAP directory access protocol, a company's workgroups (departments, sections, offices, etc.) are assigned domain names similar to Web addresses, and any LDAP-compliant Windows, Mac, Unix or Linux client can access them. \n\n Initially, Active Directory was used only for centralized domain management. However, Active Directory eventually became an umbrella title for a broad range of directory-based identity-related services. Active Directory can function in a heterogeneous, enterprise network and encompass other directories including NDS and NIS+. Cisco supports Active Directory in its IOS router operating system.",
            "url": "https://en.wikipedia.org/wiki/Active_Directory",
            "id": 218      
        }, 
        {
            "name": "Ambient network",
            "definition": "Ambient networks is a network integration design that seeks to solve problems relating to switching between networks to maintain contact with the outside world. This project aims to develop a network software-driven infrastructure that will run on top of all current or future network physical infrastructures to provide a way for devices to connect to each other, and through each other to the outside world. \n\n Example: \n\n Alice has a PAN, a Personal Area Network on her body: she has a Bluetooth enabled PDA, mobile phone and laptop that she is carrying, and are all currently turned on, and forming a network. Her laptop also has the ability to connect using an available WLAN, and her mobile phone has the ability to connect through GPRS, though GPRS is slower and much more costly for Alice to use. She is now on the move, and her laptop is downloading her emails using the GPRS connection on the mobile: \n\n  Laptop → (Bluetooth) → Mobile → (GPRS) → Mobile phone network \n\n While walking, she passes into an area covered by a free WLAN hotspot: Her PAN now immediately starts to initiate a connection with the hotspot. This is called ‘merging’ of the networks (that of the hotspot and that of her PAN). Once this merging is complete, the downloading of her email continues totally unaffected, but instead of using the expensive and slow GPRS connection, it is now using the newly established WLAN connection. If she now wants to browse the web with her PDA, the PDA will also use the WLAN connection of the laptop: \n\n PDA → (bluetooth) → Laptop → (WLAN) → Hotspot.",
            "url": "https://en.wikipedia.org/wiki/Ambient_network",
            "id": 219      
        }, 
        {
            "name": "Ambient intelligence (AmI)",
            "definition": "In computing, ambient intelligence (AmI) refers to electronic environments that are sensitive and responsive to the presence of people. Ambient intelligence was a projection on the future of consumer electronics, telecommunications and computing that was originally developed in the late 1990s by Eli Zelkha and his team at Palo Alto Ventures for the time frame 2010–2020. \n\n Ambient intelligence would allow devices to work in concert to support people in carrying out their everyday life activities, tasks and rituals in an intuitive way using information and intelligence that is hidden in the network connecting these devices (for example: The Internet of Things). As these devices grew smaller, more connected and more integrated into our environment, the technological framework behind them would disappear into our surroundings until only the user interface remains perceivable by users. \n\n The ambient intelligence paradigm builds upon pervasive computing, ubiquitous computing, profiling, context awareness, and human-centric computer interaction design, of which, is characterized by systems and technologies that are embedded, context aware, personalized, adaptive and anticipatory. A typical context of ambient intelligence environment is home, but may also be extended to work spaces (offices, co-working), public spaces (based on technologies such as smart street lights), and hospital environments.",
            "url": "https://en.wikipedia.org/wiki/Ambient_intelligence",
            "id": 220      
        }, 
        {
            "name": "Acceptable use policy (AUP)",
            "definition": "An acceptable use policy (AUP), acceptable usage policy, Internet use policy IUP), or fair use policy is a set of rules applied by the owner, creator or administrator of a computer network website, or service. That restricts the ways in which the network, website or system may be used and sets guidelines as to how it should be used. AUP documents are written for corporations, businesses, universities, schools, internet service providers (ISPs), and website owners, often to reduce the potential for legal action that may be taken by a user, and often with little prospect of enforcement. \n\n Acceptable use policies are an integral part of the framework of information security policies; it is often common practice to ask new members of an organization to sign an AUP before they are given access to its information systems. For this reason, an AUP must be concise and clear. While at the same time covering the most important points about what users are, and are not allowed to do with the IT systems of an organization, it should refer users to the more comprehensive security policy where relevant. It should also, and very notably define what sanctions will be applied if a user breaks the AUP. Compliance with this policy should as usual, be measured by regular audits.",
            "url": "https://en.wikipedia.org/wiki/Acceptable_use_policy",
            "id": 221     
        }, 
        {
            "name": "Autonomous system (Internet)",
            "definition": "An autonomous system (AS) is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain, that presents a common and clearly defined routing policy to the Internet. Each AS is assigned an autonomous system number (ASN), for use in Border Gateway Protocol (BGP) routing. Autonomous System Numbers are assigned to Local Internet Registries (LIRs) and end user organizations by their respective Regional Internet Registries (RIRs), which in turn receive blocks of ASNs for reassignment from the Internet Assigned Numbers Authority (IANA). The IANA also maintains a registry of ASNs which are reserved for private use (and should therefore not be announced to the global Internet). \n\n Originally, the definition required control by a single entity, typically an Internet service provider (ISP) or a very large organization with independent connections to multiple networks, that adhered to a single and clearly defined routing policy. In March 1996, the newer definition came into use because multiple organizations can run BGP using private AS numbers to an ISP that connects all those organizations to the Internet. Even though there may be multiple autonomous systems supported by the ISP, the Internet only sees the routing policy of the ISP. That ISP must have an officially registered ASN. \n\n The number of unique autonomous networks in the routing system of the Internet exceeded 5,000 in 1999, 30,000 in late 2008, 35,000 in mid-2010, 42,000 in late 2012, 54,000 in mid-2016 and 60,000 in early 2018. The number of allocated ASNs exceeded 100,000 as of March 2021.",
            "url": "https://en.wikipedia.org/wiki/Autonomous_system_(Internet)",
            "id": 222      
        }, 
        {
            "name": "Actuator",
            "definition": "An actuator is a component of a machine that is responsible for moving and controlling a mechanism or system, for example by opening a valve. In simple terms, it is a ‘mover’. \n\n An actuator requires a control signal and a source of energy. The control signal is relatively low energy and may be electric voltage or current, pneumatic, or hydraulic fluid pressure, or even human power. Its main energy source may be an electric current, hydraulic pressure, or pneumatic pressure. When it receives a control signal, an actuator responds by converting the source's energy into mechanical motion. In the electric, hydraulic, and pneumatic sense, it is a form of automation or automatic control. \n\n An actuator is a mechanism by which a control system acts upon to perform an operation or task. The control system can be simple (a fixed mechanical or electronic system), software-based (e.g. a printer driver, robot control system), a human, or any other input. Along with sensors and controllers, actuators are an integral component in IoT (Internet of Things) interactions.",
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
            "definition": "1. Translating data and commands from the format of one application into the format of another. It is essentially data and command conversion on an ongoing basis between two or more incompatible systems. Implementing application integration has traditionally been done by tedious programming, or occasionally one package might support the interfaces of one or two other packages. However, the trend today is to use message brokers, applications servers and other specialized integration products that provide a common connecting point. Since the advent of the Web, these pre-packaged ‘middleware’ solutions have become widely used to Web enable the enterprise. \n\n 2. Redesigning disparate information systems into one system that uses a common set of data structures and rules.",
            "url": "https://en.wikipedia.org/wiki/Enterprise_application_integration",
            "id": 226      
        }, 
        {
            "name": "Middleware",
            "definition": "Software that functions as a conversion or translation layer. Middleware is also a consolidator and integrator. It can be described as ‘software glue’. Custom-programmed middleware solutions have been developed for decades to enable one application to interface with another, which either runs on a different platform or comes from a different vendor. \n\n Today, there is a diverse group of middleware products including: transaction processing monitor (TP Monitor), messaging middleware, distributed processing, distributed database middleware, database middleware, common interfaces, application server middleware, universal computing, network logon and enterprise integration. For example illustrations, see https://www.pcmag.com/encyclopedia/term/middleware",
            "url": "https://en.wikipedia.org/wiki/Middleware",
            "id": 227      
        }, 
        {
            "name": "Message broker",
            "definition": "A message broker (also known as an integration broker or interface engine) is an intermediary computer program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. Message brokers are elements in telecommunication or computer networks where software applications communicate by exchanging formally-defined messages. Message brokers are a building block of message-oriented middleware (MOM) but are typically not a replacement for traditional middleware like MOM and remote procedure call (RPC). \n\n A message broker is an architectural pattern for message validation, transformation, and routing. It mediates communication among applications, minimizing the mutual awareness that applications should have of each other in order to be able to exchange messages, effectively implementing decoupling. \n\n The primary purpose of a broker is to take incoming messages from applications and perform some action on them. Message brokers can decouple end-points, meet specific non-functional requirements, and facilitate reuse of intermediary functions. For example, a message broker may be used to manage a workload queue or message queue for multiple receivers, providing reliable storage, guaranteed message delivery and perhaps transaction management.",
            "url": "https://en.wikipedia.org/wiki/Message_broker",
            "id": 228      
        }, 
        {
            "name": "Network programmability",
            "definition": "Network programmability is the use of software to deploy, manage, and troubleshoot network elements. A programmable network is driven by an intelligent software stack that can take action based on business requests or network events. Network programmability can help communication service providers adapt to new trends including internet of things (IoT), 5G and edge computing. \n\n Complementary to network programmability is Software Defined Networking (SDN), which not only separates the control plane and forwarding plane of network elements but also provides (application programming interfaces) APIs to control and manage them.",
            "url": "https://www.redhat.com/en/blog/architects-guide-network-programmability",
            "id": 229      
        }, 
        {
            "name": "Proxy server",
            "definition": "In computer networking, a proxy server is a server application that acts as an intermediary between a client requesting a resource and the server providing that resource. Instead of connecting directly to a server that can fulfill a request for a resource, such as a file or web page, the client directs the request to the proxy server, which evaluates the request and performs the required network transactions. \n\n This serves as a method to simplify or control the complexity of the request, or provide additional benefits such as load balancing, privacy, or security. Proxies were devised to add structure and encapsulation to distributed systems. A proxy server thus functions on behalf of the client when requesting service, potentially masking the true origin of the request to the resource server.",
            "url": "https://en.wikipedia.org/wiki/Proxy_server",
            "id": 230      
        }, 
        {
            "name": "Geo-fence",
            "definition": "A geofence is a virtual perimeter for a real-world geographic area. A geo-fence could be dynamically generated (as in a radius around a point location) or match a predefined set of boundaries (such as school zones or neighborhood boundaries). \n\n The use of a geofence is called geofencing, and one example of use involves a location-aware device of a location-based service (LBS) user entering or exiting a geo-fence. This activity could trigger an alert to the device's user as well as messaging to the geo-fence operator. This info, which could contain the location of the device, could be sent to a mobile telephone or an email account. \n\n Geofencing uses technologies like GPS, or even IP address ranges to build their virtual fence. These virtual fences can be used to track the physical location of the device active in the particular region or the fence area. The location of the person using the device is taken as geocoding data and can be used further for advertising purposes.",
            "url": "https://en.wikipedia.org/wiki/Geo-fence",
            "id": 231      
        }, 
        {
            "name": "Stack",
            "definition": "In computing, a solution stack or software stack is a set of software subsystems or components needed to create a complete platform such that no additional software is needed to support applications. Applications are said to 'run on' or 'run on top of' the resulting platform. \n\n For example, to develop a web application, the architect defines the stack as the target operating system, web server, database, and programming language. Another version of a software stack is operating system, middleware, database, and applications. Regularly, the components of a software stack are developed by different developers independently from one another. \n\n Some components/subsystems of an overall system are chosen together often enough that the particular set is referred to by a name representing the whole, rather than by naming the parts. Typically, the name is an acronym representing the individual components. Notable examples include ELK, LAMP, LAPP, MEAN, MERN and XAMPP. \n\n The term ‘solution stack’ has, historically, occasionally included hardware components as part of a final product, mixing both the hardware and software in layers of support. \n\n A full-stack developer is expected to be able to work in all the layers of the stack. A full-stack web developer can be defined as a developer or engineer who works with both the front and back ends of a website or application. This means they can lead platform builds that involve databases, user-facing websites, and working with clients during the planning phase of projects.",
            "url": "https://en.wikipedia.org/wiki/Solution_stack",
            "id": 232      
        }, 
        {
            "name": "Scripting language",
            "definition": "A scripting language or script language is a programming language for a runtime system that automates the execution of tasks that would otherwise be performed individually by a human operator. Scripting languages are usually interpreted at runtime rather than compiled. \n\n A scripting language's primitives are usually elementary tasks or API calls, and the scripting language allows them to be combined into more programs. Environments that can be automated through scripting include application software, text editors, web pages, operating system shells, embedded systems, and computer games. A scripting language can be viewed as a domain-specific language for a particular environment; in the case of scripting an application, it is also known as an extension language. Scripting languages are also sometimes referred to as very high-level programming languages, as they sometimes operate at a high level of abstraction, or as control languages, particularly for job control languages on mainframes. \n\n The term scripting language is also used in a wider sense, namely, to refer to dynamic high-level programming languages in general; some are strictly interpreted languages, while others use a form of compilation. In this context, the term script refers to a small program in such a language; typically, contained in a single file, and no larger than a few thousand lines of code. \n\n The spectrum of scripting languages ranges from small to large, and from highly domain-specific language to general-purpose programming languages. A language may start as small and highly domain-specific and later develop into a portable and general-purpose language; conversely, a general-purpose language may later develop special domain-specific dialects. \n\n Examples of scripting languages include Bash, PowerShell, Python, JavaScript and Visual Basic for Applications (VBA).",
            "url": "https://en.wikipedia.org/wiki/Scripting_language",
            "id": 233      
        }, 
        {
            "name": "Polling",
            "definition": "Polling, or polled operation, in computer science, refers to actively sampling the status of an external device by a client program as a synchronous activity. Polling is most often used in terms of input/output (I/O), and is also referred to as polled I/O or software-driven I/O. \n\n Polling is a technique to determine, through continuous interrogation, whether a terminal or device is ready to transfer data. Contrast this with event-driven or interrupt-driven techniques, in which the system, when data is ready to be transferred, sends a signal and interrupts the system.",
            "url": "https://en.wikipedia.org/wiki/Polling_(computer_science)",
            "id": 234      
        }, 
        {
            "name": "Interrupt",
            "definition": "In digital computers, an interrupt (sometimes referred to as a trap) is a request for the processor to interrupt currently executing code (when permitted), so that the event can be processed in a timely manner. If the request is accepted, the processor will suspend its current activities, save its state, and execute a function called an interrupt handler (or an interrupt service routine, ISR) to deal with the event. This interruption is often temporary, allowing the software to resume normal activities after the interrupt handler finishes, although the interrupt could instead indicate a fatal error. \n\n Interrupts are commonly used by hardware devices to indicate electronic or physical state changes that require time-sensitive attention. Interrupts are also commonly used to implement computer multitasking, especially in real-time computing. Systems that use interrupts in these ways are said to be interrupt-driven.",
            "url": "https://en.wikipedia.org/wiki/Interrupt",
            "id": 235      
        }, 
        {
            "name": "Surface-mount technology",
            "definition": "Surface-mount technology (SMT) is a method in which the electrical components are mounted directly onto the surface of a printed circuit board (PCB). An electrical component mounted in this manner is referred to as a surface-mount device (SMD). In industry, this approach has largely replaced the through-hole technology construction method of fitting components, in large part because SMT allows for increased manufacturing automation which reduces cost and improves quality. It also allows for more components to fit on a given area of substrate. Both technologies can be used on the same board, with the through-hole technology often used for components not suitable for surface mounting such as large transformers and heat-sinked power semiconductors. \n\n An SMT component is usually smaller than its through-hole counterpart because it has either smaller leads or no leads at all. It may have short pins or leads of various styles, flat contacts, a matrix of solder balls (BGAs), or terminations on the body of the component. \n\n Surface mounting was originally called ‘planar mounting’.",
            "url": "https://en.wikipedia.org/wiki/Surface-mount_technology",
            "id": 236      
        }, 
        {
            "name": "Advanced persistent threat (APT)",
            "definition": "An advanced persistent threat (APT) is a stealthy threat actor, typically a nation state or state-sponsored group, which gains unauthorized access to a computer network and remains undetected for an extended period. In recent times, the term may also refer to non-state-sponsored groups conducting large-scale targeted intrusions for specific goals. \n\n Such threat actors' motivations are typically political or economic. Every major business sector has recorded instances of cyberattacks by advanced actors with specific goals, whether to steal, spy, or disrupt. These targeted sectors include government, defense, financial services, legal services, industrial, telecoms, consumer goods and many more. Some groups utilize traditional espionage vectors, including social engineering, human intelligence and infiltration to gain access to a physical location to enable network attacks. The purpose of these attacks is to install custom malware (malicious software). \n\n The median ‘dwell-time’, the time an APT attack goes undetected, is over 100 days globally.",
            "url": "https://en.wikipedia.org/wiki/Advanced_persistent_threat",
            "id": 237      
        }, 
        {
            "name": "Autostereoscopy",
            "definition": "Autostereoscopy is any method of displaying stereoscopic images (adding binocular perception of 3D depth) without the use of special headgear, glasses, something that affects vision, or anything for eyes on the part of the viewer. Because headgear is not required, it is also called ‘glasses-free 3D’ or ‘glassesless 3D’. \n\n There are two broad approaches currently used to accommodate motion parallax and wider viewing angles: eye-tracking, and multiple views so that the display does not need to sense where the viewer's eyes are located. Examples of autostereoscopic displays technology include lenticular lens, parallax barrier, volumetric display, holographic and light field displays.",
            "url": "https://en.wikipedia.org/wiki/Autostereoscopy",
            "id": 238      
        }, 
        {
            "name": "Buffer underrun",
            "definition": "In computing, buffer underrun or buffer underflow is a state occurring when a buffer used to communicate between two devices or processes is fed with data at a lower speed than the data is being read from it. The term is distinct from buffer overflow, a condition where a portion of memory being used as a buffer has a fixed size but is filled with more than that amount of data. This requires the program or device reading from the buffer to pause its processing while the buffer refills. This can cause undesired and sometimes serious side effects because the data being buffered is generally not suited to stop-start access of this kind. \n\n In relation to concurrent programming, a buffer underrun can be considered a form of resource starvation. The terms buffer ‘underrun’ and ‘buffer underflow’ are also used to mean ‘buffer underwrite’, a condition similar to buffer overflow, but where the program is tricked into writing before the beginning of the buffer, overriding potential data there, like permission bits.",
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
            "definition": "Artificial life (often abbreviated ALife or A-Life) is a field of study wherein researchers examine systems related to natural life, its processes, and its evolution, through the use of simulations with computer models, robotics, and biochemistry. There are three main kinds of alife, named for their approaches: soft, from software; hard, from hardware; and wet, from biochemistry. Artificial life researchers study traditional biology by trying to recreate aspects of biological phenomena. \n\n Artificial life studies the fundamental processes of living systems in artificial environments in order to gain a deeper understanding of the complex information processing that define such systems. These topics are broad, but often include evolutionary dynamics, emergent properties of collective systems, biomimicry, as well as related issues about the philosophy of the nature of life and the use of lifelike properties in artistic works. \n\n The modeling philosophy of artificial life strongly differs from traditional modeling by studying not only ‘life-as-we-know-it’ but also ‘life-as-it-might-be’.",
            "url": "https://en.wikipedia.org/wiki/Artificial_life",
            "id": 241      
        }, 
        {
            "name": "Brackets vs. Braces",
            "definition": "[ ] \n\n Square brackets, or simply ‘brackets’. \n\n Brackets are used in many computer programming languages, primarily for array indexing. But they are also used to denote general tuples, sets and other structures, just as in mathematics. There may be several other uses as well, depending on the language at hand. \n\n { } \n\n Curly brackets, or simply ‘braces’. \n\n In many programming languages, curly brackets enclose groups of statements and create a local scope. Such languages (C, C#, C++ and many others) are therefore called curly bracket languages. They are also used to define structures and enumerated type in these languages. \n\n One way to remember them apart is that braces look like they are ‘bracing’ under enormous pressure, almost buckling.",
            "url": "https://en.wikipedia.org/wiki/Bracket",
            "id": 242      
        }, 
        {
            "name": "Angle brackets",
            "definition": "The ‘<‘and ‘>’ symbols that are on the comma and period keys on the keyboard. Angle brackets are also called ‘chevrons’, ‘pointy brackets’, ‘triangular brackets’, ‘diamond brackets’, ‘tuples’, ‘guillemets’, ‘left and right carets’, ‘broken brackets’, or ‘brokets’. \n\n The ASCII less-than and greater-than characters <> are often used for angle brackets. In most cases only those characters are accepted by computer programs; the Unicode angle brackets are not recognized (for instance in HTML tags). \n\n In C++ chevrons (actually less-than and greater-than) are used to surround arguments to templates. In HTML, chevrons (actually 'greater than' and 'less than' symbols) are used to bracket meta text. For example <b> denotes that the following text should be displayed as bold. Pairs of meta text tags are required – much as brackets themselves are usually in pairs. The end of the bold text segment would be indicated by </b>. This use is sometimes extended as an informal mechanism for communicating mood or tone in digital formats such as messaging, for example adding ‘<sighs>’ at the end of a sentence.",
            "url": "https://en.wikipedia.org/wiki/Bracket#Angle_brackets",
            "id": 243      
        }, 
        {
            "name": "AWS Lambda",
            "definition": "An Amazon AWS service that runs the customer's program code without them having to provision and manage a server in the AWS system. It is a prime example of function as a service (FaaS). \n\n AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced in November 2014. \n\n Node.js, Python, Java, Go, Ruby and C# (through .NET) are all officially supported, as of 2018. For pricing, AWS Lambda is metered by rounding up to the nearest millisecond with no minimum execution time.",
            "url": "https://en.wikipedia.org/wiki/AWS_Lambda",
            "id": 244      
        }, 
        {
            "name": "Software agent",
            "definition": "In computer science, a software agent is a computer program that acts for a user or other program in a relationship of agency, which derives from the Latin ‘agere’ (to do): an agreement to act on one's behalf. Such ‘action on behalf of’ implies the authority to decide which, if any, action is appropriate. Agents are colloquially known as bots, from robot. They may be embodied, as when execution is paired with a robot body, or as software such as a chatbot executing on a phone (e.g. Siri) or other computing device. Software agents may be autonomous or work together with other agents or people. Software agents interacting with people (e.g. chatbots, human-robot interaction environments) may possess human-like qualities such as natural language understanding and speech, personality or embody humanoid form. \n\n Related and derived concepts include intelligent agents (in particular exhibiting some aspects of artificial intelligence, such as reasoning), autonomous agents (capable of modifying the methods of achieving their objectives), distributed agents (being executed on physically distinct computers), multi-agent systems (distributed agents that work together to achieve an objective that could not be accomplished by a single agent acting alone), and mobile agents (agents that can relocate their execution onto different processors).",
            "url": "https://en.wikipedia.org/wiki/Software_agent",
            "id": 245      
        }, 
        {
            "name": "Sorting",
            "definition": "n computer science, arranging in an ordered sequence is called ‘sorting’. Sorting is a common operation in many applications, and efficient algorithms to perform it have been developed. \n\n The most common uses of sorted sequences are: \n\n Making lookup or search efficient; \n Making merging of sequences efficient; \n Enable processing of data in a defined order; \n\n Common sorting algorithms: \n\n Bubble/Shell sort: Exchange two adjacent elements if they are out of order. Repeat until array is sorted. \n Insertion sort: Scan successive elements for an out-of-order item, then insert the item in the proper place. \n Selection sort: Find the smallest (or biggest) element in the array, and put it in the proper place. Swap it with the value in the first position. Repeat until array is sorted. \n Quick sort: Partition the array into two segments. In the first segment, all elements are less than or equal to the pivot value. In the second segment, all elements are greater than or equal to the pivot value. Finally, sort the two segments recursively. \n Merge sort: Divide the list of elements in two parts, sort the two parts individually and then merge it. \n\n The opposite of sorting, rearranging a sequence of items in a random or meaningless order, is called shuffling.",
            "url": "https://en.wikipedia.org/wiki/Sorting",
            "id": 246      
        }, 
        {
            "name": "Isotropic vs. Anisotropic",
            "definition": "Isotropic and anisotropic are terms that describe whether or not the properties of materials depend on direction. When a property is the same in all directions, the material is isotropic. When a property varies according to direction, the material is anisotropic. The terms come from the Greek isos (equal) and tropos (way). The ‘an’ in ‘anisotropic’ means ‘not’. \n\n Properties that are isotropic in some materials and anisotropic in others include refractive index, absorbance, electrical conductivity, tensile strength, Young’s modulus, etc. \n\n Keep in mind, a material may be isotropic for one property, yet anisotropic for another. For example, a piece of polarized glass is isotropic for mechanical properties, yet anisotropic for light filtration. Also, scale is important. For example, the universe is generally isotropic and homogenous with respect to cosmic blackbody radiation, but when you examine regions more closely, you see heterogeneity and anisotropy. \n\n An isotropic antenna is an omnidirectional antenna: it radiates equal power in all directions, while an anisotropic antenna is a directional antenna: the power level is not the same in all directions.",
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
            "definition": "In computing, alias is a command in various command-line interpreters (shells), which enables a replacement of a word by another string. It is mainly used for abbreviating a system command, or for adding default arguments to a regularly used command. alias is available in Unix shells, AmigaDOS, 4DOS/4NT, KolibriOS, Windows PowerShell, ReactOS, and the EFI shell. Aliasing functionality in the MS-DOS and Microsoft Windows operating systems is provided by the DOSKey command-line utility. \n\n An alias will last for the life of the shell session. Regularly used aliases can be set from the shell's rc file (such as .bashrc) so that they will be available upon the start of the corresponding shell session. The alias commands may either be written in the config file directly or sourced from a separate file. \n\n Example: \n\n alias gc='git commit'",
            "url": "https://en.wikipedia.org/wiki/Alias_(command)",
            "id": 250      
        }, 
        {
            "name": "Alice (software)",
            "definition": "An open source, object-oriented development environment for building 3D animations, games and virtual worlds. Running under Windows, Mac and Linux, it is based on Java and is programmed by dragging and dropping predefined functions into a work area. Designed to teach fundamental concepts to novices, such as the relationship between programming statements and objects, Alice is supported by textbooks, tutorials, lessons and tests. \n\n  The software was developed first at University of Virginia in 1994, then Carnegie Mellon (from 1997), by a research group led by Randy Pausch. According to Pausch, the name ‘Alice’ comes from author Lewis Carroll, who wrote Alice’s Adventures in Wonderland. \n\n ‘Carroll was a mathematician, novelist, and photographer. Most important, he could do intellectually difficult things but also realized the most powerful thing was to be able to communicate clearly and in an entertaining way. This inspires our efforts to make something as complex as computer programming easy and fun.’",
            "url": "https://en.wikipedia.org/wiki/Randy_Pausch",
            "id": 251      
        }, 
        {
            "name": "",
            "definition": "In computer science, a high-level programming language is a programming language with strong abstraction from the details of the computer. In contrast to low-level programming languages, it may use natural language elements, be easier to use, or may automate (or even hide entirely) significant areas of computing systems (e.g. memory management), making the process of developing a program simpler and more understandable than when using a lower-level language. The amount of abstraction provided defines how ‘high-level’ a programming language is. \n\n Examples of high-level programming languages in active use today include Python, Visual Basic, Delphi, Perl, PHP, ECMAScript, Ruby, C#, Java and many others. \n\n The terms high-level and low-level are inherently relative. Some decades ago, the C language, and similar languages, were most often considered ‘high-level’, as it supported concepts such as expression evaluation, parameterised recursive functions, and data types and structures, while assembly language was considered ‘low-level’. Today, many programmers might refer to C as low-level, as it lacks a large runtime-system (no garbage collection, etc.), basically supports only scalar operations, and provides direct memory addressing. It, therefore, readily blends with assembly language and the machine level of CPUs and microcontrollers.",
            "url": "High-level programming language",
            "id": 252      
        }, 
        {
            "name": "Machine code",
            "definition": "In computer programming, machine code is any low-level programming language, consisting of machine language instructions, which are used to control a computer's central processing unit (CPU). Each instruction causes the CPU to perform a very specific task, such as a load, a store, a jump, or an arithmetic logic unit (ALU) operation on one or more units of data in the CPU's registers or memory. \n\n Machine code is a strictly numerical language which is designed to run as fast as possible, and may be considered as the lowest-level representation of a compiled or assembled computer program or as a primitive and hardware-dependent programming language. While it is possible to write programs directly in machine code, managing individual bits and calculating numerical addresses and constants manually is tedious and error-prone. For this reason, programs are very rarely written directly in machine code in modern contexts, but may be done for low level debugging, program patching (especially when assembler source is not available) and assembly language disassembly. \n\n The majority of practical programs today are written in higher-level languages or assembly language. The source code is then translated to executable machine code by utilities such as compilers, assemblers, and linkers, with the important exception of interpreted programs, which are not translated into machine code. However, the interpreter itself, which may be seen as an executor or processor performing the instructions of the source code, typically consists of directly executable machine code (generated from assembly or high-level language source code).",
            "url": "https://en.wikipedia.org/wiki/Machine_code",
            "id": 253      
        }, 
        {
            "name": "Assembly language",
            "definition": "In computer programming, assembly language (or assembler language), is any low-level programming language in which there is a very strong correspondence between the instructions in the language and the architecture's machine code instructions. Assembly language usually has one statement per machine instruction (1:1), but constants, comments, assembler directives, symbolic labels of, e.g., memory locations, registers, and macros are generally also supported. \n\n Assembly code is converted into executable machine code by a utility program referred to as an assembler. The term ‘assembler’ is generally attributed to Wilkes, Wheeler and Gill in their 1951 book The Preparation of Programs for an Electronic Digital Computer, who, however, used the term to mean ‘a program that assembles another program consisting of several sections into a single program’. The conversion process is referred to as assembly, as in assembling the source code. The computational step when an assembler is processing a program is called assembly time. Assembly language may also be called symbolic machine code. \n\n Because assembly depends on the machine code instructions, each assembly language is specific to a particular computer architecture.",
            "url": "",
            "id": 254      
        }, 
        {
            "name": "Microcode",
            "definition": "In processor design, microcode is a technique that interposes a layer of computer organization between the central processing unit (CPU) hardware and the programmer-visible instruction set architecture of a computer. Microcode is a layer of hardware-level instructions that implement higher-level machine code instructions or internal finite-state machine sequencing in many digital processing elements. Microcode is used in general-purpose central processing units, although in current desktop CPUs, it is only a fallback path for cases that the faster hardwired control unit cannot handle. \n\n Microcode typically resides in special high-speed memory and translates machine instructions, state machine data or other input into sequences of detailed circuit-level operations. It separates the machine instructions from the underlying electronics so that instructions can be designed and altered more freely. It also facilitates the building of complex multi-step instructions, while reducing the complexity of computer circuits. Writing microcode is often called microprogramming and the microcode in a particular processor implementation is sometimes called a microprogram.",
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
            "definition": "Another name for 802.11ax \n\n IEEE 802.11ax, officially marketed by the Wi-Fi Alliance as Wi-Fi 6 (2.4 GHz and 5 GHz) and Wi-Fi 6E (6 GHz), is an IEEE standard for wireless local-area networks (WLANs) and the successor of 802.11ac. It is also known as High Efficiency Wi-Fi, for the overall improvements to Wi-Fi 6 clients under dense environments. It is designed to operate in license-exempt bands between 1 and 7.125 GHz, including the 2.4 and 5 GHz bands already in common use as well as the much wider 6 GHz band (5.925–7.125 GHz in the US). \n\n The main goal of this standard is enhancing throughput-per-area in high-density scenarios, such as corporate offices, shopping malls and dense residential apartments. While the nominal data rate improvement against 802.11ac is only 37%, the overall throughput improvement (over an entire network) is 300% (hence High Efficiency).  This also translates to 75% lower latency. \n\n The quadrupling of overall throughput is made possible by a higher spectral efficiency. The key feature underpinning 802.11ax is orthogonal frequency-division multiple access (OFDMA), which is equivalent to cellular technology applied into Wi-Fi. Other improvements on spectrum utilization are better power-control methods to avoid interference with neighboring networks, higher order 1024‑QAM, up-link direction added with the down-link of MIMO and MU-MIMO to further increase throughput, as well as dependability improvements of power consumption and security protocols such as Target Wake Time and WPA3.",
            "url": "https://en.wikipedia.org/wiki/Wi-Fi_6",
            "id": 258      
        }, 
        {
            "name": "Alpha testing",
            "definition": "The alpha phase of the release life cycle is the first phase of software testing (alpha is the first letter of the Greek alphabet, used as the number 1). In this phase, developers generally test the software using white-box techniques. Additional validation is then performed using black-box or gray-box techniques, by another testing team. Moving to black-box testing inside the organization is known as alpha release. \n\n Alpha software is not thoroughly tested by the developer before it is released to customers. Alpha software may contain serious errors, and any resulting instability could cause crashes or data loss. Alpha software may not contain all of the features that are planned for the final version. In general, external availability of alpha software is uncommon in proprietary software, while open source software often has publicly available alpha versions. The alpha phase usually ends with a feature freeze, indicating that no more features will be added to the software. At this time, the software is said to be feature complete. A beta test is carried out following acceptance testing at the supplier's site (alpha test) and immediately before the general release of the software as a product. In general an alpha version or release of a software package intends to do something particular, mostly does so, yet isn't guaranteed to do so fully.",
            "url": "https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha",
            "id": 259      
        }, 
        {
            "name": "Beta testing",
            "definition": "Beta, named after the second letter of the Greek alphabet, is the software development phase following alpha. Software in the beta stage is also known as betaware. A beta phase generally begins when the software is feature complete but likely to contain a number of known or unknown bugs. Software in the beta phase will generally have many more bugs in it than completed software and speed or performance issues, and may still cause crashes or data loss. The focus of beta testing is reducing impacts to users, often incorporating usability testing. The process of delivering a beta version to the users is called beta release and is typically the first time that the software is available outside of the organization that developed it. Software beta releases can be either public or private, depending on whether they are openly available or only available to a limited audience. Beta version software is often useful for demonstrations and previews within an organization and to prospective customers. Some developers refer to this stage as a preview, preview release, prototype, technical preview or technology preview (TP), or early access. \n\n Beta testers are people who actively report issues of beta software. They are usually customers or representatives of prospective customers of the organization that develops the software. Beta testers tend to volunteer their services free of charge but often receive versions of the product they test, discounts on the release version, or other incentives. \n\n Some software is kept in so-called perpetual beta, where new features are continually added to the software without establishing a final 'stable' release. As the Internet has facilitated rapid and inexpensive distribution of software, companies have begun to take a looser approach to use of the word beta.",
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
            "definition": "A fiber Bragg grating (FBG) is a type of distributed Bragg reflector constructed in a short segment of optical fiber that reflects particular wavelengths of light and transmits all others. This is achieved by creating a periodic variation in the refractive index of the fiber core, which generates a wavelength-specific dielectric mirror. Hence a fiber Bragg grating can be used as an inline optical fiber to block certain wavelengths, can be used for sensing applications, or it can be used as wavelength-specific reflector.",
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
            "definition": "In networking, a black hole refers to a place in the network where incoming or outgoing traffic is silently discarded (or ‘dropped’), without informing the source that the data did not reach its intended recipient. When examining the topology of the network, the black holes themselves are invisible, and can only be detected by monitoring the lost traffic; hence the name. \n\n The most common form of black hole is simply an IP address that specifies a host machine that is not running or an address to which no host has been assigned. A null route or black hole route is a network route (routing table entry) that goes nowhere. Matching packets are dropped (ignored) rather than forwarded, acting as a kind of very limited firewall. The act of using null routes is often called blackhole filtering.",
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
            "definition": "A breadboard, or protoboard, is a construction base for prototyping of electronics. Originally the word referred to a literal bread board, a polished piece of wood used when slicing bread. In the 1970s the solderless breadboard (a.k.a. plugboard, a terminal array board) became available and nowadays the term ‘breadboard’ is commonly used to refer to these. \n\n Because the solderless breadboard does not require soldering, it is reusable. This makes it easy to use for creating temporary prototypes and experimenting with circuit design. For this reason, solderless breadboards are also popular with students and in technological education. Older breadboard types did not have this property. A stripboard (Veroboard) and similar prototyping printed circuit boards, which are used to build semi-permanent soldered prototypes or one-offs, cannot easily be reused. A variety of electronic systems may be prototyped by using breadboards, from small analog and digital circuits to complete central processing units (CPUs).",
            "url": "https://en.wikipedia.org/wiki/Breadboard",
            "id": 269      
        }, 
        {
            "name": "https://en.wikipedia.org/wiki/Blind_signature",
            "definition": "A method used with digital signatures when the privacy of the sender's message is extremely important and when the signing is applied to the message by a third party rather than the message creator. Before handing the message over for signing, the sender uses a blinding algorithm to scramble the message. A blind signature allows a third party to sign a message and verify that the message came from a particular sender but without them knowing the message contents.",
            "url": "https://en.wikipedia.org/wiki/Blind_signature",
            "id": 270      
        }, 
        {
            "name": "Breakout box",
            "definition": "A breakout box is a piece of electrical test equipment used to support integration testing, expedite maintenance, and streamline the troubleshooting process at the system, subsystem, and component level by simplifying the access to test signals. Breakout boxes span a wide spectrum of functionality. Some serve to break out every signal connection coming into a unit while others breakout only specific signals commonly monitored for either testing or troubleshooting purposes. Some have electrical connectors and others have optical fiber connectors. \n\n A breakout box serves as a troubleshooting tool to determine the wiring of an electrical connector interface on a networking device or computer. Typically, a breakout box is inserted between two electrical devices to determine which signal or power interconnects are active. Breakout boxes are extremely useful in troubleshooting connection problems resulting from manufacturing errors (e.g., miswiring) or defective interconnects resulting from broken wiring. Breakout boxes are specific examples of a more general category of network testing equipment called ‘status monitors’.",
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
            "name": "A binary large object (BLOB or blob)",
            "definition": "A binary large object (BLOB or blob) is a collection of binary data stored as a single entity. Blobs are typically images, audio or other multimedia objects, though sometimes binary executable code is stored as a blob. They can exist as persistent values inside some databases or version control system, or exist at runtime as program variables in some programming languages. It is not to be confused with a binary file stored in a file system. \n\n Depending on the implementation and culture around usage, the concept might be alternately referred to as a ‘basic large object’ or ‘binary data type’. The term is used in NoSQL databases, especially in key-value store databases such as Redis. The term is also used by languages that allow runtime manipulation of Blobs, like JavaScript.  \n\n In the world of free and open-source software, the term is also borrowed to refer to proprietary device drivers, which are distributed without their source code, exclusively through binary code; in such use, the term ‘binary blob’ is common. \n\n Contrast with CLOB (Character Large OBject) A database field that holds a large amount of text (character data). A CLOB is also known as a ‘memo field’ in some database programs. ",
            "url": "https://en.wikipedia.org/wiki/Binary_large_object",
            "id": 273      
        }, 
        {
            "name": "Front and back office application",
            "definition": "A front office application is any software that faces the customer directly. It provides functionality and data necessary to take orders, configure complex products and provide effective service and support to customers. It includes customer relationship management (CRM), sales force automation, customer support and field service. \n\n In turn, a back office application does not interact directly with the customer. It provides functionality for internal operations such as enterprise resource planning (ERP), inventory control, manufacturing and all of the supply chain activities associated with procuring goods, services and raw materials. If an ERP system includes order entry and customer service capabilities, that system would bridge both back office and front office.",
            "url": "https://en.wikipedia.org/wiki/Front_and_back_office_application",
            "id": 274      
        }, 
        {
            "name": "Software bloat",
            "definition": "Software bloat is a process whereby successive versions of a computer program become perceptibly slower, use more memory, disk space or processing power, or have higher hardware requirements than the previous version, while making only dubious user-perceptible improvements or suffering from feature creep. The term is not applied consistently; it is often used as a pejorative by end users (bloatware) to describe undesired user interface changes even if those changes had little or no effect on the hardware requirements. In long-lived software, perceived bloat can occur from the software servicing a large, diverse marketplace with many differing requirements. Most end users will feel they only need some limited subset of the available functions, and will regard the others as unnecessary bloat, even if end users with different requirements require those functions. \n\n Actual (measurable) bloat can occur due to de-emphasising algorithmic efficiency in favour of other concerns like developer productivity, or possibly through the introduction of new layers of abstraction like a virtual machine or other scripting engine for the purposes of convenience when developer constraints are reduced. The perception of improved developer productivity, in the case of practising development within virtual machine environments, comes from the developers no longer taking resource constraints and usage into consideration during design and development; this allows the product to be completed faster but it results in increases to the end user's hardware requirements to compensate. \n\n The term ‘bloatware’ is also used to describe unwanted pre-installed software or bundled programs.",
            "url": "https://en.wikipedia.org/wiki/Software_bloat",
            "id": 275      
        }, 
        {
            "name": "Bricks, clicks and flips",
            "definition": "A business model by which a company integrates both offline (bricks) and online (clicks) presences, sometimes with the third extra physical catalogs (flips). \n\n By the mid-2010s, many (physical store) retailers offered ordering via their website, mobile phone apps, as well as by voice over the telephone. The wide uptake of smartphones made the model even more popular, as customers could browse and order from their smartphone whenever they had spare time. The model has historically also been known by such terms as clicks and bricks, click and mortar, bricks, clicks and flips, and WAMBAM, i.e. ‘web application meets bricks and mortar’.",
            "url": "https://en.wikipedia.org/wiki/Omnichannel_retail_strategy",
            "id": 276      
        }, 
        {
            "name": "Backhaul",
            "definition": "In a hierarchical telecommunications network, the backhaul portion of the network comprises the intermediate links between the core network, or backbone network, and the small subnetworks at the edge of the network. \n\n The original definition of backhaul was to transmit a telephone call or data beyond its normal destination point and then back again in order to utilize available personnel (operators, agents, etc.) or network equipment not available at the destination location. For example, depending on distances and service arrangements, it might be cheaper to send a telephone call on a private line to a location way beyond the destination and then dial up the destination, which is back in the other direction. \n\n The term evolved into a more generic meaning and often refers to transmitting from a remote site or network to a central or main site. It implies a high-capacity line; for example, to backhaul from a wireless mesh network to the wired network means aggregating all the traffic on the wireless mesh over one or more high-speed lines to a private network or the Internet.",
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
            "definition": "Crippleware has been defined in realms of both computer software and hardware. In software, crippleware means that ‘vital features of the program such as printing or the ability to save files are disabled until the user purchases a registration key’. While crippleware allows consumers to see the software before they buy, they are unable to test its complete functionality because of the disabled functions. \n\n Hardware crippleware is ‘a hardware device that has not been designed to its full capability’. The functionality of the hardware device is limited to encourage consumers to pay for a more expensive upgraded version. Usually the hardware device considered to be crippleware can be upgraded to better or its full potential by way of a trivial change, such as removing a jumper wire. The manufacturer would most likely release the crippleware as a low-end or economy version of their product.",
            "url": "https://en.wikipedia.org/wiki/Crippleware",
            "id": 281      
        }, 
        {
            "name": "Dribbleware",
            "definition": "(1) Software that is publicly previewed well in advance of its actual release. Dribbleware is one stage beyond vaporware. \n\n (2) Software that is released in small increments, each version having a few modest enhancements.",
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
            "name": "https://en.wikipedia.org/wiki/Careware",
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
            "definition": "Grid computing is the use of widely distributed computer resources to reach a common goal. A computing grid can be thought of as a distributed system with non-interactive workloads that involve many files. Grid computing is distinguished from conventional high-performance computing systems such as cluster computing in that grid computers have each node set to perform a different task/application. Grid computers also tend to be more heterogeneous and geographically dispersed (thus not physically coupled) than cluster computers. Although a single grid can be dedicated to a particular application, commonly a grid is used for a variety of purposes. Grids are often constructed with general-purpose grid middleware software libraries. Grid sizes can be quite large. Grid computing software is sometimes referred to as 'griddleware'",
            "url": "https://en.wikipedia.org/wiki/Grid_computing",
            "id": 289      
        }, 
        {
            "name": "Nagware",
            "definition": "Nagware (also known as begware, annoyware or a nagscreen) is a pejorative term for shareware that persistently reminds the user to purchase a license. It usually does this by popping up a message when the user starts the program, or intermittently while the user is using the application. These messages can appear as windows obscuring part of the screen, or as message boxes that can quickly be closed. Some nagware keeps the message up for a certain time period, forcing the user to wait to continue to use the program. Unlicensed programs that support printing may superimpose a watermark on the printed output, typically stating that the output was produced by an unlicensed copy. \n\n Some titles display a dialog box with payment information and a message that paying will remove the notice, which is usually displayed either upon startup or after an interval while the application is running. These notices are designed to annoy the user into paying.",
            "url": "https://en.wikipedia.org/wiki/Shareware#Nagware",
            "id": 290      
        }, 
        {
            "name": "Push technology",
            "definition": "Push technology or server push, is a style of Internet-based communication where the request for a given transaction is initiated by the publisher or central server. It is contrasted with pull/get, where the request for the transmission of information is initiated by the receiver or client. \n\n Push services are often based on information preferences expressed in advance. This is called a publish/subscribe model. A client ‘subscribes’ to various information ‘channels’ provided by a server; whenever new content is available on one of those channels, the server pushes that information out to the client. \n\n Push is sometimes emulated with a polling technique, particularly under circumstances where a real push is not possible, such as sites with security policies that require rejection of incoming HTTP/S requests.",
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
            "definition": "Software that enables users to obtain enterprise-wide information more easily. Such products are considered a step up from the typical decision support tools because they more tightly integrate querying, reporting, OLAP, data mining and data warehousing functions. \n\n Many products claim BI capabilities, but the end goal is to let users slice and dice the information from their organization's numerous databases without having to wait for their IT departments to develop complex queries. \n\n Business intelligence was the 1990s buzzword for the management information system (MIS) of the 1970s and the decision support system (DSS) and executive information system (EIS) of the 1980s. MIS implementations often failed because the hardware was too slow and the software was not sophisticated. Countless DSS, EIS and OLAP tools followed, which added functionality, but were often point solutions to the problem. BI implies yet more integration and ease of use (of course, no matter what the subject, every new approach in the information field is touted as the one providing more integration and greater ease of use).",
            "url": "https://en.wikipedia.org/wiki/Predictive_analytics",
            "id": 293      
        }, 
        {
            "name": "Backronym",
            "definition": "(BACKward acRONYM) A reverse acronym. Instead of turning a multi-word term into letters, such as ‘central processing unit’ into CPU, a given set of letters becomes a multi-word term. For example, TEMPEST was a code name that was turned into ‘Telecommunications Electronics Material Protected from Emanating Spurious Transmissions’. DVD originally meant ‘digital video disc’ but was later changed to ‘digital versatile disc’.",
            "url": "https://en.wikipedia.org/wiki/Backronym",
            "id": 294      
        }, 
        {
            "name": "Software brittleness",
            "definition": "Older software that has been patched so many times that even small changes to the source code make the program fail. The term stems from metal that has been worked and reworked so often that it becomes brittle. \n\n The term may also refer to software that was designed with very little error checking or a rigid set of assumptions that are no longer valid. In such cases, even minor variations of input may cause the program to crash.",
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
            "definition": "In computing, endianness is the order or sequence of bytes of a word of digital data in computer memory. Endianness is primarily expressed as big-endian (BE) or little-endian (LE). A big-endian system stores the most significant byte of a word at the smallest memory address and the least significant byte at the largest. A little-endian system, in contrast, stores the least-significant byte at the smallest address. \n\n Bi-endianness is a feature supported by numerous computer architectures that feature switchable endianness in data fetches and stores or for instruction fetches. Other orderings are generically called middle-endian or mixed-endian.",
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
            "definition": "No-code development platforms (NCDPs) allow programmers and non-programmers to create application software through graphical user interfaces and configuration instead of traditional computer programming. No-code development platforms are closely related to low-code development platforms as both are designed to expedite the application development process. \n\n However, unlike low-code, no-code development platforms require no code writing at all, generally offering prebuilt templates that businesses can build apps with. These platforms have both increased in popularity as companies deal with the parallel trends of an increasingly mobile workforce and a limited supply of competent software developers. \n\n No-code development platforms are closely related to visual programming languages.",
            "url": "https://en.wikipedia.org/wiki/No-code_development_platform",
            "id": 302      
        },
        {
            "name": "Visual programming",
            "definition": "Developing programs with tools that allow menus, buttons, icons and other screen components to be selected from a palette. Also called a ‘GUI builder’, visual programming tools allow the user interface elements to be dragged, dropped and resized the way objects are drawn in graphics programs. Traditional source code may be completely eliminated, or it may be embedded within the graphics components. \n\n Many programming environments include a visual editor for the user interface. Although the program logic is written in a traditional language, the screen elements are programmed visually.",
            "url": "https://en.wikipedia.org/wiki/Visual_programming_language",
            "id": 303      
        },
        {
            "name": "Brochureware",
            "definition": "A website that advertises a product but contains only the equivalent of a paper brochure with no interaction. A website can be much more elaborate. For example, it can zoom into images for more detail, make recommendations based on user input, provide downloads of software demos, compute and process the sale and remember the questions users asked the last time they visited. All this is missing in brochureware.",
            "url": "https://en.wikipedia.org/wiki/Brochureware",
            "id": 304      
        },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 305      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 306      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 307      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 308      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 309      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 310      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 3      
        # },
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 4      
        # },



    ]

    return random.choice(word_list)
 
