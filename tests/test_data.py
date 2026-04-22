from app.data import QUESTIONS


def test_question_pool_has_enough_questions_for_board():
    # 24 non-free-space squares are needed for a 5x5 board.
    assert len(QUESTIONS) >= 24


def test_question_pool_covers_tech_life_topics():
    coding_habits_keywords = ("tests", "debug", "coding", "lint", "docker", "git")
    ide_keywords = ("ide", "vim", "theme", "keyboard shortcuts")
    developer_culture_keywords = ("pair", "pr", "slack", "prod", "meetups")

    assert any(
        any(keyword in question for keyword in coding_habits_keywords)
        for question in QUESTIONS
    )
    assert any(
        any(keyword in question for keyword in ide_keywords) for question in QUESTIONS
    )
    assert any(
        any(keyword in question for keyword in developer_culture_keywords)
        for question in QUESTIONS
    )
