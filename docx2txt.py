import glob
import os

import docx


# Word文書をテキストファイルに変換
def docx2txt(docx_path):
    save_path = os.path.basename(docx_path).split(".")[0] + ".txt"
    full_text = []

    try:
        doc = docx.Document(docx_path)
        for para in doc.paragraphs:
            full_text.append(para.text)

        doc_text = '\n'.join(full_text)

        # テキストファイルとして保存
        with open(save_path, 'w', encoding="utf-8") as txtf:
            txtf.write(doc_text)
    except:
        print(f"cannot extract from {docx_path}... skipped.")

docxes = glob.glob("*.docx")

for docx_input in docxes:
    docx2txt(docx_input)

os.system('git add -A')