import cx_Freeze

executables = [cx_Freeze.Executable("src/play.py")]

cx_Freeze.setup(
    name="Corona Videogame",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                ("src/images/","images")
            ]
        }
    },
    executables=executables
)