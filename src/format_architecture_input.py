# src/format_architecture_input.py

def load_and_clean_input(file_path: str) -> str:
    """
    Loads and formats vehicle architecture description for LLM input.
    - Removes excessive newlines
    - Trims white space
    - Can be extended to validate structure
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_text = file.read()

    # Basic cleanup
    cleaned = "\n".join([line.strip() for line in raw_text.splitlines() if line.strip()])
    return cleaned
