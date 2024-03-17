from enums import MetaCommandResult, PrepareResult, StatementType


class Statement():
    type: StatementType = None

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