# AWS Learning Journey Portfolio Template
# Folder structure, example README.md, placeholder markdowns, and diagram setup with sample lab and diagram

# README.md
readme_content = """
# My AWS Learning Journey ☁️

This repository documents my progress through Adrian Cantrill's AWS Solutions Architect Associate course and my path to becoming a Cloud Engineer.

## Goals
- Master AWS core services
- Build real-world projects
- Pass the AWS SAA exam
- Create a portfolio of cloud architectures and automation

## Repository Structure
- `01_notes/` - Polished notes from course topics
- `02_labs/` - Step-by-step lab documentation
- `03_projects/` - End-to-end portfolio projects
- `04_diagrams/` - Architecture diagrams and visuals
- `05_iac/` - Infrastructure as Code (CloudFormation / Terraform)
- `06_resources/` - Cheatsheets, AWS CLI commands, useful links
- `07_reflections/` - Weekly reflections and summaries

## Example Usage
Each lab folder should contain a Markdown file documenting:
- Objective of the lab
- Step-by-step implementation
- Screenshots
- Lessons learned

Diagrams should visually represent the architecture of your lab or project.
"""

# Example Folder Structure
folders = [
    '01_notes',
    '02_labs',
    '03_projects/three_tier_app',
    '04_diagrams',
    '05_iac',
    '06_resources/cheat_sheets',
    '07_reflections'
]

# Placeholder files and sample lab + diagram
placeholders = {
    '01_notes/README.md': '# Notes Index\nList of notes by AWS topics',
    '02_labs/README.md': '# Labs Index\nDocumentation for hands-on labs',
    '02_labs/sample_s3_lab.md': '# Sample S3 Static Website Lab\n\n**Objective:** Deploy a static website using S3.\n\n**Steps:**\n1. Create S3 bucket\n2. Enable static website hosting\n3. Upload HTML files\n4. Configure bucket policy\n\n**Screenshots:**\n_(Insert screenshots here)_\n\n**Lessons Learned:**\n- Permissions and bucket policy structure\n- Endpoint URL usage\n- Hosting troubleshooting tips',
    '03_projects/three_tier_app/README.md': '# Three Tier App Project\nProject overview, architecture diagram, screenshots, and steps',
    '04_diagrams/README.md': '# Diagrams Index\nAWS architecture diagrams',
    '04_diagrams/sample_s3_architecture.png': '',
    '05_iac/README.md': '# IaC Scripts\nCloudFormation or Terraform templates',
    '06_resources/README.md': '# Resources Index\nCheatsheets, commands, and useful links',
    '07_reflections/README.md': '# Reflections Index\nWeekly learning reflections'
}

# Generate template
import os

repo_name = 'aws-learning-journey-template'
os.makedirs(repo_name, exist_ok=True)

# Create folders
for folder in folders:
    os.makedirs(os.path.join(repo_name, folder), exist_ok=True)

# Create README.md
with open(os.path.join(repo_name, 'README.md'), 'w') as f:
    f.write(readme_content)

# Create placeholder files
for path, content in placeholders.items():
    full_path = os.path.join(repo_name, path)
    with open(full_path, 'w') as f:
        f.write(content)

repo_name
