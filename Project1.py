#Jung-Hyun Lee
#G00013016
#This program will allow a user to find the mass of a chemical substance (in grams), the amount of moles
#   of a chemical substance (in moles), the number of molecules of a chemical substance, and the Molarity
#   of a chemical substance (in moles per Liter).
#   The program will have a main function that will allow the user to input what he/she wants to do.
#   Then the main function will call the corresponding function depending on the choice.  Once the
#   called function makes the calculation and returns a value, the main function
#   will go through a while loop to determine if the user wants to continue.
#
#   Local variables include the following:
#       'volume' is the volume of the chemical substance in Liters
#       'mass' is the mass of a substance in grams
#       'mole' is the mole amount of a substance
#       'molecularWeight' is the amount of mass (in grams) per mole of a substance
#       'density' is the weight of a substance per volume in mL
#       'Molarity' is the conversion factor of moles per volume in Liters
#
#



#constant for Avogadro's Number, or the number of atoms in 1 mole of a substance
AVOGADRO=6.023*10**23

def introduction():
    """Introduction to the program"""
print("""
    This program will allow a user to find
        -the molecular weight (or molar mass) of a chemical substance (in grams per mole)
        -the mass of a substance (in grams)
        -the amount of moles of a substance (in moles)
        -the number of molecules of a substance
        -the volume of a substance (in Liters)
        -the Molarity of a substance (in moles per Liter)
        -the density of substance (in grams per mL)
    """)

#def conversion(volume):
#    """Finds the conversion from Liters to milliliters"""

#    milliliters=volume*1000
#    print("The volume in mL is", milliliters, "mL.\n")
#    return milliliters

def find_MolecularWeight(mass, mole):
    """Menu Option 1: Finds the molar mass or molecular weight of a substance (in grams per mol)"""

    molecularWeight=mass/mole
    print("The molecular weight is", molecularWeight, "grams per mole\n")
    return molecularWeight


def find_mass(mole, volume, molecularWeight, density):
    """Menu Option 2: Finds the mass of substance in grams"""

    mass=""
    if density is not None and volume is not None:
        mass=volume*density
    elif mole is not None and molecularWeight is not None:
        mass=mole*molecularWeight
    print("The mass of the substance is", mass, "grams.\n")
    return mass


def find_mole(mass, Molarity, molecules, volume, molecularWeight):
    """Menu Option 3:  Finds the number of moles of a substance"""

    mole=""
    if mass is not None and molecularWeight is not None:
        mole = mass*molecularWeight
    elif mole is not None and Molarity is not None:
        mole = volume*Molarity
    elif molecules is not None:
        mole = molecules*(1/AVOGADRO)
    print("The mole amount of the substance is", mole, "moles.\n")
    return mole


def find_number(molecularWeight, mass, volume, Molarity):
    """Menu Option 4:  Finds the number of molecules"""

    molecules=""
    if mass is not None and molecularWeight is not None:
        molecules=mass*(1/molecularWeight)*AVOGADRO
    if volume is not None and Molarity is not None:
        molecules=volume*Molarity*AVOGADRO
    print("The number of molecules of the substance is", molecules, "molecules.\n")
    return molecules


def find_volume(mass, mole, density, Molarity):
    """Menu Option 5:  Finds the volume of substance in Liters"""

    volume=""
    if density is not None and mass is not None:
        volume=density*mass
    elif Molarity is not None and mole is not None:
        volume=Molarity*mole
    print("The volume of the substance is", volume, "Liters.\n")
    return volume


def find_MOLARITY(mole, volume):
    """Menu Option 6:  Finds the Molarity of a substance (moles per Liter)"""

    Molarity=mole/volume
    print("The Molarity of the substance is", Molarity, "moles per Liter.\n")
    return Molarity



def find_DENSITY(mass, volume):
    """Menu Option 7:  Finds the density of a substance (grams per mL)"""

 #   vol=conversion(volume)  #value of volume is sent to conversion() and vol catches the conversion in milliliters
    density=mass/(volume*1000)
    print("The density of the substance is", density, "grams per mL.\n")
    return density


def user_choice():
    """menu"""

    print("""Do you want to
        1. Find the molecular weight of the substance (grams per mole)?
        2  Find the mass of the substance (in grams)?
        3. Find the mole amount of the substance?
        4. Find the number of molecules?
        5. Find the volume of the substance (in Liters)?
        6. Find the Molarity of the substance?
        7. Find the density of the substance?""")

    menu_choice=input("Please choose one: \n")
    #next_question=None

    if menu_choice=="1":        #menu choice #1 finds molecular weight (grams/mole)
        mass_amount=float(input("What is the mass of the substance (in grams)?"))
        number_of_moles=float(input("What is the number of moles?"))
        find_MolecularWeight(mass_amount, number_of_moles)


    if menu_choice=="2":        #menu choice #2 finds mass in grams
        try:                    #Python runs the following code,...
            number_of_moles=float(input("What is the number of moles?")) #number of moles
        except:                 #...otherwise, responds to an exception by assigning None datatype to variable
            number_of_moles=None
            pass

        try:
             volume_of_substance=float(input("What is the volume of the substance (in Liter)?"))  #volume in Liter
        except:
            volume_of_substance=None
            pass

        try:
            molar_mass=float(input("What is the molar mass of the substance (grams per mole)?"))    #molecular weight
        except:
            molar_mass=None
            pass

        try:
            density_amount=float(input("What is the density of the substance (grams per mL)?"))     #density in grams/mL
        except:
            density_amount=None
            pass

        find_mass(number_of_moles, volume_of_substance, molar_mass, density_amount)

    elif menu_choice=="3":      #menu choice #3 finds mole amount
        try:
            mass_amount=float(input("What is the mass of the substance (in grams)?"))
        except:
            mass_amount=None
            pass

        try:
            find_Molarity=float(input("What is the Molarity of the substance (in moles per Liter)?"))
        except:
            find_Molarity=None
            pass

        try:
            number_of_molecules=float(input("What is the number of molecules of the substance?"))
        except:
            number_of_molecules=None
            pass

        try:
            volume_of_substance=float(input("What is the volume of the susbstance (in Liters)?"))
        except:
            volume_of_substance=None
            pass

        try:
            molar_mass=float(input("What is the molar mass of the substance (grams per mole)?"))
        except:
            molar_mass=None
            pass

        find_mole(mass_amount, find_Molarity, number_of_molecules, volume_of_substance, molar_mass)

    elif menu_choice=="4":      #menu choice #4 finds the number of molecules
        try:
            molar_mass=float(input("What is the molecular weight of the substance (grams per mole)?"))
        except:
            molar_mass=None
            pass

        try:
            mass_amount=float(input("What is the mass of the substance (in grams)?"))
        except:
            mass_amount=None
            pass

        try:
            number_of_moles=float(input("What is the mole amount?"))
        except:
            number_of_moles=None
            pass

        try:
            volume_of_substance=float(input("What is the volume of the substance?"))
        except:
            volume_of_substance=None
            pass

        try:
            find_Molarity=float(input("What is the Molarity of the substance (moles per Liter)?"))
        except:
            find_Molarity=None
            pass

        find_number(molar_mass, mass_amount, volume_of_substance, find_Molarity)



    elif menu_choice=="5":     #menu choice #5 finds the volume in Liters
        try:
            mass_amount=float(input("What is the mass of the substance (in grams)?"))
        except:
            mass_amount=None
            pass

        try:
            number_of_moles=float(input("What is the mole amount?"))
        except:
            number_of_moles=None
            pass

        try:
            find_density=float(input("What is the density of the substance (grams per mL)?"))
        except:
            find_density=None
            pass

        try:
            find_Molarity=float(input("What is the Molarity of the substance (moles per Liter)?"))
        except:
            find_Molarity=None
            pass

        find_volume(mass_amount, number_of_moles, find_density, find_Molarity)



    elif menu_choice=="6":      #menu choice #6 finds Molarity in moles per Liter
        number_of_moles=float(input("What is the mole amount?"))
        #density_amount=float(input("What is the density of the substance (grams per mL)?"))
        volume_of_substance=float(input("What is the volume of the substance (in Liter)?"))

        find_MOLARITY(number_of_moles, volume_of_substance)



    elif menu_choice=="7":      #menu choice #7 finds density in grams per mL
        mass_amount=float(input("What is the mass of the substance (in grams)?"))
        volume_of_substance=float(input("What is the volume of the substance (in Liters)?"))

        find_DENSITY(mass_amount, volume_of_substance)


def main():
    """main () function"""
    #return values include 'molecularWeight', 'mass', 'mole', 'molecules', 'volume', 'Molarity', 'density'
    #start=True
    #while start:
    introduction()
    user_choice()
    molecularWeight=find_MolecularWeight()
    mass=find_mass()
    mole=find_mole()
    molecules=find_number()
    volume=find_volume()
    Molarity=find_MOLARITY()
    density=find_DENSITY()

    print("density is", density, "\n")
    #to_be_continued=input("Do you want to continue?")

    #if to_be_continued=="yes" or to_be_continued=="Yes":
    #    user_choice()
    #elif to_be_continued=="no":
    #    print("Have a nice day!\n")

if __name__== "__main__": main()
