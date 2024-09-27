import subprocess
import webbrowser
import os
import time

# Set your paths
project_dir = r' *** PATH TO YOUR DIRECTORY ***'
hugo_executable = os.path.join(project_dir, 'hugo.exe')
website_url = 'http://localhost:1313/'  # Default URL for Hugo local server

def start_hugo_server():
    # Navigate to the project directory
    os.chdir(project_dir)
    
    # Run the hugo server
    subprocess.Popen([hugo_executable, 'server'])

    # Give it a moment to start the server
    time.sleep(3)
    
    # Open the website in the default browser
    webbrowser.open(website_url)
    
    print(f"Website should now be running at {website_url}")

if __name__ == "__main__":
    start_hugo_server()
