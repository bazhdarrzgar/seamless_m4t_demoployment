# Language dict
language_code_to_name = {
    "ckb": "Central Kurdish",
}
LANGUAGE_NAME_TO_CODE = {v: k for k, v in language_code_to_name.items()}

# Source langs: S2ST / S2TT / ASR don't need source lang
# T2TT / T2ST use this
text_source_language_codes = [
    "ckb",
]
TEXT_SOURCE_LANGUAGE_NAMES = sorted([language_code_to_name[code] for code in text_source_language_codes])

# Target langs:
# S2ST / T2ST
# s2st_target_language_codes = [
#     "eng",
#     "arb",
#     "ben",
#     "cat",
#     "ces",
#     "cmn",
#     "cym",
#     "dan",
#     "deu",
#     "est",
#     "fin",
#     "fra",
#     "hin",
#     "ind",
#     "ita",
#     "jpn",
#     "kor",
#     "mlt",
#     "nld",
#     "pes",
#     "pol",
#     "por",
#     "ron",
#     "rus",
#     "slk",
#     "spa",
#     "swe",
#     "swh",
#     "tel",
#     "tgl",
#     "tha",
#     "tur",
#     "ukr",
#     "urd",
#     "uzn",
#     "vie",
# ]
# S2ST_TARGET_LANGUAGE_NAMES = sorted([language_code_to_name[code] for code in s2st_target_language_codes])

# S2TT / ASR
S2TT_TARGET_LANGUAGE_NAMES = TEXT_SOURCE_LANGUAGE_NAMES
# T2TT
T2TT_TARGET_LANGUAGE_NAMES = TEXT_SOURCE_LANGUAGE_NAMES
