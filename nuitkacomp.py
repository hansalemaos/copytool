from nutikacompile import compile_with_nuitka

# creates the command line and executes it in a new console

wholecommand = compile_with_nuitka(

    pyfile=r"C:\ProgramData\anaconda3\envs\copytool\copytool.py",

    icon=r"C:\Users\hansc\Downloads\3056374.png",

    disable_console=False,

    file_version="1.0.0.2",

    onefile=True,

    outputdir="c:\\copytoolcompiled",

    addfiles=[
r"C:\ProgramData\anaconda3\envs\copytool\uffs.com",
        r"C:\ProgramData\anaconda3\envs\copytool\buffercalc.cp310-win_amd64.pyd"

    ],

    delete_onefile_temp=False,  # creates a permanent cache folder

    needs_admin=True,
    arguments2add="--msvc=14.3 --noinclude-numba-mode=nofollow --jobs=1",

)

print(wholecommand)