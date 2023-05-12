import warnings


class Movie:
    def __init__(self, title, year, rating=None):
        self.title = title
        self.year = year
        self.rating = rating
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}"
    
    def __repr__(self):
        return self.__str__()


def print_list(l):
    for i, m in enumerate(l):
        print(f"\t{i+1}. {m}")


if __name__ == "__main__":
    # Rating by Filmweb 2023-05
    rocky = Movie("Rocky", 1976, 7.7)
    godft = Movie("The Godfather", 1972, 8.6)
    starg = Movie("Stargate", 1994, 7.2)
    gump = Movie("Forrest Gump", 1994, 8.5)
    leon = Movie("Leon", 1994, 8.1)
    killer = Movie("Killer", 1997, 7.7)
    
    glad = Movie("Gladiator", 2000, 8.1)
    goodfe = Movie("Goodfellas", 1990, 8.3)
    konop = Movie("Konopielka", 1981, 7.7)
    psy = Movie("Psy", 1992, 7.7)
    am12 = Movie("12 Angry Men", 1957, 8.7)
    pianist = Movie("The Pianist", 2002, 8.3)
    
    snova = Movie("2012: Supernova", 2009, 2.5)
    futro = Movie("Futro z misia", 2019, 3.3)
    
    
    mlist = [rocky, godft, starg, gump, leon, killer,
             glad, goodfe, konop, psy, am12, pianist,
             snova, futro]
    
    # alphabetic, year, rating:
    slist = sorted(mlist, key = lambda m: (m.title, m.year, m.rating))
    print("\nAlphabetic order:")
    print_list(slist)
    
    
    # year, alphabetic, rating:
    slist = sorted(mlist, key = lambda m: (m.year, m.title, m.rating))
    print("\nChronologic order:")
    print_list(slist)
        
    
    # rating, alphabetic, year :
    slist = sorted(mlist, key = lambda m: (m.rating, m.title, m.year))
    print("\nRating order:")
    print_list(slist)
        
    
    # inverse rating, alphabetic, year:
    slist = sorted(mlist, key = lambda m: (-m.rating, m.title, m.year))
    print("\nTop list:")
    print_list(slist)

    
    # inverse year, alphabetic, rating:
    slist = sorted(mlist, key = lambda m: (-m.year, m.title, m.rating))
    print("\nNewest:")
    print_list(slist)

        
    # "Hottest" - newest with the highest rating
    # one rating point decaying over 12 years,
    # so 7.0 from 2023 is equally hot as 8.0 from 2011, but not as hot as r.g. 7.5 from 2020
    slist = sorted(mlist, key = lambda m: (-m.year - m.rating*12,  m.title))
    print("\nHottest:")
    print_list(slist)

  