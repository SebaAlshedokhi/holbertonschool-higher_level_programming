#!/usr/bin/env python3
"""Creating a Simple Templating Program"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template
    """
    if not isinstance(template, str):
        print("template must String")
        return

    if not isinstance(attendees, list):
        print("attendees must be list")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("attendees list must contain only dictionaries")
        return

    if not template.strip():
        print("template is empty")
        return

    if not attendees:
        print("no data provided")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template

        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(output)
