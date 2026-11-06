from paddleocr import PaddleOCR
import numpy as np


def text_extraction(images, pipeline=None):
    """OCR a list of {"name", "image"} dicts.

    Returns {name: [{"text": str, "confidence": float}, ...]}.
    """
    if pipeline is None:
        pipeline = PaddleOCR(use_textline_orientation=True, lang="id")

    ocr_results = {}

    for img in images:
        name = img["name"]
        result = pipeline.predict(np.array(img["image"]))

        if not result:
            print(f"Skipping {name}: no result returned.")
            continue

        lines = []
        for res in result:
            for text, score in zip(res["rec_texts"], res["rec_scores"]):
                lines.append({"text": text, "confidence": float(score)})

        if not lines:
            print(f"Skipping {name}: no text detected.")
            continue

        ocr_results[name] = lines

    return ocr_results
