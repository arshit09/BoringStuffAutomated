import win32com.client as win32
import easygui

# Get user inputs using easygui
company_name = easygui.enterbox(msg="Enter Company Name")
job_position = easygui.enterbox(msg="Enter Job Position")


# Open word document
word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(
    r"D:\Data\Arshit\Apply Job\Cover Letter\src\Cover Letter.docx")

# Replace the placeholders with user inputs
doc.Content.Find.Execute(FindText="[pos]", ReplaceWith=job_position, Replace=2)
doc.Content.Find.Execute(FindText="[co]", ReplaceWith=company_name, Replace=2)

# Save as PDF
# saveas = "D:\Data\Arshit\Apply Job\Cover Letter\{}.pdf".format(company_name)
saveas = "D:\Data\Arshit\Apply Job\Cover Letter\Arshit Vaghasiya - Cover Letter.pdf"
doc.SaveAs(saveas, FileFormat=17)

doc.Content.Find.Execute(FindText=job_position, ReplaceWith="[pos]", Replace=2)
doc.Content.Find.Execute(FindText=company_name, ReplaceWith="[co]", Replace=2)

# Close document and word application
doc.Close()
word.Quit()
