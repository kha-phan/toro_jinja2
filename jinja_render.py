import json
from jinja2 import Template


def get_input_sample():
    with open("input.json", 'r', encoding='UTF-8') as file:
        return file.read()


def get_template_sample():
    with open("template.html", 'r', encoding='UTF-8') as file:
        return file.read()


def save_report(html_content):
    with open("report.html", 'w', encoding='UTF-8') as file:
        file.write(html_content)


def build_report():
    input_data = json.loads(get_input_sample())
    html_template = get_template_sample()
    jinja2_template = Template(html_template)
    html_content = jinja2_template.render(**input_data)
    save_report(html_content)
    print("create `report.html` success!")
