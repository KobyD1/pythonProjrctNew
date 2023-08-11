
import pywinauto
from pywinauto import Desktop

app= pywinauto.application.Application(backend="uia")
app.start("calc.exe")
dialog = Desktop(backend='uia').Calculator

dialog.print_control_identifiers(filename='outputs//output_calc.txt')
dialog.child_window(title="Three",auto_id="num3Button",control_type='Button').click()
dialog.child_window(auto_id="num6Button",control_type='Button').click()
results = dialog.child_window( auto_id="CalculatorResults", control_type="Text")
text = results.texts

dialog.child_window(title="Close Calculator", auto_id="Close", control_type="Button").click()
print('Test End')
