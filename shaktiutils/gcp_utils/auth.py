from shaktiutils.utilities import run_bash_cmd


def gcp_auth():
    try:
        auth_list_cmd = "gcloud auth list"
        auth_output, auth_error = run_bash_cmd(auth_list_cmd)
        if (output and not output.find("No credentialed accounts.")) or error:
            login_cmd = "gcloud auth login"
            login_output, login_error = run_bash_cmd(login_cmd)
    except:
        raise
