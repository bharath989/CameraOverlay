import requests
import xml.etree.ElementTree as ET

def get_jenkins_executors_count():
    jenkins_url = 'http://your-jenkins-url/api/xml'
    response = requests.get(jenkins_url)

    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)
        executors_count = int(root.find('executors').text)
        return executors_count
    else:
        print(f"Error: Failed to retrieve data from Jenkins API. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    executors_count = get_jenkins_executors_count()
    if executors_count is not None:
        print(f"Number of Jenkins executors: {executors_count}")
