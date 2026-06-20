def generate_reasoning(
    candidate,
    final_score
):

    strengths = []

    profile = candidate.get(
        "profile",
        {}
    ) or {}

    skills = candidate.get(
        "skills",
        []
    ) or []

    top_skills = [
        skill.get("name")
        for skill in sorted(
            skills,
            key=lambda s: s.get(
                "endorsements",
                0
            ),
            reverse=True
        )[:3]
        if skill.get("name")
    ]

    if final_score >= 85:
        strengths.append(
            "High overall suitability"
        )
    elif final_score >= 75:
        strengths.append(
            "Strong match on core skills"
        )
    else:
        strengths.append(
            "Good baseline alignment"
        )

    if top_skills:
        strengths.append(
            "Skills: " + ", ".join(
                top_skills
            )
        )

    if profile.get("years_of_experience") is not None:
        strengths.append(
            f"{profile['years_of_experience']} years experience"
        )

    if candidate.get("redrob_signals", {}).get(
        "open_to_work_flag"
    ):
        strengths.append(
            "Open to new opportunities"
        )

    headline = profile.get(
        "headline",
        "Candidate"
    )

    skill_text = (
        ", ".join(top_skills)
        if top_skills
        else "relevant skills"
    )

    reasoning = (
        f"{headline} shows {skill_text} and a strong experience profile. "
        f"The candidate is ranked based on semantic relevance, structured skills, "
        f"and recruiter-signal strength."
    )

    return {

        "strengths": strengths,

        "confidence":
        "High"
        if final_score > 80
        else "Medium",

        "reasoning": reasoning
    }
