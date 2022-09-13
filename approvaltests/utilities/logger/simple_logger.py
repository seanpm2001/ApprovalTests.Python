import inspect
from contextlib import contextmanager
from typing import Iterator

from approvaltests.utilities.string_wrapper import StringWrapper
from approvaltests.namer import StackFrameNamer


class SimpleLogger:
    logger = print
    tabbing = 0
    counter = 0
    @staticmethod
    def log_to_string():
        buffer = StringWrapper()
        SimpleLogger.logger = buffer.append
        return buffer

    @staticmethod
    @contextmanager
    def use_markers() -> Iterator[None]:
        stack = inspect.stack(1)[2]
        method_name = stack[3]
        filename = StackFrameNamer.get_class_name_for_frame(stack)
        expected = f"-> in: {method_name}(){filename}"
        SimpleLogger.log(expected)
        SimpleLogger.tabbing = SimpleLogger.tabbing + 1
        yield
        SimpleLogger.tabbing = SimpleLogger.tabbing - 1
        expected = f"<- out: {method_name}(){filename}"
        SimpleLogger.log(expected)
        pass

    @staticmethod
    def log(log_output):
        if SimpleLogger.counter != 0:
            SimpleLogger.logger("\n")
            SimpleLogger.counter = 0

        tabbing = '  ' * SimpleLogger.tabbing
        SimpleLogger.logger(f"{tabbing}{log_output}\n")

    @staticmethod
    def variable(type: str, value):
        display_variable = f"variable: {type} = {value}"
        SimpleLogger.log(display_variable)

    @staticmethod
    def hour_glass():
        SimpleLogger.counter = SimpleLogger.counter + 1
        if SimpleLogger.counter == 1:
            tabbing = '  ' * SimpleLogger.tabbing
            SimpleLogger.logger(f"{tabbing}")

        if SimpleLogger.counter % 10 == 0:
            SimpleLogger.logger(f"{int(SimpleLogger.counter/10)}")
        else:
            SimpleLogger.logger('.')

        if SimpleLogger.counter == 100:
            SimpleLogger.logger('\n')
            SimpleLogger.counter = 0