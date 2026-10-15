from paddleocr import PaddleOCR

def ocr():
    image_path = "../test-bill.jpeg"
    pipeline = PaddleOCR(use_textline_orientation=True, lang="id")

    result = pipeline.predict(image_path)

    for res in result:
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")
