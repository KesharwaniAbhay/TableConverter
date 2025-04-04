import pandas as pd

def save_tables_to_excel(tables_list, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, table_data in tables_list:
            df = pd.DataFrame(table_data)
            df.to_excel(writer, sheet_name=sheet_name[:31], index=False, header=False)
