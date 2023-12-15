from rag_experiment_accelerator.doc_loader.structuredLoader import load_structured_files
from langchain.document_loaders import Docx2txtLoader
from rag_experiment_accelerator.utils.logging import get_logger


logger = get_logger(__name__)


def load_docx_files(
    folder_path: str,
    chunk_size: str,
    overlap_size: str,
    glob_patterns: list[str] = ["docx"],
):
    """
    Load and process docx files from a given folder path.

    Args:
        folder_path (str): The path of the folder where files are located.
        chunk_size (str): The size of the chunks to split the documents into.
        overlap_size (str): The size of the overlapping parts between chunks.
        glob_patterns (list[str]): List of file extensions to consider (e.g., ["docx", ...]).

    Returns:
        list[Document]: A list of processed and split document chunks.
    """

    logger.debug("Loading docx files")

    return load_structured_files(
        file_format="DOCX",
        language=None,
        loader=Docx2txtLoader,
        folder_path=folder_path,
        chunk_size=chunk_size,
        overlap_size=overlap_size,
        glob_patterns=glob_patterns,
    )