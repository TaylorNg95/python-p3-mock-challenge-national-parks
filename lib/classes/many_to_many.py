class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and len(name) >= 3:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        st = {}
        for trip in Trip.all:
            if trip.national_park == self:
                st[trip.visitor] = True
        return [key for key, value in st.items()]
    
    def total_visits(self):
        visits = self.trips()
        if visits:
            return len(visits)
        else:
            return 0
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        st = {}
        if visitors:
            for visitor in visitors:
                if st.get(visitor):
                    st[visitor] += 1
                else:
                    st[visitor] = 1
            best_count = max([value for key, value in st.items()])
            return [key for key, value in st.items() if st[key] == best_count][0]
        else:
            return None

    @classmethod
    def most_visited(cls):
        count = {}
        for park in NationalPark.all:
                count[park] = park.total_visits()
        best_park_visits = max([value for key, value in count.items()])
        return [key for key, value in count.items() if count[key] == best_park_visits][0]


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
            # need to format as 'September 1st'

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
            # need to format as 'September 1st'

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        st = {}
        for trip in Trip.all:
            if trip.visitor == self:
                st[trip.national_park] = True
        return [key for key, value in st.items()]
    
    def total_visits_at_park(self, park):
        trips = self.trips()
        matching_visits = [trip for trip in trips if trip.national_park == park]
        return len(matching_visits)