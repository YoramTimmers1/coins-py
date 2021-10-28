# name of student: Yoram
# number of student: 99068979
# purpose of program: Het is iets wat jij geld geeft en het geeft je geld terug
# function of program:een rekenmachine voor coins
# structure of program: idk

toPay = int(float(input('Amount to pay: '))* 100) # Hier moet je nog betalen 
paid = int(float(input('Paid amount: ')) * 100) # Hier betaal je het bedrag
change = paid - toPay # Het wisselgeld is paid - Topay en dat is je change

if change > 0: # Als de change groter is dan nul
  coinValue = 500 # Dan is de coinvalue(waarde van het geld)  500
  
  while change > 0 and coinValue > 0: # als de change en de coinvalue 0 =
    nrCoins = change // coinValue # een deling die aan linker kant word aangepast en het word automatisch een geheel getal

    if nrCoins > 0: # als  nrCoins groter is dan 0 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print dan 'return maximal ', nrCoins, ' coins of ', coinValue, ' cents!'
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # hier vraagt het progamma hoeveel cents je terug je terug hebt gegeven
      change -= nrCoinsReturned * coinValue # hier doet NrCoinsReturned x coinvalue and dat word de change

# comment on code below: 
    if coinValue == 500:
      coinvalue = 300
    elif coinvalue == 300: 
      coinvalue = 200
    elif coinvalue == 200:
      coinvalue == 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')