import subprocess
import sys


def compile(filename):
    subprocess.run(['pyinstaller', f'{filename}',
                    '--onefile',
                    '--uac-admin'
                    ])


if __name__ == "__main__":
    filename = sys.argv[1]
    compile(filename)
