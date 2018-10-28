import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vuedj.settings')

import django
django.setup()
from chatbot.models import Service, Tag, Location

def populate():
    location_list = ["Edinburgh", "Midlothian", "East Lothian", "West Lothian", "Scottish Borders"]
    tag_list = ["isolation", "lonely", "anxiety", "depression","panic"]

    for loc in location_list:
        add_location(loc)

    for tag in tag_list:
        add_tag(tag)

    service_list = [
        {
            "name": "Befriending", "minAge": 18, "maxAge": 25, "locations": ["Edinburgh", "Midlothian", "Scottish Borders"],
            "tags": ["isolation", "lonely"], "description": "Befriending programme",
            "link": "http://www.health-in-mind.org.uk/services/befriending/d13/",
        },
        {
            "name": "Anxiety and Depression Support Groups", "minAge": 18, "maxAge": 25,
            "locations": ["Edinburgh", "East Lothian", "West Lothian", "Scottish Borders"],
            "tags": ["anxiety", "depression","panic"], "description": "Anxiety and Depression Support Groups",
            "link": "http://www.health-in-mind.org.uk/services/anxiety_and_depression_support_groups/d101/",
        },
        {
            "name": "Men's SHARE", "minAge": 25, "maxAge": 50,
            "locations": ["Midlothian"],
            "tags": ["anxiety", "depression","panic"], "description": "Men's SHARE",
            "link": "http://www.health-in-mind.org.uk/services/mens_share/d40/",
        },
        {
            "name": "Wellbeing College", "minAge": 16, "maxAge": 75,
            "locations": ["Scottish Borders"],
            "tags": ["lonely", "depression","isolation"], "description": "Wellbeing College",
            "link": "http://www.health-in-mind.org.uk/services/wellbeing_college/d110/",
        },
    ]

    for service in service_list:
        loc_list = []
        tag_list = []

        for l in service["locations"]:
            loc_list.append(Location.objects.get(location=l))

        for t in service["tags"]:
            tag_list.append(Tag.objects.get(tag=t))

        add_service(service["name"], service["minAge"], service["maxAge"], loc_list, tag_list,
                   service["description"], service["link"])


def add_location(name):
    l = Location.objects.get_or_create(location=name)[0]
    l.save()
    return l


def add_tag(name):
    t = Tag.objects.get_or_create(tag=name)[0]
    t.save()
    return t


def add_service(name, minAge, maxAge, loc_list, tag_list, description, link):

    s = Service.objects.get_or_create(name=name, minAge=minAge, maxAge=maxAge, description=description, link=link)[0]

    s.save()

    for l in loc_list:
        s.locations.add(l)

    for t in tag_list:
        s.tags.add(t)

    return s


if __name__ == '__main__':
    print("Starting chatbot population script")
    populate()
