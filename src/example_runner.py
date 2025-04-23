# src/example_runner.py

import argparse
from pathlib import Path
from llm_commenter import generate_full_report
from format_architecture_input import load_and_clean_input
from export_utils import save_to_markdown, save_to_pdf


def main():
    parser = argparse.ArgumentParser(description="LLM Vehicle Architecture Reviewer")
    parser.add_argument("--input", type=str, required=True, help="Path to architecture file")
    parser.add_argument("--prompt", type=str, default="prompts/architecture_review_prompt.txt")
    args = parser.parse_args()

    arch_text = load_and_clean_input(args.input)
    prompt_text = Path(args.prompt).read_text()

    full_report = generate_full_report(arch_text, prompt_text)

    print(full_report)

    # Export to files
    save_to_markdown(full_report, "output/review.md")
    save_to_pdf(full_report, "output/review.pdf")
    print("\n✅ Saved report to output/review.md and output/review.pdf")


if __name__ == "__main__":
    main()
