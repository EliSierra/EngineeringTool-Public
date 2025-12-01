import pandas as pd
from pathlib import Path
paths=Path(r"E:\Py Engineering Tool\Engineering-Tool\(1) Tool\Materials\Archive\Aluminum 6061-T6.xlsx")
paths=Path(r"E:\Py Engineering Tool\Engineering-Tool\(1) Tool\Materials\Archive\Aluminum 7050-T7451.xlsx")

data=pd.read_excel(paths, header=None)

title=data.iat[0,0]
print(title)

from pathlib import Path
import pandas as pd

