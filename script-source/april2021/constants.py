DIFFICULTY_LEVELS = ["low", "medium", "high"]

SYNONYMS_LOW = ["low", "easy", "l", "e"]
SYNONYMS_MEDIUM = ["med", "medium", "m", "mod", "moderate"]
SYNONYMS_HIGH = ["difficult", "hard", "h", "d"]

COLUMNS_QBANK_MCQ = ["question", "option1", "option2", "option3", "option4", "legend", "level", "type"]
COLUMNS_QBANK = ["question", "legend", "level", "type"]
COLUMNS_QBANK_MCQ_REPEATED = ["question", "option1", "option2", "option3", "option4", "legend", "level", "type", "repeat"]
COLUMNS_QBANK_REPEATED = ["question", "legend", "level", "type", "repeat"]
COLUMNS_FORMAT = ["param", "value"]

COLUMNS_OBJECTIVE = ["question", "option1", "option2", "option3", "option4", "legend", "level", "type", "topic"]
COLUMNS_SUBJECTIVE = ["question", "legend", "level", "type", "topic"]

difficulty_split = {
    "low": 60,
    "medium": 30,
    "high": 10
}

topic_split = [
    [(1,), 5],
    [(2,), 20],
    [(3,), 25],
    [(4,), 20],
    [(5,), 15],
    [(6,), 15],
]

# topic_split = [
#     [(2,), 20],
#     [(3,), 25],
#     [(5,4), 35],
#     [(6,1), 20],
# ]



le_preferred_topics = [2, 3, 4]

type_split_mcq = [
    ("le", 2),
    ("se", 6),
    ("sa", 10),
    ("mcq", 20)
]

type_split_no_mcq = [
    ("le", 2),
    ("se", 10),
    ("sa", 10),
    ("mcq", 0)
]

type_split_no_mcq_with_options = [
    ("le", 3),
    ("se", 12),
    ("sa", 10),
    ("mcq", 0)
]

type_split_half = [
    ("le", 1),
    ("se", 5),
    ("sa", 5),
    ("mcq", 0)
]

# type_split = [
#     ("le", 2),
#     ("se", 10),
#     ("sa", 10),
#     ("mcq", 0)
# ]

TYPE2MARKS = {
    "le" : 10,
    "se" : 5,
    "sa" : 3,
    "mcq" : 1
}

PICKING_ORDER = ['le', 'se', 'sa', 'mcq']