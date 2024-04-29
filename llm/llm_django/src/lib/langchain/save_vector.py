import langchain
from PyPDF2 import PdfFileReader
import tempfile

def from_pdf(pdfs):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        for chunk in pdfs.chunks():
            temp_file.write(chunk)

    with open(temp_file.name, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()

            # ページごとにIDを生成
            page_id = f'{pdfs.name}_page{page_num + 1}'
            
            # langchainを使用してテキストをベクトル化
            vectorizer = langchain.Vectorizer()
            page_vector = vectorizer.transform([page_text])

    # 一時ファイルを削除
    temp_file.close()