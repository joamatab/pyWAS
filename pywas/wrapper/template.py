from os import path
from rich import print
import jinja2
from jinja2 import meta
import typer

template = typer.Typer()
base = path.dirname(__file__)
template_dir = path.join(path.dirname(base), "template")
loader = jinja2.FileSystemLoader(template_dir)
env = jinja2.Environment(loader=loader)


@template.command("infos")
def new_file_from_template(template_name: str):
    """
    Give a description of the template
    """
    temp = env.loader.get_source(env, template_name)
    parsed_content = env.parse(temp)
    print(meta.find_undeclared_variables(parsed_content))


@template.command("list")
def list_available_template():
    """
    List all available template
    """
    print(env.list_templates())


@template.command("create")
def new_file_from_template(template_name: str, output_file: str = "template"):
    """
    Give a description of the template
    """
    temp_s = env.loader.get_source(env, template_name)
    parsed_content = env.parse(temp_s)
    context = dict()
    for var in meta.find_undeclared_variables(parsed_content):
        context[var] = typer.prompt(var)
    print(context)
    temp = env.get_template(template_name)
    with open(output_file, "w") as fh:
        fh.write(temp.render(context))
