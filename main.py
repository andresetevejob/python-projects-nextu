# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        mht = float(input("Veuillez saisir le montant"))
        tva = 0.2
        print("Le montant ttc est ", (mht + (mht * tva)))
        rep = input("Voulez-vous effectuer un nouveau calcul")
        if rep == 'N' or rep == 'n':
            break;

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
