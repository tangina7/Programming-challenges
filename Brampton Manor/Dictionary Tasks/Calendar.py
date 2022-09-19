mydict = {"JAN" : 1,
          "FEB" : 2,
          "MAR" : 3,
          "APR" : 4,
          "MAY" : 5,
          "JUN" : 6,
          "JUL" : 7,
          "AUG" : 8,
          "SEP" : 9,
          "OCT" : 10,
          "NOV" : 11,
          "DEC" : 12
}


def SplitDate():
    date = input("Enter a date in the form dd-mmm-yy. ")
    date2 = date.split("-")
    month = mydict[date2[1]]
    dateTuple = (int(date2[0]), month, int(date2[2]))
    print(dateTuple)
    
if __name__ == "__main__":
    SplitDate()
