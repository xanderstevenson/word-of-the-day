
import random



def return_word():

    word_list = [



        {
            "name": "wireframe",
            "definition": "A basic sketch or outline of the key information of a planned website. This 'skeleton' is used by developers and designers when laying out a webpage."
        },
        {
            "name": "kerning",
            "definition": "The space between characters (numbers, letters, puncuation) and the process of adjusting this space to improve the readabilty."
        },
        {
            "name": "leading (pronounced 'led-ing')",
            "definition": "The vertical distance between lines on a website."
        },
        {
            "name": "meta elements",
            "definition": "HTML elements that do not appear visually on a webpage but give the web browser valuable information anout the webpage, such as author, last modified, keywords, etc."
        },
        {
            "name": "self-closing tag",
            "definition": "In HTML, it's an opening tag that doesn't have a corresponding closing tag, but instead closes itse;f with a forward slash immediately prior to the right angle bracket, e.g. <img src='mysite.com/media/myimage5'/>"
        },
        {
            "name": "back end",
            "definition": "The parts of a website or webservice which are unseen but make it run. This includes databases, servers, middleware, microservices and applications."
        },

    ]


    return random.choice(word_list)



return_word()