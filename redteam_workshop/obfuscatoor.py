import re
import argparse

# Comprehensive list of VBScript reserved keywords, functions, and methods
VB_RESERVED_KEYWORDS = [
    "String", "Boolean", "Integer", "Long", "Double", "Date", "Variant", "Object",
    "If", "Then", "Else", "ElseIf", "End If", "For", "Next", "Each", "In",
    "Do", "While", "Loop", "Select", "Case", "Exit", "Wend",
    "Option", "Explicit", "Dim", "As", "Sub", "End", "End Sub", "Function", "End Function",
    "Const", "Set", "Call", "With", "End With", "On", "Error", "Resume", "Goto", "True", "False",
    "And", "Or", "Not", "Is", "Mod", "ByRef", "ByVal", "Class", "Private", "Public",
    "CreateObject", "Trim", "Len", "Mid", "Left", "Right", "Instr", "InStr", "Replace",
    "LCase", "UCase", "Chr", "Asc", "IsNumeric", "IsEmpty", "IsNull", "Split", "Join",
    "Array", "CStr", "CInt", "CLng", "CDbl", "CDate", "CSng", "CVar", "Now", "Date", "Time",
    "Exec", "Open", "Send", "StdOut.ReadAll", "StdOut.AtEndOfStream", "responseText",
]

# Create a regex pattern for reserved keywords
reserved_keywords_pattern = r'\b(' + '|'.join(re.escape(keyword) for keyword in VB_RESERVED_KEYWORDS) + r')\b'


def obfuscate_vbs(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        vbs_code = file.read()

    string_pattern = r'"([^"]*)"'  # Match strings enclosed in double quotes
    macro_name_pattern = r"(Sub|Function)\s+(\w+)"  # Match Sub or Function names
    constant_value_pattern = r"Const\s+(\w+)\s*=\s*([\w\.\-\"]+)"  # Match constants
    method_name_pattern = r"(\w+\.\w+)"  # Match method calls like obj.method

    # Temporarily store strings to preserve them
    strings = re.findall(string_pattern, vbs_code)
    string_placeholders = {f"__STR{i}__": s for i, s in enumerate(strings)}

    for placeholder, original_string in string_placeholders.items():
        vbs_code = vbs_code.replace(f'"{original_string}"', placeholder)

    def obfuscate_variables(match):
        variable = match.group(0)
        if (not re.match(reserved_keywords_pattern, variable) and
                not re.match(macro_name_pattern, variable) and
                not re.match(constant_value_pattern, variable) and
                not variable.startswith("__STR")):
            return f"var_{hash(variable) % 100000}"
        return variable

    def obfuscate_code(code):
        code = re.sub(r"\b\w+\b", obfuscate_variables, code)
        code = re.sub(method_name_pattern, lambda x: x.group(1), code)
        return code

    obfuscated_code = obfuscate_code(vbs_code)

    for placeholder, original_string in string_placeholders.items():
        obfuscated_code = obfuscated_code.replace(placeholder, f'"{original_string}"')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(obfuscated_code)

    print(f"VBScript obfuscated and saved to {output_file}")


def print_ascii_art():
    ascii_art = r"""
⠀⠀⠛⠉⠠⠀⢀⣠⠟⠋⠁⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠹⣿⢷⣦⣤⣠⣾⣿⡿⠿⠁⠀
⣁⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣓⠾⣿⣿⣿⣿⠋⠀⠀⠀⠀
⠙⠛⠛⠛⠓⠒⠒⠒⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣽⡻⣿⣷⣮⡙⠛⠛⠛⠓⠒⠛⠒
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠉⠉⠉⠈⠀⣠⡴⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠉⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠉⠉⠉⠉
⠀⠀⠀⠀⠀⢀⡴⢊⣥⣾⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⢀
⠀⠀⠀⠀⡰⢋⣴⣿⣿⣿⣿⣿⣿⣿⠋⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠁
⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠈⠀⠀⠀⠀⠐⠤⣀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢆⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢔
⠀⠀⠀⠀⢸⡟⢰⣿⣿⣿⣿⣿⡿⢁⡔⢹⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠜
⠀⠀⠀⠀⢸⠀⢸⣿⣿⣿⣿⠁⠙⢿⣴⡾⠁⠀⠀⠀⣤⣤⣴⣿⣾⣲⣄⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠈⠀⠀⢿⣏⣿⠇⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡨⠿⣿⣿⣤⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠀⠀⠀⢀⣠⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣄⡸⠁⠀⠀⢻⣿⡦⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀
⠀⠐⢚⣿⣿⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣄⣀⠀⢀⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣾⣿⡀⠀⠀
⠀⠀⠸⣿⣿⠟⢠⠏⡜⢃⠀⠀⠈⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠚⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣦⣀
⠀⠀⠀⠹⣿⡄⢸⠀⠁⠸⡀⠀⠘⠞⠈⠓⠤⠄⠀⠀⠀⠀⠀⠀⠐⠛⣉⡽⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣸⣿⣿⣿⣿⣿⡿⡄⠘⣿⣽⡇
⠀⠀⠀⠀⡠⠟⡎⠱⡄⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⡥⣾⣿⣿⣿⣿⡿⠟⠉⠀⠀⢀⣿⣿⣿⣿⣿⣿⢃⢹⡎⡉⢢⠉
⠀⠀⢠⢚⡶⢺⣆⠀⠘⣄⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠒⣲⣾⣿⣿⣿⣿⣿⡿⠋⠀⢀⣀⣤⣶⣿⣿⣿⡿⠟⣹⢿⡀⠀⣇⣸⣴⠄
⠀⠀⡼⠁⢀⠾⠚⢉⡗⡻⠀⠀⠉⠁⠒⠒⠒⠶⡒⠲⣶⣾⣿⣿⣿⣿⣿⣿⡿⠟⠃⢶⣾⣿⣿⣿⠿⠿⠿⡉⠀⠀⣇⣼⡇⣀⠜⠋⠀⠀
⠀⡜⢀⠔⠁⣠⣴⢎⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⣿⣿⣿⣿⡿⠟⣿⠃⠀⠀⠀⣈⣹⠧⠈⠉⠋⣽⢶⣷⣤⣀⠘⣾⠟⠁⠀⠀⠀⠀
⡞⡠⠃⢀⣼⠁⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⣿⠋⢀⡴⡏⠉⠙⠅⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⠃⠀⠀⠀⠀⠀⠀
⢱⠁⠀⣾⠊⠁⠒⡾⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⣿⠀⡇⡠⠋⠀⠏⢀⡠⠴⠛⠓⠂⠉⠉⠉⠉⠒⠒⠂⠤⢤⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⢠⠊⠀⣠⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣧⠾⢤⡀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠁⠀⠜⠊⠠⢇⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠈⡹⠋⠀⠀⢀⠀⡤⠒⠒⠈⠉⠉⠉⠑⡖⠢⠤⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⢀⡞⢀⡠⠊⢀⣠⠔⠉⠀⣀⠁⠀⠀⠀⠀⢀⡤⠈⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀

   Welcome to Noobfuscator - a simple yet functional VBS obfuscator 
   Version 1.0

         """
    print(ascii_art)


def main():
    parser = argparse.ArgumentParser(
        description="Obfuscate a VBScript file by renaming variables and preserving essential elements."
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help="Path to the input VBScript file."
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help="Path to save the obfuscated VBScript file."
    )

    args = parser.parse_args()

    print_ascii_art()

    try:
        obfuscate_vbs(args.input, args.output)
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
