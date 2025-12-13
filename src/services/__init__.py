"""Services for PDF extraction, AI analysis, and output formatting."""

from src.services.pdf_extractor import (
    extract_embedded_metadata,
    extract_text,
    find_pdfs,
)
from src.services.output import (
    display_metadata,
    display_error,
    display_warning,
    output_json,
)
from src.services.ai_analyzer import (
    analyze_content,
    is_ollama_available,
    is_ollama_running,
    is_model_available,
)

__all__ = [
    "extract_embedded_metadata",
    "extract_text",
    "find_pdfs",
    "display_metadata",
    "display_error",
    "display_warning",
    "output_json",
    "analyze_content",
    "is_ollama_available",
    "is_ollama_running",
    "is_model_available",
]
