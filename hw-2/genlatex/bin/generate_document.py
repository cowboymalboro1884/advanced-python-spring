def generate_document(filename, data):
    with open(filename, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\begin{document}\n\n")
        f.write(data)
        f.write("\\end{document}\n")
