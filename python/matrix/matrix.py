class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def format_rows(self):
        rows = self.matrix_string.split('\n')
        completed_rows = []
        
        for entry in rows:
            formatted_row = []
            new_list = entry.split(' ')
            for new_entry in new_list:
                formatted_entry = int(new_entry)
                formatted_row.append(formatted_entry)
            completed_rows.append(formatted_row)
        
        return completed_rows


    def format_columns(self):
        formatted_rows = self.format_rows()
        count = 0
        formatted_columns = []
        number_of_columns = 0 

        for row in formatted_rows:
            if len(row) > number_of_columns:
                number_of_columns = len(row)
        
        while count <= number_of_columns:
            formatted_column = []
            for row in formatted_rows:
                if count < len(row): 
                    formatted_column.append(row[count])
            formatted_columns.append(formatted_column)
            count = count + 1

        return formatted_columns
    

    def row(self, index):
        final_row = self.format_rows()
        row_wanted = index - 1
        
        return final_row[row_wanted]


    def column(self, index):
        final_column = self.format_columns()
        column_wanted = index - 1

        return final_column[column_wanted]

        
              
            
        
