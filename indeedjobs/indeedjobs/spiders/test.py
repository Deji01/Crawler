def location():
    urls = []

    roles = ["Graduate",
             "Intern",
             "Remote",
             "IT",
             "Data",
             "Engineer",
             "Entry",
             "Full",
             "Part",
             "Cloud",
             "Analyst",
             "UI",
             "Cyber",
             "Devops",
             "MLops",
             "Research"
             ]

    for role in roles:
        link1 = f"https://uk.indeed.com/jobs?q={role}&l=London%2C%20Greater%20London&start=10&vjk=0fe9a7e476658f5c"
        link2 = f"https://uk.indeed.com/jobs?q={role}&l=Birmingham%2C%20West%20Midlands"
        link3 = f"https://uk.indeed.com/jobs?q={role}&l=Manchester%2C%20Greater%20Manchester"
        link4 = f"https://uk.indeed.com/jobs?q={role}&l=Bristol"
        link5 = f"https://uk.indeed.com/jobs?q={role}&l=United%20Kingdom"
        link6 = f"https://uk.indeed.com/jobs?q={role}&l=Liverpool%2C%20Merseyside"
        link7 = f"https://uk.indeed.com/jobs?q={role}&l=Glasgow%2C%20Glasgow&vjk=3617eef5724cf243"
        link8 = f"https://uk.indeed.com/jobs?q={role}&l=Scotland&vjk=8982bfe91721884d"
        link9 = f"https://uk.indeed.com/jobs?q={role}&l=Leeds%2C%20West%20Yorkshire"
        link10 = f"https://uk.indeed.com/jobs?q={role}&l=Newcastle%20upon%20Tyne%2C%20Tyne%20and%20Wear"
        urls.append(link1)
        urls.append(link2)
        urls.append(link3)
        urls.append(link4)
        urls.append(link5)
        urls.append(link6)
        urls.append(link7)
        urls.append(link8)
        urls.append(link9)
        urls.append(link10)
        return urls
