from openpyxl import *
from bs4 import BeautifulSoup
import os
seg1dict={'0':'1111111100000000','1':'0011000000000000','2':'1110111000010001','3':'1111110000010001','4':'0011000100010001','5':'1101110100010001','6':'1101111100010001','7':'1111000000000000','8':'1111111100010001','9':'1111110100010001','a':'0000111000000101','b':'0000011100000101','c':'0000011000000001','d':'0000011001000101','e':'1000011101000001','f':'1000001100000001','g':'1000010101000101','h':'0000001100000101','i':'0000001000000000','j':'0000010001000100','k':'0000000001101100','l':'0000100001000100','m':'0001001000010101','n':'0001000000010100','o':'0001100000010100','p':'0110000001010100','q':'1000000101000101','r':'0000000000010100','s':'0100100001010000','t':'0000100001010100','u':'0000111000000100','v':'0000000010100000','w':'0001111000000100','x':'0000000010101010','y':'0000010101000101','z':'0000010000000011','A':'1111001100010001','B':'0111100001010100','C':'1100111100000000','D':'0111100001000100','E':'1110111100010001','F':'1100001100010001','G':'1101111100010001','H':'0011001100010001','I':'1100110001000100','J':'0011110000000000','K':'0000001100101001','L':'0000111100000000','M':'1111001101000100','N':'0011001110001000','O':'1111111100000000','P':'1110001100010001','Q':'1111000100010001','R':'1110001100011001','S':'1101110100010001','T':'1100000001000100','U':'0011111100000000','V':'0000000010100000','W':'0011111101000100','X':'0000000010101010','Y':'0000000010100100','Z':'1100110000100010'}
seg2dict={'-':'0000001','0':'1111110','1':'0110000','2':'1101101','3':'1111001','4':'0110011','5':'1011011','6':'1011111','7':'1110000','8':'1111111','9':'1111011','A':'1110111','B':'1111111','C':'1001110','D':'1111110','E':'1001111','F':'1000111'}
book=Workbook()
sheet=book.active
arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print("This program will create a truth table for you and make equations based on the outputs that you put. After you put in the # of inputs and outputs, the program will load a .xlsx file. Put in your outputs, save and close the excel sheet, and respond to the prompt on the program. The program will also ask you if you are using a 7-segment or 16-segment display. In the case you are, you will be asked to type alphanumeric letters per line, and the program will write your binary outputs to the excel file truth table.")
a=input('Number of inputs: ')
b=input('Number of outputs: ')
c=input('Please type 16 if you are using a 16 segment display. Please type 7 if you are using a 7 segment display. Please type 0 if you aren\'t using any of these displays: ')
link="32x8.com/var"+a+".html"
if int(c)==7 or int(c)==16:
    b=int(c)
arr3=arr[:int(a)]
arr2=arr[:int(a)]
arr2.reverse()
cell=0
for x in range(0,len(arr3)):
    sheet[arr3[x]+'2']=arr2[x]
sheet['A1']="Truth Table"
for x in range(0,int(b)):
    sheet[arr[x+len(arr3)+1]+'2']='y'+str(x)
for x in range(0,2**int(a)):
    d=bin(x)
    y=str(d)[2:]
    while len(y)<int(a):
        y='0'+y
    for t in range(0,int(a)):
        sheet[arr3[t]+str(x+3)]=int(y[t])
if int(c)==0:
    book.save("result.xlsx")
    print("Your truth table has been made. You may write your outputs now.")
    os.startfile('result.xlsx')
elif int(c)==16:
    print('Begin writing your alphanumeric characters below. For example, a, b, C, 5, 8, etc. per line. When you are done, type \'done\'.')
    count=0
    y=input()
    while y!='done' and count!=2**(int(a)):
        if y!='done':
            x=seg1dict[y]
            print('16-seg based output: %s'%x)
            for t in range(0,int(c)):
                sheet[arr[t+int(a)+1]+str(3+count)]=int(x[t])
            y=input()
            count+=1
    book.save("result.xlsx")
    os.startfile('result.xlsx')
    print("Your truth table has now been made")
elif int(c)==7:
    print('Begin writing your hex characters below. For example, 1, 2, 3, A, B, C, etc. per line.')
    count=0
    y=input()
    while y!='done' and count!=2**(int(a)):
        if y!='done':
            x=seg2dict[y]
            print('7-seg based output: x)
            for t in range(0,int(c)):
                sheet[arr[t+int(a)+1]+str(3+count)]=int(x[t])
            y=input()
            count+=1
    book.save("result.xlsx")
    os.startfile('result.xlsx')
