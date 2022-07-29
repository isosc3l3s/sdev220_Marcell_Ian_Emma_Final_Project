#Names:Ian Schaak, Emma(Oluwatosin) Idowu, Marcell Jackson 
#date modified: 07/11/2022
#version: python 3.10.5
#purpose: converts initial currency to display exchange rates accross central america
from tabulate import tabulate


print("This is CA Ching. This app is intended to give a quick idea of how your money will change in value over the 7 countries of Central America.\n\n")
initialValue = float(input("please enter the amount you wish to convert in a 0.00 format\n"))
format_initialValue = "{:.2f}".format(initialValue)

#list set up, but might not need all this
countries = ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panama", "USA"]

countryCurrency = ["Belizean Dollars", "Colones", "Dollar", "Quetzal", "Lempira", "Cordoba", "Balboa", "US Dollar"]

currencyCode = ["BZD", "CRC", "SVC", "GTQ", "HNL", "NIO", "PAB", "USD"]
#might not need these lists


#output to display selection options
print("\nPlease look over the list below, and Identify the 3 letter code you will need to use.\n")
print("For Belize or Belizean Dollars enter: BZD.\n")
print("For Costa Rica or Colones enter: CRC.\n")
print("For El Salvador or The US Dollar in El Salvador enter: SVC\n")
print("For Guatemala or Quetzals enter: GTQ\n")
print("For Honduras or Lempiras enter: HNL\n")
print("For Nicaragua or Cordobas enter: NIO\n")
print("For Panama or Balboas enter: PAB\n")
print("For USA or US Dollars enter: USD\n")
#end of output block for selection options

currentCountry = str(input("Please enter the 3 letter code for your current country and currency\n"))
currentCountry = currentCountry.upper()
print("\n")
print(currentCountry)
print(format_initialValue)


all_ID_Selections = [countries, countryCurrency, currencyCode]

class inBelize:
  bzdToBZD = 1
  bzdToCRC = 341.08
  bzdToSVC = 0.50
  bzdToGTQ = 3.85
  bzdToHNL = 12.20
  bzdToNIO = 17.80
  bzdToPAB = 0.50
  bzdToUSD = 0.50
  
class inCostaRica:
  crcToBZD = 0.0030
  crcToCRC = 1
  crcToSVC = 0.0015
  crcToGTQ = 0.011
  crcToHNL = 0.036
  crcToNIO = 0.052
  crcToPAB = 0.0015
  crcToUSD = 0.0015

class inElSalvador:
  svcToBZD = 2.01
  svcToCRC = 686.67
  svcToSVC = 1
  svcToGTQ = 7.74
  svcToHNL = 24.57
  svcToNIO = 35.83
  svcToPAB = 1
  svcToUSD = 1

class inGuatemala:
  gtqToBZD = 0.26
  gtqToCRC = 88.73
  gtqToSVC = 0.13
  gtqToGTQ = 1
  gtqToHNL = 3.17
  gtqToNIO = 4.63
  gtqToPAB = 0.13
  gtqToUSD = 0.13

class inHonduras:
  hnlToBZD = 0.082
  hnlToCRC = 27.95
  hnlToSVC = 0.041
  hnlToGTQ = 0.32
  hnlToHNL = 1
  hnlToNIO = 1.46
  hnlToPAB = 0.041
  hnlToUSD = 0.041

class inNicaragua:
  nioToBZD = 0.056
  nioToCRC = 19.17
  nioToSVC = 0.028
  nioToGTQ = 0.22
  nioToHNL = 0.69
  nioToNIO = 1.46
  nioToPAB = 0.028
  nioToUSD = 0.028

class inPanama:
  pabToBZD = 2.02
  pabToCRC = 687.55
  pabToSVC = 1.00
  pabToGTQ = 7.75
  pabToHNL = 24.60
  pabToNIO = 35.88
  pabToPAB = 1
  pabToUSD = 1.00

class inUsa:
  usdToBZD = 2.02
  usdToCRC = 687.55
  usdToSVC = 1.00
  usdToGTQ = 7.75
  usdToHNL = 24.60
  usdToNIO = 35.88
  usdToPAB = 1
  usdToUSD = 1.00
  
    

#print(float(inBelize.bzdToCRC)*float(format_initialValue))

 






if currentCountry == "BZD":
  bTable = [["Belize", "BZD",float(inBelize.bzdToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inBelize.bzdToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inBelize.bzdToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inBelize.bzdToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inBelize.bzdToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inBelize.bzdToNIO)*float(format_initialValue )],["Panama", "PAB", float(inBelize.bzdToPAB)*float(format_initialValue )],["United States", "USD", float(inBelize.bzdToUSD)*float(format_initialValue )],]
  table = tabulate(bTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')
  print(table)
  
if currentCountry == "CRC":
  cTable = [["Belize", "BZD",float(inCostaRica.crcToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inCostaRica.crcToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inCostaRica.crcToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inCostaRica.crcToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inCostaRica.crcToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inCostaRica.crcToNIO)*float(format_initialValue )],["Panama", "PAB", float(inCostaRica.crcToPAB)*float(format_initialValue )],["United States", "USD", float(inCostaRica.crcToUSD)*float(format_initialValue )],]
  Costatable = tabulate(cTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(Costatable)

if currentCountry == "SVC":
  eTable = [["Belize", "BZD",float(inElSalvador.svcToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inElSalvador.svcToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inElSalvador.svcToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inElSalvador.svcToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inElSalvador.svcToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inElSalvador.svcToNIO)*float(format_initialValue )],["Panama", "PAB", float(inElSalvador.svcToPAB)*float(format_initialValue )],["United States", "USD", float(inElSalvador.svcToUSD)*float(format_initialValue )],]
  elTable = tabulate(eTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(elTable)

if currentCountry == "GTQ":
  gTable = [["Belize", "BZD",float(inGuatemala.gtqToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inGuatemala.gtqToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inGuatemala.gtqToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inGuatemala.gtqToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inGuatemala.gtqToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inGuatemala.gtqToNIO)*float(format_initialValue )],["Panama", "PAB", float(inGuatemala.gtqToPAB)*float(format_initialValue )],["United States", "USD", float(inGuatemala.gtqToUSD)*float(format_initialValue )],]
  guTable = tabulate(gTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(guTable)

if currentCountry == "HNL":
  hTable = [["Belize", "BZD",float(inHonduras.hnlToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inHonduras.hnlToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inHonduras.hnlToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inHonduras.hnlToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inHonduras.hnlToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inHonduras.hnlToNIO)*float(format_initialValue )],["Panama", "PAB", float(inHonduras.hnlToPAB)*float(format_initialValue )],["United States", "USD", float(inHonduras.hnlToUSD)*float(format_initialValue )],]
  hoTable = tabulate(hTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(hoTable)

if currentCountry == "NIO":
  nTable = [["Belize", "BZD",float(inNicaragua.nioToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inNicaragua.nioToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inNicaragua.nioToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inNicaragua.nioToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inNicaragua.nioToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inNicaragua.nioToNIO)*float(format_initialValue )],["Panama", "PAB", float(inNicaragua.nioToPAB)*float(format_initialValue )],["United States", "USD", float(inNicaragua.nioToUSD)*float(format_initialValue )],]
  niTable = tabulate(nTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(niTable)

if currentCountry == "PAB":
  pTable = [["Belize", "BZD",float(inPanama.pabToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inPanama.pabToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inPanama.pabToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inPanama.pabToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inPanama.pabToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inPanama.pabToNIO)*float(format_initialValue )],["Panama", "PAB", float(inPanama.pabToPAB)*float(format_initialValue )],["United States", "USD", float(inPanama.pabToUSD)*float(format_initialValue )],]
  paTable = tabulate(pTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(paTable)

if currentCountry == "USD":
  uTable = [["Belize", "BZD",float(inUsa.usdToBZD)*float(format_initialValue )], ["Costa Rica", "CRC", float(inUsa.usdToCRC)*float(format_initialValue )], ["El Salvador", "SVC", float(inUsa.usdToSVC)*float(format_initialValue )],["Guatemala", "GTQ", float(inUsa.usdToGTQ)*float(format_initialValue )],["Honduras", "HNL", float(inUsa.usdToHNL)*float(format_initialValue )],["Nicaragua", "NIO", float(inUsa.usdToNIO)*float(format_initialValue )],["Panama", "PAB", float(inUsa.usdToPAB)*float(format_initialValue )],["United States", "USD", float(inUsa.usdToUSD)*float(format_initialValue )],]
  usTable = tabulate(uTable, headers=['Country', 'Code', 'Currency Conversion'], tablefmt='orgtbl')

  print(usTable)
