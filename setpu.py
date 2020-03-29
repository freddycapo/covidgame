import cx_Freeze

executables=[cx_Freeze.Executable("play.py")]

cx_Freeze.setup(
    name="Corona Videogame",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["images/stella2.png","images/images.jpg","images/mask.png","images/virus.png"]}},

    executables=executables
)