from paddleocr import PaddleOCR

def ocr(image):
    pipeline = PaddleOCR(use_textline_orientation=True, lang="id")
    result = pipeline.predict(image)
    return result
