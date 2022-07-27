


-- INI_DDL

CREATE  VIEW   CASHFLOW_ENGINE_LND.ORGANISATION_DUMMY AS SELECT t.* FROM src_sbx_cashflow_engine_delta.ORGANISATION_DUMMY  t
-- WHERE t.OptionId = (SELECT OptionId FROM datahub_fmc.SL2_load_cycle_info LIMIT 1)
-- AND t.Version = (SELECT Version FROM datahub_fmc.SL2_load_cycle_info LIMIT 1)
;


 
 