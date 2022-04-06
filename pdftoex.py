# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("4th_sem.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("4th_sem.pdf", "4th_sem.csv", output_format="csv", pages='all')
print(df)