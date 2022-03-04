
import random



def return_word():

    word_list = [



        {
            "name": "Wireframe",
            "definition": "A basic sketch or outline of the key information of a planned website. This 'skeleton' is used by developers and designers when laying out a webpage.",
            "url": "https://en.wikipedia.org/wiki/Website_wireframe"
        },
        {
            "name": "Kerning",
            "definition": "The space between characters (numbers, letters, puncuation) and the process of adjusting this space to improve the readabilty.",
            "url": "https://en.wikipedia.org/wiki/Kerning"
        },
        {
            "name": "Leading",
            "definition": "(pronounced 'led-ing') The vertical distance between lines on a website.",
            "url": "https://en.wikipedia.org/wiki/Leading"
        },
        {
            "name": "Scalability",
            "definition": "The ability of a system to efficiently handle a growing or shrinking workload by providing it with more or less resources. Scaling horizontally (out/in) means adding more nodes to (or removing nodes from) a system while scaling vertically (up/down) means adding resources to (or removing resources from) a single node.",
            "url": "https://en.wikipedia.org/wiki/Scalability"
        },
        {
            "name": "DevOps",
            "definition": "DevOps combines software development (dev) and IT Operations (Ops). It's primary goals include shortening the software and systems develoment lifecycles while increasing the quality of products. DevOps practices involve continuous development, continuous testing, continuous integration, continuous deployment and continuous monitoring of software applications throughout its development life cycle.",
            "url": "https://en.wikipedia.org/wiki/DevOps"
        },
        {
            "name": "CI/CD",
            "definition": "The combined practices of Continuous Integration (CI) and either Continuous delivery or Continuous deployment with the aim towards increasing efficiency and productivity. CI/CD compiles incremental changes to software code made by developers. Automated testing is performed and then automated delivery to customers is generated.",
            "url": "https://en.wikipedia.org/wiki/CI/CD"
        },
        {
            "name": "Circuit breaking",
            "definition": "Circuit breaking creates resilient microservices applications by stopping the request and response process if a service is not working. Protected functions are wrapped in circuit breakers, which, when tripped, stop receiving calls. This makes sure threads ar enot waiting on calls, which can render a system unresponsive.",
            "url": "https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern"
        },
        {
            "name": "Fault injection",
            "definition": "Fault injection is a system testing method which involves the deliberate introduction of network faults and errors into a system. It can be used to identify design or configuration weaknesses, and to ensure that the system can handle faults and recover from error conditions.",
            "url": "https://en.wikipedia.org/wiki/Fault_injection"
        },  
        {
            "name": "Sidecar",
            "definition": "Just as a sidecar can attach to a motorcycle, in software architecture a sidecar attaches to a parent application and enhances/extends its functionality.",
            "url": "https://en.wikipedia.org/wiki/Microservices#Service_mesh"
        },
        {
            "name": "Canary deployment",
            "definition": "A strategy of delayed deployment where an application is releases incrementally to a subset of users (e.g. 1%, 5%, 15%, 50%, 75%, 100%).",
            "url": "https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html",
        },  
        {
            "name": "Zero trust",
            "definition": "Zero trust is a security framework which requires all users, both internal and external to the network or organization, to be continuously validated for security posture and configuration before being granted or keeping any access to data and applications.",
            "url": "https://en.wikipedia.org/wiki/Zero_trust_security_model"
        },
        {
            "name": "Hardening",
            "definition": "The process of securing a system by reducing its vulnerability to attack. Hardening typically includes keeping software updated, changing default passwords, removing unnecessary software and accounts, and the disabling or removal of unnecessary services and software.",
            "url": "https://en.wikipedia.org/wiki/Hardening_(computing)"
        },       
        {
            "name": "Enumeration",
            "definition": "An enumeration is a complete, ordered listing of all the items in a collection. The term is commonly used in mathematics and computer science to refer to a listing of all of the elements of a set. In cybersecurity, enumeration is defined as a process which establishes an active connection to the target hosts to discover potential attack vectors in the system.",
            "url": "https://en.wikipedia.org/wiki/Enumeration"
        },       
        # {
        #     "name": "runtime",
        #     "definition": "Runtime is the period of time when a program is running. It begins when a program is opened (or executed) and ends with the program is quit or closed. Runtime is a technical term, used most often in software development. It is commonly seen in the context of a "runtime error," which is an error that occurs while a program is running. The term "runtime error" is used to distinguish from other types of errors, such as syntax errors and compilation errors, which occur before a program is run.",
        #     "url": "https://techterms.com/definition/runtime#:~:text=Runtime%20is%20the%20period%20of,most%20often%20in%20software%20development."
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
        # {
        #     "name": "",
        #     "definition": "",
        #     "url": ""
        # },       
             
   
    ]


    return random.choice(word_list)
 


return_word()