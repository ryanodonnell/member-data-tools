#### Employer / BargainingUnit / JobClass Conflicts
Use the script below to search for varying BU's within Employer-JobClass combinations. These are disallowed in VAN and must be normalized to only one value.

<pre> select distinct EmployerName, BargUnit, JobClass
     from [dbo].[table_name] t1
  where exists (select * 
     from [dbo].[table_name] t2 
     where t2.BargUnit <> t1.BargUnit
         and t2.EmployerName = t1.EmployerName
         and t2.JobClass = t1.JobClass
    )
 order by JobClass ASC</pre>

