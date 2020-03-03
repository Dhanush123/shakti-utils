import os
from shaktiutils.utilities import run_bash_cmd
from shaktiutils.constants import PROJECT_ID


def gcp_setproject():
    list_cmd = "gcloud projects list"
    output, error = run_bash_cmd(list_cmd)
    output = output.decode(
        "utf-8") if output else output
    error = error.decode(
        "utf-8") if error else error
    project_id = os.environ[PROJECT_ID]
    if not output.find(project_id) or error:
        config_cmd = "gcloud config set project {}".format(project_id)
        run_bash_cmd(config_cmd)
