from shaktiutils.utilities import run_bash_cmd


def gcp_auth():
    try:
        auth_list_cmd = "gcloud auth list"
        auth_output, auth_error = run_bash_cmd(auth_list_cmd)
        auth_output = auth_output.decode(
            "utf-8") if auth_output else auth_error
        auth_error = auth_error.decode(
            "utf-8") if auth_error else auth_error
        if (auth_output and not auth_output.find("No credentialed accounts.")) or auth_error:
            login_cmd = "gcloud auth login"
            login_output, login_error = run_bash_cmd(login_cmd)
    except:
        raise
