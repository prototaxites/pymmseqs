# pymmseqs/utils/binary.py
import os
import platform
import shutil
from sysconfig import get_path

def get_mmseqs_binary():
    """
    Retrieve the path to the mmseqs2 binary.
    Force a path by setting the MMSEQS2_PATH environment variable, otherwise check in
    MMSeqs2 is on the path. If that doesn't exist, use the bundled version.
    """
    custom_path = os.getenv('MMSEQS2_PATH')
    if custom_path:
        if os.path.exists(custom_path):
            return custom_path
        else:
            raise FileNotFoundError(
                f"mmseqs2 binary specified by MMSEQS2_PATH does not exist: {custom_path}"
            )

    mmseqs_binary = shutil.which("mmseqs")
    if mmseqs_binary:
        return mmseqs_binary
    
    system = platform.system()
    binary_name = 'mmseqs.exe' if system == 'Windows' else 'mmseqs'
    binary_path = os.path.join(get_path('purelib'), 'pymmseqs', 'bin', binary_name)
    
    if not os.path.exists(binary_path):
        raise FileNotFoundError(
            f"mmseqs2 binary not found at {binary_path}. Please ensure it is installed correctly."
        )
    
    return binary_path
