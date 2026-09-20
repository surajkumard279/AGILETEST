# -*- coding: utf-8 -*-
"""
All site content lives here. Edit, then run:  python build.py
That regenerates every .html page. Prices, dates and contact details that
the browser needs are in assets/js/config.js.
"""

BRAND = "ATECHNOLOGIES"
EMAIL = "training@ATECHNOLOGIES.com"
WHATSAPP = "910000000000"
CURRENCY = "₹"

# ---------------------------------------------------------------- categories
# slug -> file categories/<slug>.html
CATEGORIES = [
    dict(slug="ai", name="AI Courses",
         blurb="Practical classes on using AI tools in Agile delivery, from prompts to team working agreements."),
    dict(slug="ai-native", name="AI-Native Courses",
         blurb="Classes for teams that build and run products with AI at the core."),
    dict(slug="devops", name="DevOps Courses",
         blurb="Shorten the path from idea to running software with shared practices between development and operations."),
    dict(slug="icagile", name="ICAgile Courses",
         blurb="Learning-outcome based Agile classes that lead to ICAgile certificates."),
    dict(slug="scrum-at-scale", name="Scrum@Scale Courses",
         blurb="Grow Scrum beyond one team while keeping the framework light."),
    dict(slug="scrum", name="Scrum Courses",
         blurb="Core Scrum roles and practices for Scrum Masters and Product Owners."),
    dict(slug="safe", name="Scaled Agile (SAFe) Courses",
         blurb="Role-based classes for people working in a SAFe enterprise."),
    dict(slug="kanban", name="Kanban Courses",
         blurb="Design and improve flow-based work systems."),
    dict(slug="safe-micro-credential", name="SAFe Micro-credential Courses",
         blurb="Short, focused classes on one SAFe topic."),
    dict(slug="tbr", name="Training from the BACK of the Room",
         blurb="Learn how to design classes where learners do most of the talking and doing."),
]

DEFAULT_PREREQ = [
    "Everyone is welcome, whatever their experience",
    "Some familiarity with Agile ideas helps",
]
DEFAULT_INCLUDES = [
    "Live virtual class with hands-on group activities",
    "Course workbook and templates",
    "Certificate of attendance",
    "Access to a learner community after class",
]

# ------------------------------------------------------------------- courses
# featured=True  -> shown in the home page "Next class" card
# popular=True   -> shown in the home page "Popular courses" row
COURSES = [
    dict(slug="ai-for-agile-teams", cat="ai", title="AI for Agile Teams", price=32000, days=1, initials="AI",
         popular=True,
         summary="See where AI tools help an Agile team, where they get in the way, and how to bring them into planning, refinement and delivery.",
         audience=["Scrum Masters and Agile coaches", "Product owners and product managers", "Team leads and delivery managers"],
         topics=["What AI tools can and cannot do for a team", "Using AI in backlog refinement", "Writing prompts that give usable results",
                 "Checking AI output before you rely on it", "Team working agreements for AI use", "Measuring whether AI is helping"],
         outcomes=["Choose tasks that suit an AI assistant", "Write clear, reusable prompts", "Review AI output for errors and bias",
                   "Agree team rules for AI use", "Track the effect on flow and quality"],
         prereq=["No coding experience needed", "Basic familiarity with how Agile teams work"],
         includes=["Live hands-on exercises", "Reusable prompt templates", "Course workbook", "Certificate of attendance"]),

    dict(slug="prompt-engineering-for-delivery", cat="ai", title="Prompt Engineering for Delivery Teams", price=28000, days=1, initials="PE",
         summary="Build a shared prompt library for the everyday work of a delivery team: stories, test ideas, release notes and retrospectives.",
         audience=["Business analysts and product owners", "Testers and developers", "Project and program managers"],
         topics=["How prompts are structured", "Giving context and constraints", "Prompts for stories and acceptance criteria",
                 "Prompts for testing and review", "Sharing and versioning prompts", "Handling confidential information"],
         outcomes=["Structure a prompt for a specific job", "Improve a weak prompt step by step", "Build a small prompt library for your team",
                   "Spot when a task should not go to an AI tool"]),

    dict(slug="ai-native-product-owner", cat="ai-native", title="AI-Native Product Owner", price=45000, days=2, initials="AIPO",
         summary="Learn how product ownership changes when AI features, data and models are part of the product.",
         audience=["Product owners and product managers", "Business owners of AI initiatives", "Anyone writing requirements for AI features"],
         topics=["Finding problems worth solving with AI", "Writing backlog items for AI features", "Working with data and model teams",
                 "Defining quality and safety for AI output", "Experiments and release decisions", "Explaining AI behavior to stakeholders"],
         outcomes=["Frame an AI opportunity as a testable hypothesis", "Write clear acceptance criteria for AI behavior",
                   "Plan experiments and staged releases", "Communicate limits and risks to stakeholders"],
         prereq=["Experience with a product backlog", "No data science background needed"]),

    dict(slug="devops-foundations", cat="devops", title="DevOps Foundations", price=38500, days=2, initials="DO",
         summary="Understand the culture, practices and tools that move work from idea to production quickly and safely.",
         audience=["Developers and testers", "Operations and infrastructure engineers", "Managers who work with delivery teams"],
         topics=["Why DevOps exists", "Flow, feedback and learning", "Continuous integration and delivery",
                 "Infrastructure as code", "Monitoring and incident response", "Building a DevOps improvement plan"],
         outcomes=["Explain the core DevOps ideas", "Map your own delivery pipeline and find delays", "Choose practices that fit your context",
                   "Start a small, measurable improvement"]),

    dict(slug="icagile-agile-fundamentals", cat="icagile", title="ICAgile Agile Fundamentals", price=34000, days=2, initials="ICP",
         summary="A first structured look at Agile values, principles and the most common team practices.",
         audience=["People new to Agile", "Team members moving to an Agile team", "Managers supporting Agile teams"],
         topics=["Agile values and principles", "Common Agile methods compared", "Roles on an Agile team",
                 "Planning, tracking and reviewing work", "Working with customers", "Continuous improvement"],
         outcomes=["Describe the Agile mindset in plain terms", "Compare Scrum, Kanban and XP practices", "Take part in the main Agile events",
                   "Suggest improvements for your own team"],
         prereq=["No prior Agile experience required"]),

    dict(slug="scrum-at-scale-practitioner", cat="scrum-at-scale", title="Scrum@Scale Practitioner", price=48900, days=2, initials="S@S",
         summary="Learn how several Scrum teams stay aligned through scaled events, shared backlogs and clear leadership roles.",
         audience=["Scrum Masters and Product Owners", "Executives and managers of several teams", "Agile coaches"],
         topics=["Scrum recap and the scaling problem", "The Scrum Master and Product Owner cycles", "Scaled events and cadences",
                 "Removing shared impediments", "Metrics for many teams", "Planning your own rollout"],
         outcomes=["Describe the scaled Scrum structure", "Run a scaled event with several teams", "Spot and clear cross-team impediments",
                   "Sketch a first rollout step for your organization"],
         prereq=["Working knowledge of Scrum", "Experience on or near a Scrum team"]),

    dict(slug="certified-scrummaster", cat="scrum", title="Certified ScrumMaster® (CSM)", price=44500, days=2, initials="CSM",
         popular=True,
         summary="Learn the Scrum framework and the Scrum Master's role in helping a team deliver working software often.",
         audience=["New and aspiring Scrum Masters", "Project managers moving to Agile", "Team members who want to understand Scrum well"],
         topics=["Agile and Scrum foundations", "Scrum roles, events and artifacts", "Facilitating the Scrum events",
                 "Coaching a self-managing team", "Handling common team problems", "Growing as a Scrum Master"],
         outcomes=["Explain Scrum accurately to a new team", "Facilitate each Scrum event", "Help a team improve how it works",
                   "Deal with typical impediments"],
         includes=["Live virtual class with hands-on group activities", "Course workbook and templates",
                   "Preparation for the certification assessment", "Access to a learner community after class"]),

    dict(slug="certified-scrum-product-owner", cat="scrum", title="Certified Scrum Product Owner® (CSPO)", price=44500, days=2, initials="CSPO",
         popular=True,
         summary="Learn how a Product Owner sets direction, orders the backlog and keeps a team focused on value.",
         audience=["Product owners and product managers", "Business analysts", "Stakeholders who steer a product"],
         topics=["The Product Owner's role", "Vision and product goals", "Building and ordering a backlog",
                 "Writing and splitting stories", "Working with stakeholders", "Measuring value"],
         outcomes=["Write a clear product goal", "Order a backlog by value and risk", "Split large items into small, useful ones",
                   "Run a productive review with stakeholders"],
         includes=["Live virtual class with hands-on group activities", "Course workbook and templates",
                   "Preparation for the certification assessment", "Access to a learner community after class"]),

    dict(slug="safe-ssm", cat="safe", title="AI-Empowered SAFe® Scrum Master (SSM)", price=52390, days=2, initials="SSM",
         featured=True, popular=True,
         summary="Learn how a Scrum Master supports a team on an Agile Release Train and helps run team and program events. The course prepares you for the certification exam, and the fee includes one exam attempt for the Certified SAFe® 6 Scrum Master credential.",
         about=["This two-day class looks at the Scrum Master role from the point of view of a whole enterprise, not a single team. You work through how a team prepares for and delivers a Program Increment (PI), the planning cycle that keeps every level of the organization aligned.",
                "Where a classic Scrum Master course focuses on team-level Scrum, this one is about how a Scrum Master helps a team succeed alongside many other teams."],
         audience=["New and experienced Scrum Masters", "Team leads who guide a delivery team", "Release Train Engineers"],
         topics=["How Scrum works inside a scaled enterprise", "What a Scrum Master does, and does not do", "Taking part in PI planning",
                 "Facilitating iteration execution", "Closing out a Program Increment", "Coaching an Agile team"],
         prereq=["Familiarity with Agile concepts and principles", "Awareness of Scrum, Kanban and Extreme Programming (XP)",
                 "Working knowledge of how software or hardware is developed"],
         outcomes=["Describe how Scrum runs in a scaled enterprise", "Facilitate Scrum events", "Run an effective iteration",
                   "Support a Program Increment from start to finish", "Keep the team improving",
                   "Coach Agile teams toward better business results", "Support a DevOps approach"],
         includes=["One exam attempt, with the exam fee included", "Hands-on virtual collaboration activities",
                   "Preparation for, and eligibility to take, the certification exam", "One year of access to the learning platform"],
         callout="You must attend both days to be eligible for the exam."),

    dict(slug="safe-popm", cat="safe", title="SAFe® Product Owner/Product Manager (POPM)", price=62700, days=2, initials="POPM",
         summary="Learn how product owners and product managers plan, prioritize and deliver value on an Agile Release Train.",
         audience=["Product owners", "Product managers", "Business owners and business analysts"],
         topics=["Customer-centric product thinking", "Building and refining the backlog", "Preparing for PI planning",
                 "Supporting iteration execution", "Delivering and measuring value", "Working with stakeholders"],
         outcomes=["Connect team backlogs to program goals", "Prioritize by economic value", "Take part in PI planning with confidence",
                   "Judge whether delivered work met its goal"],
         prereq=["Experience with product or business analysis work", "Awareness of Scrum and Kanban"]),

    dict(slug="safe-lpm", cat="safe", title="SAFe® Lean Portfolio Management (LPM)", price=114880, days=2, initials="LPM",
         summary="Learn how strategy, funding and governance connect to the teams that do the work.",
         audience=["Executives and portfolio managers", "Enterprise and solution architects", "Finance and program office leaders"],
         topics=["Connecting strategy to execution", "Lean budgets and funding value streams", "Managing the portfolio backlog",
                 "Guardrails and governance", "Measuring portfolio progress", "Leading through change"],
         outcomes=["Describe lean portfolio practices", "Set up funding around value streams", "Choose useful portfolio measures",
                   "Plan a first improvement in your own portfolio"],
         prereq=["Experience in portfolio, finance or leadership roles"]),

    dict(slug="safe-hardware-teams", cat="safe", title="SAFe® for Hardware Teams", price=81230, days=2, initials="HW",
         summary="Apply Agile and lean ways of working to hardware and systems development, where changes are costly and lead times are long.",
         audience=["Hardware and systems engineers", "Engineering managers", "Program and product managers in hardware companies"],
         topics=["Why hardware needs different Agile thinking", "Set-based design and early learning", "Planning around long lead times",
                 "Integration and testing cadence", "Working with suppliers", "Improving flow in engineering"],
         outcomes=["Plan hardware work in short learning cycles", "Reduce risk with early integration", "Coordinate with suppliers using shared cadences",
                   "Pick a first pilot in your organization"]),

    dict(slug="kanban-system-design", cat="kanban", title="Kanban System Design", price=46000, days=2, initials="KSD",
         summary="Design a Kanban system for your own work: map the flow, set limits, and choose policies and measures that help.",
         audience=["Team leads and managers", "Agile coaches", "Operations and support teams"],
         topics=["Visualizing work and workflow", "Work-in-progress limits", "Classes of service and policies",
                 "Flow metrics and forecasting", "Feedback loops and cadences", "Evolving the system"],
         outcomes=["Map your own workflow", "Set sensible limits and policies", "Read flow metrics", "Forecast delivery from your own data"]),

    dict(slug="safe-agile-contracting", cat="safe-micro-credential", title="SAFe® Agile Contracting for Government", price=66810, days=1, initials="ACG",
         summary="Learn how to write and manage contracts that support Agile delivery in a government setting.",
         audience=["Contracting officers and specialists", "Program managers", "Legal and procurement staff"],
         topics=["Why traditional contracts strain Agile work", "Contract structures that allow change", "Working with incremental delivery",
                 "Reviews and acceptance", "Managing risk and compliance", "Case examples"],
         outcomes=["Match contract structure to the way work is delivered", "Define acceptance in incremental terms",
                   "Spot clauses that block iteration"],
         prereq=["Experience in contracting or procurement"]),

    dict(slug="training-from-the-back-of-the-room", cat="tbr", title="Training from the BACK of the Room", price=36000, days=2, initials="TBR",
         summary="Learn a four-step way to design classes where learners connect, do, share and reflect instead of listening to lectures.",
         audience=["Trainers and facilitators", "Agile coaches", "Team leads who teach"],
         topics=["Why people learn more by doing", "The four steps of a learner-led session", "Designing activities that stick",
                 "Working in a virtual room", "Giving instructions people can follow", "Redesigning one of your own sessions"],
         outcomes=["Design a short learner-led session", "Replace a lecture with an activity", "Run activities well online",
                   "Get useful feedback from learners"]),
]

# --------------------------------------------------------------------- team
TEAM = [
    dict(name="Team member name", role="Lead trainer", bio="Add a short bio here: years of experience, certifications and the topics this person teaches.", initials="TM"),
    dict(name="Team member name", role="Agile coach", bio="Add a short bio here: the kinds of teams and organizations this person has coached.", initials="TM"),
    dict(name="Team member name", role="Consultant", bio="Add a short bio here: the industries and transformation work this person has led.", initials="TM"),
    dict(name="Team member name", role="Program manager", bio="Add a short bio here: how this person supports learners before and after class.", initials="TM"),
]

# ----------------------------------------------------------------- services
CONSULTING = [
    ("Agile assessment", "We review how your teams plan, deliver and learn today, and give you a short list of changes that would help most."),
    ("Transformation roadmap", "A staged plan for adopting Agile ways of working, with clear goals for each stage and the people who own them."),
    ("Launching release trains and team of teams", "Practical support to set up teams, roles and cadences so several teams can plan and deliver together."),
    ("Leadership alignment", "Working sessions that help managers and executives support the change rather than slow it down."),
]
COACHING = [
    ("Team coaching", "Regular sessions with a team to improve planning, flow and collaboration in the context of its real work."),
    ("Scrum Master and Product Owner coaching", "One-to-one guidance for people growing into these roles, with practice on real situations."),
    ("Leadership coaching", "Support for managers and executives who are changing how they lead and make decisions."),
    ("Coaching after training", "Follow-up sessions in the weeks after a class to turn what people learned into habits."),
]
TOOLS = [
    ("Tool one", "Describe the tool and how it helps your learners or clients. Link to the vendor page below.", "https://example.com"),
    ("Tool two", "Describe the tool and how it helps your learners or clients. Link to the vendor page below.", "https://example.com"),
]

# --------------------------------------------------------------------- site
# Full public address of the site, WITH trailing slash. Used for canonical
# links, sitemap.xml and the 404 page. Change it to your real address, e.g.
#   https://yourname.github.io/agile-site/     or     https://www.yourdomain.com/
SITE_URL = "https://example.github.io/agile-site/"
