def count_blocks(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    block_count = 0
    loop_count = 0
    indent_level = 0

    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            continue

        if line.startswith("def ") or line.startswith("class "):
            block_count += 1
            indent_level += 1
        elif line.endswith(":"):
            indent_level += 1
            if "for " in line or "while " in line:
                loop_count += 1
        elif line == "":
            indent_level -= 1

    return block_count, loop_count

filename = "primenumbers.py"  # 解析するファイル名を指定してください
block_count, loop_count = count_blocks(filename)
print("ブロックの数:", block_count)
print("ループの数:", loop_count)
