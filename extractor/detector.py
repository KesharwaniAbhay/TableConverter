def find_tables_on_page(page):
    extracted_tables = page.extract_tables()

    if not extracted_tables:
        all_words = page.extract_words()
        text_by_line = {}

        for word in all_words:
            line_key = round(word['top'], 1)
            if line_key not in text_by_line:
                text_by_line[line_key] = []
            text_by_line[line_key].append(word)

        lines_sorted = sorted(text_by_line.items(), key=lambda x: x[0])
        extracted_tables = [[
            [word['text'] for word in sorted(words, key=lambda x: x['x0'])]
            for _, words in lines_sorted
        ]]

    return extracted_tables
