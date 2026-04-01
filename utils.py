from pypdf import PdfReader, PdfWriter


class PDFMetadataEditor:
    FIELDS = ["title", "author", "subject", "keywords", "creator", "producer"]

    def __init__(self, filepath: str):
        self.filepath = filepath
        reader = PdfReader(filepath)
        existing = reader.metadata or {}
        self._meta = {
            "title": existing.get("/Title", ""),
            "author": existing.get("/Author", ""),
            "subject": existing.get("/Subject", ""),
            "keywords": existing.get("/Keywords", ""),
            "creator": existing.get("/Creator", ""),
            "producer": existing.get("/Producer", ""),
        }

    def set_title(self, value: str):
        self._meta["title"] = value

    def set_author(self, value: str):
        self._meta["author"] = value

    def set_subject(self, value: str):
        self._meta["subject"] = value

    def set_keywords(self, value: str):
        self._meta["keywords"] = value

    def set_creator(self, value: str):
        self._meta["creator"] = value

    def set_producer(self, value: str):
        self._meta["producer"] = value

    def set_batch(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.FIELDS:
                raise ValueError(f"Unknown metadata field: '{key}'. Valid fields: {self.FIELDS}")
            self._meta[key] = value

    def save(self, output_path: str = None):
        reader = PdfReader(self.filepath)
        writer = PdfWriter()
        writer.append(reader)
        writer.add_metadata({
            f"/{k.capitalize()}": v
            for k, v in self._meta.items() if v
        })
        out = output_path or self.filepath
        with open(out, "wb") as f:
            writer.write(f)

    @property
    def metadata(self) -> dict:
        return dict(self._meta)
