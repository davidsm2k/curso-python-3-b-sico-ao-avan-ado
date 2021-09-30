import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col, to_date, coalesce

lst1 = ["Jay","Raj","Jack"]
lst2 = [12,15,14]
list3 = ['1998-11-23','1998-11-23', '1998-11-23']
df = pd.DataFrame(list(zip(lst1,lst2, list3)), columns = ['Nome','Idade', 'Nasc.'])
# df = df.withColumn('Nasc.', coalesce(to_date(col('Nasc.'), 'yyyy-MM-dd'), to_date(col('Nasc.'), 'dd.MM.yyyy')))


