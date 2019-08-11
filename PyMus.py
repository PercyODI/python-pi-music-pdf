import uuid
import json
import base64
from typing import List, Dict, Any

class PyMusPage:
    def __init__(self, pdfId: uuid.UUID, pageNum: int, annotations: list) -> None:
        self.pdfId: uuid.UUID = pdfId
        self.pageNum: int = pageNum
        self.annotations: List = annotations

    @staticmethod
    def from_dict(jsonDict: Dict[str, Any]) -> "PyMusPage":
        return PyMusPage(pdfId=uuid.UUID(jsonDict["pdfId"]), pageNum=jsonDict["pageNum"], annotations = jsonDict["annotations"])


class PyMusPdf:
    def __init__(self, id: uuid.UUID, byteArr: bytes) -> None:
        self.id: uuid.UUID = id
        self.bytes: bytes = byteArr

    @staticmethod
    def from_dict(jsonDict: Dict[str, Any]) -> "PyMusPdf":
        return PyMusPdf(id=uuid.UUID(jsonDict["id"]), byteArr=base64.b64decode(jsonDict["bytes"]))
    

class PyMusView:
    def __init__(self, pages: List[PyMusPage]) -> None:
        self.pages: List[PyMusPage] = pages

    @staticmethod
    def from_list(jsonDictList: List[Dict[str, Any]]) -> "PyMusView":
        return PyMusView(pages = list(map(lambda pageDict: PyMusPage.from_dict(pageDict), jsonDictList)))

class PyMusData:
    def __init__(self, pdfs: List[PyMusPdf], pages: List[PyMusView]) -> None:
        self.pdfs: List[PyMusPdf] = pdfs
        self.views: List[PyMusView] = pages

    def to_json(self) -> str:
        pass

    @staticmethod
    def from_json(jsonStr: str) -> "PyMusData":
        jsonDict: dict = json.loads(jsonStr)
        jsonPdfsList: List = jsonDict["pdfs"]
        jsonPdfs = list(map(lambda pdfDict: PyMusPdf.from_dict(pdfDict), jsonPdfsList))

        jsonPagesList = jsonDict["pages"]
        jsonPages = list(map(lambda pageList: PyMusView.from_list(pageList), jsonPagesList))
        return PyMusData(pdfs = jsonPdfs, pages = jsonPages)