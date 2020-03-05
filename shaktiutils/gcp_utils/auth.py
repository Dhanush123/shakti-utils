import os

from shaktiutils.utilities import run_bash_cmd
from dotenv import load_dotenv, find_dotenv


def gcp_auth():

    try:
        auth_list_cmd = "gcloud auth list"
        auth_output, auth_error = run_bash_cmd(auth_list_cmd)
        auth_output = auth_output.decode(
            "utf-8") if auth_output else auth_output
        auth_error = auth_error.decode(
            "utf-8") if auth_error else auth_error
        if (auth_output and auth_output.find("No credentialed accounts.") != -1) or auth_error:
            login_cmd = "gcloud auth login"
            login_output, login_error = run_bash_cmd(login_cmd)
    except:
        raise


def get_env_creds():
    os.chdir(os.getcwd())
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path=dotenv_path)
