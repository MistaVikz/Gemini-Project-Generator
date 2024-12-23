import os
from utils.gemini_calls import *
from utils.io_functions import *

api_key=os.environ["GOOGLE_API_KEY"]
charter_prompt = "Write a brief Project Charter document for our product idea. The Project Charter should include the following sections: \n    1) Project Title and Description\n    2) Project Purpose or Justification\n    3) Objectives and Constraints\n    4) Scope Description\n    5) Project Deliverables\n    6) Project Budget\n    7) Stakeholder Identification\n    8) High-Level Risks and Assumptions\n\n    Our product idea is: "
risk_prompt = "Write a risk assessment plan that identifies assesses and outlines strategies to manage risks in the project based on the following project_charter:"
plan_prompt = """Write a project plan based upon a project charter. The output of the project plan needs to be in tabular format. The columns are as follows: Task name, duration, dependencies, status, resources.
                Example of output: 
                Task Name|Duration|Dependencies|Status|Resources
                Creating Plan|1 day|None|Not Started|Leadership team
                Documentation|3 days|Creating Plan|Not Started|Development team, internal software "
                Please use the following project charter: """

def main():
    # Get project idea from user.
    project_idea = input('What would you like to build?: ')

    # Generate project charter.
    project_charter = call_gemini(api_key,project_idea, charter_prompt)
    print(project_charter)
    write_document(project_charter,1,False)

    # Generate risk management plan.
    risk_management=call_gemini(api_key,project_charter, risk_prompt)
    print(risk_management)
    write_document(risk_management,2,True)

    # Generate project plan.
    project_plan = call_gemini(api_key,project_charter, plan_prompt)
    print(project_plan)
    spreadsheet = write_plan(project_plan)
    write_presentation(spreadsheet)

if __name__=='__main__':
    main()