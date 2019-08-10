import uuid
from typing import List, Dict, Any
import json
import base64

class PyMusData:
    def __init__(self, pdfs: List["PyMusPdf"], pages: List["PyMusView"]):
        self.pdfs: List["PyMusPdf"] = pdfs
        self.views: List["PyMusView"] = pages

    def to_json(self) -> str:
        pass

    @staticmethod
    def from_json(jsonStr: str):
        jsonDict: Dict[int, Any] = json.loads(jsonStr)
        jsonPdfsList: List = jsonDict["pdfs"]
        jsonPdfs = list(map(lambda pdfDict: PyMusPdf.from_dict(pdfDict), jsonPdfsList))

        jsonPagesList = jsonDict["pages"]
        jsonPages = list(map(lambda pageList: PyMusView.from_list(pageList), jsonPagesList))
        return PyMusData(pdfs = jsonPdfs, pages = jsonPages)

class PyMusPage:
    def __init__(self, pdfId: uuid.UUID, pageNum: int, annotations: List["PyMusAnnotation"]):
        self.pdfId = pdfId
        self.pageNum = pageNum
        self.annotations = annotations

    @staticmethod
    def from_dict(jsonDict: Dict[str, Any]):
        return PyMusPage(pdfId=uuid.UUID(jsonDict["pdfId"]), pageNum=jsonDict["pageNum"], annotations = jsonDict["annotations"])


class PyMusPdf:
    def __init__(self, id: uuid.UUID, byteArr: bytes):
        self.id = id
        self.bytes = byteArr

    @staticmethod
    def from_dict(jsonDict: Dict[str, Any]):
        return PyMusPdf(id=uuid.UUID(jsonDict["id"]), byteArr=base64.b64decode(jsonDict["bytes"]))
    

class PyMusView:
    def __init__(self, pages: List["PyMusPage"]):
        self.pages = pages

    @staticmethod
    def from_list(jsonDictList: List[Dict[str, Any]]):
        return PyMusView(pages = list(map(lambda pageDict: PyMusPage.from_dict(pageDict), jsonDictList)))