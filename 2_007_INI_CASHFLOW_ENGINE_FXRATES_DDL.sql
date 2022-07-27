


-- INI_DDL
    
CREATE VIEW CASHFLOW_ENGINE_LND.FXRATES (
  ValuationDate, 
  EffectFromDate,
  EffectToDate,
  CalculationEntity,
  FromCurrency,
  ToCurrency,
  ConversionRate,
  ConversionType,
  DataSource,
  Context,
  optionId,
  Version,
  input_file,
  input_time
)

AS 

WITH fxrates_raw AS ( 
SELECT t.* FROM src_sbx_cashflow_engine_delta.FXRATES  t
WHERE t.OptionId = (SELECT OptionId FROM datahub_fmc.SL2_load_cycle_info LIMIT 1)
AND t.Version = (SELECT Version FROM datahub_fmc.SL2_load_cycle_info LIMIT 1)

)




 
SELECT * FROM fxrates_raw 
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
;