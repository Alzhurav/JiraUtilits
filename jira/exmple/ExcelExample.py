import openpyxl

wb2 = openpyxl.load_workbook('example.xlsx')
ws = wb2.active

print(ws['C3'].value + ' ' + ws['B3'].value + ' ' + str(ws['A3'].value))


# font0 = xlwt.Font()
# font0.name = 'Times New Roman'
# font0.colour_index = 2
# font0.bold = True
#
# style0 = xlwt.XFStyle()
# style0.font = font0
#
# style1 = xlwt.XFStyle()
# style1.num_format_str = 'D-MMM-YY'
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')
#
# ws.write(0, 0, 'Test', style0)
# ws.write(1, 0, datetime.now(), style1)
# ws.write(2, 0, 'dfsdfs')
# ws.write(2, 1, 1)
# ws.write(2, 2, xlwt.Formula("A3+B3"))
#
# wb.save('example.xls')