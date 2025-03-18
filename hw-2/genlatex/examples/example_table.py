from genlatex.bin.generate_table import generate_table

from genlatex.bin.generate_document import generate_document

planet_data = [
    ["Планета", "Масса (×10²⁴ кг)", "Диаметр (км)", "Спутники", "Тип"],
    ["Меркурий", 0.330, 4879, 0, "Терриподобная"],
    ["Венера", 4.87, 12104, 0, "Терриподобная"],
    ["Земля", 5.97, 12756, 1, "Терриподобная"],
    ["Марс", 0.642, 6792, 2, "Терриподобная"],
    ["Юпитер", 1898.0, 139820, 79, "Газовый гигант"],
    ["Сатурн", 568.0, 116460, 82, "Газовый гигант"]
]

latex_table = generate_table(planet_data)

filename = "../artifacts/generate_table/example.tex"

generate_document(filename, latex_table)
