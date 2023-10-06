import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

    def program_school(self):
        # Get the JSON response from the API
        api_response = self.get_programs()

        # Parse the JSON data
        programs = json.loads(api_response)

        # Extract and collect the names of schools or organizations
        schools = set()
        for program in programs:
            agency = program.get("agency")
            if agency:
                schools.add(agency)

        return schools

if __name__ == "__main__":
    programs = GetPrograms()
    program_schools = programs.program_school()

    for school in program_schools:
        print(school)
