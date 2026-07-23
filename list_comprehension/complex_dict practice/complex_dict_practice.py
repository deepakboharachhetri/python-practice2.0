data={
  "company": "TechCorp",
  "fiscal_year": 2026,
  "departments": [
    {
      "name": "Engineering",
      "budget": 500000,
      "location": "New York",
      "employees": [
        {
          "id": 101,
          "name": "Alice Johnson",
          "role": "Senior Developer",
          "active": True,
          "skills": ["Python", "AWS", "Docker"],
          "projects": [
            {"name": "Project Alpha", "status": "completed", "hours_logged": 120},
            {"name": "Project Beta", "status": "active", "hours_logged": 45}
          ]
        },
        {
          "id": 102,
          "name": "Bob Smith",
          "role": "Junior Developer",
          "active": True,
          "skills": ["JavaScript", "React"],
          "projects": [
            {"name": "Project Beta", "status": "active", "hours_logged": 80}
          ]
        },
        {
          "id": 103,
          "name": "Charlie Brown",
          "role": "DevOps Engineer",
          "active": False,
          "skills": ["Kubernetes", "AWS", "Terraform"],
          "projects": []
        }
      ]
    },
    {
      "name": "Marketing",
      "budget": 200000,
      "location": "London",
      "employees": [
        {
          "id": 201,
          "name": "Diana Prince",
          "role": "Manager",
          "active": True,
          "skills": ["SEO", "Analytics"],
          "projects": [
            {"name": "Campaign X", "status": "active", "hours_logged": 30}
          ]
        }
      ]
    }
  ]
}

def return_hour_logged_project_80_employee(data,common_base):
    employee_gte_hour_logged=[]
    for dept in common_base:
          for employee in dept.get("employees"):
              for project in employee.get("projects"):
                  if project.get("hours_logged")>=45 and employee not in employee_gte_hour_logged:
                      employee_gte_hour_logged.append(employee)
    return employee_gte_hour_logged


def return_hour_logged_project_employee(data,common_base):
    employee_gte_hour_logged=[]
    for dept in common_base:
          for employee in dept.get("employees"):
              for project in employee.get("projects"):
                  if project.get("hours_logged")>=45 and employee not in employee_gte_hour_logged:
                      employee_gte_hour_logged.append(employee)
    return employee_gte_hour_logged


def return_aws_employee(data, common_base):
    aws_employee = []
    for dept in common_base:
        for employee in dept.get("employees"):
            if "AWS" in employee.get("skills"):
                aws_employee.append(employee)
    # print(aws_employee)
    return aws_employee


def display_employee(data):
    aws_id = []
    for employee in data:
        aws_id.append(employee.get('id'))
    return aws_id



if __name__ == "__main__":

        common_base=data.get("departments")
        # employees that have  aws skill

        print("Employee who have 'AWS' skill", display_employee(return_aws_employee(data, common_base)))

        # return new_list
        print("employee_id whose hours_logged is greater than 45",display_employee(return_hour_logged_project_employee(data,common_base)))