def enter_data_to_html(data):
    """
    Enter data to html
    """
    # Open html file
    html_file = open("templates/email/inform.html", "r")
    html = html_file.read()

    
    html = html.replace(
        "Unique_userame",
        data["username"]
    )
    html = html.replace(
        "Unique_Password",
        data["password"]
    )
    html = html.replace(
        'supervisor_name',
        data["supervisor_name"]
    )
    html = html.replace(
        'Unique_Number',
        data["system_number"]
    )
    html = html.replace(
        'Unique_Compnayname',
        data["company_name"]
    )
    return html
