import datetime
List = [int(i) for i in input().split()]
FDate = datetime.date(year=List[0], month=List[1], day=List[2])
Delta = datetime.timedelta(days=int(input()))
SDate = FDate + Delta
SDate = str(SDate)
SDate = SDate.split('-')
for i in SDate:
    print(int(i), end=' ')