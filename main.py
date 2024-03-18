from enums import MetaCommandResult, PrepareResult, StatementType
from constants import COLUMN_EMAIL_SIZE, COLUMNS_USERNAME_SIZE, PAGE_SIZE, TABLE_MAX_PAGES
from utilities import size_of_attribute
from ctypes import c_uint32,  create_string_buffer




class Row():
    
    def __init__(self) -> None:
        self.id = c_uint32()
        self.username = create_string_buffer(COLUMNS_USERNAME_SIZE)
        self.email = create_string_buffer(COLUMN_EMAIL_SIZE)

ID_SIZE = size_of_attribute(Row, 'id')
USERNAME_SIZE = size_of_attribute(Row, 'username')
EMAIL_SIZE = size_of_attribute(Row, 'email')

# Calculate offsets
ID_OFFSET = 0
USERNAME_OFFSET = ID_OFFSET + ID_SIZE
EMAIL_OFFSET = USERNAME_OFFSET + USERNAME_SIZE

# Calculate total row size
ROW_SIZE = ID_SIZE + USERNAME_SIZE + EMAIL_SIZE


# Total number of rows we can store page is page_size bytes / row_size bytes
ROWS_PER_PAGE = PAGE_SIZE / ROW_SIZE
# Total number of rows a table can hold is rows_per_page bytes * 100
# if I can only store 4 rows in a page then for next page we need another page
# maximum rows that can be created is rows_per_page * table_max_pages. eg: 4 * 100 = 4000
TABLE_MAX_ROWS = ROWS_PER_PAGE * TABLE_MAX_PAGES 


class Statement():
    type: StatementType = None
    row_to_insert: Row

def execute_statement(statement: Statement):
    match statement.type:
        case StatementType.STATEMENT_INSERT:
            print("Insetign Statement")
            return
        case StatementType.STATEMENT_SELECT:
            print("selecting statement")
            return
        
        
    

def prepare_statement(command: str, statement: Statement):

    if command[:6] == 'insert':
        statement.type = StatementType.STATEMENT_INSERT
        argsAssigned = command.split(' ')
        if len(argsAssigned) < 4:
            return PrepareResult.PREPARE_SYNTAX_ERROR
        
        statement.row_to_insert.id = argsAssigned[1]
        statement.row_to_insert.username = argsAssigned[2]
        statement.row_to_insert.email = argsAssigned[3]

        return PrepareResult.PREPARE_SUCCESS
    
    if command[:5] == 'select':
        statement.type = StatementType.STATEMENT_SELECT
        return PrepareResult.PREPARE_SUCCESS
    
    return PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT

def do_meta_command(command: str):
    if command == ".exit":
        quit()
    return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND


def main():
    while True:
        command = input("db > ")

        if command[:1] == '.':
            match (do_meta_command(command)):
                case MetaCommandResult.META_COMMAND_SUCCESS:
                    continue
                case MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND:
                    print(f"Unrecognized command {command}")
                    continue
        statement = Statement()
        match (prepare_statement(command, statement)):
            case PrepareResult.PREPARE_SUCCESS:
                pass
            case PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT:
                print(f"Unrecognized keyword at start of {command}")
                continue

        execute_statement(statement)
        print("Executed")

        

# run main function
if __name__ == "__main__":
    main()