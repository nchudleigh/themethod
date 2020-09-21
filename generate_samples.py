import random
import string
from datetime import datetime
from tqdm import tqdm
from time import sleep

PROMPTS = ["The Greatest That Ever Lived", "The other Sample"]
# The number of samples to get per prompt
SAMPLE_COUNT = 5
SAMPLE_LENGTH = 3000


def generate_sample(prompt: str) -> str:
    return prompt + _generate_random_text(SAMPLE_LENGTH)


def _generate_random_text(length: int) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def _get_datestring():
    return datetime.now().strftime("%Y-%m-%d")


def _slugify_text(input: str) -> str:
    return input.lower().replace(" ", "_").replace(".", "").replace("'", "")


def _generate_filename(prompt: str) -> str:
    prompt_slug = _slugify_text(prompt)
    datestring = _get_datestring()
    return f"{prompt_slug}-{datestring}-{_generate_random_text(3)}.txt"


def create_and_write_file(filename: str, sample: str):
    file = open(filename, mode="w+")
    file.write(sample)
    file.close()


progress_bar = tqdm(total=len(PROMPTS) * SAMPLE_COUNT)
for prompt in PROMPTS:
    file_content = ""
    for i in range(SAMPLE_COUNT):
        progress_bar.set_description(f"{prompt}: {i} of {SAMPLE_COUNT}")
        sample = generate_sample(prompt)
        filename = _generate_filename(prompt)
        create_and_write_file(filename, sample)
        progress_bar.update(1)

