import pprint,openpyxl

'''
{

'AL':{    

           'd': { 'C':100,'pop':1 }  
           'd1': { 'C':100,'pop':1 }  
           'd3': { 'C':100,'pop':1 }   
      }  
}
'''

wb=openpyxl.load_workbook('E:\\text.xlsx')
sheet=wb.active
## 字典就是 键值对
