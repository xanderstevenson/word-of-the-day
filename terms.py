
import random



def return_word():

    word_list = [



        {
            "name": "wireframe",
            "definition": "A basic sketch or outline of the key information of a planned website. This 'skeleton' is used by developers and designers when laying out a webpage.",
            "url": ""
        },
        {
            "name": "kerning",
            "definition": "The space between characters (numbers, letters, puncuation) and the process of adjusting this space to improve the readabilty.",
            "url": ""
        },
        {
            "name": "leading",
            "definition": "(pronounced 'led-ing') The vertical distance between lines on a website.",
            "url": ""
        },
        {
            "name": "meta elements",
            "definition": "HTML elements that do not appear visually on a webpage but give the web browser valuable information anout the webpage, such as author, last modified, keywords, etc.",
            "url": ""
        },
        {
            "name": "self-closing tag",
            "definition": "In HTML, it's an opening tag that doesn't have a corresponding closing tag, but instead closes itse;f with a forward slash immediately prior to the right angle bracket, e.g. <img src='mysite.com/media/myimage5'/>",
            "url": ""
        },
        {
            "name": "back end",
            "definition": "The parts of a website or webservice which are unseen but make it run. This includes databases, servers, middleware, microservices and applications.",
            "url": ""
        },
        {
            "name": "circuit breaking",
            "definition": "Circuit breaking creates resilient microservices applications by stopping the request and response process if a service is not working. Protected functions are wrapped in circuit breakers, which, when tripped, stop receiving calls. This makes sure threads ar enot waiting on calls, which can render a system unresponsive.",
            "url": ""
        },
        {
            "name": "fault injection",
            "definition": "Fault injection is a system testing method which involves the deliberate introduction of network faults and errors into a system. It can be used to identify design or configuration weaknesses, and to ensure that the system can handle faults and recover from error conditions.",
        },  
        {
            "name": "sidecar",
            "definition": "Just as a sidecar can attach to a motorcycle, in software architecture a sidecar attaches to a parent application and enhances/extends its functionality.",
            "url": ""
        },
        {
            "name": "canary deployment",
            "definition": "A strategy of delayed deployment where an application is releases incrementally to a subset of users (e.g. 1%, 5%, 15%, 50%, 75%, 100%).",
        },  
        {
            "name": "zero trust",
            "definition": "Zero trust is a security framework which requires all users, both internal and external to the network or organization, to be continuously validated for security posture and configuration before being granted or keeping any access to data and applications.",
            "url": ""
        },
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