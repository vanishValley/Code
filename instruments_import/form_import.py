import pandas as pd

def infer_mysql_type(value):
    """根据单元格值推断 MySQL 数据类型"""
    if isinstance(value, (int, str)) and str(value).lstrip('-').isdigit():
        return "INT"
    elif isinstance(value, float) or (isinstance(value, str) and value.replace('.', '', 1).lstrip('-').isdigit()):
        return "FLOAT"
    elif isinstance(value, str):
        try:
            pd.to_datetime(value)
            return "DATE"
        except ValueError:
            return "VARCHAR(255)"
    elif isinstance(value, pd.Timestamp):
        return "DATETIME"
    else:
        return "VARCHAR(255)"

def generate_create_table_sql(columns_with_types, table_name="instrument_data"):
    """生成 CREATE TABLE SQL 语句"""
    columns_sql = "`id` INT AUTO_INCREMENT PRIMARY KEY,\n    "
    columns_sql += ",\n    ".join([f"`{col}` {dtype}" for col, dtype in columns_with_types.items()])
    sql = f"CREATE TABLE `{table_name}` (\n    {columns_sql}\n);"
    return sql

def generate_insert_sql(data_row, table_name="instrument_data"):
    """生成 INSERT INTO SQL 语句"""
    keys = ['`' + str(k) + '`' for k in data_row.keys()]
    values = []
    for v in data_row.values():
        if pd.isna(v):  # 处理空值
            values.append("NULL")
        elif isinstance(v, (int, float)):
            values.append(str(v))
        else:
            try:
                # 如果是日期格式，转为 DATE 类型格式
                date_val = pd.to_datetime(v).strftime('%Y-%m-%d')
                values.append(f"'{date_val}'")
            except Exception:
                values.append(f"'{str(v).replace('\'', '\'\'')}'")
    keys_str = ", ".join(keys)
    values_str = ", ".join(values)
    sql = f"INSERT INTO `{table_name}` ({keys_str}) VALUES ({values_str});"
    return sql

def excel_to_sql(file_path, output_file='instrument_data_inserts.sql.txt', sheet_name=0, table_name="instrument_data"):
    # 使用 xlrd 引擎读取 .xls 文件
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None, engine='xlrd')

    # 获取列名（第一行）
    columns = list(df.iloc[0].astype(str))

    # 推断每列的数据类型（使用第二行）
    sample_row = df.iloc[1]
    column_types = {}
    for col_name, value in zip(columns, sample_row):
        column_types[col_name] = infer_mysql_type(value)

    # 生成建表语句
    create_sql = generate_create_table_sql(column_types, table_name)

    # 生成插入语句（从第2行开始）
    insert_sqls = []
    for idx, row in df.iloc[1:].iterrows():
        data_dict = dict(zip(columns, row))
        insert_sql = generate_insert_sql(data_dict, table_name)
        insert_sqls.append(insert_sql)

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("-- 创建表语句\n")
        f.write(create_sql + "\n\n")
        f.write("-- 插入数据语句\n")
        for sql in insert_sqls:
            f.write(sql + "\n")

    print(f"✅ SQL 文件已成功保存至：{output_file}")
    return create_sql, insert_sqls

# 示例入口
if __name__ == "__main__":
    file_path = "instruments.xls"         # 替换为你的 .xls 文件路径
    output_file = "instrument_data_inserts_sql.txt"  # 输出文件路径
    sheet_name = 0                    # 可以指定 sheet 名称或索引，如 "Sheet1"

    excel_to_sql(file_path, output_file=output_file, sheet_name=sheet_name, table_name="instrument_data")