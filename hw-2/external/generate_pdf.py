from mygenlatex import generate_table, generate_document, generate_image

def generate_pdf():
    planet_data = [
        ["Planet", "Mass (mnogo kg)", "Diameter (km)", "Moons", "Type"],
        ["Mercury", 0.330, 4879, 0, "Terrestrial"],
        ["Venus", 4.87, 12104, 0, "Terrestrial"],
        ["Earth", 5.97, 12756, 1, "Terrestrial"],
        ["Mars", 0.642, 6792, 2, "Terrestrial"],
        ["Jupiter", 1898.0, 139820, 79, "Gas Giant"],
        ["Saturn", 568.0, 116460, 82, "Gas Giant"]
    ]

    latex_table = generate_table(planet_data)
    latex_image = generate_image("./images/gofman.jpeg", "Igor Gofman")
    filename = "./doc.tex"

    data = latex_table + latex_image
    generate_document(filename, data)


if __name__ == "__main__":
    generate_pdf()
