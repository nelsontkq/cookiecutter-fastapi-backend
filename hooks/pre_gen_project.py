import re
import sys

MODULE_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug}}"
python_version = "{{ cookiecutter.py_version}}"


if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. Please only use alphanumeric names only."  # noqa
        % module_name
    )

    # Exit to cancel project
    sys.exit(1)

if python_version not in ["3.8", "3.9", "3.10", "3.11"]:
    print(f"{python_version} is not a valid version. Please use >= 3.8 and <= 11")

    sys.exit(1)
