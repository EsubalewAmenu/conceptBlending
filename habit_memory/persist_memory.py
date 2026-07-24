from pathlib import Path
import re


MEMORY_PATH = Path(__file__).with_name("memory.metta")


def _metta_atom_to_text(value):
    text = str(value)
    text = re.sub(r"'([^']*)'", r"\1", text)
    if text.startswith("[") and text.endswith("]"):
        text = text[1:-1].replace(",", "")
    if text.startswith("(") and text.endswith(")"):
        text = text.replace(",", "")
    return text


def _concept_name_from_blend_text(blend_text):
    names = re.findall(r"[A-Za-z0-9_-]+", blend_text)
    return "habit-" + "-".join(names) if names else "habit-empty"


def _v_predicate_from_blend_text(blend_text):
    names = re.findall(r"[A-Za-z0-9_-]+", blend_text)
    property_lines = [
        f"      ({name} (WorldSpecSet ()) 1.0)"
        for name in names
    ]
    properties = "\n".join(property_lines)
    return (
        f"(Concept {_concept_name_from_blend_text(blend_text)}\n"
        "  (V-predicate\n"
        "    (Property\n"
        f"{properties})))"
    )


def persist_blend(blend):
    """Append a selected blend to memory.metta as a persistent habit fact."""
    blend_text = _metta_atom_to_text(blend).strip()
    if not blend_text.startswith("("):
        blend_text = f"({blend_text})"

    existing = MEMORY_PATH.read_text() if MEMORY_PATH.exists() else ""
    separator = "" if existing.endswith("\n") or existing == "" else "\n"
    MEMORY_PATH.write_text(f"{existing}{separator}{blend_text}\n")
    return blend_text
