def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else "<no line>"
        line2 = lines2[i].strip() if i < len(lines2) else "<no line>"

        if line1 != line2:
            print(f"Line {i+1} mismatch:")
            print(f"File 1: {line1}")
            print(f"File 2: {line2}")
            print("-" * 30)

compare_files("text1.txt", "text2.txt")