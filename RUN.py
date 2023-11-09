import os
from pathlib import Path
import sys
import os.path


def get_sorted_list(lst):
    items_nums = {}

    for element in lst:
        nums_of_items = ''

        for c in element:
            if c.isdigit():
                nums_of_items += c
            else:
                break

        items_nums[element] = int(nums_of_items) if nums_of_items else 0

    return [key for key, value in sorted(items_nums.items(), key=lambda x: (x[1] == 0, x[1]))]


def parse_folder(path):
    path = Path(path)

    files_list = []

    for item in path.rglob("*"):
        name = os.path.basename(item)

        if name.split('.')[-1] == 'mp4':
            files_list.append(name)

    return get_sorted_list(files_list)


def main():
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    data = parse_folder(path)

    with open('VideoForScreen(не удалять).m3u', 'wt', encoding='utf-8') as out:
        out.write('#EXTM3U\n\n')

        [out.write(f"#EXTINF:1{i}, Sample artist name - Sample track title\nD:\\__VideoForScreen\\{file_}\n\n")
         for i, file_ in enumerate(data, start=1)]


if __name__ == '__main__':
    main()
