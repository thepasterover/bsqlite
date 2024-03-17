from enum import Enum


class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = 1,
    META_COMMAND_UNRECOGNIZED_COMMAND = 2

class PrepareResult(Enum):
    PREPARE_SUCCESS = 1,
    PREPARE_UNRECOGNIZED_STATEMENT = 2
    PREPARE_SYNTAX_ERROR = 3

class StatementType(Enum):
    STATEMENT_INSERT = 1,
    STATEMENT_SELECT = 2