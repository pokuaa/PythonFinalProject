#function to convert from gramme to kilograms
#defining the function
def grammeToKilogram():
    gramme = eval(input('Enter any  number in grammes: '))
    kilogram = 0.001*gramme
    # return kilogram to memory
    return kilogram

#takes gramme and converts it to tonnes
def grammeToTonnes():
     gramme = eval(input('Enter any  number in grammes: '))
     tonnes =0.000001 *gramme
     return tonnes
   
#function to convert from gramme to pounds
def grammeToPounds():
     gramme = eval(input('Enter any  number in grammes: '))
     pounds = 0.0022*gramme
     return pounds


def mlToLitres():
    ml = eval(input('Enter any  number in ml: '))
    litres = 0.001*ml
    return litres


def LitresToMl():
    litres = eval(input('Enter any  number in litres: '))
    ml = 1000*litres
    return ml


def LitresToCubic_metre():
     litres = eval(input('Enter any  number in Cubic_metre: '))
     Cubic_metre = 1000*litres
     return Cubic_metre


def Cubic_metreToLitres():
     Cubic_metre = eval(input('Enter any  number in Cuic_metre: '))
    #allows user to input value in cubic_metre 
     Litres = 0.001*cubic_metre
     return Litres


def CmToMetres():
     cm = eval(input('Enter any  number in cm: '))
     metre = 0.01*cm
     return metre


def MetresToCm():
     metre = eval(input('Enter any  number in metre: '))
     cm = 100*metre
     return cm


#takes cm and converts it to metres
def CmToMetres():
     cm = eval(input('Enter any  number in cm: '))
     metre = 0.01*cm
     return metre


def MilesToft():
     miles = eval(input('Enter any  number in miles: '))
     ft = 528*miles
     return ft


def ftToMiles():
    ft = eval(input('Enter any  number in ft: '))
    miles = 0.002*ft
    return miles


def kmToMetres():
    km = eval(input('Enter any  number in km: '))
    metre = 1000*km
    return metre


def MetresToKm():
    metre = eval(input('Enter any  number in metre: '))
#allows user to input value in metres
    km = 0.001*metre
    return km

# displays the various units of conversion and allows the user to enter their preferred unit of conversion
def main():
    line='====='*10
    print('Welcome to the Unit Converter Calculator.\nBelow gives a list of unit conversions\Enter the the quantity you want to convert here')
    print(line)
    print()
    print('1. convert from grammes to kilograms\n2. convert from to grammes to tonnes\n3.convert from grammes  to pounds ')
    print('4. convert from ml to litres \n5. convert from litres to ml\n6.convert from litres to cubic_metre')
    print('7. convert from cubic_metres to litres \n8. convert from cm to metres\n9.convert from metres to cm')
    print('10. convert from cm  to m \n11. convert from miles to ft \n12.convert from ft to miles')
    print('13. convert from km to metres \n14. convert from metres to km')
    print()
    print(line)

     
    # ask user for the choice of quantity and converts it to a different unit of the same quantity.
    choice = input('Enter choice to convert from one unit to another: ')
#check which function to call per the users choice 
    if choice == '1':
        a=grammeToKilogram()
        print(a,'kg')
        
    elif choice == '2':
        b = grammeToTonnes()
        print(b,'tonnes')
    
    
    elif choice == '3':
        c = grammeToPounds()
        print(c,'pounds')
    elif choice == '4':
        d = mlToLitres()
        print(d,'ltrs')
        
    elif choice == '5':
        d = LitresToMl()
        print(d,'ml')
        
    elif choice == '6':
        d = LitresToCubic_metre()
        print(d,'cm^3')
        
    elif choice == '7':
        d = Cubic_metreToLitres()
        print(d,'ltrs')
        
    elif choice == '8':
        d = CmToMetres()
        print(d,'metres')
    
    elif choice == '9':
        d = MetresToCm()
        print(d,'cm')
        
    elif choice == '10':
        d = CmToMetres()
        print(d,'metres')
        
    elif choice == '11':
        d = ftToMiles()
        print(d,'miles')
        
    elif choice == '12':
        d = ftToMiles()
        print(d,'miles')
        
    elif choice == '13':
        d = kmToMetres()
        print(d,'ltrs')
        
    elif choice == '14':
        MetresToKm()
        print(d,'metres')
        
    # checking if the user entered a wrong input   
    else:
        print('Reconsider your input')
        
     
        
        
    
    
    
    
#calling the main function   
main()