import pdfkit
'''
def save_pdf_example():
    name='out.pdf'
    config = pdfkit.configuration(wkhtmltopdf=r"F:\wkhtmltopdf\bin\wkhtmltopdf.exe")
    url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000'
    pdfkit.from_url(url, name, configuration=config)
save_pdf_example()
'''
def save_pdf_note(htmls, file_name):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
             ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    config = pdfkit.configuration(wkhtmltopdf=r"F:\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_url(htmls, file_name, configuration=config)
    #name=r'E:\python_example\pdf_files'+'\\'+'2'
    #save_pdf('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000',name+'.pdf')

#save_pdf.save_pdf_note('https://www.cnblogs.com/my8100/p/7738366.html','out.pdf')
