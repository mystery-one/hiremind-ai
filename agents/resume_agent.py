class ResumeAgent:

    def process_resume(self, resume_text):

        extracted = {
            "skills": [],
            "projects": []
        }

        skills = [
            "python",
            "tensorflow",
            "pytorch",
            "sql",
            "nlp"
        ]

        for skill in skills:
            if skill.lower() in resume_text.lower():
                extracted["skills"].append(skill)

        return extracted