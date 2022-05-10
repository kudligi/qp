$Names=@()
Import-CSV timetable.csv 
| ForEach-Object 
{ $Names += $_.Name }
echo $Names