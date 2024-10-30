from django.shortcuts import render

#Nice Database Setup : List of dictionaries
project_list = [
    {
        "title": "Public Transport Assistant",
        "image": "app_mydetail/images/transport.png",
        "serial": "One",
        "year": 2024,
        "description": "The Public Transport Assistant for Estimated Time of Arrival (ETA) project aims to revolutionize the way people navigate public transport systems by providing real-time, accurate information about arrival times, delays, and optimal routes.",
        "link": "https://github.com/ChandraMohan-Sah/Public_Transport_Assistent"
    },
    {
        "title": "Course Selling Website",
        "image": "app_mydetail/images/teaching.png",
        "serial": "Two",
        "year": 2023,
        "description": "Our mission is to empower individuals with the knowledge and skills they need to achieve their personal and professional goals.",
        "link": "#"
    },
    {
        "title": "Instant Messages: Chat App",
        "image": "app_mydetail/images/messaging.png",
        "serial": "Three",
        "year": 2022,
        "description": "The ultimate chat app for seamless and secure instant messaging. Whether you're chatting with friends, family, or colleagues, our app ensures fast, reliable, and private communication. Experience a new level of connectivity.",
        "link": "#"
    },
    {
        "title": "DBMS Simple Project : CRUD Operation",
        "image": "app_mydetail/images/Database.jpg",
        "serial": "four",
        "year": 2022,
        "description": "Database management project that applies CRUD operation and instantly the actions can be seen on the dashboard",
        "link": "https://github.com/ChandraMohan-Sah/Website-ElephantSQL-Project"
    },
        {
        "title": "Everlasting Portfolio",
        "image": "app_mydetail/images/portfolio.png",
        "serial": "five",
        "year": 2022,
        "description": "Explore an Everlasting Portfolio – a showcase of innovation, skill, and growth that evolves with every project.",
        "link": "https://github.com/ChandraMohan-Sah/StaticPortfolioWeb/tree/main/Portfolio"
    },
    {
        "title": "Canteen Management System ",
        "image": "app_mydetail/images/canteen.jpg",
        "serial": "six",
        "year": 2022,
        "description": "A Canteen Management System is used to streamline operations, allowing orders, inventory, and payments to be managed efficiently while improving customer satisfaction.",
        "link": "https://github.com/ChandraMohan-Sah/Canteen-Management-System"
    }
]



experiences = [
    {
        "tech":"CPP",
        "percentage":"95%",
        "color":"w3-blue"
    },
    {
        "tech":"Arduino Programming",
        "percentage":"35%",
        "color":"w3-grey"
    },
    {
        "tech":"Python",
        "percentage":"85%",
        "color":"w3-red"
    },

    {
        "tech":"HTML, CSS, Javascript",
        "percentage":"20%",
        "color":"w3-pink"
    },
    {
        "tech":"Django and DRF",
        "percentage":"85%",
        "color": " w3-teal"
    },
    {
        "tech":"Database with MySQL",
        "percentage":"75%",
        "color":"w3-teal"
    },
    {
        "tech":"git and Github",
        "percentage":"35%",
        "color":"w3-grey"
    },

    {
        "tech":"Kicad",
        "percentage":"35%",
        "color":"w3-brown"
    },
    {
        "tech":"Linux Familiarity",
        "percentage":"50%",
        "color":"w3-green"
    }


]



def home(request):
    context = {
        "projects": project_list,
        "experiences": experiences
    }

    return render(request, 'base.html', context)






