\# AWS Learning Journey Portfolio Template

\# Folder structure, example README.md, placeholder markdowns, and diagram setup with sample lab and diagram



\# README.md

readme\_content = """

\# My AWS Learning Journey ☁️



This repository documents my progress through Adrian Cantrill's AWS Solutions Architect Associate course and my path to becoming a Cloud Engineer.



\## Goals

\- Master AWS core services

\- Build real-world projects

\- Pass the AWS SAA exam

\- Create a portfolio of cloud architectures and automation



\## Repository Structure

\- `01\_notes/` - Polished notes from course topics

\- `02\_labs/` - Step-by-step lab documentation

\- `03\_projects/` - End-to-end portfolio projects

\- `04\_diagrams/` - Architecture diagrams and visuals

\- `05\_iac/` - Infrastructure as Code (CloudFormation / Terraform)

\- `06\_resources/` - Cheatsheets, AWS CLI commands, useful links

\- `07\_reflections/` - Weekly reflections and summaries



\## Example Usage

Each lab folder should contain a Markdown file documenting:

\- Objective of the lab

\- Step-by-step implementation

\- Screenshots

\- Lessons learned



Diagrams should visually represent the architecture of your lab or project.

"""



\# Example Folder Structure

folders = \[

&nbsp;   '01\_notes',

&nbsp;   '02\_labs',

&nbsp;   '03\_projects/three\_tier\_app',

&nbsp;   '04\_diagrams',

&nbsp;   '05\_iac',

&nbsp;   '06\_resources/cheat\_sheets',

&nbsp;   '07\_reflections'

]



\# Placeholder files and sample lab + diagram

placeholders = {

&nbsp;   '01\_notes/README.md': '# Notes Index\\nList of notes by AWS topics',

&nbsp;   '02\_labs/README.md': '# Labs Index\\nDocumentation for hands-on labs',

&nbsp;   '02\_labs/sample\_s3\_lab.md': '# Sample S3 Static Website Lab\\n\\n\*\*Objective:\*\* Deploy a static website using S3.\\n\\n\*\*Steps:\*\*\\n1. Create S3 bucket\\n2. Enable static website hosting\\n3. Upload HTML files\\n4. Configure bucket policy\\n\\n\*\*Screenshots:\*\*\\n\_(Insert screenshots here)\_\\n\\n\*\*Lessons Learned:\*\*\\n- Permissions and bucket policy structure\\n- Endpoint URL usage\\n- Hosting troubleshooting tips',

&nbsp;   '03\_projects/three\_tier\_app/README.md': '# Three Tier App Project\\nProject overview, architecture diagram, screenshots, and steps',

&nbsp;   '04\_diagrams/README.md': '# Diagrams Index\\nAWS architecture diagrams',

&nbsp;   '04\_diagrams/sample\_s3\_architecture.png': '',

&nbsp;   '05\_iac/README.md': '# IaC Scripts\\nCloudFormation or Terraform templates',

&nbsp;   '06\_resources/README.md': '# Resources Index\\nCheatsheets, commands, and useful links',

&nbsp;   '07\_reflections/README.md': '# Reflections Index\\nWeekly learning reflections'

}



\# Generate template

import os



repo\_name = 'aws-learning-journey-template'

os.makedirs(repo\_name, exist\_ok=True)



\# Create folders

for folder in folders:

&nbsp;   os.makedirs(os.path.join(repo\_name, folder), exist\_ok=True)



\# Create README.md

with open(os.path.join(repo\_name, 'README.md'), 'w') as f:

&nbsp;   f.write(readme\_content)



\# Create placeholder files

for path, content in placeholders.items():

&nbsp;   full\_path = os.path.join(repo\_name, path)

&nbsp;   with open(full\_path, 'w') as f:

&nbsp;       f.write(content)



repo\_name



