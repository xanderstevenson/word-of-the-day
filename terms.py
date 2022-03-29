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
        {
            "name": "DevOps",
            "definition": "DevOps combines software development (dev) and IT Operations (Ops). It's primary goals include shortening the software and systems develoment lifecycles while increasing the quality of products. DevOps practices involve continuous development, continuous testing, continuous integration, continuous deployment and continuous monitoring of software applications throughout its development life cycle.",
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
            "definition": "A computer infrastructure (VMs, containers, network appliances, etc.) that can’t be altered once it’s deployed, which makes it easier to prevent and mitigate security vulnerabilities. This is often with enforced via an automated process that overwrites unauthorized changes or through a system that won’t allow changes in the first place. \n \n Containers are an excellent example of immutable infrastructure because persistent changes to containers can only be made by creating a new version of the container or recreating the existing container from its image.",
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
            "definition": "A software testing technique that repeatedly applies inputs on a module to ensure it is functioning correctly and that there are no bugs. Gorilla testing is a manual testing procedure and is performed on selected modules of the software system with selected test cases. \n\n The main objective is to test specific modules heavily and find any faults in their implementation. Since the tester manually applies the same test case repeatedly, it is also known as Torture Testing, Fault Tolerance Testing, or Frustrating Testin",
            "url": "https://www.educative.io/edpresso/what-is-gorilla-testing",
            "id": 41     
        },  
        {
            "name": "Monkey testing",
            "definition": "In software testing, monkey testing is a technique where the user tests the application or system by providing random inputs and checking the behavior, or seeing whether the application or system will crash. Monkey testing is usually implemented as random, automated unit tests.",
            "url": "https://en.wikipedia.org/wiki/Monkey_testing",
            "id": 42     
        },  
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 43     
        # },  
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 44     
        # },  
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 45     
        # },  
        #     {
        #     "name": "",
        #     "definition": "",
        #     "url": "",
        #     "id": 46     
        # }, 

    ]


    # test_dict = {"id": "33",}
    
    # return test_dict
    return random.choice(word_list)
 
