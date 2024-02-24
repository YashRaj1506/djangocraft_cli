import typer
import subprocess
import shutil
import os

app = typer.Typer()

@app.command()
def djangostartauth(project_name: str, auth_app_name: str):

    urls = [
        "https://github.com/YashRaj1506/djangocraft_cli_datafiles.git",
    ]

    root_dir = os.getcwd()

    for url in urls:
        subprocess.run(["git","clone", url], cwd=root_dir)

    print("Execution at process_0 completed successfully")    


    # extraction_command = "pip install build && cd dist && tar -xzvf djangocraft-1.0.4.tar.gz && cd .."

    # extraction_execution_for_tar = subprocess.run(extraction_command, shell=True, capture_output=True, text=True)

    # if extraction_execution_for_tar.returncode == 0:
    #     typer.echo("project started succesfully:")
    #     typer.echo(extraction_execution_for_tar.stdout)

    # else:
    #         typer.echo("Error executing command during result_0:")
    #         typer.echo(extraction_execution_for_tar.stderr)    

    full_command = (f"pip install django && pip freeze > requirements.txt && django-admin startproject {project_name} && cd {project_name} && python manage.py startapp {auth_app_name} && cd - ")

    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        typer.echo("project started succesfully:")
        typer.echo(result.stdout)

        destination_forms = f"{project_name}/{auth_app_name}/forms.py"
        

        process()

        shutil.copyfile("djangocraft_cli_datafiles/data/for_forms.txt", f"{destination_forms}")

        full_command_2 = (f"cd {project_name} && cd {auth_app_name} && touch urls.py && touch forms.py && cd .. && cd ..")

        result_2 = subprocess.run(full_command_2, shell=True, capture_output=True, text=True)

        if result_2.returncode == 0:
            typer.echo("project started succesfully at result_2:")
            typer.echo(result_2.stdout)

        else:
            typer.echo("Error executing command during result_2:")
            typer.echo(result_2.stderr)

        destination_views = f"{project_name}/{auth_app_name}/views.py"
        destination_models = f"{project_name}/{auth_app_name}/models.py"
        destination_urls = f"{project_name}/{auth_app_name}/urls.py"



        shutil.copyfile("djangocraft_cli_datafiles/data/for_views.txt", f"{destination_views}")
        shutil.copyfile("djangocraft_cli_datafiles/data/for_models.txt", f"{destination_models}")
        shutil.copyfile("djangocraft_cli_datafiles/data/for_urls.txt", f"{destination_urls}")

        full_command_3 = (f"cd {project_name} && cd {auth_app_name} && mkdir templates && cd templates && touch base.html && touch home.html && mkdir registration && cd registration && touch login.html && touch register.html && cd .. && cd ..")

        result_3 = subprocess.run(full_command_3, shell=True, capture_output=True, text=True)

        if result_3.returncode == 0:
            typer.echo("project started succesfully at result_3:")
            typer.echo(result_3.stdout)

        else:
            typer.echo("Error executing command during result_3:")
            typer.echo(result_3.stderr)


        destination_base = f"{project_name}/{auth_app_name}/templates/base.html"
        destination_home = f"{project_name}/{auth_app_name}/templates/home.html"
        destination_register = f"{project_name}/{auth_app_name}/templates/registration/register.html"
        destination_login = f"{project_name}/{auth_app_name}/templates/registration/login.html"

        shutil.copyfile("djangocraft_cli_datafiles/data/for_basehtml.txt",f"{destination_base}")
        shutil.copyfile("djangocraft_cli_datafiles/data/for_homehtml.txt", f"{destination_home}")
        shutil.copyfile("djangocraft_cli_datafiles/data/for_loginhtml.txt", f"{destination_login}")
        shutil.copyfile("djangocraft_cli_datafiles/data/for_registerhtml.txt", f"{destination_register}")

        file_loc_at_settingpy = f"{project_name}/{project_name}/settings.py"
        urls_at_root = f"{project_name}/{project_name}/urls.py"

        # write_Data_to_settingpy(file_loc_at_settingpy, auth_app_name)
        add_to_installed_apps(file_loc_at_settingpy, auth_app_name)

        # add_to_BASEdir(file_loc_at_settingpy, auth_app_name)

        # add_dirs_to_templates(file_loc_at_settingpy, auth_app_name)

        write_Data_to_lastappend(file_loc_at_settingpy, auth_app_name)

        replace_line(file_loc_at_settingpy, 58, auth_app_name)

        replace_line_urls(urls_at_root, 22 , auth_app_name)

        replace_line_urls2(urls_at_root, 18, auth_app_name)

        shutil.copyfile("djangocraft_cli_datafiles/data/for_forms_backup.txt", "djangocraft_cli_datafiles/data/for_forms.txt")

        full_command_4 = (f"cd {project_name} && python manage.py makemigrations && python manage.py migrate && cd ..")

        result_4 = subprocess.run(full_command_4, shell=True, capture_output=True, text=True)

        if result_4.returncode == 0:
            typer.echo("project started succesfully at result_4:")
            typer.echo(result_4.stdout)

        else:
            typer.echo("Error executing command during result_4:")
            typer.echo(result_4.stderr)



        #need to add migration commands

    else:
        typer.echo("Error executing command:")
        typer.echo(result.stderr)

    # superusercreation(project_name)

    loc_for_auth_admin = f"{project_name}/{auth_app_name}/admin.py"  

    admin_auth_user_add(project_name, auth_app_name, loc_for_auth_admin)      

@app.command()
def process():
    try:
        # Ask the user for the number of inputs
        num_inputs = typer.prompt("Enter the number of fields you want in registration page: ", type=int)

        # Ask the user to enter each input name
        input_names = []
        for i in range(num_inputs):
            input_name = typer.prompt(f"Enter input {i+1}: ")
            input_names.append(input_name)

        # Display the entered input names
        typer.echo("Entered input names:")
        for input_name in input_names:
            typer.echo(input_name)

        list_file = "djangocraft_cli_datafiles/data/for_forms.txt"

        write_list_to_file(list_file,input_names)

        typer.echo("Commands executed successfully!")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")


@app.command()
def help():
    
    data_to_print = "To start the project use code :\n python main.py djangostart ProjectName Authentication_app_Name\n"
    data_to_print2 = "Then you will get the option to setup the field entries on your registration page,\n fill them and you are ready to go with them"
    print(data_to_print + data_to_print2)

@app.command()
def djangoforpro(project_name : str):
    full_command = (f"pip install django && pip freeze > requirements.txt && django-admin startproject {project_name} ")

    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        typer.echo("project started succesfully:")
        typer.echo(result.stdout)

    else:
        typer.echo("Error executing command:")
        typer.echo(result.stderr)    




def write_list_to_file(file_path, input_list):
    with open(file_path, 'a') as file:
        file.write("[")
        for item in input_list:

            file.write(f"'{item}',")

        file.write("]")

def write_Data_to_settingpy(file_path, input_data):
    with open(file_path, 'r+') as data_read:

        data_read.seek(340)
        data_read.write(f"'{input_data}',")

def write_Data_to_lastappend(file_path, authapp):
    with open(file_path, 'a') as data_read_2:
        data_read_2.write(f"AUTH_USER_MODEL = '{authapp}.CustomUser'")


def add_to_installed_apps(file_path, app_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    installed_apps_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('INSTALLED_APPS'):
            installed_apps_index = i
            break

    if installed_apps_index is not None:
        # Find the line where INSTALLED_APPS starts
        installed_apps_index += 1

        # Insert the new app name at the appropriate position
        lines.insert(installed_apps_index, f"    '{app_name}',\n")

        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print("INSTALLED_APPS section not found in the file.")

# def add_to_BASEdir(file_path, app_name):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     installed_apps_index = None
#     for i, line in enumerate(lines):
#         if line.strip().startswith(f"'DIRS': ["):
#             installed_apps_index = i
#             break
#
#     if installed_apps_index is not None:
#         # Find the line where INSTALLED_APPS starts
#         installed_apps_index += 0
#
#         # Insert the new app name at the appropriate position
#         lines.insert(installed_apps_index, f" BASE_DIR / \"{app_name}/templates\" ")
#
#         # Write the modified contents back to the file
#         with open(file_path, 'w') as file:
#             file.writelines(lines)
#     else:
#         print("INSTALLED_APPS section not found in the file.")

def add_dirs_to_templates(file_path, additional_dirs):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if "'DIRS':" in line:
            start_index = i + 1
            for j, next_line in enumerate(lines[start_index:], start=start_index):
                if "]" in next_line:
                    end_index = j
                    break

    if start_index is not None and end_index is not None:
        # Insert additional_dirs between the square brackets
        lines[start_index:end_index] = f" BASE_DIR / \"{additional_dirs}/templates\" "

        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print("Error: 'DIRS' section not found in the settings file.")


def replace_line(file_path, line_number, auth_name):
    # Read the original file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the specific line
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = "        'DIRS': [BASE_DIR / \"" + auth_name + "/templates\"],\n"

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Error: Line number {line_number} is out of range.")

def replace_line_urls(file_path, line_number, auth_name):
    # Read the original file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the specific line
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = '    path("", include("' + auth_name + '.urls")),\n]'
        # lines[line_number] = "]"


        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Error: Line number {line_number} is out of range.")

def replace_line_urls2(file_path, line_number, auth_name):
    # Read the original file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the specific line
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = 'from django.urls import path , include'
        # lines[line_number] = "]"


        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Error: Line number {line_number} is out of range.")


# def superusercreation(project_name):

#     print("Create Your SuperUser")

#     process_1 = f"cd {project_name} && python manage.py createsuperuser" 

#     processing = subprocess.run(process_1, shell=True, capture_output=True, text=True)     

def admin_auth_user_add(project_name, auth_name, source):
    with open(source,'r') as file_to_copy:
        read_data = file_to_copy.readlines()

        data_to_copy = f"from .models import CustomUser\n"
        data_to_copy_2 = f"admin.site.register(CustomUser)"
    
    with open(source, 'a') as file_2:
        file_2.writelines(data_to_copy)
        file_2.writelines(data_to_copy_2)

if __name__ == "__main__":
    app()

