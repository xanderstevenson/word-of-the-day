import random


##                        ATTENTION DEVELOPERS!!
##     Hi, please add new definitions to the end of the list. 
##     A Wikipedia entry is the default url unless it is lacking or absent.



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
        +{
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
            "definition": "A cloud-computing model where the cloud providers own, operate and offer hardware and software for consumers on an on-demand and pay-as-you-go model. The resources offered are scalable physical or virtualized storage, compute and network resources.",
            "url": "https://en.wikipedia.org/wiki/Infrastructure_as_a_service",
            "id": 21       
        },       
        {
            "name": "Infrastructure as Code (IaC)",
            "definition": "The process of managing and provisioning infrastructure based on machine-readable definition files as opposed to manual configuration done on hardware or through shell scripts or other, interactive configuration tools.",
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
            "definition": "A type of serverless cloud computing service where code is executed in response to events or triggers but without the need for maintaining the complex infrastructure typically associated with building and launching applications. \n \n Building an application following this model is one way of achieving a 'serverless' architecture, and is typically used when building microservices applications. With FaaS, users manage only functions and data while the cloud provider manages the application. \n \n This allows developers to get the functions they need without paying for services when code isn’t running. Some popular FaaS examples include: Amazon’s AWS Lambda, Google Cloud Functions and Microsoft Azure Functions.",
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
            "definition": "A set of principles and practices which incorporates aspects of software engineering and applies them to infrastructure and operations problems.The main goals are to create scalable and highly reliable software systems. Site reliability engineering is closely related to DevOps, a set of practices that combine software development and IT operations, and SRE has also been described as a specific implementation of DevOps. However, while DevOps is focused on getting code to production, SRE ensures that the code running in production works properly.",
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
            "name": "Extended reality",
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
            "definition": "A connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build or use such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API.",
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
            "definition": "Responsive web design (RWD) or responsive design is an approach to web design that aims to make web pages render well on a variety of devices and window or screen sizes from minimum to maximum display size to ensure usability and satisfaction. /n/n A responsive design adapts the web-page layout to the viewing environment by using techniques such as fluid proportion-based grids, flexible images, and CSS3 media queries, an extension of the @media rule, in the following ways: \n - The fluid grid concept calls for page element sizing to be in relative units like percentages, rather than absolute units like pixels or points. \n - Flexible images are also sized in relative units, so as to prevent them from displaying outside their containing element. \n - Media queries allow the page to use different CSS style rules based on characteristics of the device the site is being displayed on, e.g. width of the rendering surface (browser window width or a physical display size). \n - Responsive layouts automatically adjust and adapt to any device screen size, whether it is a desktop, a laptop, a tablet, or a mobile phone. \n\n Responsive web design became more important as users of mobile devices came to account for the majority of web site visitors",
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
            "definition": "Nearly all programming paradigms support some level of grouping and encapsulation of concerns into separate, independent entities. Aspect-oriented programming entails breaking down program logic into distinct parts (so-called concerns, which are cohesive areas of functionality). AOP aims to increase modularity by allowing the separation of cross-cutting concerns. \n\n  Systems are composed of several components, each responsible for a specific piece of functionality. But often these components also carry additional responsibilities beyond their core functionality. System services such as logging, transaction management, and security often find their way into components whose core responsibilities is something else. These system services are commonly referred to as cross-cutting concerns because they tend to cut across multiple components in a system. Logging exemplifies a crosscutting concern because a logging strategy necessarily affects every logged part of the system. Logging thereby crosscuts all logged classes and methods.  \n\n Aspect-oriented programming allows for the creation of relationships between different classes. These relationships are arbitrary, but can be used to encapsulate the housekeeping code needed to create compatibility between two classes. \n\n AOP is a technique for building common, reusable routines that can be applied applicationwide. During development this facilitates separation of core application logic and common, repeatable tasks (input validation, logging, error handling, etc.). At runtime, you can use AOP to hot-patch applications that are vulnerable to SQL injection, or embed intrusion detection and audit logging capabilities directly into an application without modifying the underlying source code.",
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
            "definition": "A functional specification (also, functional spec, specs, functional specifications document (FSD), functional requirements specification) in systems engineering and software development is a document that specifies the functions that a system or component must perform (often part of a requirements specification). \\n The documentation typically describes what is needed by the system user as well as requested properties of inputs and outputs (e.g. of the software system). A functional specification is the more technical response to a matching requirements document, e.g. the Product Requirements Document ‘PRD’. Thus it picks up the results of the requirements analysis stage. On more complex systems multiple levels of functional specifications will typically nest to each other, e.g. on the system level, on the module level and on the level of technical details.",
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
            "definition": "Patches are often temporary fixes between full releases of software packages. Patches are used to correct both large and small issues that may or may not require fixing a software bug, installing new drivers, addressing new security vulnerabilities, addressing software stability issues or upgrading the software. Generally, patches are automatic updates that self-install packages in various sizes and are delivered on a set schedule. They can be included in the product’s new version release with additional updates and fixes. \n\n Hotfixes can also solve many of the same issues as a patch, but it is applied to a ‘hot’ system—a live system—to fix an issue immediately and without creating system downtimes or outages. Normally, you’ll create a hotfix quickly, as an urgent measure against issues that need to be fixed immediately and outside of your normal development flow. Unlike patches, hotfixes address very specific issues like adding a new feature, bug, or security fix or changing database schema. Importantly, hotfixes are not always publicly released, in contrast to patches. \n\n Where a hotfix is executed quickly without restarting any systems or hardware, a coldfix is just the opposite. Implementing a coldfix requires users to log out of the software while entire systems need to be rebooted for fixes to go into effect. They’re normally announced several days ahead of time to give users advanced notice the service will be unavailable while the fix is completed. Notices generally include estimated times the service will be back online. \n\n A bugfix sounds a lot like a hotfix, but the difference lies in the timing and execution of the correction. Bugfixes generally describe issues that are found and resolved during production or testing phases or even after deployment as part of the normal release cycle of a product. Hotfixes are applied only after the product has been released and is live. Implementing a bugfix, also known as a program temporary fix (PTF), can be as simple as adding missing parentheses in a piece of code. But the fix can become quite challenging if the symptoms don’t clearly point to a cause. Once you’ve uncovered the root cause and issued a bug fix, it’s not uncommon for your programmers to find that one bugfix can actually introduce a new bug.",
            "url": "https://www.bmc.com/blogs/patch-hotfix-coldfix-bugfix/",
            "id": 122     
        },        
        {
            "name": "Integrated development environment (IDE)",
            "definition": "A software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. Some IDEs, such as NetBeans and Eclipse, contain the necessary compiler, interpreter, or both; others, such as SharpDevelop and Lazarus, do not. \n\n The boundary between an IDE and other parts of the broader software development environment is not well-defined; sometimes a version control system or various tools to simplify the construction of a graphical user interface (GUI) are integrated. Many modern IDEs also have a class browser, an object browser, and a class hierarchy diagram for use in object-oriented software development.",
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
            "definition": "Joint Application Development in short JAD is the process which is used to design and develop computer based system/solutions. It collects requirements side by side as per business needs while developing new information systems for a company that means JAD involves the client or end-users in designing and development process. It also comprises of approaches for improving the quality of specification and user participation through a successive collaborative workshops called JAD sessions. Since client is involved throughout the development process it leads to faster development times and greater client satisfaction.",
            "url": "https://en.wikipedia.org/wiki/Joint_application_design",
            "id": 125     
        },           
        {
            "name": "KISS Principle (Keep It Simple, Stupid)",
            "definition": "KISS, an acronym for keep it simple, stupid, is a design principle noted by the U.S. Navy in 1960. The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided. The phrase has been associated with aircraft engineer Kelly Johnson. The term ‘KISS principle’ was in popular use by 1970. Variations on the phrase include: ‘Keep it simple, silly’, ‘keep it short and simple’, ‘keep it short and sweet’, ‘keep it simple and straightforward’, ‘keep it small and simple’, ‘keep it simple, soldier’, ‘keep it simple, sailor’, or ‘keep it sweet and simple’.",
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
            "definition": "The idea that various programming structures can be likened to the structures of well-known pasta dishes: \n\n Unstructured procedural programming is called spaghetti code. Spaghetti code is often considered a pejorative phrase for unstructured and difficult-to-maintain source code. In this sense, spaghetti code can be caused by several factors, such as volatile project requirements, lack of programming style rules, and software engineers with insufficient ability or experience. \n\n Lasagna code refers to structured programming code whose layers are so complicated and intertwined that making a change in one layer would necessitate changes in all other layers. \n\n Ravioli code is a term specific to object-oriented programming. It describes code that comprises well-structured classes that are easy to understand in isolation, but difficult to understand as a whole.",
            "url": "https://en.wikipedia.org/wiki/Spaghetti_code",
            "id": 131      
        },     
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 132      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 133      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 134      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 135      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 136      
        # },     
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 137      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 138      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 139      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 140      
        # },     
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # },   
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # },     
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # },     
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id":      
        # }, 
    ]

    return random.choice(word_list)
 
