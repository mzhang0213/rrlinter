import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from .editor import PDFMetadataEditor


def make():
    load_dotenv()

    resumes = os.getenv("RESUME_PATH")
    if not resumes:
        print("RESUME_PATH not set. Add it to your .env file.")
        return

    folders = os.listdir(resumes)
    for i, fol in enumerate(folders, 1):
        print(f"{i}. {fol}")
    folder_choice = folders[int(input(f"which 1..{len(folders)}\n")) - 1]

    folder = os.path.join(resumes, folder_choice)
    files = [p for p in Path(folder).rglob("*") if p.is_file() and not p.name.startswith(".") and p.suffix == ".pdf"]

    pdf_name = os.getenv("PDF_NAME")
    my_name = os.getenv("MY_NAME")

    for f in files:
        new_folder = f.parent / f.stem
        new_folder.mkdir(exist_ok=True)
        new_file = new_folder / (pdf_name + (".pdf" if pdf_name[-4:] != ".pdf" else ""))

        editor = PDFMetadataEditor(str(f))
        editor.set_author(my_name)
        editor.set_creator(my_name)
        editor.set_keywords("")
        editor.set_producer("")
        editor.set_subject("")
        editor.set_title(pdf_name)
        editor.save(str(new_file))

        f.unlink()

    print(f"Done. Processed {len(files)} file(s).")


def main():
    parser = argparse.ArgumentParser(prog="rrlinter")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("make", help="Lint and reorganize resume PDFs")

    args = parser.parse_args()
    if args.command == "make":
        make()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
