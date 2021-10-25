from pathlib import Path

TITLE_WIDTH = 20
COUNT_WIDTH = 5


def count_files(path: Path):
    count = len(list(path.glob('*.py')))
    if count > 0:
        return path.stem, count
    return '', 0


def write_intro(f):
    f.write(
        """
# LeetCode Solutions

A bunch of LeetCode problems and their solution (in Python 3.8)

(Comments in the code are written in Chinese)

"""
    )


def write_category(path: Path, f):
    f.write(f'## {path.stem}\n\n')
    for file in path.iterdir():
        f.write(f'* [{file.stem}]({file.as_posix()})\n')
    f.write('\n')


def generate_readme(file='README.md'):
    path = Path(file)
    f = path.open('w', encoding='utf-8')
    write_intro(f)
    f.write(f'|{"Catagory":<{TITLE_WIDTH}}|{"Count":<{COUNT_WIDTH}}|\n')
    f.write('|' + '-' * TITLE_WIDTH + '|' + '-' * COUNT_WIDTH + '|\n')

    root = Path('./Problems')
    total = 0
    categories = []
    for folder in root.iterdir():
        if folder.is_dir():
            categories.append(folder)
            title, count = count_files(folder)
            if count == 0:
                continue
            f.write(f'|{title:<{TITLE_WIDTH}}|{count:<{COUNT_WIDTH}}|\n')
            total += count
    f.write(f'|{"Total":<{TITLE_WIDTH}}|{total:<{COUNT_WIDTH}}|\n\n')

    # for category in categories:
    #     write_category(category, f)

    f.close()


generate_readme()
