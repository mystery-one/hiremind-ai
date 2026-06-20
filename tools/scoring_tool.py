def calculate_final_score(
    semantic_score,
    experience_score,
    skill_score
):

    final_score = (
        0.5 * semantic_score +
        0.3 * experience_score +
        0.2 * skill_score
    )

    return round(final_score, 2)