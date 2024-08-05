import jinja2


TEMPLATE_NAME = "README.md.tpl"
OUTFILE_NAME = "README.md"


def main() -> None:
    with open(TEMPLATE_NAME, "r") as fd:
        template = jinja2.Template(fd.read())

    with open(OUTFILE_NAME, "w") as fd:
        fd.write(template.render())


if __name__ == "__main__":
    main()
