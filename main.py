from pyscript import document, display

def checkList(e):

    zeph_list = ["Erin Rioflorido", "Inno Pena", "Mandy Cajanding", "Chloe Adlawan", "Meyer Cruz", "Audrey Tan", "Aleynah Redillas"]

    firstnm = document.getElementById("firstnm").value
    surnm = document.getElementById("surnm").value

    name = firstnm + " " + surnm

    confirm_name = name in zeph_list

    message = (
        f"Sorry {name}, you are not part of ZEPHYR.",
        f"Yey! {name}, you are part of ZEPHYR."
    )

    document.getElementById("output1").innerHTML = message[confirm_name]

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "He": ("Helium", 2, 4.0026),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.948),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222.0)
}


def checkElement(e):

    element_Name = document.getElementById("symbolInput").value

    var2 = non_metals.get(element_Name, ("Element not found", "-", "-"))

    document.getElementById("resultDisplay").innerHTML = f"""
        Symbol: {element_Name}
        <br>
        Element: {var2[0]}
        <br>
        Atomic Number: {var2[1]}
        <br>
        Atomic Mass: {var2[2]}
    """

def add_member(e):

    grade_7 = {'Deandre Faiyaz'}
    grade_8 = {'Samantha Bautista'}
    grade_9 = {'Chloe Adlawan'}
    grade_10 = {'Julia Bermudez'}

    members = grade_7 | grade_8 | grade_9 | grade_10

    input_member = document.getElementById('input1').value
    input_member2 = document.getElementById('input2').value

    new_member = {input_member + " " + input_member2}

    all_member = members | new_member
    total_member = len(all_member)

    member_list = "<br>".join(sorted(all_member))

    document.getElementById('output1').innerHTML = (
        f"<b>Grade 7:</b> {', '.join(sorted(grade_7))}<br>"
        f"<b>Grade 8:</b> {', '.join(sorted(grade_8))}<br>"
        f"<b>Grade 9:</b> {', '.join(sorted(grade_9))}<br>"
        f"<b>Grade 10:</b> {', '.join(sorted(grade_10))}<br><br>"
        f"<b>All Members:</b><br>{member_list}<br><br>"
        f"<b>Total Members:</b> {total_member}"
    )
