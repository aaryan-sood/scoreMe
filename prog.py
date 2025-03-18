import pdfplumber
import pandas as pd
import re

def extract_transactions(pdf_path, output_excel):
    transactions = []
    pattern = re.compile(r"(\d{2}-[A-Za-z]{3}-\d{4})\s+([A-Z])\s+([\s\S]*?)\s+([\d,]+\.\d{2})\s+([\d,]+\.\d{2}[A-Za-z]*)")

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                matches = pattern.findall(text)
                for match in matches:
                    date, txn_type, description, amount, balance = match
                    transactions.append([date, txn_type, description.strip(), amount, balance])

    df = pd.DataFrame(transactions, columns=["Date", "Type", "Description", "Amount", "Balance"])

    # Save to Excel
    df.to_excel(output_excel, index=False)

    print(f"Extracted transactions saved to {output_excel}")

# Example usage
pdf_path = "test3.pdf"
output_excel = "extracted_transactions.xlsx"
extract_transactions(pdf_path, output_excel)
extract_transactions("test6.pdf","output.xlsx")