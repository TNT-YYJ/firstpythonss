import pprint,openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='happy2017'
wb.save('x.xlsx')  ## 创建

##保存
wb1=openpyxl.load_workbook('x.xlsx')
wb1.save('x1.xlsx')## 即使有错误，名字不同，也不会覆盖

##
wb2=openpyxl.Workbook()
sheet2=wb2.active
wb2.create_sheet(title='first',index=0)
wb2.remove_sheet(wb2.get_sheet_by_name('first')) ## 只能根据名字来进行操作
wb2.save('temp2.xlsx')

##直接赋值
sheet2['A1']='hello value '

##直接赋值
ws2=wb2.create_sheet('rang names')
for row in range(1,10):
    ws2.append(range(17))


## list给值
ws2=wb2.create_sheet('List')
rows=[
    [1,2,3],
    [12,22,32],
    [11,21,31],
]
for row in rows:
    ws2.append(row)


ws3=wb2.create_sheet(title='data')
for row in range(1,2):
    for col in range(1,2):
        ws3.cell(column=col,row=row,value=str(col))

