import os
from pathlib import Path
from typing import Dict, List

class StudyManager:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def scan_subjects(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Parses folder structure:
        subjects/
          subject_name/
            chapter_name/
              note1.md
        """
        structure = {}
        if not self.base_path.exists():
            return structure

        for subject in self.base_path.iterdir():
            if subject.is_dir():
                structure[subject.name] = []
                for chapter in subject.iterdir():
                    if chapter.is_dir():
                        notes = [f.name for f in chapter.glob("*.md")]
                        structure[subject.name].append({
                            "chapter": chapter.name,
                            "notes": notes,
                            "path": str(chapter)
                        })
        return structure
