class JDAnalyzerAgent:

    def analyze_jd(self, jd_text):

        skills = []
        
        keywords = [
            "python",
            "machine learning",
            "deep learning",
            "nlp",
            "sql",
            "tensorflow"
        ]

        for word in keywords:
            if word.lower() in jd_text.lower():
                skills.append(word)

        return {
            "required_skills": skills,
            "experience": "2+ years"
        }