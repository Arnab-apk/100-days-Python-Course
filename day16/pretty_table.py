from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["pakachu","Squrtle","Charmandar"])
table.add_column("Type",["Electric","Water","Fire"])
table.align ="r"
print(table)