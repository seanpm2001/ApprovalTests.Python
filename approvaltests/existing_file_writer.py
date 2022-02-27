import shutil

from approvaltests.core import Options
from approvaltests.core import Writer


class ExistingFileWriter(Writer):
    def __init__(self, file_name: str, options: Options) -> None:
        self.file_name = file_name
        self.options = options

    def write_received_file(self, received_file: str) -> str:
        # if we dont have a scrubber just do the regular thing
        # if we do have a scrubber read the file in, scrub it and write
        shutil.copyfile(self.file_name, received_file)
        return received_file
