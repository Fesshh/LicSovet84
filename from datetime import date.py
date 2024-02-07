from datetime import date, timedelta
days = '5'
delt = timedelta(days=int(days))
datt = date.fromisoformat('2024-01-01')
t = date.today()

if datt<t: print("YES")
else: print("NO")