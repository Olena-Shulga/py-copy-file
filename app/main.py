def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        print("The command is not formatted correctly")
    else:
        file1 = command.split(" ")[1]
        file1_copy = command.split(" ")[2]
        if file1 != file1_copy and command.split(" ")[0] == "cp":
            try:
                with (open(file1, "r") as file_in,
                      open(file1_copy, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print(f"The file {file1} does not exist")
