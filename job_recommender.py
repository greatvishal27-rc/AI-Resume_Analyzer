import pandas as pd

skills_data = pd.read_csv("skills.csv")

def recommend_jobs(resume_text):

    jobs = []

    for index, row in skills_data.iterrows():

        skill = row["Skill"]

        if skill.lower() in resume_text.lower():
            jobs.append(row["Job Role"])

    return list(set(jobs))