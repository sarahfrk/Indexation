import sys
import argparse
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from RI import MyWindow
from RI.functions import func

current_file = Path(__file__).resolve()
PATH = current_file.parent

collection_dir = PATH/"my_collection"
evaluation_dir = PATH/"evaluation"
judgement = evaluation_dir/"Judgements.txt"
queries = evaluation_dir/"Queries.txt"
results_dir = PATH/"my_results"


def init_indexer():
    indexer = func(
        documents_dir=collection_dir,
        results_dir=results_dir,
        judgements_path=judgement,
        queries_path=queries,
        doc_prefix="D",
    )
    return indexer

def main(): 
    parser = argparse.ArgumentParser(description="Indexer application")
    parser.add_argument(
        "-r",
        "--reprocess",
        action="store_true",
        help="Regenerate index files if this flag is provided",
    )

    indexer = init_indexer()

    args = parser.parse_args()
    if args.reprocess:
        indexer.mainFrame.process_docs()
    app = QApplication(sys.argv)
    window = MyWindow(indexer)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
