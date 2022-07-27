import os
import re
import glob

euro2euro_sql = """SELECT * FROM fxrates_raw 
UNION 
SELECT 
  (SELECT ValuationDate FROM fxrates_raw LIMIT 1) AS ValuationDate, 
  20201231 AS EffectFromDate, 
  20201231 AS EffectToDate, 
  "*" AS CalculationEntity,
  "EUR" AS FromCurrency, 
  "EUR" AS ToCurrency, 
  1.0 AS ConversionRate, 
  "None" AS ConversionType,
  "None" AS DataSource, 
  "IFRS17" AS Context, 
  (SELECT OptionId FROM datahub_fmc.SL2_load_cycle_info LIMIT 1) AS optionId,
  (SELECT Version FROM datahub_fmc.SL2_load_cycle_info LIMIT 1) AS Version, 
  "Manually added record" AS input_file, 
  current_timestamp() AS input_time
;"""

def turn_script_nb(file_path: str):
    result = False
    try:
        for filename in glob.glob(f"{file_path}", recursive=True):
            #Adding Euro2Euro FxRates
            if "INI_CASHFLOW_ENGINE_FXRATES_DDL" in filename or "CDC_CASHFLOW_ENGINE_FXRATES_DDL" in filename:
                with open(filename, "r+") as f:
                    content = f.read()
                    if euro2euro_sql not in content:
                        f.write(euro2euro_sql)

            tables_list=(
                "INI_CASHFLOW_ENGINE_CURRENCY_DDL" in filename 
                or "INI_CASHFLOW_ENGINE_POLICYDUMMY_DDL" in filename 
                or "INI_CASHFLOW_ENGINE_ORGANISATIONDUMMY_DDL" in filename
                )
            if tables_list:
                print(filename)
                with open(filename, "r+") as f:
                    content = f.read()
                    if "-- WHERE" not in content or "-- AND" not in content:
                        replaced_content = re.sub("WHERE", "-- WHERE", content)
                        replaced_content = re.sub("AND", "-- AND", replaced_content)
                        f.seek(0, 0)
                        f.truncate()
                        f.write(replaced_content)         
        result = True
    except Exception as e:
        print(e)
    return result


turn_script_nb("C:\\Users\\abaitali\\Desktop\\Python Script\\**")

